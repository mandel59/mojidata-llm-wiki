#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    from cli_support import configure_utf8_stdio
except ModuleNotFoundError:
    from tools.cli_support import configure_utf8_stdio

from wiki_store import (
    DEFAULT_SCHEMA,
    LINK_RE,
    SCHEME_RE,
    WIKI,
    iter_markdown_files,
    load_schema,
    parse_frontmatter_header,
    split_frontmatter,
    validate_page_schema,
    validate_schema_definition,
)


DEFAULT_BUNDLE = WIKI
DATE_HEADING_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\s*$")


def validate_timestamp(path: Path, value: object) -> list[str]:
    if value in (None, ""):
        return []
    if not isinstance(value, str):
        return [f"{path}: timestamp must be a string"]
    normalized = value.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return [f"{path}: timestamp is not ISO 8601: {value!r}"]
    if parsed.time() == datetime.min.time() and "T" not in value:
        return [f"{path}: timestamp must include a time, not just a date"]
    return []


def validate_concept(path: Path, text: str, schema: dict[str, object]) -> list[str]:
    document = split_frontmatter(path, text)
    if document.header is None:
        return document.errors + [f"{path}: concept document is missing YAML frontmatter"]

    data, frontmatter_errors = parse_frontmatter_header(path, document.header)
    errors = document.errors + frontmatter_errors
    errors.extend(validate_page_schema(path, data, schema))
    errors.extend(validate_timestamp(path, data.get("timestamp")))
    return errors


def validate_index(path: Path, bundle: Path, text: str) -> list[str]:
    rel = path.relative_to(bundle).as_posix()
    document = split_frontmatter(path, text)
    body = document.body
    errors = list(document.errors)

    if document.header is not None:
        if rel != "index.md":
            errors.append(f"{path}: only the bundle-root index.md may declare frontmatter")
        data, frontmatter_errors = parse_frontmatter_header(path, document.header)
        errors.extend(frontmatter_errors)
        extra_keys = sorted(set(data) - {"okf_version"})
        if extra_keys:
            errors.append(f"{path}: root index.md frontmatter only permits okf_version")
        if data.get("okf_version") != "0.1":
            errors.append(f'{path}: root index.md must declare okf_version: "0.1"')

    if not body.lstrip().startswith("#"):
        errors.append(f"{path}: index.md should start with a heading")

    return errors


def validate_log(path: Path, text: str) -> list[str]:
    document = split_frontmatter(path, text)
    body = document.body
    errors = list(document.errors)
    if document.header is not None:
        errors.append(f"{path}: log.md must not contain frontmatter")

    if not body.lstrip().startswith("#"):
        errors.append(f"{path}: log.md should start with a heading")

    dates: list[str] = []
    for line_number, line in enumerate(body.splitlines(), start=1):
        if line.startswith("## "):
            match = DATE_HEADING_RE.match(line)
            if not match:
                errors.append(f"{path}:{line_number}: log date heading must be YYYY-MM-DD")
            else:
                dates.append(match.group(1))

    if dates != sorted(dates, reverse=True):
        errors.append(f"{path}: log date headings must be newest first")

    return errors


def validate_links(path: Path, bundle: Path, text: str) -> list[str]:
    errors: list[str] = []
    normalized_text = text.replace("\\", "/")
    for forbidden in [".cache/", "raw/", "downloads/"]:
        if forbidden in normalized_text:
            errors.append(f"{path}: wiki content must not link to {forbidden}")

    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if not target or target.startswith("#") or SCHEME_RE.match(target):
            continue

        target_path = target.split("#", 1)[0].split("?", 1)[0]
        if not target_path.endswith(".md"):
            continue

        if target_path.startswith("/"):
            resolved = bundle / target_path.lstrip("/")
        else:
            resolved = path.parent / target_path
        if not resolved.exists():
            errors.append(f"{path}: broken markdown link: {target}")

    return errors


def validate_bundle(bundle: Path, schema_path: Path) -> list[str]:
    schema = load_schema(schema_path)
    errors = validate_schema_definition(schema, schema_path)
    for path in iter_markdown_files(bundle):
        text = path.read_text(encoding="utf-8")
        if path.name == "index.md":
            errors.extend(validate_index(path, bundle, text))
        elif path.name == "log.md":
            errors.extend(validate_log(path, text))
        else:
            errors.extend(validate_concept(path, text, schema))
        errors.extend(validate_links(path, bundle, text))
    return errors


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the wiki as an OKF v0.1 bundle.")
    parser.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    configure_utf8_stdio()
    args = parse_args(argv or sys.argv[1:])
    errors = validate_bundle(args.bundle, args.schema)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"OKF bundle OK: {args.bundle}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
