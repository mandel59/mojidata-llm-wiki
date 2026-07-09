import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from tools.check_wiki_review import (
    CatalogEntry,
    available_catalog_name_index,
    catalog_entries_mentioned_in_line,
    escape_obsidian_tags_in_markdown,
    line_describes_document_as_unavailable,
    unescape_hashes_in_inline_code_markdown,
)


class CheckWikiReviewTests(unittest.TestCase):
    def test_escapes_obsidian_tag_like_body_tokens(self):
        fixed, findings = escape_obsidian_tags_in_markdown(
            "UTC #187 が UAX #38 の revision を確認した。\n"
        )

        self.assertEqual(fixed, "UTC \\#187 が UAX \\#38 の revision を確認した。\n")
        self.assertEqual(findings, [(1, "#187"), (1, "#38")])

    def test_leaves_headings_code_and_link_targets_unchanged(self):
        fixed, findings = escape_obsidian_tags_in_markdown(
            "# Heading\n"
            "See [section](topic.md#anchor) and `UTC #187`.\n"
            "```text\n"
            "#define TAG 1\n"
            "```\n"
            "WG2 #73 は本文なので対象。\n"
        )

        self.assertEqual(
            fixed,
            "# Heading\n"
            "See [section](topic.md#anchor) and `UTC #187`.\n"
            "```text\n"
            "#define TAG 1\n"
            "```\n"
            "WG2 \\#73 は本文なので対象。\n",
        )
        self.assertEqual(findings, [(6, "#73")])

    def test_keeps_existing_escapes(self):
        fixed, findings = escape_obsidian_tags_in_markdown("UTC \\#187 は処理済み。\n")

        self.assertEqual(fixed, "UTC \\#187 は処理済み。\n")
        self.assertEqual(findings, [])

    def test_unescapes_overescaped_hashes_only_in_inline_code(self):
        fixed, findings = unescape_hashes_in_inline_code_markdown(
            "`PRI \\#546` と `UAX \\#38` は過剰。\n"
            "本文の PRI \\#546 は対象外。\n"
            "```text\n"
            "`PRI \\#546`\n"
            "```\n"
        )

        self.assertEqual(
            fixed,
            "`PRI #546` と `UAX #38` は過剰。\n"
            "本文の PRI \\#546 は対象外。\n"
            "```text\n"
            "`PRI \\#546`\n"
            "```\n",
        )
        self.assertEqual(findings, [(1, "`PRI \\#546`"), (1, "`UAX \\#38`")])

    def test_stale_unavailable_candidate_index_only_returns_available_mentions(self):
        available = CatalogEntry(
            registry="irg",
            entry_id="irg-n2933",
            doc_number="IRG N2933",
            status="available",
            document_url="https://www.unicode.org/irg/docs/n2933.pdf",
        )
        unavailable = CatalogEntry(
            registry="irg",
            entry_id="irg-n2952",
            doc_number="IRG N2952",
            status="missing",
            document_url=None,
        )
        index = available_catalog_name_index({available.entry_id: available, unavailable.entry_id: unavailable})

        candidates = catalog_entries_mentioned_in_line(
            "`IRG N2933` は文書実体未確認。`IRG N2952` も未確認。", index
        )

        self.assertEqual([entry.entry_id for entry in candidates], ["irg-n2933"])
        self.assertTrue(line_describes_document_as_unavailable("`IRG N2933` は文書実体未確認。", available))


if __name__ == "__main__":
    unittest.main()
