#!/usr/bin/env python3
from __future__ import annotations

import sys
from typing import TextIO


def _configure_stream(stream: TextIO) -> None:
    reconfigure = getattr(stream, "reconfigure", None)
    if callable(reconfigure):
        reconfigure(encoding="utf-8", errors="replace")


def configure_utf8_stdio() -> None:
    """Force CLI text streams to UTF-8 where the runtime supports it."""
    _configure_stream(sys.stdin)
    _configure_stream(sys.stdout)
    _configure_stream(sys.stderr)
