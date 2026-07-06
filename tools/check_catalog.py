#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.unicode_registry import read_jsonl


DEFAULT_CATALOG = ROOT / "catalog" / "registries"
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


def check_registry(catalog_dir: Path, registry: str) -> tuple[int, list[str]]:
    path = catalog_dir / registry / "documents.jsonl"
    if not path.exists():
        return 0, []

    errors: list[str] = []
    entries = read_jsonl(path)
    seen: set[tuple[str, str | None]] = set()
    for index, entry in enumerate(entries, start=1):
        missing = REQUIRED_FIELDS - set(entry)
        if missing:
            errors.append(f"{path}:{index}: missing fields: {', '.join(sorted(missing))}")
        if entry.get("registry") != registry:
            errors.append(f"{path}:{index}: registry mismatch: {entry.get('registry')!r}")
        key = (entry.get("entry_id", ""), entry.get("document_url"))
        if key in seen:
            errors.append(f"{path}:{index}: duplicate entry_id/url: {key}")
        seen.add(key)
        if entry.get("document_url") and ".cache/" in entry["document_url"]:
            errors.append(f"{path}:{index}: document_url points at local cache")
    return len(entries), errors


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate generated registry manifests.")
    parser.add_argument("--catalog-dir", type=Path, default=DEFAULT_CATALOG)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    total = 0
    all_errors: list[str] = []
    for registry in ["utc", "wg2", "irg"]:
        count, errors = check_registry(args.catalog_dir, registry)
        total += count
        all_errors.extend(errors)
        print(f"{registry}: {count} document(s)")

    if all_errors:
        for error in all_errors:
            print(error, file=sys.stderr)
        return 1

    print(f"total: {total} document(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
