import tempfile
import unittest
from pathlib import Path

from tools.wiki_store import load_concepts, parse_frontmatter_header


class WikiStoreTests(unittest.TestCase):
    def test_frontmatter_rejects_unquoted_hash_in_scalar(self):
        data, errors = parse_frontmatter_header(
            Path("page.md"),
            "title: UTC #187 Meeting Minutes\nslug: utc-meeting-187",
        )

        self.assertEqual(data["title"], "UTC #187 Meeting Minutes")
        self.assertEqual(errors, ["page.md:2: frontmatter value containing # must be quoted"])

    def test_frontmatter_rejects_unquoted_hash_in_inline_list(self):
        _data, errors = parse_frontmatter_header(
            Path("page.md"),
            "aliases: [UAX #38 Revision 40, PRI #534]",
        )

        self.assertEqual(errors, ["page.md:2: frontmatter value containing # must be quoted"])

    def test_frontmatter_allows_quoted_hash(self):
        _data, errors = parse_frontmatter_header(
            Path("page.md"),
            'aliases: ["UAX #38 Revision 40", "PRI #534"]',
        )

        self.assertEqual(errors, [])

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

    def test_load_concepts_rejects_ambiguous_aliases(self):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = Path(tmp)
            topics = bundle / "topics"
            topics.mkdir()
            for slug in ["first", "second"]:
                (topics / f"{slug}.md").write_text(
                    f"---\ntype: Topic\ntitle: {slug.title()}\nslug: {slug}\naliases: [Shared Name]\n---\n\n# {slug}\n",
                    encoding="utf-8",
                )

            with self.assertRaisesRegex(ValueError, "ambiguous concept aliases") as raised:
                load_concepts(bundle)
            self.assertIn("shared-name: first, second", str(raised.exception))


if __name__ == "__main__":
    unittest.main()
