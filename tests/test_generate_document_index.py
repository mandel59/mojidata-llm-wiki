import tempfile
import unittest
from pathlib import Path

from tools.generate_document_index import render_index


class GenerateDocumentIndexTests(unittest.TestCase):
    def test_groups_documents_by_registry_and_descending_year(self):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = Path(tmp)
            documents = bundle / "documents"
            documents.mkdir()
            (documents / "index.md").write_text(
                "# Documents\n\n- [Old](old.md) - Preserved description。\n",
                encoding="utf-8",
            )
            for name, registry, date in [("old", "utc", "2024-01-01"), ("new", "utc", "2026-01-01"), ("irg", "irg", "")]:
                (documents / f"{name}.md").write_text(
                    f"---\ntype: Source Document\ntitle: {name}\nentry_id: {name}\ndoc_number: {name.upper()}\nregistry: {registry}\ndate: \"{date}\"\nsource: Test\n---\n\n# {name}\n",
                    encoding="utf-8",
                )

            rendered = render_index(bundle)

        self.assertLess(rendered.index("### 2026"), rendered.index("### 2024"))
        self.assertIn("- [OLD](old.md) - Preserved description。", rendered)
        self.assertIn("## IRG\n\n### Undated", rendered)

    def test_escapes_hash_in_display_number(self):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = Path(tmp)
            documents = bundle / "documents"
            documents.mkdir()
            (documents / "index.md").write_text("# Documents\n", encoding="utf-8")
            (documents / "pri-1.md").write_text(
                '---\ntype: Source Document\ntitle: Review\nentry_id: pri-1\ndoc_number: "PRI #1"\nregistry: pri\ndate: "2026-01-01"\nsource: UTC\n---\n',
                encoding="utf-8",
            )
            rendered = render_index(bundle)
        self.assertIn("[PRI \\#1](pri-1.md)", rendered)


if __name__ == "__main__":
    unittest.main()
