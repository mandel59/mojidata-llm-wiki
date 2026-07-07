import tempfile
import unittest
from pathlib import Path

from tools.find_digest_candidates import CatalogEntry, collect_candidates
from tools.wiki_store import load_concepts


class FindDigestCandidatesTests(unittest.TestCase):
    def test_collects_topic_relation_and_body_mentions(self):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = Path(tmp)
            (bundle / "topics").mkdir()
            (bundle / "documents").mkdir()

            (bundle / "topics" / "non-kana.md").write_text(
                """---
type: Topic
title: Non Kana
slug: non-kana
documents: [utc-l2-26-001, wg2-n9999]
---

# Non Kana

See L2/26-002 for follow-up.
""",
                encoding="utf-8",
            )
            (bundle / "documents" / "existing.md").write_text(
                """---
type: Source Document
title: Existing Alias
entry_id: existing
doc_number: L2/25-001
aliases: [WG2 N9999]
topics: [non-kana]
---

# Existing Alias
""",
                encoding="utf-8",
            )

            concepts = load_concepts(bundle)

        catalog = {
            "utc-l2-26-001": CatalogEntry(
                "utc",
                "utc-l2-26-001",
                "L2/26-001",
                "2026-01-01",
                "First missing document",
                "UTC",
                "available",
                "https://www.unicode.org/L2/L2026/26001.pdf",
            ),
            "utc-l2-26-002": CatalogEntry(
                "utc",
                "utc-l2-26-002",
                "L2/26-002",
                "2026-01-02",
                "Mentioned missing document",
                "UTC",
                "available",
                "https://www.unicode.org/L2/L2026/26002.pdf",
            ),
            "wg2-n9999": CatalogEntry(
                "wg2",
                "wg2-n9999",
                "WG2 N9999",
                "2026-01-03",
                "Existing alias document",
                "WG2",
                "available",
                "https://www.unicode.org/wg2/docs/n9999.pdf",
            ),
        }

        candidates = collect_candidates(concepts, catalog, topic_names=["non-kana"])
        self.assertEqual([candidate.entry.entry_id for candidate in candidates], ["utc-l2-26-001", "utc-l2-26-002"])
        self.assertEqual(candidates[0].references[0].kind, "frontmatter")
        self.assertEqual(candidates[1].references[0].kind, "body")

    def test_excludes_related_topic_pages(self):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = Path(tmp)
            (bundle / "topics").mkdir()

            (bundle / "topics" / "kana.md").write_text(
                """---
type: Topic
title: Kana
slug: kana
documents: [utc-l2-26-003]
---

# Kana
""",
                encoding="utf-8",
            )
            (bundle / "topics" / "non-kana.md").write_text(
                """---
type: Topic
title: Non Kana
slug: non-kana
documents: [utc-l2-26-004]
---

# Non Kana
""",
                encoding="utf-8",
            )

            concepts = load_concepts(bundle)

        catalog = {
            "utc-l2-26-003": CatalogEntry(
                "utc",
                "utc-l2-26-003",
                "L2/26-003",
                "2026-01-03",
                "Kana document",
                "UTC",
                "available",
                "https://www.unicode.org/L2/L2026/26003.pdf",
            ),
            "utc-l2-26-004": CatalogEntry(
                "utc",
                "utc-l2-26-004",
                "L2/26-004",
                "2026-01-04",
                "Non-kana document",
                "UTC",
                "available",
                "https://www.unicode.org/L2/L2026/26004.pdf",
            ),
        }

        candidates = collect_candidates(concepts, catalog, exclude_topic_names=["kana"])
        self.assertEqual([candidate.entry.entry_id for candidate in candidates], ["utc-l2-26-004"])


if __name__ == "__main__":
    unittest.main()
