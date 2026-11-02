#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
from bisect import bisect_right
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
EVENTS = WIKI / "events"
DEFAULT_SCHEMA = ROOT / "schema" / "concept_types.json"
RESERVED_FILENAMES = {"index.md", "log.md"}
RELATION_KEYS = ["documents", "topics", "people", "meetings", "events"]

KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
EDITORIAL_START = "<!-- editorial:"
FENCE_PREFIX = r"[ \t]*(?:> ?)*(?:(?:[-+*]|\d+[.)])[ \t]+)?"
MARKDOWN_TOKEN_RE = re.compile(rf"(?m:^{FENCE_PREFIX}(?:`{{3,}}|~{{3,}})[^\r\n]*\r?$)|<!--|`+")
FENCE_RE = re.compile(rf"^{FENCE_PREFIX}(?P<marker>`{{3,}}|~{{3,}})(?P<info>[^\r\n]*)\r?$")


@dataclass(frozen=True)
class EditorialNote:
    start: int
    end: int
    text: str
    line: int
    end_line: int


@dataclass(frozen=True)
class EditorialDocument:
    source: str
    article: str
    notes: tuple[EditorialNote, ...]
    errors: list[str]
    # Code and comments, including ordinary comments, are opaque to headings.
    opaque_spans: tuple[tuple[int, int], ...]

    def require_valid(self) -> None:
        if self.errors:
            raise ValueError("\n".join(self.errors))

    def masked(self) -> str:
        """Hide notes while retaining source offsets and line numbers."""
        self.require_valid()
        parts: list[str] = []
        cursor = 0
        for note in self.notes:
            parts.append(self.source[cursor:note.start])
            parts.append(re.sub(r"[^\r\n]", " ", self.source[note.start:note.end]))
            cursor = note.end
        parts.append(self.source[cursor:])
        return "".join(parts)


def split_editorial_notes(text: str, path: Path = Path("<markdown>"), first_line: int = 1) -> EditorialDocument:
    """Scan Markdown comments without interpreting fenced/inline code as notes.

    On malformed input keep the whole source; consumers must require_valid()
    before using its article view. Editing can still inspect the raw source.
    """
    notes: list[EditorialNote] = []
    errors: list[str] = []
    opaque: list[tuple[int, int]] = []
    line_starts = [0] + [match.end() for match in re.finditer("\n", text)]

    def line_at(offset: int) -> int:
        return first_line + bisect_right(line_starts, offset) - 1

    cursor = 0
    while match := MARKDOWN_TOKEN_RE.search(text, cursor):
        start = match.start()
        token = match.group()
        escape_start = start
        while escape_start and text[escape_start - 1] == "\\":
            escape_start -= 1
        if (start - escape_start) % 2:
            cursor = match.end()
            continue
        fence = FENCE_RE.fullmatch(token)
        if fence and not (fence["marker"][0] == "`" and "`" in fence["info"]):
            marker = fence["marker"]
            close = re.compile(
                rf"(?m)^[ \t]*(?:> ?)*{re.escape(marker[0])}{{{len(marker)},}}[ \t]*\r?$"
            ).search(text, match.end())
            end = close.end() if close else len(text)
            opaque.append((start, end))
            cursor = end
            continue
        if token == "<!--":
            close_at = text.find("-->", match.end())
            end = close_at + 3 if close_at >= 0 else len(text)
            opaque.append((start, end))
            if text.startswith(EDITORIAL_START, start):
                if close_at < 0:
                    errors.append(f"{path}:{line_at(start)}: editorial note is not closed")
                if "<!--" in text[start + len(EDITORIAL_START):close_at if close_at >= 0 else len(text)]:
                    errors.append(f"{path}:{line_at(start)}: editorial note must not contain nested comments")
                notes.append(EditorialNote(
                    start, end, text[start + len(EDITORIAL_START):close_at if close_at >= 0 else len(text)].strip(),
                    line_at(start), line_at(max(start, end - 1)),
                ))
            cursor = end
            continue
        # A backtick run only starts code if a matching run exists.
        tick_start = start + token.find("`") if "`" in token else start
        ticks = re.match(r"`+", text[tick_start:])
        if ticks:
            tick_end = tick_start + len(ticks.group())
            close = re.compile(rf"(?<!`)`{{{len(ticks.group())}}}(?!`)").search(text, tick_end)
            if close:
                opaque.append((tick_start, close.end()))
                cursor = close.end()
                continue
            cursor = tick_end
            continue
        cursor = match.end()

    parts: list[str] = []
    cursor = 0
    for note in notes:
        parts.append(text[cursor:note.start])
        cursor = note.end
    parts.append(text[cursor:])
    return EditorialDocument(text, text if errors else "".join(parts), tuple(notes), errors, tuple(opaque))


