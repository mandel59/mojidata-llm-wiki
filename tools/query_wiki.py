#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import deque
from pathlib import Path
from typing import Iterable

from check_events import WIKI, parse_frontmatter, string_list


LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
RELATION_KEYS = ["documents", "topics", "people", "meetings", "events"]


def split_frontmatter_body(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    data, errors = parse_frontmatter(path)
    if errors:
        raise SystemExit("\n".join(errors))
    if not text.startswith("---"):
        return data, text
    lines = text.splitlines()
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return data, "\n".join(lines[index + 1 :])
    return data, text


def concept_id(path: Path, data: dict[str, object]) -> str:
    for key in ["slug", "entry_id"]:
        value = data.get(key)
        if isinstance(value, str) and value:
            return value
    return path.stem


def concept_type(path: Path, data: dict[str, object]) -> str:
    value = data.get("type")
    if isinstance(value, str) and value:
        return value
    if path.parent.name == "events":
        return "Event"
    return "Concept"


def scalar(data: dict[str, object], key: str) -> str:
    value = data.get(key)
    return value if isinstance(value, str) else ""


def iter_concept_files(bundle: Path = WIKI) -> Iterable[Path]:
    for path in sorted(bundle.rglob("*.md")):
        if path.name in {"index.md", "log.md"}:
            continue
        yield path


def load_concepts() -> dict[str, dict[str, object]]:
    concepts: dict[str, dict[str, object]] = {}
    path_to_id: dict[Path, str] = {}

    for path in iter_concept_files():
        data, body = split_frontmatter_body(path)
        cid = concept_id(path, data)
        rel_path = path.relative_to(WIKI).as_posix()
        concept = {
            "id": cid,
            "path": rel_path,
            "type": concept_type(path, data),
            "title": scalar(data, "title") or cid,
            "description": scalar(data, "description"),
            "date": scalar(data, "date"),
            "status": scalar(data, "status"),
            "tags": string_list(data, "tags"),
            "bodies": string_list(data, "bodies"),
            "documents": string_list(data, "documents"),
            "topics": string_list(data, "topics"),
            "people": string_list(data, "people"),
            "meetings": string_list(data, "meetings"),
            "events": string_list(data, "events"),
            "_body": body,
            "_fs_path": path,
        }
        concepts[cid] = concept
        path_to_id[path.resolve()] = cid

    for concept in concepts.values():
        path = concept["_fs_path"]
        links = sorted(
            target
            for target in resolve_markdown_links(path, str(concept["_body"]), path_to_id)
            if target in concepts and target != concept["id"]
        )
        frontmatter_links = []
        for key in RELATION_KEYS:
            frontmatter_links.extend(item for item in concept[key] if item in concepts)
        concept["links"] = sorted(set(links + frontmatter_links))

    for concept in concepts.values():
        concept["backlinks"] = sorted(source["id"] for source in concepts.values() if concept["id"] in source["links"])

    return concepts


def resolve_markdown_links(path: Path, body: str, path_to_id: dict[Path, str]) -> set[str]:
    targets: set[str] = set()
    for match in LINK_RE.finditer(body):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if not target or target.startswith("#") or SCHEME_RE.match(target):
            continue
        target_path = target.split("#", 1)[0].split("?", 1)[0]
        if not target_path.endswith(".md"):
            continue
        resolved = (path.parent / target_path).resolve()
        cid = path_to_id.get(resolved)
        if cid:
            targets.add(cid)
    return targets


def public_concept(concept: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in concept.items() if not key.startswith("_")}


def filter_concepts(concepts: Iterable[dict[str, object]], args: argparse.Namespace) -> list[dict[str, object]]:
    result = []
    for concept in concepts:
        if args.type and concept["type"] != args.type:
            continue
        if args.status and concept["status"] != args.status:
            continue
        if args.topic and args.topic not in concept["topics"]:
            continue
        if args.people and args.people not in concept["people"]:
            continue
        if args.document and args.document not in concept["documents"]:
            continue
        if args.body and args.body not in concept["bodies"]:
            continue
        if args.tag and args.tag not in concept["tags"]:
            continue
        result.append(concept)
    return result


def sort_concepts(concepts: list[dict[str, object]], sort_key: str, reverse: bool) -> list[dict[str, object]]:
    def key(concept: dict[str, object]) -> tuple[str, str]:
        primary = concept.get(sort_key)
        return (primary if isinstance(primary, str) else "", str(concept["id"]))

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


def find_start(concepts: dict[str, dict[str, object]], name: str) -> str:
    if name in concepts:
        return name
    normalized = name.replace("\\", "/")
    matches = [cid for cid, concept in concepts.items() if concept["path"] == normalized or concept["path"].endswith(f"/{normalized}")]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise SystemExit(f"concept not found: {name}")
    raise SystemExit(f"ambiguous concept: {name}: {', '.join(matches)}")


def walk_related(concepts: dict[str, dict[str, object]], start: str, depth: int, direction: str) -> list[dict[str, object]]:
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
            neighbors.update(str(item) for item in concept["links"])
        if direction in {"in", "both"}:
            neighbors.update(str(item) for item in concept["backlinks"])

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
    args = parse_args(argv or sys.argv[1:])
    concepts = load_concepts()

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
