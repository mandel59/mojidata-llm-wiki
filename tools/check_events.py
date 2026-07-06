#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
EVENTS = WIKI / "events"

KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")


def split_frontmatter(path: Path, text: str) -> tuple[str | None, list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, []
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "\n".join(lines[1:index]), []
    return None, [f"{path}: frontmatter is not closed"]


def parse_value(value: str | None) -> object:
    if value is None:
        return ""
    value = value.strip()
    if value == "":
        return ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_value(item) for item in inner.split(",")]
    return value


def parse_frontmatter(path: Path) -> tuple[dict[str, object], list[str]]:
    header, errors = split_frontmatter(path, path.read_text(encoding="utf-8"))
    if header is None:
        return {}, errors + [f"{path}: event is missing YAML frontmatter"]

    data: dict[str, object] = {}
    for offset, line in enumerate(header.splitlines(), start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = KEY_RE.match(line)
        if not match:
            errors.append(f"{path}:{offset}: cannot parse frontmatter line")
            continue
        key, value = match.groups()
        if key in data:
            errors.append(f"{path}:{offset}: duplicate frontmatter key: {key}")
        data[key] = parse_value(value)
    return data, errors


def string_list(data: dict[str, object], key: str) -> list[str]:
    value = data.get(key)
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    return []


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
    required_strings = ["type", "title", "description", "slug", "kind", "date", "status"]
    for key in required_strings:
        value = data.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path}: missing non-empty {key}")

    if data.get("type") != "Event":
        errors.append(f"{path}: type must be Event")
    if data.get("kind") != "event":
        errors.append(f"{path}: kind must be event")
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
