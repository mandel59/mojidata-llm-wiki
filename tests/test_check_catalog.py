from __future__ import annotations

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.check_catalog import check_derived_documents, check_registry


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
    def test_registry_warns_when_entry_id_has_different_urls(self) -> None:
        with TemporaryDirectory() as tmp:
            catalog_dir = Path(tmp)
            registry_dir = catalog_dir / "wg2"
            registry_dir.mkdir()
            first = catalog_entry(catalog_source=None) | {
                "entry_id": "wg2-n4563",
                "registry": "wg2",
                "doc_number": "WG2 N4563",
                "display_number": "WG2 N4563",
                "document_url": "https://www.unicode.org/wg2/docs/n4563.pdf",
            }
            second = first | {
                "document_url": "https://www.unicode.org/wg2/docs/n4653.pdf",
            }
            (registry_dir / "documents.jsonl").write_text(
                "\n".join(json.dumps(entry) for entry in (first, second)) + "\n",
                encoding="utf-8",
            )

            count, errors, warnings = check_registry(catalog_dir, "wg2")

        self.assertEqual(count, 2)
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)
        self.assertIn("duplicate entry_id with different document_url", warnings[0])

    def test_registry_rejects_exact_duplicate(self) -> None:
        with TemporaryDirectory() as tmp:
            catalog_dir = Path(tmp)
            registry_dir = catalog_dir / "irg"
            registry_dir.mkdir()
            entry = catalog_entry(catalog_source=None)
            (registry_dir / "documents.jsonl").write_text(
                "\n".join(json.dumps(entry) for _ in range(2)) + "\n",
                encoding="utf-8",
            )

            _count, errors, warnings = check_registry(catalog_dir, "irg")

        self.assertTrue(any("duplicate entry_id/url" in error for error in errors))
        self.assertEqual(warnings, [])

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
