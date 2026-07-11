import tempfile
import unittest
from pathlib import Path

from tools.generate_event_indexes import render_index


class GenerateEventIndexesTests(unittest.TestCase):
    def test_renders_linked_topic_titles_and_body_groups(self):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = Path(tmp)
            topics = bundle / "topics"
            events_dir = bundle / "events"
            topics.mkdir()
            events_dir.mkdir()
            (topics / "sample.md").write_text(
                "---\ntype: Topic\ntitle: Sample Topic\nslug: sample\nstatus: active\n---\n\n# Sample\n",
                encoding="utf-8",
            )
            event_path = events_dir / "sample-event.md"
            event_data = {
                "title": "Sample Event #1",
                "date": "2026-01-01",
                "description": "Description",
                "topics": ["sample"],
                "bodies": ["IRG"],
            }

            rendered = render_index([(event_path, event_data)], bundle)

        self.assertIn("### [Sample Topic](../topics/sample.md)", rendered)
        self.assertIn("## By Body\n\n### IRG", rendered)
        self.assertIn("[Sample Event \\#1](sample-event.md)", rendered)


if __name__ == "__main__":
    unittest.main()
