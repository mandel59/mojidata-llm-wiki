from __future__ import annotations

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.check_catalog import check_derived_documents


def catalog_entry(catalog_source: str | None = "derived") -> dict:
    entry = {
        "entry_id": "irg-n2878",
        "registry": "irg",
        "doc_number": "IRG N2878",
        "display_number": "IRG N2878",
        "subject": "Updated proposal to encode CJK Unified Ideographs Components",
        "source": "China & TCA",
        "date": "",
        "status": "referenced",
        "document_url": None,
        "related_links": [],
        "register_url": None,
        "provenance": [
            {
                "entry_id": "irg-n2890",
                "url": "https://www.unicode.org/irg/docs/n2890-IRGN2878Feedback.pdf",
                "note": "Feedback target named in the title.",
            }
        ],
    }
    if catalog_source is not None:
        entry["catalog_source"] = catalog_source
    return entry


class CheckCatalogTest(unittest.TestCase):
    def test_derived_overlay_entry_must_be_merged_as_derived(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            catalog_dir = root / "catalog" / "registries"
            (catalog_dir / "irg").mkdir(parents=True)
            (catalog_dir / "irg" / "documents.jsonl").write_text(
                json.dumps(catalog_entry(), sort_keys=True) + "\n",
                encoding="utf-8",
            )
            derived_path = root / "config" / "derived_documents.json"
            derived_path.parent.mkdir()
            derived_path.write_text(
                json.dumps({"entries": [catalog_entry()]}, sort_keys=True),
                encoding="utf-8",
            )

            count, errors = check_derived_documents(derived_path, catalog_dir)

        self.assertEqual(count, 1)
        self.assertEqual(errors, [])

    def test_derived_overlay_entry_cannot_shadow_generated_entry(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            catalog_dir = root / "catalog" / "registries"
            (catalog_dir / "irg").mkdir(parents=True)
            (catalog_dir / "irg" / "documents.jsonl").write_text(
                json.dumps(catalog_entry(catalog_source=None), sort_keys=True) + "\n",
                encoding="utf-8",
            )
            derived_path = root / "config" / "derived_documents.json"
            derived_path.parent.mkdir()
            derived_path.write_text(
                json.dumps({"entries": [catalog_entry()]}, sort_keys=True),
                encoding="utf-8",
            )

            _count, errors = check_derived_documents(derived_path, catalog_dir)

        self.assertTrue(any("shadows a generated registry entry" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
