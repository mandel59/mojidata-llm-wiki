#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

try:
    from cli_support import configure_utf8_stdio
except ModuleNotFoundError:
    from tools.cli_support import configure_utf8_stdio

from pypdf import PdfReader


def looks_unusable(text: str) -> bool:
    if len(text) < 500:
        return False
    slash_digit_runs = text.count("/i255") + sum(text.count(f"/{digit}") for digit in range(10))
    letters = sum(1 for char in text if char.isalpha())
    return slash_digit_runs > 200 and letters < len(text) * 0.08


def extract_pdf(pdf_path: Path, output_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    extracted: list[str] = []
    with output_path.open("w", encoding="utf-8") as fh:
        for page_index, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            extracted.append(text)
            fh.write(f"\n\n--- page {page_index} ---\n\n")
            fh.write(text)
            if not text.endswith("\n"):
                fh.write("\n")
    return "\n".join(extracted)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract text from PDFs into an ignored cache directory.")
    parser.add_argument("pdfs", nargs="+", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path(".cache/unicode-docs-text"))
    return parser.parse_args()


def main() -> int:
    configure_utf8_stdio()
    args = parse_args()
    for pdf_path in args.pdfs:
        output_path = args.output_dir / pdf_path.parent.name / f"{pdf_path.stem}.txt"
        text = extract_pdf(pdf_path, output_path)
        print(f"{pdf_path} -> {output_path}")
        if looks_unusable(text):
            print(f"warning: extracted text may be unusable for digest: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
