#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    from cli_support import configure_utf8_stdio
except ModuleNotFoundError:
    from tools.cli_support import configure_utf8_stdio

try:
    from wiki_store import (
        WIKI, Concept, WikiPage, concept_matches_lookup, iter_markdown_files,
        load_concepts, read_page, split_editorial_notes,
    )
except ModuleNotFoundError:
    from tools.wiki_store import (
        WIKI, Concept, WikiPage, concept_matches_lookup, iter_markdown_files,
        load_concepts, read_page, split_editorial_notes,
    )


HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*#*\s*$")


@dataclass(frozen=True)
class MarkdownHeading:
    level: int
    title: str
    line_index: int
    anchor: str


def markdown_anchor(title: str) -> str:
    anchor = title.strip().lower()
    anchor = re.sub(r"[^\w\u3040-\u30ff\u3400-\u9fff -]+", "", anchor)
    anchor = re.sub(r"\s+", "-", anchor)
    return anchor.strip("-")


def load_page_target(name: str, bundle: Path = WIKI) -> WikiPage:
    path = Path(name)
    if path.exists():
        path = path.resolve()
        root = bundle.resolve() if path.is_relative_to(bundle.resolve()) else path.parent
        return read_page(path, root)

    concepts = load_concepts(bundle)
    cid = find_concept(concepts, name)
    concept = concepts[cid]
    return read_page(concept.path, bundle)


def load_markdown_target(name: str, view: str = "article") -> tuple[str, Path, str]:
    page = load_page_target(name)
    return page.path.stem, page.path, page.body if view == "editing" else page.article_body


def find_concept(concepts: dict[str, Concept], name: str) -> str:
    matches = [cid for cid, concept in concepts.items() if concept_matches_lookup(concept, name)]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise SystemExit(f"Markdown concept not found: {name}")
    raise SystemExit(f"ambiguous Markdown concept: {name}: {', '.join(matches)}")


def detect_headings(markdown: str) -> list[MarkdownHeading]:
    headings: list[MarkdownHeading] = []
    seen: dict[str, int] = {}
    document = split_editorial_notes(markdown)
    document.require_valid()
    offset = 0
    span_index = 0
    for index, raw_line in enumerate(markdown.splitlines(keepends=True)):
        line = raw_line.rstrip("\r\n")
        while span_index < len(document.opaque_spans) and document.opaque_spans[span_index][1] <= offset:
            span_index += 1
        hidden = span_index < len(document.opaque_spans) and document.opaque_spans[span_index][0] <= offset
        offset += len(raw_line)
        if hidden:
            continue
        match = HEADING_RE.match(line)
        if not match:
            continue
        title = match.group("title").strip()
        base_anchor = markdown_anchor(title)
        count = seen.get(base_anchor, 0)
        seen[base_anchor] = count + 1
        anchor = base_anchor if count == 0 else f"{base_anchor}-{count}"
        headings.append(MarkdownHeading(len(match.group("marks")), title, index, anchor))
    return headings


def editorial_note_rows(page: WikiPage) -> list[dict[str, object]]:
    page.editorial.require_valid()
    headings = detect_headings(page.body)
    lines = page.editorial.masked().splitlines()
    rows: list[dict[str, object]] = []
    for note in page.editorial.notes:
        start = note.line - page.body_start_line
        end = note.end_line - page.body_start_line
        heading = next((item.title for item in reversed(headings) if item.line_index <= start), "")
        before = [line.strip() for line in lines[:start + 1] if line.strip()][-2:]
        after = [line.strip() for line in lines[end:] if line.strip()][:2]
        rows.append({
            "path": page.rel_path, "line": note.line, "end_line": note.end_line,
            "heading": heading, "text": note.text, "context_before": "\n".join(before),
            "context_after": "\n".join(after),
        })
    return rows


