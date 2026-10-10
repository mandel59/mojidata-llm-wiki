from __future__ import annotations

import unittest
import io
import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from tools.unicode_registry import cache_path_for_url, discover_register_urls, parse_register_documents, read_jsonl, write_jsonl

from tools.sync_registries import (
    catalog_change_lines,
    count_derived_entries,
    merge_derived_entries,
    merge_latest_entries,
    should_refresh_registry_url,
    sync_one,
)


class SyncRegistriesTest(unittest.TestCase):
    def test_online_sync_refreshes_root_and_latest_but_not_historical_pages(self) -> None:
        config = {
            "root_url": "https://example.test/registry.html",
            "latest_url": "https://example.test/current.html",
        }

        self.assertTrue(
            should_refresh_registry_url(
                config["root_url"], config, offline=False, refresh=False
            )
        )
        self.assertTrue(
            should_refresh_registry_url(
                config["latest_url"], config, offline=False, refresh=False
            )
        )
        self.assertFalse(
            should_refresh_registry_url(
                "https://example.test/register-2025.html",
                config,
                offline=False,
                refresh=False,
            )
        )

    def test_refresh_and_offline_modes_are_explicit(self) -> None:
        config = {
            "root_url": "https://example.test/registry.html",
            "latest_url": "https://example.test/current.html",
        }
        historical_url = "https://example.test/register-2025.html"

        self.assertTrue(
            should_refresh_registry_url(
                historical_url, config, offline=False, refresh=True
            )
        )
        self.assertFalse(
            should_refresh_registry_url(
                config["latest_url"], config, offline=True, refresh=True
            )
        )

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


class PriSyncRegressionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.config = json.loads(
            (Path(__file__).resolve().parents[1] / "config/registries.json").read_text(encoding="utf-8")
        )["registries"]["pri"]
        self.open_url = self.config["latest_url"]
        self.resolved_url = "https://www.unicode.org/review/resolved.html"
        self.archive_url = "https://www.unicode.org/review/resolved-pri.html"
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.catalog = Path(self.temp.name) / "catalog"
        self.cache = Path(self.temp.name) / "cache"
        self.manifest = self.catalog / "pri/documents.jsonl"
        self.cache.joinpath("pri").mkdir(parents=True)
        self.historical = self.entry(99, self.archive_url)
        write_jsonl(self.manifest, [self.historical])
        self.catalog.joinpath("pri/registers.json").write_text(json.dumps({
            "registers": [{"url": self.archive_url, "document_count": 1}],
            "latest_only": False,
        }), encoding="utf-8")

    @staticmethod
    def html(*numbers: int) -> str:
        rows = "".join(
            f'<tr><td>{number}</td><td><a href="/ivd/pri/pri{number}/">IVD registration</a></td>'
            '<td>2026.07.31</td><td>IVD Registrar</td></tr>'
            for number in numbers
        )
        return f"<html><table>{rows}</table></html>"

    def entry(self, number: int, url: str) -> dict:
        # Parse as a current resolved row, then retain its historical provenance.
        entry = parse_register_documents("pri", self.html(number), self.resolved_url)[0]
        entry["register_url"] = url
        return entry

    def sync(self, *, latest_only: bool = True, offline: bool = False) -> dict:
        return sync_one("pri", self.config, self.catalog, self.cache, [], latest_only, offline, False)

    def response(self, pages: dict[str, str]):
        def respond(request, timeout):
            self.assertEqual(timeout, 60)
            self.assertIn(request.full_url, pages)
            return io.BytesIO(pages[request.full_url].encode("utf-8"))
        return respond

    def test_default_config_includes_mutable_resolved_page_in_latest_sync(self) -> None:
        self.assertEqual(discover_register_urls(self.config, "", latest_only=True),
                         [self.open_url, self.resolved_url])
        for offline in [False, True]:
            with self.subTest(offline=offline):
                self.assertEqual(should_refresh_registry_url(
                    self.resolved_url, self.config, offline=offline, refresh=False
                ), not offline)
        self.assertFalse(should_refresh_registry_url(
            self.archive_url, self.config, offline=False, refresh=False
        ))

    def test_latest_sync_catches_open_to_resolved_despite_stale_cache(self) -> None:
        cache_path_for_url(self.cache / "pri", self.resolved_url).write_text(
            self.html(), encoding="utf-8"
        )
        with patch("tools.sync_registries.urlopen", side_effect=self.response({
            self.open_url: self.html(546), self.resolved_url: self.html(259),
        })) as network:
            self.sync()
            self.assertEqual([call.args[0].full_url for call in network.call_args_list],
                             [self.open_url, self.resolved_url])
        before = read_jsonl(self.manifest)
        self.assertEqual(next(e for e in before if e["entry_id"] == "pri-546")["review_status"], "open")

        with patch("tools.sync_registries.urlopen", side_effect=self.response({
            self.open_url: self.html(), self.resolved_url: self.html(259, 546),
        })):
            metadata = self.sync()
        after = read_jsonl(self.manifest)
        by_id = {e["entry_id"]: e for e in after}
        self.assertEqual(set(by_id), {"pri-99", "pri-259", "pri-546"})
        self.assertEqual(by_id["pri-546"]["review_status"], "resolved")
        self.assertEqual(by_id["pri-546"]["register_url"], self.resolved_url)
        self.assertEqual(by_id["pri-99"], self.historical)
        self.assertEqual(metadata["document_count"], 3)
        self.assertFalse(metadata["latest_only"])
        self.assertEqual({r["url"] for r in metadata["registers"]},
                         {self.open_url, self.resolved_url, self.archive_url})
        self.assertEqual(catalog_change_lines(before, after), [
            "  pri-546: updated (register_url, review_status: open -> resolved)"
        ])

        with patch("tools.sync_registries.urlopen") as network:
            self.sync(offline=True)
            network.assert_not_called()
        self.assertEqual(read_jsonl(self.manifest), after)
        self.assertEqual(catalog_change_lines(after, read_jsonl(self.manifest)), [])

    def test_full_sync_refreshes_resolved_but_reuses_fixed_archives(self) -> None:
        for url in self.config["register_urls"]:
            cache_path_for_url(self.cache / "pri", url).write_text(self.html(), encoding="utf-8")
        with patch("tools.sync_registries.urlopen", side_effect=self.response({
            self.open_url: self.html(), self.resolved_url: self.html(546),
        })) as network:
            self.sync(latest_only=False)
        self.assertEqual({call.args[0].full_url for call in network.call_args_list},
                         {self.open_url, self.resolved_url})
        entries = read_jsonl(self.manifest)
        self.assertEqual(entries[0]["entry_id"], "pri-546")
        self.assertEqual(entries[0]["review_status"], "resolved")

    def test_resolved_fetch_failure_leaves_catalog_untouched(self) -> None:
        original = self.manifest.read_bytes()
        metadata_path = self.catalog / "pri/registers.json"
        original_metadata = metadata_path.read_bytes()
        def respond(request, timeout):
            if request.full_url == self.resolved_url:
                raise TimeoutError("resolved page unavailable")
            return io.BytesIO(self.html().encode("utf-8"))
        with patch("tools.sync_registries.urlopen", side_effect=respond):
            with self.assertRaisesRegex(RuntimeError, "resolved page unavailable"):
                self.sync()
        self.assertEqual(self.manifest.read_bytes(), original)
        self.assertEqual(metadata_path.read_bytes(), original_metadata)

    def test_latest_merge_preserves_archive_variants_but_replaces_moved_issue(self) -> None:
        archived = self.entry(174, self.archive_url)
        archived["document_url"] = self.archive_url + "#pri-174"
        current = self.entry(174, self.resolved_url)
        opened = self.entry(546, self.open_url)
        opened["review_status"] = "open"
        opened["document_url"] = "https://www.unicode.org/review/pri546/old.html"
        resolved = self.entry(546, self.resolved_url)
        merged = merge_latest_entries([archived, current, opened], [current, resolved],
                                      [self.open_url, self.resolved_url])
        self.assertEqual(merged, [archived, current, resolved])

    def test_change_report_includes_new_removed_and_revised_entries(self) -> None:
        old = self.entry(546, self.open_url)
        new = dict(old, document_url="https://www.unicode.org/ivd/pri/pri546/revised.html")
        self.assertEqual(catalog_change_lines([old, self.historical], [new, self.entry(560, self.open_url)]), [
            "  pri-546: updated (document_url)", "  pri-560: added", "  pri-99: removed"
        ])
        self.assertEqual(catalog_change_lines([old, new], [new, old]), [])


if __name__ == "__main__":
    unittest.main()
