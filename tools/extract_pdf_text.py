#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader


def extract_pdf(pdf_path: Path, output_path: Path) -> None:
    reader = PdfReader(str(pdf_path))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as fh:
        for page_index, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            fh.write(f"\n\n--- page {page_index} ---\n\n")
            fh.write(text)
            if not text.endswith("\n"):
                fh.write("\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract text from PDFs into an ignored cache directory.")
    parser.add_argument("pdfs", nargs="+", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path(".cache/unicode-docs-text"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    for pdf_path in args.pdfs:
        output_path = args.output_dir / pdf_path.parent.name / f"{pdf_path.stem}.txt"
        extract_pdf(pdf_path, output_path)
        print(f"{pdf_path} -> {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

