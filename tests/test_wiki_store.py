import tempfile
import unittest
from pathlib import Path

from tools.wiki_store import load_concepts


class WikiStoreTests(unittest.TestCase):
    def test_frontmatter_relations_resolve_aliases(self):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = Path(tmp)
            documents = bundle / "documents"
            topics = bundle / "topics"
            documents.mkdir()
            topics.mkdir()

            (documents / "utc-l2-15-239.md").write_text(
                """---
type: Source Document
title: Proposal of Japanese HENTAIGANA
entry_id: utc-l2-15-239
doc_number: L2/15-239
aliases: [WG2 N4674]
---

# L2/15-239
""",
                encoding="utf-8",
            )
            (topics / "kana.md").write_text(
                """---
type: Topic
title: Kana
slug: kana
documents: [wg2-n4674]
---

# Kana
""",
                encoding="utf-8",
            )

            concepts = load_concepts(bundle)

        kana = concepts["kana"]
        self.assertEqual(kana.relations["documents"], ["wg2-n4674"])
        self.assertEqual(kana.unresolved_relations, {})
        self.assertIn("utc-l2-15-239", kana.links)
        self.assertIn("kana", concepts["utc-l2-15-239"].backlinks)


if __name__ == "__main__":
    unittest.main()