def article_text(text: str) -> str:
    document = split_editorial_notes(text)
    document.require_valid()
    return document.article


def article_spans(document: EditorialDocument) -> Iterable[tuple[int, int]]:
    """Source spans outside notes, for edits that must retain notes verbatim."""
    document.require_valid()
    cursor = 0
    for note in document.notes:
        yield cursor, note.start
        cursor = note.end
    yield cursor, len(document.source)


def preserve_editorial_notes(source: str, article: str) -> str:
    """Carry notes through article edits; refuse edits destroying their anchors."""
    document = split_editorial_notes(source)
    document.require_valid()
    if not document.notes:
        return article
    if document.article == article:
        return source
    updated = split_editorial_notes(article)
    updated.require_valid()
    if updated.notes:
        raise ValueError("replacement must be an article view without editorial notes")
    opcodes = SequenceMatcher(None, document.article, article, autojunk=False).get_opcodes()
    insertions: list[tuple[int, str]] = []
    removed = 0
    for note in document.notes:
        position = note.start - removed
        anchor = next((j1 + position - i1 for tag, i1, i2, j1, _j2 in opcodes
                       if tag == "equal" and i1 <= position <= i2), None)
        if anchor is None:
            raise ValueError(f"editorial note at line {note.line}: edit removes its context; preserve or relocate it explicitly")
        note_source = source[note.start:note.end]
        source_prefix = source[source.rfind("\n", 0, note.start) + 1:note.start]
        source_line_end = source.find("\n", note.end)
        source_suffix = source[note.end:source_line_end if source_line_end >= 0 else len(source)]
        if not source_prefix.strip() and not source_suffix.strip():
            # A regenerated index may collapse the empty line left by removal.
            # Keep a standalone HTML comment from swallowing the next heading.
            if article[article.rfind("\n", 0, anchor) + 1:anchor].strip():
                note_source = "\n" + note_source
            if anchor < len(article) and article[anchor] != "\n":
                note_source += "\n"
        insertions.append((anchor, note_source))
        removed += note.end - note.start
    parts: list[str] = []
    cursor = 0
    for position, note_source in insertions:
        parts.extend([article[cursor:position], note_source])
        cursor = position
    parts.append(article[cursor:])
    return "".join(parts)


@dataclass(frozen=True)
class FrontmatterDocument:
    header: str | None
    body: str
    errors: list[str]
    body_start_line: int = 1


@dataclass(frozen=True)
class WikiPage:
    path: Path
    rel_path: str
    frontmatter: dict[str, object]
    body: str
    errors: list[str]
    editorial: EditorialDocument
    body_start_line: int = 1

    @property
    def article_body(self) -> str:
        if self.errors:
            raise ValueError("\n".join(self.errors))
        return self.editorial.article


@dataclass(frozen=True)
class Concept:
    id: str
    aliases: list[str]
    type: str
    title: str
    path: Path
    rel_path: str
    frontmatter: dict[str, object]
    body: str
    relations: dict[str, list[str]]
    unresolved_relations: dict[str, list[str]]
    links: list[str]
    backlinks: list[str]


def split_frontmatter(path: Path, text: str) -> FrontmatterDocument:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return FrontmatterDocument(None, text, [])

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            header = "".join(lines[1:index]).rstrip("\r\n")
            body = "".join(lines[index + 1 :])
            return FrontmatterDocument(header, body, [], index + 2)

    return FrontmatterDocument(None, text, [f"{path}: frontmatter is not closed"])


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


def value_has_unquoted_comment_marker(value: str | None) -> bool:
    if value is None:
        return False
    quote: str | None = None
    escaped = False
    for index, char in enumerate(value):
        if quote is not None:
            if quote == '"' and char == "\\" and not escaped:
                escaped = True
                continue
            if char == quote and not escaped:
                quote = None
            escaped = False
            continue
        if char in {"'", '"'}:
            quote = char
            continue
        if char == "#" and (index == 0 or value[index - 1].isspace()):
            return True
    return False


