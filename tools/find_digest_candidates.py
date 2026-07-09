#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

try:
    from .cli_support import configure_utf8_stdio
    from .unicode_registry import parse_doc_number
    from .wiki_store import Concept, ROOT, WIKI, concept_matches_lookup, load_concepts, normalize_lookup_key, scalar
except ImportError:
    from cli_support import configure_utf8_stdio
    from unicode_registry import parse_doc_number
    from wiki_store import Concept, ROOT, WIKI, concept_matches_lookup, load_concepts, normalize_lookup_key, scalar


CATALOG = ROOT / "catalog" / "registries"
DEFAULT_FETCH_CACHE = ROOT / ".cache" / "unicode-docs"
FETCH_SUCCESS_INDEX = "cache-index.jsonl"
FETCH_FAILURE_INDEX = "fetch-failures.jsonl"
MENTIONED_DOC_RE = re.compile(
    r"(?:"
    r"\b(?:"
    r"L2/\d{2}-\d{3}(?:R[0-9A-Z]*)?"
    r"|WG2\s*N\d{3,4}(?:R\d*)?"
    r"|IRG\s+N\d{3,4}(?:R\d*)?"
    r")\b"
    r"|(?<![A-Za-z0-9_-])(?-i:N\d{3,4}(?:R\d*)?)\b"
    r")",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class CatalogEntry:
    registry: str
    entry_id: str
    doc_number: str
    date: str
    subject: str
    source: str
    status: str
    document_url: str | None

    @property
    def available(self) -> bool:
        return self.status == "available" and bool(self.document_url)


@dataclass(frozen=True)
class Reference:
    concept_id: str
    rel_path: str
    source_type: str
    kind: str
    detail: str


@dataclass(frozen=True)
class DigestCandidate:
    entry: CatalogEntry
    references: tuple[Reference, ...]

    @property
    def source_count(self) -> int:
        return len({reference.rel_path for reference in self.references})

    @property
    def reference_count(self) -> int:
        return len(self.references)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="List available catalog documents referenced by the wiki but missing Source Document pages."
    )
    parser.add_argument("--topic", action="append", default=[], help="Limit source pages to a topic or its related pages.")
    parser.add_argument("--exclude-topic", action="append", default=[], help="Exclude a topic and its related pages.")
    parser.add_argument(
        "--source-type",
        action="append",
        default=[],
        help="Limit source pages by concept type, e.g. Topic, Source Document, Event.",
    )
    parser.add_argument(
        "--status",
        choices=["available", "available-or-referenced", "all"],
        default="available",
        help="Catalog document statuses to report.",
    )
    parser.add_argument("--min-refs", type=int, default=1, help="Minimum reference count for a candidate.")
    parser.add_argument("--limit", type=int, help="Maximum number of candidates to print.")
    parser.add_argument("--no-body-mentions", action="store_true", help="Only use frontmatter documents relations.")
    parser.add_argument(
        "--include-fetch-failures",
        action="store_true",
        help="Include documents whose latest local fetch attempt failed.",
    )
    parser.add_argument(
        "--fetch-cache-dir",
        type=Path,
        default=DEFAULT_FETCH_CACHE,
        help="Directory containing cache-index.jsonl and fetch-failures.jsonl.",
    )
    parser.add_argument("--format", choices=["table", "json"], default="table")
    return parser.parse_args(argv)


def load_catalog(catalog_root: Path = CATALOG) -> dict[str, CatalogEntry]:
    entries: dict[str, CatalogEntry] = {}
    for path in sorted(catalog_root.glob("*/documents.jsonl")):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            try:
                data = json.loads(line)
            except json.JSONDecodeError as error:
                raise SystemExit(f"{path}:{line_number}: invalid JSON: {error}") from error
            entry_id = data.get("entry_id")
            if not isinstance(entry_id, str) or not entry_id:
                continue
            entries[entry_id] = CatalogEntry(
                registry=str(data.get("registry") or ""),
                entry_id=entry_id,
                doc_number=str(data.get("doc_number") or ""),
                date=str(data.get("date") or ""),
                subject=str(data.get("subject") or ""),
                source=str(data.get("source") or ""),
                status=str(data.get("status") or ""),
                document_url=data.get("document_url") if isinstance(data.get("document_url"), str) else None,
            )
    return entries


