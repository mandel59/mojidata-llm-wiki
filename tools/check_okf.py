#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "wiki"
RESERVED_FILENAMES = {"index.md", "log.md"}

KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
DATE_HEADING_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\s*$")


def split_frontmatter(path: Path, text: str) -> tuple[str | None, str, list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text, []

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            header = "\n".join(lines[1:index])
            body = "\n".join(lines[index + 1 :])
            return header, body, []

    return None, text, [f"{path}: frontmatter is not closed"]


def parse_value(value: str | None) -> object:
    if value is None:
        return ""
    value = value.strip()
    if value == "":
        return ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_value(item) for item in inner.split(",")]
    return value


def parse_frontmatter(path: Path, header: str) -> tuple[dict[str, object], list[str]]:
    data: dict[str, object] = {}
    errors: list[str] = []

    for offset, line in enumerate(header.splitlines(), start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = KEY_RE.match(line)
        if not match:
            errors.append(f"{path}:{offset}: cannot parse frontmatter line")
            continue
        key, value = match.groups()
        if key in data:
            errors.append(f"{path}:{offset}: duplicate frontmatter key: {key}")
        data[key] = parse_value(value)

    return data, errors


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


def validate_concept(path: Path, text: str) -> list[str]:
    header, _body, errors = split_frontmatter(path, text)
    if header is None:
        return errors + [f"{path}: concept document is missing YAML frontmatter"]

    data, frontmatter_errors = parse_frontmatter(path, header)
    errors.extend(frontmatter_errors)

    concept_type = data.get("type")
    if not isinstance(concept_type, str) or not concept_type.strip():
        errors.append(f"{path}: concept document is missing non-empty type")
    if "kind" in data:
        errors.append(f"{path}: frontmatter key kind is deprecated; use type")

    tags = data.get("tags")
    if tags is not None and not isinstance(tags, list):
        errors.append(f"{path}: tags must be a YAML list")

    errors.extend(validate_timestamp(path, data.get("timestamp")))
    return errors


def validate_index(path: Path, bundle: Path, text: str) -> list[str]:
    rel = path.relative_to(bundle).as_posix()
    header, body, errors = split_frontmatter(path, text)

    if header is not None:
        if rel != "index.md":
            errors.append(f"{path}: only the bundle-root index.md may declare frontmatter")
        data, frontmatter_errors = parse_frontmatter(path, header)
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
    header, body, errors = split_frontmatter(path, text)
    if header is not None:
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


def iter_markdown_files(bundle: Path) -> list[Path]:
    try:
        result = subprocess.run(
            [
                "git",
                "ls-files",
                "--cached",
                "--others",
                "--exclude-standard",
                "--",
                str(bundle.relative_to(ROOT)),
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError, ValueError):
        return sorted(bundle.rglob("*.md"))

    files: list[Path] = []
    for line in result.stdout.splitlines():
        path = ROOT / line
        if path.suffix == ".md" and path.is_file():
            files.append(path)
    return sorted(files)


def validate_bundle(bundle: Path) -> list[str]:
    errors: list[str] = []
    for path in iter_markdown_files(bundle):
        text = path.read_text(encoding="utf-8")
        if path.name == "index.md":
            errors.extend(validate_index(path, bundle, text))
        elif path.name == "log.md":
            errors.extend(validate_log(path, text))
        else:
            errors.extend(validate_concept(path, text))
        errors.extend(validate_links(path, bundle, text))
    return errors


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the wiki as an OKF v0.1 bundle.")
    parser.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    bundle = args.bundle
    errors = validate_bundle(bundle)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"OKF bundle OK: {bundle}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
