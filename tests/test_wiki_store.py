import tempfile
import unittest
from pathlib import Path

import yaml

from tools.wiki_store import load_concepts, parse_frontmatter_header, render_page, split_frontmatter


class WikiStoreTests(unittest.TestCase):
    def test_frontmatter_rejects_unquoted_hash_in_scalar(self):
        data, errors = parse_frontmatter_header(
            Path("page.md"),
            "title: UTC #187 Meeting Minutes\nslug: utc-meeting-187",
        )

        self.assertEqual(data, {})
        self.assertEqual(len(errors), 1)
        self.assertIn("frontmatter value containing # must be quoted", errors[0])

    def test_frontmatter_rejects_unquoted_hash_in_inline_list(self):
        _data, errors = parse_frontmatter_header(
            Path("page.md"),
            "aliases: [UAX #38 Revision 40, PRI #534]",
        )

        self.assertEqual(len(errors), 1)
        self.assertIn("invalid YAML frontmatter", errors[0])

    def test_frontmatter_allows_quoted_hash(self):
        _data, errors = parse_frontmatter_header(
            Path("page.md"),
            'aliases: ["UAX #38 Revision 40", "PRI #534"]',
        )

        self.assertEqual(errors, [])

    def test_frontmatter_rejects_markdown_escape_in_double_quotes(self):
        for value in ['"IRG Meeting \\#67"', '["IRG Meeting \\#67"]']:
            with self.subTest(value=value):
                _data, errors = parse_frontmatter_header(Path("page.md"), f"title: {value}")

                self.assertEqual(len(errors), 1)
                self.assertIn("page.md:2:", errors[0])
                self.assertIn("invalid YAML frontmatter:", errors[0])
                self.assertIn("unknown escape character", errors[0])

    def test_frontmatter_uses_yaml_quoting_and_list_rules(self):
        data, errors = parse_frontmatter_header(
            Path("page.md"),
            'title: "IRG Meeting #67: \\"Agenda\\""\n'
            "description: 'Convenor''s notes'\n"
            'aliases: ["Meeting #67, agenda", "C:\\\\docs", "line\\nnext", "\\N"]',
        )

        self.assertEqual(errors, [])
        self.assertEqual(data, {
            "title": 'IRG Meeting #67: "Agenda"',
            "description": "Convenor's notes",
            "aliases": ["Meeting #67, agenda", "C:\\docs", "line\nnext", "\u0085"],
        })

    def test_frontmatter_render_roundtrip_preserves_literal_strings(self):
        metadata = {
            "title": 'IRG #67: "Agenda"',
            "aliases": ["a, b", "[draft]", "C:\\notes", "2026-11-03", "true", ""],
            "description": "literal \\# and a newline\nnext line",
        }
        rendered = render_page(metadata, "UTC \\#187\n")
        document = split_frontmatter(Path("page.md"), rendered)
        data, errors = parse_frontmatter_header(Path("page.md"), document.header)

        self.assertEqual(errors, [])
        self.assertEqual(data, metadata)
        self.assertEqual(yaml.safe_load(document.header), metadata)
        self.assertEqual(document.body, "\nUTC \\#187\n")

    def test_frontmatter_supports_block_lists_multiline_scalars_and_comments(self):
        data, errors = parse_frontmatter_header(
            Path("page.md"),
            '# metadata\ntitle: "IRG Meeting #67" # title comment\n'
            'aliases:\n  - "Meeting #67, agenda"\n  - Schedule\n'
            'description: |-\n  Agenda #67\n  Convenor\'s notes\n'
            'date: 2026-11-03\nflag: true\n',
        )

        self.assertEqual(errors, [])
        self.assertEqual(data, {
            "title": "IRG Meeting #67",
            "aliases": ["Meeting #67, agenda", "Schedule"],
            "description": "Agenda #67\nConvenor's notes",
            "date": "2026-11-03",
            "flag": "true",
        })

    def test_frontmatter_rejects_duplicate_keys(self):
        data, errors = parse_frontmatter_header(Path("page.md"), "title: First\ntitle: Second")

        self.assertEqual(data, {})
        self.assertEqual(errors, ["page.md:3:1: invalid YAML frontmatter: duplicate frontmatter key: title"])

    def test_frontmatter_rejects_non_mapping_and_multiple_documents(self):
        for header in ["[Topic, Source Document]", "Topic", "title: First\n---\ntitle: Second"]:
            with self.subTest(header=header):
                data, errors = parse_frontmatter_header(Path("page.md"), header)
                self.assertEqual(data, {})
                self.assertEqual(len(errors), 1)

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