def _read_jsonl(path: Path) -> Iterable[dict[str, object]]:
    if not path.exists():
        return []
    records: list[dict[str, object]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError as error:
            raise SystemExit(f"{path}:{line_number}: invalid JSON: {error}") from error
        if isinstance(data, dict):
            records.append(data)
    return records


def load_latest_fetch_failures(cache_dir: Path = DEFAULT_FETCH_CACHE) -> set[str]:
    latest: dict[str, tuple[str, str]] = {}
    success_path = cache_dir / FETCH_SUCCESS_INDEX
    failure_path = cache_dir / FETCH_FAILURE_INDEX

    for record in _read_jsonl(success_path):
        entry_id = record.get("entry_id")
        timestamp = record.get("fetched_at")
        if isinstance(entry_id, str) and entry_id and isinstance(timestamp, str):
            latest[entry_id] = max(latest.get(entry_id, ("", "")), (timestamp, "success"))

    for record in _read_jsonl(failure_path):
        entry_id = record.get("entry_id")
        timestamp = record.get("failed_at")
        if isinstance(entry_id, str) and entry_id and isinstance(timestamp, str):
            latest[entry_id] = max(latest.get(entry_id, ("", "")), (timestamp, "failure"))

    return {entry_id for entry_id, (_timestamp, state) in latest.items() if state == "failure"}


def catalog_by_doc_number(catalog: dict[str, CatalogEntry]) -> dict[str, CatalogEntry]:
    by_doc_number: dict[str, CatalogEntry] = {}
    for entry in catalog.values():
        parsed = parse_doc_number(entry.registry, entry.doc_number)
        if parsed is None:
            continue
        _display, canonical, _entry_id = parsed
        by_doc_number[normalize_lookup_key(canonical)] = entry
    return by_doc_number


def concept_alias_map(concepts: dict[str, Concept]) -> dict[str, str]:
    aliases: dict[str, str] = {}
    for cid, concept in concepts.items():
        aliases.setdefault(normalize_lookup_key(cid), cid)
        for alias in concept.aliases:
            aliases.setdefault(normalize_lookup_key(alias), cid)
    return aliases


def resolve_topic(name: str, concepts: dict[str, Concept]) -> str:
    matches = [
        cid
        for cid, concept in concepts.items()
        if concept.type == "Topic" and concept_matches_lookup(concept, name)
    ]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise SystemExit(f"topic not found: {name}")
    raise SystemExit(f"ambiguous topic: {name}: {', '.join(matches)}")


def concept_in_topics(concept: Concept, topic_ids: set[str]) -> bool:
    if not topic_ids:
        return True
    return concept.id in topic_ids or bool(topic_ids & set(concept.relations.get("topics", [])))


def source_concepts(
    concepts: dict[str, Concept],
    include_topics: set[str],
    exclude_topics: set[str],
    source_types: set[str],
) -> list[Concept]:
    result: list[Concept] = []
    for concept in concepts.values():
        if source_types and concept.type not in source_types:
            continue
        if include_topics and not concept_in_topics(concept, include_topics):
            continue
        if exclude_topics and concept_in_topics(concept, exclude_topics):
            continue
        result.append(concept)
    return sorted(result, key=lambda concept: concept.rel_path)


def candidate_status_matches(entry: CatalogEntry, status: str) -> bool:
    if status == "all":
        return True
    if status == "available-or-referenced":
        return entry.available or entry.status == "referenced"
    return entry.available


def has_existing_document_page(entry: CatalogEntry, concepts: dict[str, Concept], aliases: dict[str, str]) -> bool:
    if entry.entry_id in concepts:
        return True
    for name in [entry.entry_id, entry.doc_number]:
        if name and normalize_lookup_key(name) in aliases:
            return True
    return False


def entry_from_reference(
    value: str,
    catalog: dict[str, CatalogEntry],
    by_doc_number: dict[str, CatalogEntry],
    concepts: dict[str, Concept],
    aliases: dict[str, str],
    status: str,
    exclude_entry_ids: set[str],
) -> CatalogEntry | None:
    if normalize_lookup_key(value) in aliases:
        return None
    entry = catalog.get(value)
    if entry is None:
        entry = by_doc_number.get(normalize_lookup_key(value))
    if entry is None:
        return None
    if not candidate_status_matches(entry, status):
        return None
    if entry.entry_id in exclude_entry_ids:
        return None
    if has_existing_document_page(entry, concepts, aliases):
        return None
    return entry


def mentioned_catalog_entry(
    mention: str, by_doc_number: dict[str, CatalogEntry], context_registry: str
) -> CatalogEntry | None:
    if re.match(r"^L2/", mention, re.IGNORECASE):
        candidates = [("utc", mention)]
    elif re.match(r"^WG2\s*N", mention, re.IGNORECASE):
        candidates = [("wg2", mention)]
    elif re.match(r"^IRG\s+N", mention, re.IGNORECASE):
        candidates = [("irg", mention)]
    elif re.match(r"^N\d{3,4}(?:R\d*)?$", mention):
        if context_registry == "wg2":
            candidates = [("wg2", mention)]
        elif context_registry == "irg":
            candidates = [("irg", f"IRG {mention}")]
        else:
            return None
    else:
        return None

    for registry, text in candidates:
        parsed = parse_doc_number(registry, text)
        if parsed is None:
            continue
        _display, canonical, _entry_id = parsed
        entry = by_doc_number.get(normalize_lookup_key(canonical))
        if entry is not None:
            return entry
    return None


def collect_candidates(
    concepts: dict[str, Concept],
    catalog: dict[str, CatalogEntry],
    *,
    topic_names: Iterable[str] = (),
    exclude_topic_names: Iterable[str] = (),
    source_types: Iterable[str] = (),
    status: str = "available",
    include_body_mentions: bool = True,
    exclude_entry_ids: Iterable[str] = (),
) -> list[DigestCandidate]:
    aliases = concept_alias_map(concepts)
    by_doc_number = catalog_by_doc_number(catalog)
    include_topics = {resolve_topic(name, concepts) for name in topic_names}
    exclude_topics = {resolve_topic(name, concepts) for name in exclude_topic_names}
    source_type_set = set(source_types)
    excluded = set(exclude_entry_ids)

    references_by_entry: dict[str, list[Reference]] = {}
    for concept in source_concepts(concepts, include_topics, exclude_topics, source_type_set):
        for value in concept.relations.get("documents", []):
            entry = entry_from_reference(value, catalog, by_doc_number, concepts, aliases, status, excluded)
            if entry is None:
                continue
            references_by_entry.setdefault(entry.entry_id, []).append(
                Reference(concept.id, concept.rel_path, concept.type, "frontmatter", value)
            )

        if not include_body_mentions:
            continue
        context_registry = scalar(concept.frontmatter, "registry")
        for line_number, line in enumerate(concept.body.splitlines(), start=1):
            for match in MENTIONED_DOC_RE.finditer(line):
                mention = match.group(0)
                if normalize_lookup_key(mention) in aliases:
                    continue
                entry = mentioned_catalog_entry(mention, by_doc_number, context_registry)
                if entry is None:
                    continue
                if not candidate_status_matches(entry, status):
                    continue
                if entry.entry_id in excluded:
                    continue
                if has_existing_document_page(entry, concepts, aliases):
                    continue
                references_by_entry.setdefault(entry.entry_id, []).append(
                    Reference(concept.id, concept.rel_path, concept.type, "body", f"{mention}@{line_number}")
                )

    candidates = [
        DigestCandidate(catalog[entry_id], tuple(references))
        for entry_id, references in references_by_entry.items()
        if entry_id in catalog
    ]
    return sorted(
        candidates,
        key=lambda item: (-item.source_count, -item.reference_count, item.entry.date, item.entry.entry_id),
    )


def candidate_to_dict(candidate: DigestCandidate) -> dict[str, object]:
    entry = candidate.entry
    return {
        "entry_id": entry.entry_id,
        "doc_number": entry.doc_number,
        "registry": entry.registry,
        "date": entry.date,
        "subject": entry.subject,
        "source": entry.source,
        "status": entry.status,
        "document_url": entry.document_url,
        "source_count": candidate.source_count,
        "reference_count": candidate.reference_count,
        "references": [
            {
                "concept_id": reference.concept_id,
                "path": reference.rel_path,
                "type": reference.source_type,
                "kind": reference.kind,
                "detail": reference.detail,
            }
            for reference in candidate.references
        ],
    }


def table_cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_table(candidates: list[DigestCandidate]) -> str:
    lines = [
        "| pages | refs | entry_id | doc_number | date | subject | examples |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for candidate in candidates:
        entry = candidate.entry
        examples = ", ".join(
            f"{reference.rel_path}:{reference.kind}" for reference in candidate.references[:3]
        )
        lines.append(
            "| "
            + " | ".join(
                table_cell(value)
                for value in [
                    candidate.source_count,
                    candidate.reference_count,
                    entry.entry_id,
                    entry.doc_number,
                    entry.date,
                    entry.subject,
                    examples,
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    configure_utf8_stdio()
    args = parse_args(argv or sys.argv[1:])
    concepts = load_concepts(WIKI)
    catalog = load_catalog(CATALOG)
    candidates = collect_candidates(
        concepts,
        catalog,
        topic_names=args.topic,
        exclude_topic_names=args.exclude_topic,
        source_types=args.source_type,
        status=args.status,
        include_body_mentions=not args.no_body_mentions,
        exclude_entry_ids=() if args.include_fetch_failures else load_latest_fetch_failures(args.fetch_cache_dir),
    )
    candidates = [candidate for candidate in candidates if candidate.reference_count >= args.min_refs]
    if args.limit is not None:
        candidates = candidates[: args.limit]

    if args.format == "json":
        print(json.dumps([candidate_to_dict(candidate) for candidate in candidates], ensure_ascii=False, indent=2))
    else:
        print(render_table(candidates))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
