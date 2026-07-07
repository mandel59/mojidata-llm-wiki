#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

from wiki_store import (
    ROOT,
    WIKI,
    Concept,
    LINK_RE,
    SCHEME_RE,
    load_concepts,
    read_page,
    scalar,
    string_list,
    normalize_lookup_key,
)
from unicode_registry import parse_doc_number


CATALOG = ROOT / "catalog" / "registries"
ROOT_TOPIC_HEADING = "## Current Topics"
UNAVAILABLE_PATTERNS = [
    "文書実体未確認",
    "文書実体は未確認",
    "文書実体を確認できなかった",
    "文書実体を取得できなかった",
    "未確認",
]
TENTATIVE_PATTERNS = [
    "予定文書",
]
MENTIONED_DOC_RE = re.compile(
    r"(?:"
    r"\b(?:"
    r"L2/\d{2}-\d{3}(?:R[0-9A-Z]*)?"
    r"|WG2\s*N\d{3,4}(?:R\d*)?"
    r"|IRG\s+N\d{3,4}(?:R\d*)?"
    r")\b"
    r"|(?<![A-Za-z0-9_-])(?-i:N\d{3,4}(?:R\d*)?)\b"
    r")",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class CatalogEntry:
    registry: str
    entry_id: str
    doc_number: str
    status: str
    document_url: str | None

    @property
    def available(self) -> bool:
        return self.status == "available" and bool(self.document_url)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Review higher-level wiki consistency rules.")
    parser.add_argument("--fix", action="store_true", help="Apply safe frontmatter and root topic index fixes.")
    parser.add_argument(
        "--min-unresolved-doc-refs",
        type=int,
        default=5,
        help="Flag available catalog documents referenced this many times without a wiki page.",
    )
    return parser.parse_args(argv)


def load_catalog() -> dict[str, CatalogEntry]:
    entries: dict[str, CatalogEntry] = {}
    for path in sorted(CATALOG.glob("*/documents.jsonl")):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            try:
                data = json.loads(line)
            except json.JSONDecodeError as error:
                raise SystemExit(f"{path}:{line_number}: invalid JSON: {error}") from error
            entry_id = data.get("entry_id")
            if not isinstance(entry_id, str) or not entry_id:
                continue
            entries[entry_id] = CatalogEntry(
                registry=str(data.get("registry") or ""),
                entry_id=entry_id,
                doc_number=str(data.get("doc_number") or ""),
                status=str(data.get("status") or ""),
                document_url=data.get("document_url") if isinstance(data.get("document_url"), str) else None,
            )
    return entries


def markdown_link_targets(path: Path, body: str) -> list[str]:
    targets: list[str] = []
    for match in LINK_RE.finditer(body):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if not target or target.startswith("#") or SCHEME_RE.match(target):
            continue
        target = target.split("#", 1)[0].split("?", 1)[0]
        if target:
            targets.append(target)
    return targets


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def check_no_local_links_outside_wiki() -> list[str]:
    errors: list[str] = []
    for path in sorted(WIKI.rglob("*.md")):
        rel_path = path.relative_to(WIKI).as_posix()
        page = read_page(path)
        for target in markdown_link_targets(path, page.body):
            if target.startswith("//"):
                continue
            resolved = (path.parent / target).resolve()
            if not is_relative_to(resolved, WIKI.resolve()):
                errors.append(f"{rel_path}: local Markdown link points outside wiki bundle: {target}")
    return errors


def check_local_markdown_links_exist() -> list[str]:
    errors: list[str] = []
    for path in sorted(WIKI.rglob("*.md")):
        rel_path = path.relative_to(WIKI).as_posix()
        page = read_page(path)
        for target in markdown_link_targets(path, page.body):
            if target.startswith("//") or not target.endswith(".md"):
                continue
            resolved = (path.parent / target).resolve()
            if not is_relative_to(resolved, WIKI.resolve()):
                continue
            if not resolved.is_file():
                errors.append(f"{rel_path}: local Markdown link target does not exist: {target}")
    return errors


def links_from_index(index_path: Path) -> set[str]:
    page = read_page(index_path)
    links: set[str] = set()
    for target in markdown_link_targets(index_path, page.body):
        if target.endswith(".md"):
            links.add((index_path.parent / target).resolve().relative_to(WIKI.resolve()).as_posix())
    return links


def check_directory_indexes() -> list[str]:
    checks = {
        WIKI / "topics" / "index.md": [path for path in (WIKI / "topics").glob("*.md") if path.name != "index.md"],
        WIKI / "documents" / "index.md": [
            path for path in (WIKI / "documents").glob("*.md") if path.name != "index.md"
        ],
        WIKI / "people" / "index.md": [path for path in (WIKI / "people").glob("*.md") if path.name != "index.md"],
        WIKI / "events" / "index.md": [path for path in (WIKI / "events").glob("*.md") if path.name != "index.md"],
        WIKI / "families" / "index.md": [
            path for path in (WIKI / "families").glob("*.md") if path.name != "index.md"
        ],
        WIKI / "meetings" / "index.md": [
            path for path in (WIKI / "meetings").rglob("*.md") if path.name != "index.md"
        ],
    }

    errors: list[str] = []
    for index_path, pages in checks.items():
        indexed = links_from_index(index_path)
        for page in pages:
            rel_path = page.resolve().relative_to(WIKI.resolve()).as_posix()
            if rel_path not in indexed:
                errors.append(f"{index_path.relative_to(WIKI).as_posix()}: missing link to {rel_path}")
    return errors


def topic_index_entries() -> dict[str, str]:
    index = WIKI / "topics" / "index.md"
    entries: dict[str, str] = {}
    for line in index.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^- \[([^\]]+)\]\(([^)]+\.md)\)(.*)$", line)
        if not match:
            continue
        title, target, suffix = match.groups()
        slug = Path(target).stem
        entries[slug] = f"- [{title}](topics/{slug}.md){suffix}"
    return entries


