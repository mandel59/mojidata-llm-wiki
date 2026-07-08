#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from cli_support import configure_utf8_stdio
except ModuleNotFoundError:
    from tools.cli_support import configure_utf8_stdio

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.unicode_registry import read_jsonl


DEFAULT_CATALOG = ROOT / "catalog" / "registries"
DEFAULT_DERIVED_DOCUMENTS = ROOT / "config" / "derived_documents.json"
REGISTRIES = ("utc", "wg2", "irg")
REQUIRED_FIELDS = {
    "entry_id",
    "registry",
    "doc_number",
    "display_number",
    "subject",
    "source",
    "date",
    "status",
    "document_url",
    "related_links",
    "register_url",
}


def validate_entry(entry: dict, location: str, expected_registry: str | None = None) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_FIELDS - set(entry)
    if missing:
        errors.append(f"{location}: missing fields: {', '.join(sorted(missing))}")
    if expected_registry is not None and entry.get("registry") != expected_registry:
        errors.append(f"{location}: registry mismatch: {entry.get('registry')!r}")
    document_url = entry.get("document_url")
    if isinstance(document_url, str) and ".cache/" in document_url:
        errors.append(f"{location}: document_url points at local cache")
    return errors


def check_registry(catalog_dir: Path, registry: str) -> tuple[int, list[str]]:
    path = catalog_dir / registry / "documents.jsonl"
    if not path.exists():
        return 0, []

    errors: list[str] = []
    entries = read_jsonl(path)
    seen: set[tuple[str, str | None]] = set()
    for index, entry in enumerate(entries, start=1):
        location = f"{path}:{index}"
        errors.extend(validate_entry(entry, location, expected_registry=registry))
        key = (entry.get("entry_id", ""), entry.get("document_url"))
        if key in seen:
            errors.append(f"{location}: duplicate entry_id/url: {key}")
        seen.add(key)
    return len(entries), errors


def load_catalog_entries(catalog_dir: Path) -> dict[tuple[str, str], dict]:
    entries: dict[tuple[str, str], dict] = {}
    for registry in REGISTRIES:
        path = catalog_dir / registry / "documents.jsonl"
        if not path.exists():
            continue
        for entry in read_jsonl(path):
            registry_key = entry.get("registry")
            entry_id = entry.get("entry_id")
            if isinstance(registry_key, str) and isinstance(entry_id, str):
                entries[(registry_key, entry_id)] = entry
    return entries


def check_derived_documents(path: Path, catalog_dir: Path) -> tuple[int, list[str]]:
    if not path.exists():
        return 0, []

    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return 0, [f"{path}: invalid JSON: {error}"]

    entries = data.get("entries")
    if not isinstance(entries, list):
        return 0, [f"{path}: entries must be a list"]

    catalog_entries = load_catalog_entries(catalog_dir)
    seen: set[tuple[str, str]] = set()
    for index, entry in enumerate(entries, start=1):
        location = f"{path}:entries[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{location}: entry must be an object")
            continue

        registry = entry.get("registry")
        expected_registry = registry if isinstance(registry, str) and registry in REGISTRIES else None
        errors.extend(validate_entry(entry, location, expected_registry=expected_registry))
        if registry not in REGISTRIES:
            errors.append(f"{location}: registry must be one of {', '.join(REGISTRIES)}")
        if entry.get("catalog_source") != "derived":
            errors.append(f"{location}: catalog_source must be 'derived'")
        provenance = entry.get("provenance")
        if not isinstance(provenance, list) or not provenance:
            errors.append(f"{location}: provenance must be a non-empty list")

        entry_id = entry.get("entry_id")
        if not isinstance(registry, str) or not isinstance(entry_id, str):
            continue
        key = (registry, entry_id)
        if key in seen:
            errors.append(f"{location}: duplicate derived entry_id: {entry_id}")
        seen.add(key)

        catalog_entry = catalog_entries.get(key)
        if catalog_entry is None:
            errors.append(f"{location}: derived entry is not merged into catalog; run sync_registries.py")
        elif catalog_entry.get("catalog_source") != "derived":
            errors.append(f"{location}: derived entry shadows a generated registry entry: {entry_id}")

    return len(entries), errors


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate generated registry manifests.")
    parser.add_argument("--catalog-dir", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--derived-documents", type=Path, default=DEFAULT_DERIVED_DOCUMENTS)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    configure_utf8_stdio()
    args = parse_args(argv or sys.argv[1:])
    total = 0
    all_errors: list[str] = []
    for registry in REGISTRIES:
        count, errors = check_registry(args.catalog_dir, registry)
        total += count
        all_errors.extend(errors)
        print(f"{registry}: {count} document(s)")
    derived_count, derived_errors = check_derived_documents(args.derived_documents, args.catalog_dir)
    all_errors.extend(derived_errors)
    print(f"derived overlay: {derived_count} document(s)")

    if all_errors:
        for error in all_errors:
            print(error, file=sys.stderr)
        return 1

    print(f"total: {total} document(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