def parse_frontmatter_header(path: Path, header: str) -> tuple[dict[str, object], list[str]]:
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
        if value_has_unquoted_comment_marker(value):
            errors.append(f"{path}:{offset}: frontmatter value containing # must be quoted")
        data[key] = parse_value(value)

    return data, errors


def parse_frontmatter(path: Path) -> tuple[dict[str, object], list[str]]:
    document = split_frontmatter(path, path.read_text(encoding="utf-8"))
    if document.header is None:
        return {}, document.errors + [f"{path}: document is missing YAML frontmatter"]
    data, errors = parse_frontmatter_header(path, document.header)
    return data, document.errors + errors


def read_page(path: Path, bundle: Path = WIKI) -> WikiPage:
    text = path.read_text(encoding="utf-8")
    document = split_frontmatter(path, text)
    data: dict[str, object] = {}
    errors = list(document.errors)
    if document.header is not None:
        data, frontmatter_errors = parse_frontmatter_header(path, document.header)
        errors.extend(frontmatter_errors)
    editorial = split_editorial_notes(document.body, path, document.body_start_line)
    errors.extend(editorial.errors)
    return WikiPage(path, path.relative_to(bundle).as_posix(), data, document.body, errors, editorial, document.body_start_line)


def scalar(data: dict[str, object], key: str) -> str:
    value = data.get(key)
    return value if isinstance(value, str) else ""


def string_list(data: dict[str, object], key: str) -> list[str]:
    value = data.get(key)
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    return []


def concept_id(path: Path, data: dict[str, object]) -> str:
    for key in ["slug", "entry_id"]:
        value = data.get(key)
        if isinstance(value, str) and value:
            return value
    return path.stem


def concept_type(data: dict[str, object]) -> str:
    value = data.get("type")
    return value if isinstance(value, str) and value else "Concept"


def iter_markdown_files(bundle: Path = WIKI) -> list[Path]:
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


def iter_concept_files(bundle: Path = WIKI) -> Iterable[Path]:
    for path in iter_markdown_files(bundle):
        if path.name not in RESERVED_FILENAMES:
            yield path


def resolve_markdown_links(path: Path, body: str, path_to_id: dict[Path, str]) -> set[str]:
    targets: set[str] = set()
    for match in LINK_RE.finditer(body):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if not target or target.startswith("#") or SCHEME_RE.match(target):
            continue
        target_path = target.split("#", 1)[0].split("?", 1)[0]
        if not target_path.endswith(".md"):
            continue
        resolved = (path.parent / target_path).resolve()
        cid = path_to_id.get(resolved)
        if cid:
            targets.add(cid)
    return targets


def load_concepts(bundle: Path = WIKI) -> dict[str, Concept]:
    rows: dict[str, dict[str, object]] = {}
    path_to_id: dict[Path, str] = {}

    for path in iter_concept_files(bundle):
        page = read_page(path, bundle)
        if page.errors:
            raise ValueError("\n".join(page.errors))
        cid = concept_id(path, page.frontmatter)
        relations = {key: string_list(page.frontmatter, key) for key in RELATION_KEYS}
        rows[cid] = {
            "id": cid,
            "aliases": concept_aliases(path, page.frontmatter),
            "type": concept_type(page.frontmatter),
            "title": scalar(page.frontmatter, "title") or cid,
            "path": path,
            "rel_path": page.rel_path,
            "frontmatter": page.frontmatter,
            "body": page.article_body,
            "relations": relations,
        }
        path_to_id[path.resolve()] = cid

    alias_to_id: dict[str, str] = {}
    alias_sources: dict[str, set[str]] = {}
    for cid, row in rows.items():
        frontmatter = row["frontmatter"]
        assert isinstance(frontmatter, dict)
        relation_aliases = [cid]
        for key in ["slug", "entry_id", "doc_number"]:
            value = frontmatter.get(key)
            if isinstance(value, str) and value:
                relation_aliases.append(value)
        relation_aliases.extend(string_list(frontmatter, "aliases"))
        for alias in relation_aliases:
            if isinstance(alias, str):
                key = normalize_lookup_key(alias)
                alias_sources.setdefault(key, set()).add(cid)
                alias_to_id.setdefault(key, cid)

    collisions = {key: ids for key, ids in alias_sources.items() if len(ids) > 1}
    if collisions:
        details = [f"{key}: {', '.join(sorted(ids))}" for key, ids in sorted(collisions.items())]
        raise ValueError("ambiguous concept aliases:\n" + "\n".join(details))

    link_map: dict[str, list[str]] = {}
    unresolved_relation_map: dict[str, dict[str, list[str]]] = {}
    for cid, row in rows.items():
        path = row["path"]
        body = row["body"]
        relations = row["relations"]
        assert isinstance(path, Path)
        assert isinstance(body, str)
        assert isinstance(relations, dict)
        links = sorted(
            target
            for target in resolve_markdown_links(path, body, path_to_id)
            if target in rows and target != cid
        )
        frontmatter_links: list[str] = []
        unresolved_relations: dict[str, list[str]] = {}
        for key in RELATION_KEYS:
            resolved_items = [resolve_relation_target(item, rows, alias_to_id) for item in relations[key]]
            found = [item for item in resolved_items if item is not None]
            frontmatter_links.extend(found)
            missing = [item for item, resolved in zip(relations[key], resolved_items) if resolved is None]
            if missing:
                unresolved_relations[key] = missing
        link_map[cid] = sorted(set(links + frontmatter_links))
        unresolved_relation_map[cid] = unresolved_relations

    backlinks = {cid: sorted(source for source, links in link_map.items() if cid in links) for cid in rows}

    return {
        cid: Concept(
            id=cid,
            aliases=row["aliases"],  # type: ignore[arg-type]
            type=str(row["type"]),
            title=str(row["title"]),
            path=row["path"],  # type: ignore[arg-type]
            rel_path=str(row["rel_path"]),
            frontmatter=row["frontmatter"],  # type: ignore[arg-type]
            body=str(row["body"]),
            relations=row["relations"],  # type: ignore[arg-type]
            unresolved_relations=unresolved_relation_map[cid],
            links=link_map[cid],
            backlinks=backlinks[cid],
        )
        for cid, row in rows.items()
    }


