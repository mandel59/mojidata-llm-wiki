#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.unicode_registry import read_jsonl


DEFAULT_CATALOG = ROOT / "catalog" / "registries"
DEFAULT_CACHE = ROOT / ".cache" / "unicode-docs"
USER_AGENT = "mojidata-llm-wiki/0.1 (+https://unicode.org/)"


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-").lower()


def load_entries(catalog_dir: Path, registry: str) -> list[dict]:
    registries = ["utc", "wg2", "irg"] if registry == "all" else [registry]
    entries: list[dict] = []
    for key in registries:
        entries.extend(read_jsonl(catalog_dir / key / "documents.jsonl"))
    return entries


def select_entries(entries: list[dict], docs: list[str], grep: str | None, all_entries: bool) -> list[dict]:
    if all_entries:
        return entries
    wanted = {doc.lower() for doc in docs}
    pattern = re.compile(grep, re.IGNORECASE) if grep else None
    selected = []
    for entry in entries:
        haystack = " ".join(
            str(entry.get(key, ""))
            for key in ["entry_id", "doc_number", "display_number", "subject", "source", "date"]
        )
        if entry.get("entry_id", "").lower() in wanted or entry.get("doc_number", "").lower() in wanted:
            selected.append(entry)
        elif pattern and pattern.search(haystack):
            selected.append(entry)
    return selected


def fetch_binary(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=120) as response:
        return response.read()


def filename_for(entry: dict) -> str:
    url = entry.get("document_url") or ""
    name = Path(urlparse(url).path).name
    if name:
        return safe_name(name)
    return safe_name(entry["entry_id"]) + ".bin"


def materialize(entry: dict, cache_dir: Path, refresh: bool = False) -> dict:
    if not entry.get("document_url"):
        raise ValueError(f"{entry['entry_id']} has no document_url")

    target_dir = cache_dir / entry["registry"] / safe_name(entry["entry_id"])
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / filename_for(entry)

    if target.exists() and not refresh:
        body = target.read_bytes()
        state = "cached"
    else:
        body = fetch_binary(entry["document_url"])
        target.write_bytes(body)
        state = "fetched"

    return {
        "entry_id": entry["entry_id"],
        "registry": entry["registry"],
        "doc_number": entry["doc_number"],
        "url": entry["document_url"],
        "path": str(target),
        "sha256": hashlib.sha256(body).hexdigest(),
        "bytes": len(body),
        "state": state,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch selected documents from catalog manifests into ignored local cache.")
    parser.add_argument("--registry", choices=["all", "utc", "wg2", "irg"], default="all")
    parser.add_argument("--doc", action="append", default=[], help="Document number or entry_id. Can be repeated.")
    parser.add_argument("--grep", help="Case-insensitive regex matched against document metadata.")
    parser.add_argument("--all", action="store_true", help="Fetch every document with a URL. Use carefully.")
    parser.add_argument("--limit", type=int, help="Maximum number of matched documents to fetch.")
    parser.add_argument("--refresh", action="store_true", help="Refetch even when the file already exists.")
    parser.add_argument("--catalog-dir", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if not args.all and not args.doc and not args.grep:
        print("select at least one of --doc, --grep, or --all", file=sys.stderr)
        return 2

    entries = load_entries(args.catalog_dir, args.registry)
    selected = [entry for entry in select_entries(entries, args.doc, args.grep, args.all) if entry.get("document_url")]
    if args.limit is not None:
        selected = selected[: args.limit]

    args.cache_dir.mkdir(parents=True, exist_ok=True)
    index_path = args.cache_dir / "cache-index.jsonl"
    with index_path.open("a", encoding="utf-8") as index:
        for entry in selected:
            record = materialize(entry, args.cache_dir, refresh=args.refresh)
            index.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            index.write("\n")
            print(f"{record['state']}: {record['entry_id']} -> {record['path']}")

    print(f"{len(selected)} document(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
