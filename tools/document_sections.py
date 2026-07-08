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

from wiki_store import Concept, concept_matches_lookup, load_concepts, read_page


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


def load_markdown_target(name: str) -> tuple[str, Path, str]:
    path = Path(name)
    if path.exists():
        page = read_page(path.resolve(), path.resolve().parents[0])
        return path.stem, path, page.body

    concepts = load_concepts()
    cid = find_concept(concepts, name)
    concept = concepts[cid]
    return concept.id, concept.path, concept.body


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
    for index, line in enumerate(markdown.splitlines()):
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

    section = subparsers.add_parser("section", help="Extract a Markdown section by heading substring.")
    section.add_argument("page", help="Concept id, alias, wiki path, or local Markdown path.")
    section.add_argument("heading", help="Case-insensitive substring of the heading.")
    section.add_argument("--no-heading", action="store_true", help="Omit the matched heading line.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    configure_utf8_stdio()
    args = parse_args(argv or sys.argv[1:])
    _cid, _path, markdown = load_markdown_target(args.page)

    if args.command == "toc":
        print(render_toc(detect_headings(markdown), args.format))
        return 0
    if args.command == "section":
        print(extract_section(markdown, args.heading, include_heading=not args.no_heading), end="")
        return 0
    raise SystemExit(f"unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
