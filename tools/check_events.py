#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from wiki_store import EVENTS, WIKI, parse_frontmatter, string_list

ROOT = Path(__file__).resolve().parents[1]


def load_document_ids() -> set[str]:
    ids: set[str] = set()
    for path in (ROOT / "catalog" / "registries").glob("*/documents.jsonl"):
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                entry = json.loads(line)
                entry_id = entry.get("entry_id")
                if isinstance(entry_id, str):
                    ids.add(entry_id)

    derived = ROOT / "config" / "derived_documents.json"
    if derived.exists():
        data = json.loads(derived.read_text(encoding="utf-8"))
        for entry in data.get("entries", []):
            entry_id = entry.get("entry_id")
            if isinstance(entry_id, str):
                ids.add(entry_id)
    return ids


def load_concept_slugs() -> dict[str, set[str]]:
    slugs = {"topics": set(), "people": set(), "meetings": set()}
    directories = {
        "topics": WIKI / "topics",
        "people": WIKI / "people",
        "meetings": WIKI / "meetings",
    }
    for key, directory in directories.items():
        for path in directory.rglob("*.md"):
            if path.name == "index.md":
                continue
            data, _errors = parse_frontmatter(path)
            slug = data.get("slug")
            if isinstance(slug, str) and slug:
                slugs[key].add(slug)
            else:
                slugs[key].add(path.stem)
    return slugs


def validate_event(path: Path, document_ids: set[str], concept_slugs: dict[str, set[str]]) -> list[str]:
    data, errors = parse_frontmatter(path)
    required_strings = ["type", "title", "description", "slug", "date", "status"]
    for key in required_strings:
        value = data.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path}: missing non-empty {key}")

    if data.get("type") != "Event":
        errors.append(f"{path}: type must be Event")
    if data.get("slug") != path.stem:
        errors.append(f"{path}: slug must match filename stem")

    for key in ["documents", "topics", "tags"]:
        if not isinstance(data.get(key), list) or not string_list(data, key):
            errors.append(f"{path}: {key} must be a non-empty YAML list")

    for document in string_list(data, "documents"):
        if document not in document_ids:
            errors.append(f"{path}: unknown document entry_id: {document}")

    for topic in string_list(data, "topics"):
        if topic not in concept_slugs["topics"]:
            errors.append(f"{path}: unknown topic slug: {topic}")

    for person in string_list(data, "people"):
        if person not in concept_slugs["people"]:
            errors.append(f"{path}: unknown people slug: {person}")

    for meeting in string_list(data, "meetings"):
        if meeting not in concept_slugs["meetings"]:
            errors.append(f"{path}: unknown meeting slug: {meeting}")

    return errors


def main() -> int:
    document_ids = load_document_ids()
    concept_slugs = load_concept_slugs()
    errors: list[str] = []

    for path in sorted(EVENTS.glob("*.md")):
        if path.name == "index.md":
            continue
        errors.extend(validate_event(path, document_ids, concept_slugs))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Event pages OK: {EVENTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