def render_notes(rows: list[dict[str, object]], fmt: str) -> str:
    if fmt == "json":
        return json.dumps(rows, ensure_ascii=False, indent=2)

    def cell(value: object) -> str:
        return str(value).replace("|", "\\|").replace("\n", "<br>")

    lines = ["| path | line | heading | note | context before | context after |", "| --- | --- | --- | --- | --- | --- |"]
    for row in rows:
        lines.append("| " + " | ".join(cell(row[key]) for key in (
            "path", "line", "heading", "text", "context_before", "context_after",
        )) + " |")
    return "\n".join(lines)


def render_toc(headings: list[MarkdownHeading], fmt: str) -> str:
    rows = [
        {"level": heading.level, "title": heading.title, "line": heading.line_index + 1, "anchor": heading.anchor}
        for heading in headings
    ]
    if fmt == "json":
        return json.dumps(rows, ensure_ascii=False, indent=2)
    lines = ["| level | line | title | anchor |", "| --- | --- | --- | --- |"]
    for row in rows:
        lines.append(f"| {row['level']} | {row['line']} | {row['title']} | #{row['anchor']} |")
    return "\n".join(lines)


def extract_section(markdown: str, heading_query: str, include_heading: bool = True) -> str:
    lines = markdown.splitlines()
    headings = detect_headings(markdown)
    normalized_query = heading_query.lower()
    matches = [heading for heading in headings if normalized_query in heading.title.lower()]
    if not matches:
        raise SystemExit(f"section not found: {heading_query}")

    heading = matches[0]
    start = heading.line_index if include_heading else heading.line_index + 1
    end = len(lines)
    for candidate in headings:
        if candidate.line_index <= heading.line_index:
            continue
        if candidate.level <= heading.level:
            end = candidate.line_index
            break
    return "\n".join(lines[start:end]).strip() + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print a Markdown page TOC or extract one Markdown section.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    toc = subparsers.add_parser("toc", help="Print Markdown headings for a wiki concept or .md file.")
    toc.add_argument("page", help="Concept id, alias, wiki path, or local Markdown path.")
    toc.add_argument("--format", choices=["table", "json"], default="table")
    toc.add_argument("--view", choices=["article", "editing"], default="article")

    section = subparsers.add_parser("section", help="Extract a Markdown section by heading substring.")
    section.add_argument("page", help="Concept id, alias, wiki path, or local Markdown path.")
    section.add_argument("heading", help="Case-insensitive substring of the heading.")
    section.add_argument("--no-heading", action="store_true", help="Omit the matched heading line.")
    section.add_argument("--view", choices=["article", "editing"], default="article")

    read = subparsers.add_parser("read", help="Read an article, its editing source, or its editorial notes.")
    read.add_argument("page")
    read.add_argument("--view", choices=["article", "editing", "notes"], default="article")
    read.add_argument("--format", choices=["table", "json"], default="table", help="Output format for notes.")

    notes = subparsers.add_parser("notes", help="List notes from a page or across the bundle.")
    notes.add_argument("page", nargs="?")
    notes.add_argument("--bundle", type=Path, default=WIKI)
    notes.add_argument("--format", choices=["table", "json"], default="table")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    configure_utf8_stdio()
    args = parse_args(argv or sys.argv[1:])
    try:
        if args.command == "notes":
            pages = [load_page_target(args.page, args.bundle)] if args.page else (
                read_page(path, args.bundle) for path in iter_markdown_files(args.bundle)
            )
            rows = [row for page in pages for row in editorial_note_rows(page)]
            print(render_notes(rows, args.format))
            return 0
        if args.command == "read" and args.view == "notes":
            print(render_notes(editorial_note_rows(load_page_target(args.page)), args.format))
            return 0
        _cid, _path, markdown = load_markdown_target(args.page, args.view)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    if args.command == "read":
        print(markdown, end="" if markdown.endswith("\n") else "\n")
        return 0
    if args.command == "toc":
        print(render_toc(detect_headings(markdown), args.format))
        return 0
    if args.command == "section":
        print(extract_section(markdown, args.heading, include_heading=not args.no_heading), end="")
        return 0
    raise SystemExit(f"unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