def resolve_relation_target(
    target: str, rows: dict[str, dict[str, object]], alias_to_id: dict[str, str]
) -> str | None:
    if target in rows:
        return target
    return alias_to_id.get(normalize_lookup_key(target))


def concepts_by_type(concepts: Iterable[Concept], type_name: str) -> list[Concept]:
    return [concept for concept in concepts if concept.type == type_name]


def concept_aliases(path: Path, data: dict[str, object]) -> list[str]:
    aliases = [path.stem]
    for key in ["slug", "entry_id", "doc_number", "title"]:
        value = data.get(key)
        if isinstance(value, str) and value:
            aliases.append(value)
    aliases.extend(string_list(data, "aliases"))
    return sorted(set(aliases), key=lambda item: item.lower())


def normalize_lookup_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def concept_matches_lookup(concept: Concept, name: str) -> bool:
    normalized = normalize_lookup_key(name)
    if concept.id == name or normalize_lookup_key(concept.id) == normalized:
        return True
    if concept.rel_path == name.replace("\\", "/") or concept.rel_path.endswith(f"/{name.replace('\\', '/')}"):
        return True
    return any(alias == name or normalize_lookup_key(alias) == normalized for alias in concept.aliases)


def find_concept_path(group: str, slug: str, bundle: Path = WIKI) -> Path:
    roots = {
        "topic": bundle / "topics",
        "people": bundle / "people",
        "meeting": bundle / "meetings",
    }
    root = roots[group]
    for path in root.rglob("*.md"):
        if path.name == "index.md":
            continue
        data, _errors = parse_frontmatter(path)
        if data.get("slug") == slug or path.stem == slug:
            return path
    raise SystemExit(f"cannot find {group}: {slug}")


def load_schema(path: Path = DEFAULT_SCHEMA) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_schema_definition(schema: dict[str, object], path: Path = DEFAULT_SCHEMA) -> list[str]:
    errors: list[str] = []
    common = schema.get("common")
    types = schema.get("types")
    if not isinstance(common, dict):
        errors.append(f"{path}: common must be an object")
        common = {}
    if not isinstance(types, dict) or not types:
        errors.append(f"{path}: types must be a non-empty object")
        types = {}

    deprecated = set(string_list(common, "deprecated"))
    for type_name, raw_type_schema in types.items():
        if not isinstance(raw_type_schema, dict):
            errors.append(f"{path}: type schema must be an object: {type_name}")
            continue
        required = set(string_list(raw_type_schema, "required"))
        conflicts = sorted(required & deprecated)
        if conflicts:
            errors.append(f"{path}: type {type_name} requires deprecated fields: {', '.join(conflicts)}")
        relations = raw_type_schema.get("relations", {})
        if relations is not None and not isinstance(relations, dict):
            errors.append(f"{path}: type {type_name} relations must be an object")
        enums = raw_type_schema.get("enums", {})
        if enums is not None and not isinstance(enums, dict):
            errors.append(f"{path}: type {type_name} enums must be an object")
        if isinstance(enums, dict):
            for field_name, allowed in enums.items():
                if not isinstance(allowed, list) or not all(isinstance(item, str) for item in allowed):
                    errors.append(f"{path}: type {type_name} enum {field_name} must be a list of strings")
    return errors


