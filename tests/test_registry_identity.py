from __future__ import annotations

import tempfile
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from tools.find_digest_candidates import catalog_by_doc_number, load_catalog
from tools.check_wiki_review import catalog_by_doc_number as review_catalog_by_doc_number
from tools.sync_registries import merge_latest_entries, sync_one
from tools.unicode_registry import (
    cache_path_for_url, dedupe_entries, index_catalog_entries,
    parse_register_documents, read_jsonl, write_jsonl,
)


class RegistryIdentityTests(unittest.TestCase):
    def test_irg_explicit_duplicate_rows_keep_number_and_all_documents(self):
        html = '''<table>
<tr><td><a href="docs/n1210-Resolutions.pdf">IRG N1210</a></td><td>IRG resolutions</td></tr>
<tr class="duplicate"><td><a href="docs/n1210-SC2Resolutions14.pdf">IRG N1210</a></td><td>SC2 resolutions</td></tr>
<tr class="duplicate"><td><a href="docs/n1210-WG2Resolutions48.pdf">IRG N1210</a></td><td>WG2 resolutions</td></tr>
<tr><td><a href="docs/n1110-FirstCall.pdf">IRG N1110</a></td><td>First call</td></tr>
<tr class="duplicate"><td><a href="docs/n1110r-FirstCall.pdf">IRG N1110R</a></td><td>Revised first call</td></tr>
</table>'''
        entries = parse_register_documents("irg", html, "https://www.unicode.org/irg/Register-1001.html")
        indexed = index_catalog_entries(entries)
        self.assertEqual(set(indexed), {
            "irg-n1210", "irg-n1210-sc2resolutions14", "irg-n1210-wg2resolutions48", "irg-n1110", "irg-n1110r",
        })
        self.assertEqual(indexed["irg-n1210-sc2resolutions14"]["doc_number"], "IRG N1210")
        self.assertEqual(indexed["irg-n1210-sc2resolutions14"]["registry_duplicate_of"], "irg-n1210")
        self.assertEqual(len({entry["document_url"] for entry in entries}), 5)
        self.assertEqual(parse_register_documents("irg", html, "https://www.unicode.org/irg/Register-1001.html"), entries)

    def test_unknown_collisions_are_not_automatically_renumbered(self):
        html = '''<table>
<tr><td><a href="docs/n1022-first.pdf">IRG N1022</a></td><td>First</td></tr>
<tr><td><a href="docs/n1022-other.pdf">IRG N1022</a></td><td>Other</td></tr>
</table>'''
        entries = parse_register_documents("irg", html, "https://www.unicode.org/irg/Register-1001.html")
        with self.assertRaisesRegex(ValueError, "ambiguous catalog entry_id irg-n1022"):
            index_catalog_entries(entries)

    def test_number_correction_is_source_specific_and_retains_evidence(self):
        url = "https://www.unicode.org/wg2/docs/n4653-comment.pdf"
        correction = {
            "document_url": url, "registry_doc_number": "WG2 N4563", "canonical_doc_number": "WG2 N4653",
            "reason": "PDF header is N4653", "evidence_url": url,
        }
        html = '<table><tr><td><a href="docs/n4653-comment.pdf">4563</a></td><td>Comment</td></tr></table>'
        entry, = parse_register_documents("wg2", html, "https://www.unicode.org/wg2/Register-4500.html", [correction])
        self.assertEqual(entry["entry_id"], "wg2-n4653")
        self.assertEqual(entry["doc_number"], "WG2 N4653")
        self.assertEqual(entry["display_number"], "WG2 N4563")
        self.assertEqual(entry["number_correction"]["evidence_url"], url)
        uncorrected, = parse_register_documents("wg2", html, "https://www.unicode.org/wg2/Register-4500.html")
        self.assertEqual(uncorrected["entry_id"], "wg2-n4563")
        fixed_source, = parse_register_documents("wg2", html.replace(">4563<", ">4653<"), "https://www.unicode.org/wg2/Register-4500.html", [correction])
        self.assertEqual(fixed_source["entry_id"], "wg2-n4653")
        self.assertNotIn("number_correction", fixed_source)
        with self.assertRaisesRegex(ValueError, "source number changed"):
            parse_register_documents("wg2", html.replace(">4563<", ">4564<"), "https://www.unicode.org/wg2/Register-4500.html", [correction])

    def test_pri_legacy_uses_actual_table_and_plain_html_anchors(self):
        samples = [
            ('<table><tr><td><a name="pri174">174</a></td><td>Report</td><td>2011.01.31</td></tr></table>', "pri174"),
            ('<p id="pri-174">174 Report 2011.01.31</p>', "pri-174"),
        ]
        for html, anchor in samples:
            with self.subTest(anchor=anchor):
                entry, = parse_register_documents("pri", html, "https://www.unicode.org/review/resolved-pri-100.html")
                self.assertTrue(entry["document_url"].endswith("#" + anchor))

    def test_pri_alias_merge_preserves_archive_metadata_origins_and_background_links(self):
        archive = "https://www.unicode.org/review/resolved-pri-100.html"
        index = "https://www.unicode.org/review/resolved.html"
        url = archive + "#pri174"
        direct = {"registry": "pri", "entry_id": "pri-174", "doc_number": "PRI #174", "document_url": url,
                  "register_url": archive, "subject": "Report", "related_links": [{"text": "draft", "url": "https://www.unicode.org/reports/tr49/"}]}
        indirect = {**direct, "register_url": index, "subject": "Short index title", "related_links": [{"text": "Report", "url": url}]}
        for originals in ([direct, indirect], [indirect, direct]):
            merged, = dedupe_entries(originals)
            self.assertEqual(merged["register_url"], archive)
            self.assertEqual(merged["register_urls"], sorted([archive, index]))
            self.assertEqual(merged["related_links"], direct["related_links"])
            self.assertEqual(merged["subject"], "Report")
            self.assertEqual(dedupe_entries([merged, indirect]), [merged])

    def test_non_pri_deduplication_still_prefers_newer_metadata(self):
        old = {"registry": "wg2", "entry_id": "wg2-n5351", "doc_number": "WG2 N5351", "document_url": None, "subject": "Old"}
        self.assertEqual(dedupe_entries([old, {**old, "subject": "Updated"}])[0]["subject"], "Updated")

    def test_refresh_of_archive_retains_unrefreshed_index_provenance(self):
        archive = "https://www.unicode.org/review/resolved-pri-100.html"
        index = "https://www.unicode.org/review/resolved.html"
        entry = {"registry": "pri", "entry_id": "pri-174", "doc_number": "PRI #174", "document_url": archive + "#pri174",
                 "register_url": archive, "register_urls": sorted([archive, index]), "subject": "Old", "related_links": []}
        refreshed = {key: value for key, value in entry.items() if key != "register_urls"}
        refreshed["subject"] = "Updated"
        merged, = dedupe_entries(merge_latest_entries([entry], [refreshed], [archive]))
        self.assertEqual(merged["subject"], "Updated")
        self.assertEqual(merged["register_urls"], sorted([archive, index]))
        self.assertEqual(dedupe_entries(merge_latest_entries([merged], [refreshed], [archive])), [merged])

    def test_catalog_reader_rejects_ambiguous_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_jsonl(root / "irg/documents.jsonl", [
                {"registry": "irg", "entry_id": "irg-n1022", "document_url": "https://example.com/first.pdf"},
                {"registry": "irg", "entry_id": "irg-n1022", "document_url": "https://example.com/other.pdf"},
            ])
            with self.assertRaisesRegex(ValueError, "ambiguous catalog entry_id"):
                load_catalog(root)

    def test_reused_document_number_does_not_resolve_to_an_arbitrary_document(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_jsonl(root / "irg/documents.jsonl", [
                {"registry": "irg", "entry_id": "irg-n1022", "doc_number": "IRG N1022", "document_url": "https://example.com/first.pdf"},
                {"registry": "irg", "entry_id": "irg-n1022-report", "doc_number": "IRG N1022", "document_url": "https://example.com/report.pdf"},
            ])
            catalog = load_catalog(root)
            self.assertNotIn("irg-n1022", catalog_by_doc_number(catalog))
            self.assertNotIn("irg-n1022", review_catalog_by_doc_number(catalog))
            self.assertEqual(catalog["irg-n1022-report"].document_url, "https://example.com/report.pdf")

    def test_selected_register_sync_preserves_other_archives_and_metadata(self):
        archive = "https://www.unicode.org/irg/Register-1001.html"
        other_archive = "https://www.unicode.org/irg/Register-0001.html"
        config = {"name": "IRG", "root_url": "https://www.unicode.org/irg/IRG-register.html", "latest_url": "https://www.unicode.org/irg/IRG-curdoc.html"}
        html = '<table><tr><td><a href="docs/n1022.pdf">IRG N1022</a></td><td>Original</td></tr><tr class="duplicate"><td><a href="docs/n1022-report.pdf">IRG N1022</a></td><td>Report</td></tr></table>'
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            catalog, cache = root / "catalog", root / "cache"
            original = parse_register_documents("irg", '<table><tr><td>IRG N080</td><td>Old meeting</td></tr></table>', other_archive)[0]
            write_jsonl(catalog / "irg/documents.jsonl", [original])
            metadata = catalog / "irg/registers.json"
            metadata.write_text('{"registers": [{"url": "' + other_archive + '", "document_count": 1}]}', encoding="utf-8")
            (cache / "irg").mkdir(parents=True)
            cache_path_for_url(cache / "irg", archive).write_text(html, encoding="utf-8")
            result = sync_one("irg", config, catalog, cache, [], False, True, False, [archive])
            entries = read_jsonl(catalog / "irg/documents.jsonl")
            self.assertIn(original, entries)
            self.assertEqual(set(index_catalog_entries(entries)), {"irg-n080", "irg-n1022", "irg-n1022-report"})
            self.assertEqual(result["document_count"], 3)
            self.assertEqual({r["url"] for r in result["registers"]}, {archive, other_archive})
            self.assertFalse(result["latest_only"])
            self.assertEqual(result["last_sync_register_urls"], [archive])
            with self.assertRaisesRegex(ValueError, "existing manifest"):
                sync_one("irg", config, root / "empty", cache, [], False, True, False, [archive])


if __name__ == "__main__":
    unittest.main()