def root_current_topic_links() -> set[str]:
    root = WIKI / "index.md"
    page = read_page(root)
    return {Path(target).stem for target in markdown_link_targets(root, page.body) if target.startswith("topics/")}


def check_root_current_topics(concepts: dict[str, Concept], fix: bool) -> list[str]:
    topic_ids = {concept.id for concept in concepts.values() if concept.type == "Topic"}
    present = root_current_topic_links()
    missing = sorted(topic_ids - present)
    if fix and missing:
        fix_root_current_topics(missing)
    return [f"index.md: Current Topics is missing topics/{slug}.md" for slug in missing]


def fix_root_current_topics(missing: list[str]) -> None:
    root = WIKI / "index.md"
    text = root.read_text(encoding="utf-8")
    entries = topic_index_entries()
    lines = [entries[slug] for slug in missing if slug in entries]
    if not lines:
        return
    pattern = re.compile(rf"({re.escape(ROOT_TOPIC_HEADING)}\n(?:.*?\n)*?)(\n## )", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return
    replacement = match.group(1).rstrip() + "\n" + "\n".join(lines) + "\n" + match.group(2)
    write_text_raw(root, text[: match.start()] + replacement + text[match.end() :])


def check_meeting_bodies(concepts: dict[str, Concept], fix: bool) -> list[str]:
    errors: list[str] = []
    for concept in concepts.values():
        if concept.type != "Meeting":
            continue
        body = scalar(concept.frontmatter, "body")
        bodies = string_list(concept.frontmatter, "bodies")
        if body and body not in bodies:
            errors.append(f"{concept.rel_path}: Meeting has body={body} but bodies does not include it")
            if fix:
                insert_frontmatter_field_after(concept.path, "body", f"bodies: [{body}]")
    return errors


def check_synthesis_members(concepts: dict[str, Concept], fix: bool) -> list[str]:
    errors: list[str] = []
    for concept in concepts.values():
        if concept.type != "Synthesis":
            continue
        members = string_list(concept.frontmatter, "members")
        topics = string_list(concept.frontmatter, "topics")
        missing = [member for member in members if member not in topics]
        if missing:
            errors.append(f"{concept.rel_path}: Synthesis members missing from topics relation: {', '.join(missing)}")
            if fix:
                value = ", ".join(topics + missing)
                insert_frontmatter_field_after(concept.path, "members", f"topics: [{value}]")
    return errors


def insert_frontmatter_field_after(path: Path, after_key: str, field_line: str) -> None:
    text = path.read_text(encoding="utf-8")
    newline = "\r\n" if "\r\n" in text else "\n"
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, flags=re.DOTALL)
    if not match:
        return
    header = match.group(1)
    key = field_line.split(":", 1)[0]
    if re.search(rf"^{re.escape(key)}:", header, flags=re.MULTILINE):
        return
    pattern = re.compile(rf"^({re.escape(after_key)}:.*)$", flags=re.MULTILINE)
    if not pattern.search(header):
        return
    new_header = pattern.sub(rf"\1{newline}{field_line}", header, count=1)
    write_text_raw(path, text[: match.start(1)] + new_header + text[match.end(1) :])


