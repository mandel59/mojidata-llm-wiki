from __future__ import annotations

import sys
import unittest
from unittest.mock import patch

from tools.cli_support import configure_utf8_stdio


class ReconfigurableStream:
    def __init__(self) -> None:
        self.calls: list[dict[str, str]] = []

    def reconfigure(self, **kwargs: str) -> None:
        self.calls.append(kwargs)


class CliSupportTests(unittest.TestCase):
    def test_configure_utf8_stdio_reconfigures_standard_streams(self) -> None:
        stdin = ReconfigurableStream()
        stdout = ReconfigurableStream()
        stderr = ReconfigurableStream()

        with (
            patch.object(sys, "stdin", stdin),
            patch.object(sys, "stdout", stdout),
            patch.object(sys, "stderr", stderr),
        ):
            configure_utf8_stdio()

        for stream in [stdin, stdout, stderr]:
            self.assertEqual(stream.calls, [{"encoding": "utf-8", "errors": "replace"}])

    def test_configure_utf8_stdio_allows_non_reconfigurable_streams(self) -> None:
        stream = object()

        with (
            patch.object(sys, "stdin", stream),
            patch.object(sys, "stdout", stream),
            patch.object(sys, "stderr", stream),
        ):
            configure_utf8_stdio()


if __name__ == "__main__":
    unittest.main()