def validate_page_schema(path: Path, data: dict[str, object], schema: dict[str, object]) -> list[str]:
    errors: list[str] = []
    common = schema.get("common", {})
    types = schema.get("types", {})
    if not isinstance(common, dict) or not isinstance(types, dict):
        return [f"{DEFAULT_SCHEMA}: invalid schema structure"]

    for key in string_list(common, "required"):
        if not _has_non_empty_value(data, key):
            errors.append(f"{path}: concept document is missing non-empty {key}")

    for key in string_list(common, "deprecated"):
        if key in data:
            errors.append(f"{path}: frontmatter key {key} is deprecated")

    for key in string_list(common, "list_fields"):
        if key in data and not isinstance(data.get(key), list):
            errors.append(f"{path}: {key} must be a YAML list")

    identity_fields = string_list(common, "identity_fields")
    if common.get("filename_stem_must_match_identity") is True:
        for identity_key in identity_fields:
            identity_value = data.get(identity_key)
            if isinstance(identity_value, str) and identity_value and identity_value != path.stem:
                errors.append(f"{path}: filename stem must match {identity_key}: {identity_value}")

    type_name = data.get("type")
    if not isinstance(type_name, str) or not type_name:
        return errors
    type_schema = types.get(type_name)
    if not isinstance(type_schema, dict):
        errors.append(f"{path}: unknown concept type: {type_name}")
        return errors

    for key in string_list(type_schema, "required"):
        if not _has_non_empty_value(data, key):
            errors.append(f"{path}: {type_name} is missing non-empty {key}")
    for key in string_list(type_schema, "non_empty_lists"):
        if not isinstance(data.get(key), list) or not string_list(data, key):
            errors.append(f"{path}: {key} must be a non-empty YAML list")
    enums = type_schema.get("enums", {})
    if isinstance(enums, dict):
        for key, raw_allowed in enums.items():
            if key not in data:
                continue
            allowed = raw_allowed if isinstance(raw_allowed, list) else []
            value = data.get(key)
            if not isinstance(value, str) or value not in allowed:
                errors.append(f"{path}: {key} must be one of: {', '.join(str(item) for item in allowed)}")
    return errors


def _has_non_empty_value(data: dict[str, object], key: str) -> bool:
    value = data.get(key)
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return bool(value)
    return value is not None


def replace_marker_block(text: str, start: str, end: str, replacement: str) -> tuple[str, bool]:
    document = split_editorial_notes(text)
    document.require_valid()
    marker_re = re.compile(rf"{re.escape(start)}.*?{re.escape(end)}", re.DOTALL)
    if not marker_re.search(document.article):
        return text, False
    updated = marker_re.sub(lambda _match: replacement, document.article)
    return preserve_editorial_notes(text, updated), True


def update_frontmatter(
    path: Path, transform: Callable[[dict[str, object]], dict[str, object]], bundle: Path = WIKI
) -> None:
    page = read_page(path, bundle)
    if page.errors:
        raise ValueError("\n".join(page.errors))
    new_frontmatter = transform(dict(page.frontmatter))
    text = render_page(new_frontmatter, page.body)
    path.write_text(text, encoding="utf-8")


def render_page(frontmatter: dict[str, object], body: str) -> str:
    lines = ["---"]
    for key, value in frontmatter.items():
        lines.append(f"{key}: {render_value(value)}")
    lines.extend(["---", "", body.rstrip(), ""])
    return "\n".join(lines)


def render_value(value: object) -> str:
    if isinstance(value, list):
        return "[" + ", ".join(render_value(item) for item in value) + "]"
    if isinstance(value, str) and (":" in value or "#" in value):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def relative_link(from_path: Path, to_path: Path, title: object) -> str:
    rel = os.path.relpath(to_path, start=from_path.parent).replace(os.sep, "/")
    return f"[{title}]({rel})"