def write_text_raw(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="")


def catalog_names(entry: CatalogEntry) -> set[str]:
    names = {entry.entry_id}
    if entry.doc_number:
        names.add(entry.doc_number)
    return names


def catalog_by_doc_number(catalog: dict[str, CatalogEntry]) -> dict[str, CatalogEntry]:
    by_number: dict[str, CatalogEntry] = {}
    for entry in catalog.values():
        if entry.doc_number:
            by_number[normalize_lookup_key(entry.doc_number)] = entry
    return by_number


def concept_by_alias(concepts: dict[str, Concept]) -> dict[str, Concept]:
    aliases: dict[str, Concept] = {}
    for concept in concepts.values():
        for alias in concept.aliases:
            aliases.setdefault(normalize_lookup_key(alias), concept)
    return aliases


def mentioned_catalog_entry(
    mention: str, by_doc_number: dict[str, CatalogEntry], context_registry: str
) -> CatalogEntry | None:
    if re.match(r"^L2/", mention, re.IGNORECASE):
        candidates = [("utc", mention)]
    elif re.match(r"^WG2\s*N", mention, re.IGNORECASE):
        candidates = [("wg2", mention)]
    elif re.match(r"^IRG\s+N", mention, re.IGNORECASE):
        candidates = [("irg", mention)]
    elif re.match(r"^N\d{3,4}(?:R\d*)?$", mention):
        if context_registry == "wg2":
            candidates = [("wg2", mention)]
        elif context_registry == "irg":
            candidates = [("irg", f"IRG {mention}")]
        else:
            return None
    else:
        return None

    for registry, text in candidates:
        parsed = parse_doc_number(registry, text)
        if parsed is None:
            continue
        _display, canonical, _entry_id = parsed
        return by_doc_number.get(normalize_lookup_key(canonical))
    return None


def concept_captures_mentioned_document(concept: Concept, target_id: str) -> bool:
    if target_id == concept.id:
        return True
    if target_id in concept.links:
        return True
    return target_id in concept.relations.get("documents", [])


def check_source_document_mentions_captured(
    concepts: dict[str, Concept], catalog: dict[str, CatalogEntry]
) -> list[str]:
    by_doc_number = catalog_by_doc_number(catalog)
    by_alias = concept_by_alias(concepts)
    errors: list[str] = []

    for concept in sorted(concepts.values(), key=lambda item: item.rel_path):
        if concept.type != "Source Document":
            continue

        context_registry = scalar(concept.frontmatter, "registry")
        seen_targets: set[str] = set()
        for line_number, line in enumerate(concept.body.splitlines(), start=1):
            for match in MENTIONED_DOC_RE.finditer(line):
                mention = match.group(0)
                alias_target = by_alias.get(normalize_lookup_key(mention))
                if alias_target is not None:
                    if concept_captures_mentioned_document(concept, alias_target.id):
                        continue
                    if alias_target.id in seen_targets:
                        continue
                    seen_targets.add(alias_target.id)
                    errors.append(
                        f"{concept.rel_path}:{line_number}: mentions {mention} but does not capture "
                        f"{alias_target.id} in documents relation or Markdown link"
                    )
                    continue

                entry = mentioned_catalog_entry(mention, by_doc_number, context_registry)
                if entry is None or not entry.available:
                    continue
                if concept_captures_mentioned_document(concept, entry.entry_id):
                    continue
                if entry.entry_id in seen_targets:
                    continue
                seen_targets.add(entry.entry_id)
                errors.append(
                    f"{concept.rel_path}:{line_number}: mentions available catalog document {mention} "
                    f"({entry.entry_id}) but does not capture it in documents relation or Markdown link"
                )
    return errors


