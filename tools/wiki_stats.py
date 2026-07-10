#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

try:
    from .cli_support import configure_utf8_stdio
    from .find_digest_candidates import (
        DigestCandidate,
        CatalogEntry,
        collect_candidates,
        concept_alias_map,
        has_existing_document_page,
        load_catalog,
        load_latest_fetch_failures,
    )
    from .wiki_store import Concept, ROOT, WIKI, load_concepts
except ImportError:
    from cli_support import configure_utf8_stdio
    from find_digest_candidates import (
        DigestCandidate,
        CatalogEntry,
        collect_candidates,
        concept_alias_map,
        has_existing_document_page,
        load_catalog,
        load_latest_fetch_failures,
    )
    from wiki_store import Concept, ROOT, WIKI, load_concepts


CATALOG = ROOT / "catalog" / "registries"
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize wiki/catalog coverage and next-work signals.")
    parser.add_argument("--wiki", type=Path, default=WIKI)
    parser.add_argument("--catalog-root", type=Path, default=CATALOG)
    parser.add_argument("--top", type=int, default=15, help="Rows to show in ranked sections.")
    parser.add_argument("--recent-since", default="2026-01-01", help="YYYY-MM-DD lower bound for recent catalog gaps.")
    parser.add_argument(
        "--include-fetch-failures",
        action="store_true",
        help="Include documents whose latest local fetch attempt failed in digest candidate counts.",
    )
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    return parser.parse_args(argv)


def count_by(values: Iterable[str]) -> dict[str, int]:
    return dict(sorted(Counter(values).items()))


