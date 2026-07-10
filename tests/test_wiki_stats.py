import tempfile
import unittest
from pathlib import Path

from tools.find_digest_candidates import CatalogEntry
from tools.wiki_stats import unresolved_relation_summary
from tools.wiki_store import load_concepts


class WikiStatsTests(unittest.TestCase):
    def test_unresolved_relations_are_grouped_by_actionable_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = Path(tmp)
            (bundle / "topics").mkdir()
            (bundle / "topics" / "sample.md").write_text(
                """---
type: Topic
title: Sample
slug: sample
documents: [utc-l2-26-001, utc-l2-26-002, missing-document]
people: [missing-person]
---

# Sample
""",
                encoding="utf-8",
            )
            concepts = load_concepts(bundle)

        catalog = {
            "utc-l2-26-001": CatalogEntry(
                "utc", "utc-l2-26-001", "L2/26-001", "2026-01-01", "Available", "UTC",
                "available", "https://www.unicode.org/L2/L2026/26001.pdf",
            ),
            "utc-l2-26-002": CatalogEntry(
                "utc", "utc-l2-26-002", "L2/26-002", "2026-01-02", "Unavailable", "UTC",
                "referenced", None,
            ),
        }

        summary = unresolved_relation_summary(concepts, catalog, top=5)

        self.assertEqual(summary["by_key"], {"documents": 3, "people": 1})
        self.assertEqual(
            summary["by_status"],
            {
                "available_document": 1,
                "unavailable_document": 1,
                "unknown_document": 1,
                "unmaterialized_concept": 1,
            },
        )


if __name__ == "__main__":
    unittest.main()
