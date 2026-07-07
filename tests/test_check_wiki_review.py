import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from tools.check_wiki_review import escape_obsidian_tags_in_markdown


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


if __name__ == "__main__":
    unittest.main()
