#!/usr/bin/env python3
"""Prepare bounded, deduplicated full-text reviews and record checked snapshots."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

try:
    from cli_support import configure_utf8_stdio
    from wiki_store import ROOT, WIKI, LINK_RE, iter_markdown_files, read_page, split_editorial_notes
except ModuleNotFoundError:
    from tools.cli_support import configure_utf8_stdio
    from tools.wiki_store import ROOT, WIKI, LINK_RE, iter_markdown_files, read_page, split_editorial_notes


LEDGER = ROOT / "maintenance" / "editorial-note-migration.json"
REPORT = ROOT / "maintenance" / "editorial-note-migration.md"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_ledger(path: Path, bundle: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    paths = [item["path"] for item in data["files"]]
    actual = {p.relative_to(bundle).as_posix() for p in iter_markdown_files(bundle)}
    if len(paths) != len(set(paths)) or set(paths) != actual:
        raise ValueError("ledger file inventory differs from the bundle; reconcile it before review")
    for item in data["files"]:
        if digest(bundle / item["path"]) != item["content_sha256"]:
            raise ValueError(f"{item['path']}: snapshot changed; reconcile the ledger before review")
    return data


def paragraphs(body: str) -> list[str]:
    document = split_editorial_notes(body)
    document.require_valid()
    parts: list[str] = []
    start = 0
    span_index = 0
    for separator in re.finditer(r"\n[ \t]*\n", body):
        while span_index < len(document.opaque_spans) and document.opaque_spans[span_index][1] <= separator.start():
            span_index += 1
        if span_index < len(document.opaque_spans) and document.opaque_spans[span_index][0] <= separator.start():
            continue
        parts.append(body[start:separator.start()].strip())
        start = separator.end()
    parts.append(body[start:].strip())
    return [part for part in parts if part]


def compact_links(text: str) -> str:
    # Keep every label and annotation. Only link destinations are omitted;
    # their syntax and targets are checked by the existing wiki validators.
    text = LINK_RE.sub(lambda m: m.group(0)[1:].split("](", 1)[0], text)
    return re.sub(r"<https?://[^<>\s]+>", "<URL>", text)


def prepare_packet(data: dict, ledger_path: Path, bundle: Path, directory: str,
                   max_chars: int) -> tuple[str, dict]:
    known: set[str] = set()
    for item in data["files"]:
        if item["full_text_review"] == "reviewed":
            page = read_page(bundle / item["path"], bundle)
            if page.errors:
                raise ValueError("\n".join(page.errors))
            known.update(paragraphs(page.article_body))
    output: list[str] = []
    selected: list[dict] = []
    used = 0
    for item in data["files"]:
        if item["full_text_review"] != "pending":
            continue
        if directory and not item["path"].startswith(directory.rstrip("/") + "/"):
            continue
        page = read_page(bundle / item["path"], bundle)
        if page.errors:
            raise ValueError("\n".join(page.errors))
        page.editorial.require_valid()
        parts = paragraphs(page.article_body)
        unseen = [part for part in parts if part not in known]
        rendered_parts: list[str] = []
        heading = ""
        displayed_heading = ""
        for part in parts:
            if re.fullmatch(r"#{1,6} [^\n]+", part):
                heading = part
            if part in known:
                continue
            if heading and heading != displayed_heading and part != heading:
                rendered_parts.append(heading)
            rendered_parts.append(compact_links(part))
            displayed_heading = heading
        context = {key: page.frontmatter.get(key) for key in ("title", "type", "date", "source")}
        rendered = (f"\n=== {item['path']} ===\n" + json.dumps(context, ensure_ascii=False)
                    + f"\n既読と完全一致: {len(parts) - len(unseen)}/{len(parts)} 段落\n"
                    + "\n\n".join(rendered_parts) + "\n")
        if used + len(rendered) > max_chars:
            if not selected:
                raise ValueError(f"{item['path']}: needs at least --max-chars {len(rendered)}; nothing was clipped")
            break
        selected.append({"path": item["path"], "sha256": item["content_sha256"]})
        output.append(rendered)
        used += len(rendered)
        # Later pages in the same packet may reuse text already printed here.
        known.update(parts)
    text = "".join(output)
    receipt = {"version": 1, "ledger_sha256": digest(ledger_path), "complete": True,
               "directory": directory, "max_chars": max_chars,
               "render_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), "pages": selected}
    return text, receipt


def record_packet(ledger_path: Path, receipt: dict, bundle: Path, defer: set[str] | None = None) -> dict:
    if receipt.get("version") != 1 or receipt.get("complete") is not True or not receipt.get("pages"):
        raise ValueError("receipt is not a complete, nonempty review packet")
    if digest(ledger_path) != receipt.get("ledger_sha256"):
        raise ValueError("ledger changed after preview; prepare a new packet")
    data = load_ledger(ledger_path, bundle)
    _text, expected = prepare_packet(data, ledger_path, bundle, receipt["directory"], receipt["max_chars"])
    if expected != receipt:
        raise ValueError("receipt differs from the complete preview; prepare a new packet")
    deferred = defer or set()
    selected_paths = {row["path"] for row in receipt["pages"]}
    if not deferred <= selected_paths:
        raise ValueError("deferred pages must belong to the displayed packet")
    if deferred == selected_paths:
        raise ValueError("all pages were deferred; no reviews recorded")
    index = {item["path"]: item for item in data["files"]}
    seen = set()
    for row in receipt["pages"]:
        item = index.get(row["path"])
        if row["path"] in seen or item is None or item["full_text_review"] != "pending":
            raise ValueError("receipt contains duplicate, unknown, or already reviewed pages")
        if digest(bundle / row["path"]) != row["sha256"]:
            raise ValueError(f"{row['path']}: content changed after preview")
        seen.add(row["path"])
    for row in receipt["pages"]:
        if row["path"] in deferred:
            continue
        item = index[row["path"]]
        item["full_text_review"] = "reviewed"
        item["full_text_review_method"] = (
            "本文の全段落を精査。既読記事または同じ表示内と完全一致する段落の再読だけを省略。"
            "リンクの表示名と注記は読む。リンク先URLは既存の機械検査で確認する。"
        )
        if item["status"] == "screened":
            item["status"] = "reviewed-no-candidate"
            item["reason"] = "検索候補なし。本文全体の編集記述混入を確認し、移行対象なし。"
    ledger_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return data


def refresh_report(data: dict, report: Path) -> None:
    text = report.read_text(encoding="utf-8")
    articles = [item for item in data["files"] if item["status"] != "excluded"]
    counts = Counter(item["status"] for item in data["files"])
    done = sum(item["full_text_review"] == "reviewed" for item in articles)
    rows = ["| 区分 | ページ数 |", "| --- | ---: |"]
    for label, state in [("候補精査・変更・検証済み", "reviewed-changed"),
                         ("候補精査済み・本文に残す", "reviewed-retained"),
                         ("検索候補なし・全文精査済み", "reviewed-no-candidate"),
                         ("検索候補なし・全文精査は未実施", "screened"),
                         ("対象外の index / log", "excluded")]:
        rows.append(f"| {label} | {counts[state]} |")
    summary = "\n".join(rows) + (
        f"\n\n全文精査済みは **{done} / {len(articles)}ページ**。未完了は{len(articles) - done}ページ。"
        f"そのうち{counts['screened']}ページは検索候補がなかったページ。候補行と周辺だけの確認は全文精査に数えない。"
        "全文精査は記事本文の編集記述混入の確認を指す。\n\n"
    )
    begin = text.index("| 区分 | ページ数 |")
    end = text.index("## 本文に残す判断", begin)
    text = text[:begin] + summary + text[end:]
    rows = ["| ディレクトリ | 全文精査済み | 未完了 |", "| --- | ---: | ---: |"]
    def directory_of(item: dict) -> str:
        return item["path"].split("/")[0] if "/" in item["path"] else "."

    for directory in sorted({directory_of(item) for item in articles}):
        subset = [item for item in articles if directory_of(item) == directory]
        count = sum(item["full_text_review"] == "reviewed" for item in subset)
        rows.append(f"| {directory} | {count} | {len(subset) - count} |")
    begin = text.index("| ディレクトリ | 全文精査済み | 未完了 |")
    following_heading = re.search(r"\n## ", text[begin:])
    end = begin + following_heading.start() if following_heading else len(text)
    report.write_text(text[:begin] + "\n".join(rows) + "\n" + text[end:], encoding="utf-8", newline="\n")


def main() -> int:
    configure_utf8_stdio()
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    packet = sub.add_parser("packet")
    packet.add_argument("--directory", default="")
    packet.add_argument("--max-chars", type=int, default=8000)
    packet.add_argument("--receipt", type=Path, required=True)
    record = sub.add_parser("record")
    record.add_argument("receipt", type=Path)
    record.add_argument("--defer", action="append", default=[], help="Leave a displayed page pending when it needs edits.")
    args = parser.parse_args()
    try:
        data = load_ledger(LEDGER, WIKI)
        if args.command == "status":
            articles = [item for item in data["files"] if item["status"] != "excluded"]
            done = sum(item["full_text_review"] == "reviewed" for item in articles)
            print(f"Full-text review: {done}/{len(articles)}; pending: {len(articles) - done}")
        elif args.command == "packet":
            text, receipt = prepare_packet(data, LEDGER, WIKI, args.directory, args.max_chars)
            if not receipt["pages"]:
                print("No pending pages in this selection.")
                return 0
            args.receipt.parent.mkdir(parents=True, exist_ok=True)
            args.receipt.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(text, end="")
            print(f"\nDisplayed {len(receipt['pages'])} complete pages; record only after reviewing this output.")
        else:
            receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
            data = record_packet(LEDGER, receipt, WIKI, set(args.defer))
            refresh_report(data, REPORT)
            print(f"Recorded {len(receipt['pages']) - len(set(args.defer))} full-text reviews.")
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"error: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