def table(headers: list[str], rows: Iterable[Iterable[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(cell(value) for value in row) + " |")
    return "\n".join(lines)


def cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def source_document_coverage(concepts: dict[str, Concept], catalog: dict[str, CatalogEntry]) -> list[dict[str, object]]:
    aliases = concept_alias_map(concepts)
    rows: list[dict[str, object]] = []
    registries = sorted({entry.registry for entry in catalog.values()})
    for registry in registries:
        entries = [entry for entry in catalog.values() if entry.registry == registry]
        available = [entry for entry in entries if entry.available]
        paged = [entry for entry in entries if has_existing_document_page(entry, concepts, aliases)]
        available_paged = [entry for entry in available if has_existing_document_page(entry, concepts, aliases)]
        rows.append(
            {
                "registry": registry,
                "catalog": len(entries),
                "available": len(available),
                "paged": len(paged),
                "available_paged": len(available_paged),
                "available_coverage_pct": round(100 * len(available_paged) / len(available), 1) if available else 0.0,
            }
        )
    return rows


def source_documents_by_registry(concepts: dict[str, Concept]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for concept in concepts.values():
        if concept.type != "Source Document":
            continue
        registry = concept.frontmatter.get("registry")
        counts[str(registry) if isinstance(registry, str) and registry else "(none)"] += 1
    return dict(sorted(counts.items()))


def source_documents_by_document_type(concepts: dict[str, Concept]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for concept in concepts.values():
        if concept.type != "Source Document":
            continue
        document_type = concept.frontmatter.get("document_type")
        counts[str(document_type) if isinstance(document_type, str) and document_type else "(none)"] += 1
    return dict(sorted(counts.items()))


def unresolved_relation_summary(
    concepts: dict[str, Concept], catalog: dict[str, CatalogEntry], top: int
) -> dict[str, object]:
    by_key: Counter[str] = Counter()
    by_status: Counter[str] = Counter()
    pages: list[dict[str, object]] = []
    for concept in concepts.values():
        total = 0
        for key, values in concept.unresolved_relations.items():
            by_key[key] += len(values)
            total += len(values)
            for value in values:
                if key != "documents":
                    by_status["unmaterialized_concept"] += 1
                    continue
                entry = catalog.get(value)
                if entry is None:
                    by_status["unknown_document"] += 1
                elif entry.available:
                    by_status["available_document"] += 1
                else:
                    by_status["unavailable_document"] += 1
        if total:
            pages.append(
                {
                    "id": concept.id,
                    "type": concept.type,
                    "path": concept.rel_path,
                    "unresolved": total,
                    "keys": ", ".join(f"{key}:{len(values)}" for key, values in sorted(concept.unresolved_relations.items())),
                }
            )
    pages.sort(key=lambda row: (-int(row["unresolved"]), str(row["path"])))
    return {
        "by_key": dict(sorted(by_key.items())),
        "by_status": dict(sorted(by_status.items())),
        "top_pages": pages[:top],
        "total": sum(by_key.values()),
    }


def synthesis_coverage(concepts: dict[str, Concept]) -> dict[str, object]:
    topic_ids = {concept.id for concept in concepts.values() if concept.type == "Topic"}
    memberships: defaultdict[str, list[str]] = defaultdict(list)
    syntheses: list[dict[str, object]] = []
    for concept in sorted(concepts.values(), key=lambda item: item.id):
        if concept.type != "Synthesis":
            continue
        members = set(concept.relations.get("topics", []))
        raw_members = concept.frontmatter.get("members")
        if isinstance(raw_members, list):
            members.update(item for item in raw_members if isinstance(item, str))
        for member in members:
            memberships[member].append(concept.id)
        syntheses.append({"id": concept.id, "title": concept.title, "members": len(members)})

    unassigned = sorted(topic_id for topic_id in topic_ids if topic_id not in memberships)
    multi_assigned = sorted(
        {"topic": topic_id, "syntheses": ", ".join(sorted(names))}
        for topic_id, names in memberships.items()
        if topic_id in topic_ids and len(names) > 1
    )
    return {"syntheses": syntheses, "unassigned_topics": unassigned, "multi_assigned_topics": multi_assigned}


def recent_unpaged_available(
    concepts: dict[str, Concept], catalog: dict[str, CatalogEntry], since: str, top: int
) -> list[dict[str, object]]:
    aliases = concept_alias_map(concepts)
    entries = [
        entry
        for entry in catalog.values()
        if entry.available
        and ISO_DATE_RE.match(entry.date)
        and entry.date >= since
        and not has_existing_document_page(entry, concepts, aliases)
    ]
    entries.sort(key=lambda entry: (entry.date, entry.registry, entry.entry_id), reverse=True)
    return [
        {
            "date": entry.date,
            "registry": entry.registry,
            "entry_id": entry.entry_id,
            "doc_number": entry.doc_number,
            "subject": entry.subject,
        }
        for entry in entries[:top]
    ]


def digest_candidate_rows(candidates: list[DigestCandidate], top: int) -> list[dict[str, object]]:
    return [
        {
            "pages": candidate.source_count,
            "refs": candidate.reference_count,
            "registry": candidate.entry.registry,
            "entry_id": candidate.entry.entry_id,
            "doc_number": candidate.entry.doc_number,
            "date": candidate.entry.date,
            "subject": candidate.entry.subject,
        }
        for candidate in candidates[:top]
    ]


def build_stats(args: argparse.Namespace) -> dict[str, object]:
    concepts = load_concepts(args.wiki)
    catalog = load_catalog(args.catalog_root)
    failed_fetch_entry_ids = set() if args.include_fetch_failures else load_latest_fetch_failures()
    candidates = collect_candidates(concepts, catalog, status="available", exclude_entry_ids=failed_fetch_entry_ids)

    return {
        "concepts": {
            "total": len(concepts),
            "by_type": count_by(concept.type for concept in concepts.values()),
        },
        "source_documents": {
            "by_registry": source_documents_by_registry(concepts),
            "by_document_type": source_documents_by_document_type(concepts),
        },
        "catalog_coverage": source_document_coverage(concepts, catalog),
        "unresolved_relations": unresolved_relation_summary(concepts, catalog, args.top),
        "synthesis_coverage": synthesis_coverage(concepts),
        "digest_candidates": {
            "total": len(candidates),
            "excluded_fetch_failures": len(failed_fetch_entry_ids),
            "by_registry": count_by(candidate.entry.registry for candidate in candidates),
            "top": digest_candidate_rows(candidates, args.top),
        },
        "recent_unpaged_available": recent_unpaged_available(concepts, catalog, args.recent_since, args.top),
    }


def render_markdown(stats: dict[str, object]) -> str:
    concepts = stats["concepts"]  # type: ignore[index]
    source_documents = stats["source_documents"]  # type: ignore[index]
    unresolved = stats["unresolved_relations"]  # type: ignore[index]
    synthesis = stats["synthesis_coverage"]  # type: ignore[index]
    candidates = stats["digest_candidates"]  # type: ignore[index]

    parts: list[str] = ["# Wiki Stats", ""]
    parts.append(f"- Concepts: {concepts['total']}")  # type: ignore[index]
    parts.append(f"- Digest candidates: {candidates['total']}")  # type: ignore[index]
    if candidates.get("excluded_fetch_failures"):  # type: ignore[union-attr]
        parts.append(f"- Excluded fetch failures: {candidates['excluded_fetch_failures']}")  # type: ignore[index]
    parts.append(f"- Unresolved relation values: {unresolved['total']}")  # type: ignore[index]

    parts.extend(["", "## Concepts by Type", ""])
    parts.append(table(["type", "count"], sorted(concepts["by_type"].items())))  # type: ignore[index,union-attr]

    parts.extend(["", "## Source Documents by Registry", ""])
    parts.append(table(["registry", "count"], sorted(source_documents["by_registry"].items())))  # type: ignore[index,union-attr]

    parts.extend(["", "## Source Documents by Document Type", ""])
    parts.append(table(["document_type", "count"], sorted(source_documents["by_document_type"].items())))  # type: ignore[index,union-attr]

    parts.extend(["", "## Catalog Coverage", ""])
    parts.append(
        table(
            ["registry", "catalog", "available", "paged", "available_paged", "available_coverage_pct"],
            (
                [
                    row["registry"],
                    row["catalog"],
                    row["available"],
                    row["paged"],
                    row["available_paged"],
                    row["available_coverage_pct"],
                ]
                for row in stats["catalog_coverage"]  # type: ignore[index]
            ),
        )
    )

    parts.extend(["", "## Digest Candidates by Registry", ""])
    parts.append(table(["registry", "count"], sorted(candidates["by_registry"].items())))  # type: ignore[index,union-attr]

    parts.extend(["", "## Top Digest Candidates", ""])
    parts.append(
        table(
            ["pages", "refs", "registry", "entry_id", "doc_number", "date", "subject"],
            (
                [
                    row["pages"],
                    row["refs"],
                    row["registry"],
                    row["entry_id"],
                    row["doc_number"],
                    row["date"],
                    row["subject"],
                ]
                for row in candidates["top"]  # type: ignore[index]
            ),
        )
    )

    parts.extend(["", "## Recent Unpaged Available Documents", ""])
    parts.append(
        table(
            ["date", "registry", "entry_id", "doc_number", "subject"],
            (
                [row["date"], row["registry"], row["entry_id"], row["doc_number"], row["subject"]]
                for row in stats["recent_unpaged_available"]  # type: ignore[index]
            ),
        )
    )

    parts.extend(["", "## Unresolved Relations", ""])
    parts.append(table(["relation", "count"], sorted(unresolved["by_key"].items())))  # type: ignore[index,union-attr]

    parts.extend(["", "## Unresolved Relations by Status", ""])
    parts.append(table(["status", "count"], sorted(unresolved["by_status"].items())))  # type: ignore[index,union-attr]

    parts.extend(["", "## Top Unresolved Relation Pages", ""])
    parts.append(
        table(
            ["unresolved", "type", "id", "path", "keys"],
            (
                [row["unresolved"], row["type"], row["id"], row["path"], row["keys"]]
                for row in unresolved["top_pages"]  # type: ignore[index]
            ),
        )
    )

    parts.extend(["", "## Syntheses", ""])
    parts.append(table(["id", "title", "members"], ([row["id"], row["title"], row["members"]] for row in synthesis["syntheses"])))  # type: ignore[index]

    parts.extend(["", "## Topics Not in Any Synthesis", ""])
    unassigned = synthesis["unassigned_topics"]  # type: ignore[index]
    parts.append(", ".join(unassigned) if unassigned else "(none)")

    parts.extend(["", "## Topics in Multiple Syntheses", ""])
    multi = synthesis["multi_assigned_topics"]  # type: ignore[index]
    parts.append(
        table(["topic", "syntheses"], ([row["topic"], row["syntheses"]] for row in multi))
        if multi
        else "(none)"
    )

    return "\n".join(parts)


def main(argv: list[str] | None = None) -> int:
    configure_utf8_stdio()
    args = parse_args(argv or sys.argv[1:])
    stats = build_stats(args)
    if args.format == "json":
        print(json.dumps(stats, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(stats))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
