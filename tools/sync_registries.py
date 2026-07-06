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
    write_jsonl,
)


DEFAULT_CONFIG = ROOT / "config" / "registries.json"
DEFAULT_CATALOG = ROOT / "catalog" / "registries"
DEFAULT_CACHE = ROOT / ".cache" / "unicode-registry"
USER_AGENT = "mojidata-llm-wiki/0.1 (+https://unicode.org/)"


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


def sync_one(
    registry_key: str,
    registry_config: dict,
    catalog_dir: Path,
    cache_dir: Path,
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

    entries = dedupe_entries(entries)
    target_dir = catalog_dir / registry_key
    write_jsonl(target_dir / "documents.jsonl", entries)

    metadata = {
        "registry": registry_key,
        "name": registry_config["name"],
        "latest_only": latest_only,
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
    parser.add_argument("--catalog-dir", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    config = load_config(args.config)
    registries = config["registries"]
    selected = registries.keys() if args.registry == "all" else [args.registry]

    for registry_key in selected:
        metadata = sync_one(
            registry_key,
            registries[registry_key],
            args.catalog_dir,
            args.cache_dir,
            args.latest_only,
            args.offline,
            args.refresh,
        )
        print(f"{registry_key}: {metadata['document_count']} documents from {len(metadata['registers'])} register(s)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
