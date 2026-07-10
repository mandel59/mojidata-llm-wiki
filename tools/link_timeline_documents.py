#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from cli_support import configure_utf8_stdio
except ModuleNotFoundError:
    from tools.cli_support import configure_utf8_stdio

try:
    from wiki_store import WIKI, Concept, load_concepts, relative_link
except ModuleNotFoundError:
    from tools.wiki_store import WIKI, Concept, load_concepts, relative_link

CODE_RE = re.compile(r"`([^`]+)`")


def document_lookup(concepts: dict[str, Concept]) -> dict[str, Concept]:
    lookup: dict[str, Concept] = {}
    ambiguous: set[str] = set()
    for concept in concepts.values():
        if concept.type != "Source Document":
            continue
        values = {concept.id, concept.title, str(concept.frontmatter.get("doc_number", ""))}
        values.update(str(value) for value in concept.frontmatter.get("aliases", []) if isinstance(value, str))
        for value in values:
            key = value.strip().casefold()
            if not key:
                continue
            if key in lookup and lookup[key].id != concept.id:
                ambiguous.add(key)
            else:
                lookup[key] = concept
    for key in ambiguous:
        lookup.pop(key, None)
    return lookup


def link_timeline(text: str, path: Path, lookup: dict[str, Concept]) -> tuple[str, int]:
    lines = text.splitlines(keepends=True)
    in_history = False
    changes = 0
    for index, line in enumerate(lines):
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading:
            level = len(heading.group(1))
            if level == 2:
                in_history = heading.group(2) == "経緯"
            elif level < 2:
                in_history = False
        if not in_history or not line.lstrip().startswith("|"):
            continue

        def replace(match: re.Match[str]) -> str:
            nonlocal changes
            label = match.group(1)
            concept = lookup.get(label.strip().casefold())
            if concept is None:
                return match.group(0)
            changes += 1
            return relative_link(path, concept.path, label)

        lines[index] = CODE_RE.sub(replace, line)
    return "".join(lines), changes


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Link resolvable document numbers in wiki history tables.")
    parser.add_argument("--write", action="store_true", help="Write changes; otherwise report a dry run.")
    parser.add_argument("--bundle", type=Path, default=WIKI)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    configure_utf8_stdio()
    args = parse_args(argv or sys.argv[1:])
    concepts = load_concepts(args.bundle)
    lookup = document_lookup(concepts)
    files = 0
    links = 0
    for path in sorted((args.bundle / "topics").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        updated, count = link_timeline(text, path, lookup)
        if not count:
            continue
        files += 1
        links += count
        print(f"{path.relative_to(args.bundle)}: {count}")
        if args.write:
            with path.open("w", encoding="utf-8", newline="") as handle:
                handle.write(updated)
    print(f"{'updated' if args.write else 'would update'} {links} link(s) in {files} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
