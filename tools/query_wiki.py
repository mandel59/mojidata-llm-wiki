#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import deque
from typing import Iterable

try:
    from cli_support import configure_utf8_stdio
except ModuleNotFoundError:
    from tools.cli_support import configure_utf8_stdio

from wiki_store import Concept, concept_matches_lookup, load_concepts, scalar, string_list


def public_concept(concept: Concept) -> dict[str, object]:
    return {
        "id": concept.id,
        "aliases": concept.aliases,
        "path": concept.rel_path,
        "type": concept.type,
        "title": concept.title,
        "description": scalar(concept.frontmatter, "description"),
        "date": scalar(concept.frontmatter, "date"),
        "status": scalar(concept.frontmatter, "status"),
        "tags": concept.relations.get("tags", string_list(concept.frontmatter, "tags")),
        "bodies": string_list(concept.frontmatter, "bodies"),
        "documents": concept.relations["documents"],
        "topics": concept.relations["topics"],
        "people": concept.relations["people"],
        "meetings": concept.relations["meetings"],
        "events": concept.relations["events"],
        "unresolved_relations": concept.unresolved_relations,
        "links": concept.links,
        "backlinks": concept.backlinks,
    }


def filter_concepts(concepts: Iterable[Concept], args: argparse.Namespace) -> list[Concept]:
    result = []
    for concept in concepts:
        if args.type and concept.type != args.type:
            continue
        if args.status and scalar(concept.frontmatter, "status") != args.status:
            continue
        if args.topic and args.topic not in concept.relations["topics"]:
            continue
        if args.people and args.people not in concept.relations["people"]:
            continue
        if args.document and args.document not in concept.relations["documents"]:
            continue
        if args.body and args.body not in string_list(concept.frontmatter, "bodies"):
            continue
        if args.tag and args.tag not in string_list(concept.frontmatter, "tags"):
            continue
        if args.alias and not any(args.alias.lower() in alias.lower() for alias in concept.aliases):
            continue
        result.append(concept)
    return result


def sort_concepts(concepts: list[Concept], sort_key: str, reverse: bool) -> list[Concept]:
    def key(concept: Concept) -> tuple[str, str]:
        if sort_key == "id":
            primary = concept.id
        elif sort_key == "path":
            primary = concept.rel_path
        elif sort_key == "type":
            primary = concept.type
        elif sort_key == "title":
            primary = concept.title
        else:
            primary = scalar(concept.frontmatter, sort_key)
        return (primary, concept.id)

    return sorted(concepts, key=key, reverse=reverse)


def render_table(concepts: list[dict[str, object]]) -> str:
    lines = ["| id | type | date | title | path |", "| --- | --- | --- | --- | --- |"]
    for concept in concepts:
        lines.append(
            f"| {concept['id']} | {concept['type']} | {concept['date']} | {concept['title']} | {concept['path']} |"
        )
    return "\n".join(lines)


def render_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2)


def find_start(concepts: dict[str, Concept], name: str) -> str:
    if name in concepts:
        return name
    normalized = name.replace("\\", "/")
    matches = [cid for cid, concept in concepts.items() if concept_matches_lookup(concept, normalized)]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise SystemExit(f"concept not found: {name}")
    raise SystemExit(f"ambiguous concept: {name}: {', '.join(matches)}")


def walk_related(concepts: dict[str, Concept], start: str, depth: int, direction: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    seen = {start}
    queue: deque[tuple[str, int, str]] = deque([(start, 0, "")])

    while queue:
        cid, distance, via = queue.popleft()
        concept = concepts[cid]
        rows.append({"distance": distance, "via": via, **public_concept(concept)})
        if distance >= depth:
            continue

        neighbors: set[str] = set()
        if direction in {"out", "both"}:
            neighbors.update(concept.links)
        if direction in {"in", "both"}:
            neighbors.update(concept.backlinks)

        for neighbor in sorted(neighbors):
            if neighbor in seen:
                continue
            seen.add(neighbor)
            queue.append((neighbor, distance + 1, cid))
    return rows


def render_related_table(rows: list[dict[str, object]]) -> str:
    lines = ["| distance | id | type | date | title | via | path |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for row in rows:
        lines.append(
            f"| {row['distance']} | {row['id']} | {row['type']} | {row['date']} | {row['title']} | {row['via']} | {row['path']} |"
        )
    return "\n".join(lines)


def add_common_filters(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--type", help="Filter by frontmatter type, e.g. Event or Topic.")
    parser.add_argument("--status")
    parser.add_argument("--topic")
    parser.add_argument("--people")
    parser.add_argument("--document")
    parser.add_argument("--body")
    parser.add_argument("--tag")
    parser.add_argument("--alias", help="Filter by alias substring.")
    parser.add_argument("--sort", choices=["date", "title", "id", "path", "type", "status"], default="title")
    parser.add_argument("--reverse", action="store_true")
    parser.add_argument("--format", choices=["table", "json"], default="table")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Query wiki concepts and their links.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List concepts from frontmatter metadata.")
    add_common_filters(list_parser)

    event_parser = subparsers.add_parser("events", help="List events sorted by date.")
    add_common_filters(event_parser)
    event_parser.set_defaults(type="Event", sort="date")

    show_parser = subparsers.add_parser("show", help="Show one concept as JSON.")
    show_parser.add_argument("concept")

    related_parser = subparsers.add_parser("related", help="Walk links and backlinks from a concept.")
    related_parser.add_argument("concept")
    related_parser.add_argument("--depth", type=int, default=1)
    related_parser.add_argument("--direction", choices=["out", "in", "both"], default="both")
    related_parser.add_argument("--format", choices=["table", "json"], default="table")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    configure_utf8_stdio()
    args = parse_args(argv or sys.argv[1:])
    try:
        concepts = load_concepts()
    except ValueError as error:
        raise SystemExit(str(error)) from error

    if args.command in {"list", "events"}:
        rows = filter_concepts(concepts.values(), args)
        rows = sort_concepts(rows, args.sort, args.reverse)
        public_rows = [public_concept(row) for row in rows]
        print(render_json(public_rows) if args.format == "json" else render_table(public_rows))
        return 0

    if args.command == "show":
        cid = find_start(concepts, args.concept)
        print(render_json(public_concept(concepts[cid])))
        return 0

    if args.command == "related":
        cid = find_start(concepts, args.concept)
        rows = walk_related(concepts, cid, args.depth, args.direction)
        print(render_json(rows) if args.format == "json" else render_related_table(rows))
        return 0

    raise SystemExit(f"unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
