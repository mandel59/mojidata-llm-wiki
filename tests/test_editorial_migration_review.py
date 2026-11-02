import json
from pathlib import Path
import tempfile
import unittest

from tools.editorial_migration_review import digest, load_ledger, paragraphs, prepare_packet, record_packet, refresh_report


class EditorialMigrationReviewTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.bundle = self.root / "wiki"
        self.bundle.mkdir()
        self.ledger = self.root / "progress.json"
        self.data = {"files": []}

    def page(self, name, body, reviewed=False):
        path = self.bundle / name
        path.write_text("---\ntype: Topic\ntitle: " + path.stem + "\n---\n\n" + body, encoding="utf-8")
        self.data["files"].append({"path": name, "content_sha256": digest(path),
                                  "full_text_review": "reviewed" if reviewed else "pending",
                                  "status": "screened"})
        self.save()
        return path

    def save(self):
        self.ledger.write_text(json.dumps(self.data), encoding="utf-8")

    def packet(self, limit=10000):
        return prepare_packet(load_ledger(self.ledger, self.bundle), self.ledger, self.bundle, "", limit)

    def test_reuses_only_exact_paragraphs_and_hides_notes(self):
        self.page("a.md", "共通の段落。\n\n別の段落。", reviewed=True)
        self.page("b.md", "共通の段落。\n\n共通の段落ではない。\n\n<!-- editorial: 秘密の作業メモ -->")
        text, receipt = self.packet()
        self.assertNotIn("秘密の作業メモ", text)
        self.assertNotIn("\n共通の段落。", text)
        self.assertIn("共通の段落ではない。", text)
        self.assertEqual([row["path"] for row in receipt["pages"]], ["b.md"])

    def test_cannot_record_after_page_changes(self):
        page = self.page("a.md", "確認対象。")
        _text, receipt = self.packet()
        before = self.ledger.read_bytes()
        page.write_text(page.read_text(encoding="utf-8") + "\n新しい本文。", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "snapshot changed"):
            record_packet(self.ledger, receipt, self.bundle)
        self.assertEqual(self.ledger.read_bytes(), before)

    def test_cannot_record_tampered_or_stale_preview(self):
        self.page("a.md", "確認対象。")
        _text, receipt = self.packet()
        receipt["render_sha256"] = "wrong"
        with self.assertRaisesRegex(ValueError, "differs"):
            record_packet(self.ledger, receipt, self.bundle)
        _text, receipt = self.packet()
        self.ledger.write_text(self.ledger.read_text() + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "ledger changed"):
            record_packet(self.ledger, receipt, self.bundle)

    def test_never_clips_a_page_or_records_pages_not_displayed(self):
        self.page("a.md", "最初のページ。")
        text, _receipt = self.packet()
        self.page("b.md", "後のページは別の本文。")
        _text, receipt = self.packet(limit=len(text))
        self.assertEqual(len(receipt["pages"]), 1)
        result = record_packet(self.ledger, receipt, self.bundle)
        self.assertEqual([row["full_text_review"] for row in result["files"]], ["reviewed", "pending"])
        with self.assertRaisesRegex(ValueError, "nothing was clipped"):
            self.packet(limit=10)

    def test_inventory_mismatch_requires_reconciliation(self):
        self.page("a.md", "本文。")
        (self.bundle / "new.md").write_text("新規ページ。", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "inventory differs"):
            load_ledger(self.ledger, self.bundle)

    def test_reused_headings_still_show_section_context(self):
        self.page("a.md", "## 本文\n\n既読の本文。", reviewed=True)
        self.page("b.md", "## 本文\n\n初めて読む本文。")
        text, _receipt = self.packet()
        self.assertIn("## 本文\n\n初めて読む本文。", text)

    def test_keeps_link_labels_and_source_annotations(self):
        self.page("a.md", "[調査中](https://example.com)（2026-11-02の取得失敗）。\n\n<https://example.com>（本文の日付）。")
        text, _receipt = self.packet()
        self.assertIn("調査中（2026-11-02の取得失敗）", text)
        self.assertIn("<URL>（本文の日付）", text)
        self.assertNotIn("https://example.com", text)

    def test_code_example_is_an_atomic_review_unit(self):
        code = "```markdown\n## 見出し\n\n<!-- editorial: これは例 -->\n```"
        self.assertEqual(paragraphs("前。\n\n" + code + "\n\n後。"), ["前。", code, "後。"])
        self.page("a.md", "## 見出し", reviewed=True)
        self.page("b.md", code)
        text, _receipt = self.packet()
        self.assertIn(code, text)

    def test_report_refresh_preserves_other_sections(self):
        self.page("a.md", "本文。")
        report = self.root / "report.md"
        report.write_text(
            "# 進捗\n\n| 区分 | ページ数 |\n古い集計\n\n## 本文に残す判断\n判断。\n\n"
            "| ディレクトリ | 全文精査済み | 未完了 |\n古い集計\n\n"
            "## 効率的な確認手順\nこの手順を保持する。\n\n## 検証\n検証記録。\n",
            encoding="utf-8",
        )
        refresh_report(self.data, report)
        result = report.read_text(encoding="utf-8")
        self.assertIn("## 効率的な確認手順\nこの手順を保持する。", result)
        self.assertIn("## 検証\n検証記録。", result)
        self.assertIn("| . | 0 | 1 |", result)


if __name__ == "__main__":
    unittest.main()
