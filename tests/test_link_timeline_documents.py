import unittest
from pathlib import Path

from tools.link_timeline_documents import link_timeline
from tools.wiki_store import Concept


class LinkTimelineDocumentsTests(unittest.TestCase):
    def test_links_only_history_table_code_tokens(self):
        target = Path("C:/repo/wiki/documents/utc-l2-26-099.md")
        concept = Concept(
            "utc-l2-26-099", [], "Source Document", "L2/26-099", target,
            "documents/utc-l2-26-099.md", {"doc_number": "L2/26-099"}, "", {}, {}, [], [],
        )
        text = "## 概要\n`L2/26-099`\n\n## 経緯\n| 日付 | 文書 |\n| --- | --- |\n| now | `L2/26-099` / `missing` |\n"
        updated, count = link_timeline(text, Path("C:/repo/wiki/topics/sample.md"), {"l2/26-099": concept})
        self.assertEqual(count, 1)
        self.assertIn("[L2/26-099](../documents/utc-l2-26-099.md)", updated)
        self.assertIn("## 概要\n`L2/26-099`", updated)
        self.assertIn("`missing`", updated)


if __name__ == "__main__":
    unittest.main()
