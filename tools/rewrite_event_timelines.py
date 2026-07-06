#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

from check_events import EVENTS, WIKI, parse_frontmatter, string_list


START = "<!-- events:start -->"
END = "<!-- events:end -->"
MARKER_RE = re.compile(rf"{re.escape(START)}.*?{re.escape(END)}", re.DOTALL)


def load_events() -> list[tuple[Path, dict[str, object]]]:
    events: list[tuple[Path, dict[str, object]]] = []
    for path in sorted(EVENTS.glob("*.md")):
        if path.name == "index.md":
            continue
        data, errors = parse_frontmatter(path)
        if errors:
            raise SystemExit("\n".join(errors))
        events.append((path, data))
    return events


def find_concept(kind: str, slug: str) -> Path:
    roots = {
        "topic": WIKI / "topics",
        "people": WIKI / "people",
        "meeting": WIKI / "meetings",
    }
    root = roots[kind]
    for path in root.rglob("*.md"):
        if path.name == "index.md":
            continue
        data, _errors = parse_frontmatter(path)
        if data.get("slug") == slug or path.stem == slug:
            return path
    raise SystemExit(f"cannot find {kind}: {slug}")


def select_events(
    events: list[tuple[Path, dict[str, object]]],
    *,
    topic: str | None,
    people: str | None,
    meeting: str | None,
) -> list[tuple[Path, dict[str, object]]]:
    selected: list[tuple[Path, dict[str, object]]] = []
    for item in events:
        _path, data = item
        if topic and topic not in string_list(data, "topics"):
            continue
        if people and people not in string_list(data, "people"):
            continue
        if meeting and meeting not in string_list(data, "meetings"):
            continue
        selected.append(item)
    return sorted(selected, key=lambda item: (str(item[1].get("date", "")), str(item[1].get("title", ""))))


def relative_link(from_path: Path, to_path: Path, title: object) -> str:
    rel = os.path.relpath(to_path, start=from_path.parent).replace(os.sep, "/")
    return f"[{title}]({rel})"


def render_table(target: Path, events: list[tuple[Path, dict[str, object]]]) -> str:
    lines = [
        START,
        "| 日付 | Body | Event | 要点 |",
        "| --- | --- | --- | --- |",
    ]
    for path, data in events:
        date = data.get("date", "")
        bodies = " / ".join(string_list(data, "bodies"))
        title = data.get("title", path.stem)
        description = data.get("description", "")
        lines.append(f"| {date} | {bodies} | {relative_link(target, path, title)} | {description} |")
    lines.append(END)
    return "\n".join(str(line) for line in lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render or rewrite event timeline marker blocks.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--topic")
    group.add_argument("--people")
    group.add_argument("--meeting")
    parser.add_argument("--write", action="store_true", help="Rewrite an existing marker block in the target page.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.topic:
        target = find_concept("topic", args.topic)
    elif args.people:
        target = find_concept("people", args.people)
    else:
        target = find_concept("meeting", args.meeting)

    events = select_events(load_events(), topic=args.topic, people=args.people, meeting=args.meeting)
    table = render_table(target, events)

    if not args.write:
        print(table)
        return 0

    text = target.read_text(encoding="utf-8")
    if not MARKER_RE.search(text):
        print(f"{target}: marker block not found; dry-run output follows", file=sys.stderr)
        print(table)
        return 1

    target.write_text(MARKER_RE.sub(table, text), encoding="utf-8")
    print(f"Updated {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
