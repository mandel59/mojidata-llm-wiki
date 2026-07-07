from __future__ import annotations

import unittest

from tools.sync_registries import count_derived_entries, merge_derived_entries


class SyncRegistriesTest(unittest.TestCase):
    def test_merge_derived_entries_skips_existing_registry_entry(self) -> None:
        entries = [
            {
                "entry_id": "irg-n2878r3",
                "registry": "irg",
                "doc_number": "IRG N2878R3",
            }
        ]
        derived = [
            {
                "entry_id": "irg-n2878",
                "registry": "irg",
                "doc_number": "IRG N2878",
                "status": "referenced",
            },
            {
                "entry_id": "irg-n2878r3",
                "registry": "irg",
                "doc_number": "IRG N2878R3",
                "status": "referenced",
            },
            {
                "entry_id": "wg2-n2878",
                "registry": "wg2",
                "doc_number": "WG2 N2878",
                "status": "referenced",
            },
        ]

        merged = merge_derived_entries(entries, "irg", derived)

        self.assertEqual([entry["entry_id"] for entry in merged], ["irg-n2878r3", "irg-n2878"])
        self.assertEqual(merged[1]["status"], "referenced")
        self.assertEqual(merged[1]["catalog_source"], "derived")

    def test_count_derived_entries_only_counts_materialized_overlay_entries(self) -> None:
        entries = [
            {
                "entry_id": "irg-n2878",
                "registry": "irg",
                "doc_number": "IRG N2878",
                "catalog_source": "derived",
            },
            {
                "entry_id": "irg-n2878r3",
                "registry": "irg",
                "doc_number": "IRG N2878R3",
            },
        ]
        derived = [
            {
                "entry_id": "irg-n2878",
                "registry": "irg",
                "doc_number": "IRG N2878",
            },
            {
                "entry_id": "irg-n2878r3",
                "registry": "irg",
                "doc_number": "IRG N2878R3",
            },
        ]

        self.assertEqual(count_derived_entries(entries, "irg", derived), 1)


if __name__ == "__main__":
    unittest.main()
