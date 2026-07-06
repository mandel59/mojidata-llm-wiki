#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.unicode_registry import (
    cache_path_for_url,
    dedupe_entries,
    discover_register_urls,
    load_config,
    parse_register_documents,
    read_jsonl,
    write_jsonl,
)


DEFAULT_CONFIG = ROOT / "config" / "registries.json"
DEFAULT_DERIVED_DOCUMENTS = ROOT / "config" / "derived_documents.json"
DEFAULT_CATALOG = ROOT / "catalog" / "registries"
DEFAULT_CACHE = ROOT / ".cache" / "unicode-registry"
USER_AGENT = "mojidata-llm-wiki/0.1 (+https://github.com/mandel59/mojidata-llm-wiki)"


def fetch_text(url: str, cache_dir: Path, offline: bool = False, refresh: bool = False) -> str:
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path = cache_path_for_url(cache_dir, url)
    if offline:
        if not cache_path.exists():
            raise FileNotFoundError(f"offline cache miss: {cache_path} for {url}")
        return cache_path.read_text(encoding="utf-8", errors="replace")
    if cache_path.exists() and not refresh:
        return cache_path.read_text(encoding="utf-8", errors="replace")

    request = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=60) as response:
            body = response.read()
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RuntimeError(f"failed to fetch {url}: {exc}") from exc

    text = body.decode("utf-8", errors="replace")
    cache_path.write_text(text, encoding="utf-8")
    return text


def load_derived_documents(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    return data.get("entries", [])


def merge_derived_entries(entries: list[dict], registry_key: str, derived_entries: list[dict]) -> list[dict]:
    existing_entry_ids = {entry["entry_id"] for entry in entries}
    merged = list(entries)
    for entry in derived_entries:
        if entry.get("registry") != registry_key:
            continue
        if entry["entry_id"] in existing_entry_ids:
            continue
        merged.append(entry)
        existing_entry_ids.add(entry["entry_id"])
    return merged


def load_register_metadata(path: Path) -> dict | None:
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def merge_latest_entries(existing_entries: list[dict], latest_entries: list[dict]) -> list[dict]:
    latest_ids = {(entry["registry"], entry["entry_id"]) for entry in latest_entries}
    preserved_entries = [
        entry
        for entry in existing_entries
        if (entry["registry"], entry["entry_id"]) not in latest_ids
    ]
    return preserved_entries + latest_entries


def merge_register_metadata(existing_metadata: dict | None, latest_registers: list[dict]) -> list[dict]:
    if not existing_metadata:
        return latest_registers

    by_url = {
        register["url"]: dict(register)
        for register in existing_metadata.get("registers", [])
    }
    for register in latest_registers:
        by_url[register["url"]] = dict(register)
    return list(by_url.values())


def count_derived_entries(entries: list[dict], registry_key: str, derived_entries: list[dict]) -> int:
    derived_entry_ids = {
        entry["entry_id"]
        for entry in derived_entries
        if entry.get("registry") == registry_key
    }
    return sum(1 for entry in entries if entry["entry_id"] in derived_entry_ids)


def sync_one(
    registry_key: str,
    registry_config: dict,
    catalog_dir: Path,
    cache_dir: Path,
    derived_entries: list[dict],
    latest_only: bool,
    offline: bool,
    refresh: bool,
) -> dict:
    registry_cache = cache_dir / registry_key
    if latest_only:
        register_urls = [registry_config["latest_url"]]
    else:
        root_html = fetch_text(registry_config["root_url"], registry_cache, offline=offline, refresh=refresh)
        register_urls = discover_register_urls(registry_config, root_html, latest_only=False)

    entries: list[dict] = []
    registers: list[dict] = []
    for register_url in register_urls:
        html = fetch_text(register_url, registry_cache, offline=offline, refresh=refresh)
        register_entries = parse_register_documents(registry_key, html, register_url)
        entries.extend(register_entries)
        registers.append(
            {
                "url": register_url,
                "document_count": len(register_entries),
            }
        )

    fetched_register_document_count = len(entries)
    target_dir = catalog_dir / registry_key
    existing_metadata = load_register_metadata(target_dir / "registers.json")
    existing_entries: list[dict] = []
    if latest_only:
        existing_entries = read_jsonl(target_dir / "documents.jsonl")
        if existing_entries:
            entries = merge_latest_entries(existing_entries, entries)
            registers = merge_register_metadata(existing_metadata, registers)

    register_document_count = len(entries)
    entries = merge_derived_entries(entries, registry_key, derived_entries)
    entries = dedupe_entries(entries)
    write_jsonl(target_dir / "documents.jsonl", entries)

    metadata = {
        "registry": registry_key,
        "name": registry_config["name"],
        "latest_only": bool(latest_only and not existing_entries),
        "last_sync_latest_only": latest_only,
        "last_sync_register_document_count": fetched_register_document_count,
        "derived_document_count": count_derived_entries(entries, registry_key, derived_entries),
        "document_count": len(entries),
        "registers": registers,
    }
    target_dir.mkdir(parents=True, exist_ok=True)
    with (target_dir / "registers.json").open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(metadata, ensure_ascii=False, indent=2, sort_keys=True))
        fh.write("\n")
    return metadata


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync unicode.org document registries into commit-safe manifests.")
    parser.add_argument("--registry", choices=["all", "utc", "wg2", "irg"], default="all")
    parser.add_argument("--latest-only", action="store_true", help="Only sync each registry's current register page.")
    parser.add_argument("--offline", action="store_true", help="Use cached registry HTML only.")
    parser.add_argument("--refresh", action="store_true", help="Refetch registry HTML even when cached.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--derived-documents", type=Path, default=DEFAULT_DERIVED_DOCUMENTS)
    parser.add_argument("--catalog-dir", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    config = load_config(args.config)
    derived_entries = load_derived_documents(args.derived_documents)
    registries = config["registries"]
    selected = registries.keys() if args.registry == "all" else [args.registry]

    for registry_key in selected:
        metadata = sync_one(
            registry_key,
            registries[registry_key],
            args.catalog_dir,
            args.cache_dir,
            derived_entries,
            args.latest_only,
            args.offline,
            args.refresh,
        )
        print(f"{registry_key}: {metadata['document_count']} documents from {len(metadata['registers'])} register(s)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