def line_describes_document_as_unavailable(line: str, entry: CatalogEntry) -> bool:
    has_unavailable_claim = any(pattern in line for pattern in UNAVAILABLE_PATTERNS)
    for sentence in re.split(r"(?<=。)", line):
        if not any(pattern in sentence for pattern in UNAVAILABLE_PATTERNS):
            continue
        for name in catalog_names(entry):
            escaped = re.escape(name)
            if re.search(rf"`?{escaped}`?(?:\s*(?:は|が)|\s+-)", sentence):
                return True

    for name in catalog_names(entry):
        escaped = re.escape(name)
        if has_unavailable_claim and re.search(rf"^\s*[-*]\s+`?{escaped}`?\s+-", line):
            return True
        if any(pattern in line for pattern in TENTATIVE_PATTERNS) and re.search(rf"予定文書\s+`?{escaped}`?", line):
            return True
    return False


def check_stale_unavailable_text(catalog: dict[str, CatalogEntry]) -> list[str]:
    available = [entry for entry in catalog.values() if entry.available]
    errors: list[str] = []
    for path in sorted(WIKI.rglob("*.md")):
        rel_path = path.relative_to(WIKI).as_posix()
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not any(pattern in line for pattern in UNAVAILABLE_PATTERNS):
                continue
            for entry in available:
                if line_describes_document_as_unavailable(line, entry):
                    errors.append(
                        f"{rel_path}:{line_number}: describes available catalog document as unconfirmed or tentative: {entry.entry_id}"
                    )
    return errors


def check_frequent_unresolved_documents(
    concepts: dict[str, Concept], catalog: dict[str, CatalogEntry], minimum: int
) -> list[str]:
    counts: Counter[str] = Counter()
    sources: dict[str, list[str]] = defaultdict(list)
    for concept in concepts.values():
        for entry_id in concept.unresolved_relations.get("documents", []):
            counts[entry_id] += 1
            sources[entry_id].append(concept.rel_path)

    errors: list[str] = []
    for entry_id, count in counts.most_common():
        entry = catalog.get(entry_id)
        if count < minimum or not entry or not entry.available:
            continue
        examples = ", ".join(sources[entry_id][:3])
        errors.append(
            f"{entry_id}: available catalog document is referenced {count} times without a wiki page"
            f" (examples: {examples})"
        )
    return errors


def run_checks(args: argparse.Namespace) -> list[str]:
    catalog = load_catalog()
    concepts = load_concepts()

    errors: list[str] = []
    errors.extend(check_no_local_links_outside_wiki())
    errors.extend(check_local_markdown_links_exist())
    errors.extend(check_directory_indexes())

    fixable_errors: list[str] = []
    fixable_errors.extend(check_root_current_topics(concepts, args.fix))
    fixable_errors.extend(check_meeting_bodies(concepts, args.fix))
    fixable_errors.extend(check_synthesis_members(concepts, args.fix))

    if args.fix:
        concepts = load_concepts()
        errors.extend(check_root_current_topics(concepts, False))
        errors.extend(check_meeting_bodies(concepts, False))
        errors.extend(check_synthesis_members(concepts, False))
    else:
        errors.extend(fixable_errors)

    errors.extend(check_stale_unavailable_text(catalog))
    errors.extend(check_frequent_unresolved_documents(concepts, catalog, args.min_unresolved_doc_refs))
    errors.extend(check_source_document_mentions_captured(concepts, catalog))
    return errors


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    errors = run_checks(args)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Wiki review checks OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
