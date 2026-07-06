from __future__ import annotations

import unittest

from tools.unicode_registry import discover_register_urls, parse_register_documents


UTC_SAMPLE = """
<html><body>
<table>
<tr><th>Doc Number</th><th>Subject</th><th>Source</th><th>Date</th></tr>
<tr>
  <td><a href="L2026/26093.htm">L2/26-093</a></td>
  <td>UTC #187 meeting minutes</td>
  <td>Robin Leroy</td>
  <td>2026-04-29</td>
</tr>
</table>
</body></html>
"""


WG2_SAMPLE = """
<html><body>
<table>
<tr><td><a href="Register-4750.html">4750-4999</a></td><td><a href="Register-5000.html">5000-5249</a></td><td>Latest Register</td><td>5250-5499</td></tr>
<tr><td><a href="docs/n5354.pdf">5354</a></td><td>WG2 meeting #73 recommendations</td><td>Michel Suignard</td><td>2026-06-27</td></tr>
<tr><td>5370</td><td></td><td></td><td></td></tr>
</table>
</body></html>
"""


IRG_SAMPLE = """
<html><body>
<table>
<tr><td><a href="n2909.pdf">IRG N2909</a></td><td>IRG Meeting #66 Recommendations and Action Items</td><td>IRG Convenor</td><td>2026-03-19</td></tr>
<tr><td>IRG N2762 (unused)</td><td></td><td></td><td></td></tr>
</table>
</body></html>
"""


ROOT_SAMPLE = """
<html><body>
<a href="L-curdoc.htm">Latest Register</a>
<a href="L2026/Register-2026.html">2026</a>
<a href="not-a-register.html">ignore</a>
</body></html>
"""


class RegistryParserTest(unittest.TestCase):
    def test_parse_utc_document(self) -> None:
        entries = parse_register_documents("utc", UTC_SAMPLE, "https://www.unicode.org/L2/L-curdoc.htm")
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["entry_id"], "utc-l2-26-093")
        self.assertEqual(entries[0]["doc_number"], "L2/26-093")
        self.assertEqual(entries[0]["document_url"], "https://www.unicode.org/L2/L2026/26093.htm")

    def test_parse_wg2_document_and_reserved_number(self) -> None:
        entries = parse_register_documents("wg2", WG2_SAMPLE, "https://www.unicode.org/wg2/WG2-curdoc.html")
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0]["entry_id"], "wg2-n5354")
        self.assertEqual(entries[0]["doc_number"], "WG2 N5354")
        self.assertEqual(entries[1]["entry_id"], "wg2-n5370")
        self.assertEqual(entries[1]["status"], "unposted")

    def test_parse_irg_document_and_unused_number(self) -> None:
        entries = parse_register_documents("irg", IRG_SAMPLE, "https://www.unicode.org/irg/IRG-curdoc.html")
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0]["entry_id"], "irg-n2909")
        self.assertEqual(entries[0]["document_url"], "https://www.unicode.org/irg/n2909.pdf")
        self.assertEqual(entries[1]["status"], "unused")

    def test_discover_utc_register_urls(self) -> None:
        config = {
            "root_url": "https://www.unicode.org/L2/",
            "latest_url": "https://www.unicode.org/L2/L-curdoc.htm",
            "register_href_patterns": ["L-curdoc\\.htm$", "L\\d{4}/Register-\\d{4}\\.html$"],
        }
        urls = discover_register_urls(config, ROOT_SAMPLE)
        self.assertEqual(
            urls,
            [
                "https://www.unicode.org/L2/L-curdoc.htm",
                "https://www.unicode.org/L2/L2026/Register-2026.html",
            ],
        )


if __name__ == "__main__":
    unittest.main()
