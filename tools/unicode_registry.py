from __future__ import annotations

import hashlib
import html
import json
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse, urlunparse


@dataclass(frozen=True)
class Link:
    text: str
    url: str


@dataclass(frozen=True)
class Cell:
    text: str
    links: tuple[Link, ...]


def clean_text(value: str) -> str:
    return " ".join(html.unescape(value).split())


class RegistryHTMLParser(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.links: list[Link] = []
        self.rows: list[tuple[Cell, ...]] = []

        self._row_cells: list[Cell] | None = None
        self._cell_text: list[str] | None = None
        self._cell_links: list[Link] | None = None

        self._anchor_href: str | None = None
        self._anchor_text: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "tr":
            self._row_cells = []
        elif tag in {"td", "th"} and self._row_cells is not None:
            self._cell_text = []
            self._cell_links = []
        elif tag == "a":
            href = attrs_dict.get("href")
            if href:
                self._anchor_href = urljoin(self.base_url, href)
                self._anchor_text = []

    def handle_data(self, data: str) -> None:
        if self._cell_text is not None:
            self._cell_text.append(data)
        if self._anchor_text is not None:
            self._anchor_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._anchor_href and self._anchor_text is not None:
            link = Link(clean_text("".join(self._anchor_text)), self._anchor_href)
            self.links.append(link)
            if self._cell_links is not None:
                self._cell_links.append(link)
            self._anchor_href = None
            self._anchor_text = None
        elif tag in {"td", "th"} and self._row_cells is not None and self._cell_text is not None:
            self._row_cells.append(Cell(clean_text("".join(self._cell_text)), tuple(self._cell_links or [])))
            self._cell_text = None
            self._cell_links = None
        elif tag == "tr" and self._row_cells is not None:
            if self._row_cells:
                self.rows.append(tuple(self._row_cells))
            self._row_cells = None


UTC_REVISION_SUFFIX_RE = r"R[0-9A-Z]*"
NUMBERED_REVISION_SUFFIX_RE = r"R\d*"
UTC_DOC_RE = re.compile(rf"^L2/(\d{{2}})-(\d{{3}})({UTC_REVISION_SUFFIX_RE})?$", re.IGNORECASE)
WG2_DOC_RE = re.compile(rf"^(?:WG2\s*)?N?(\d{{3,4}})({NUMBERED_REVISION_SUFFIX_RE})?$", re.IGNORECASE)
IRG_DOC_RE = re.compile(rf"^IRG\s+N(\d{{3,4}})({NUMBERED_REVISION_SUFFIX_RE})?(?:\s+\(unused\))?$", re.IGNORECASE)
UTC_URL_DOC_RE = re.compile(rf"(?<!\d)(\d{{2}})-?(\d{{3}})({UTC_REVISION_SUFFIX_RE})?(?=[._-]|$)", re.IGNORECASE)
WG2_URL_DOC_RE = re.compile(rf"(?:^|[/_-])n0*(\d{{3,4}})({NUMBERED_REVISION_SUFFIX_RE})?(?=[._-]|$)", re.IGNORECASE)
IRG_URL_DOC_RE = re.compile(rf"(?:^|[/_-])n0*(\d{{3,4}})({NUMBERED_REVISION_SUFFIX_RE})?(?=[._-]|$)", re.IGNORECASE)
DATE_RE = re.compile(r"\b(19|20)\d{2}-\d{2}-\d{2}\b")
VERSION_LINK_RE = re.compile(r"\b(original|previous|revision|revised|draft|proposed)\b", re.IGNORECASE)


def parse_html(html_text: str, base_url: str) -> RegistryHTMLParser:
    parser = RegistryHTMLParser(base_url)
    parser.feed(html_text)
    parser.close()
    return parser


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def cache_path_for_url(cache_dir: Path, url: str, suffix: str = ".html") -> Path:
    parsed = urlparse(url)
    basename = Path(parsed.path).name or "index"
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
    safe_basename = re.sub(r"[^A-Za-z0-9._-]+", "_", basename)
    return cache_dir / f"{digest}-{safe_basename}{suffix if not safe_basename.endswith(suffix) else ''}"


def discover_register_urls(config: dict, root_html: str, latest_only: bool = False) -> list[str]:
    if latest_only:
        return [normalize_registry_url(config["latest_url"])]

    root_url = config["root_url"]
    parser = parse_html(root_html, root_url)
    patterns = [re.compile(pattern, re.IGNORECASE) for pattern in config.get("register_href_patterns", [])]
    urls: list[str] = []

    for link in parser.links:
        relative_part = link.url.removeprefix(root_url)
        if any(pattern.search(link.url) or pattern.search(relative_part) for pattern in patterns):
            urls.append(normalize_registry_url(link.url))

    urls.append(normalize_registry_url(config["latest_url"]))
    return sorted(set(urls))


def normalize_registry_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.netloc.lower() == "www.unicode.org" and parsed.scheme == "http":
        return urlunparse(parsed._replace(scheme="https"))
    return url


def parse_register_documents(registry: str, html_text: str, register_url: str) -> list[dict]:
    parser = parse_html(html_text, register_url)
    entries: list[dict] = []

    for row in parser.rows:
        entries.extend(parse_row_entries(registry, row, register_url))

    return entries


def parse_row(registry: str, row: tuple[Cell, ...], register_url: str) -> dict | None:
    entries = parse_row_entries(registry, row, register_url)
    return entries[0] if entries else None


def parse_row_entries(registry: str, row: tuple[Cell, ...], register_url: str) -> list[dict]:
    if not row:
        return []

    first = row[0].text
    full_row_text = clean_text(" ".join(cell.text for cell in row))
    parsed_number = parse_doc_number(registry, first)
    if parsed_number is None:
        return []

    all_links = [link for cell in row for link in cell.links]
    number_links = list(row[0].links)
    document_url = number_links[0].url if number_links else None
    primary_number = choose_primary_doc_number(registry, parsed_number, document_url)

    entries = [
        make_catalog_entry(
            registry=registry,
            parsed_number=primary_number,
            row=row,
            register_url=register_url,
            full_row_text=full_row_text,
            all_links=all_links,
            document_url=document_url,
        )
    ]

    primary_base = doc_base_key(registry, primary_number[1])
    seen = {(entries[0]["entry_id"], entries[0].get("document_url"))}
    for link in all_links:
        if link.url == document_url:
            continue
        linked_number = parse_doc_number(registry, link.text) or parse_doc_number_from_url(registry, link.url)
        if linked_number is None:
            continue
        if doc_base_key(registry, linked_number[1]) != primary_base:
            continue
        if linked_number[2] == primary_number[2]:
            continue
        if not is_version_link(registry, link):
            continue

        entry = make_catalog_entry(
            registry=registry,
            parsed_number=linked_number,
            row=row,
            register_url=register_url,
            full_row_text=full_row_text,
            all_links=all_links,
            document_url=link.url,
        )
        key = (entry["entry_id"], entry.get("document_url"))
        if key not in seen:
            entries.append(entry)
            seen.add(key)

    return entries


def choose_primary_doc_number(
    registry: str,
    parsed_number: tuple[str, str, str],
    document_url: str | None,
) -> tuple[str, str, str]:
    if not document_url:
        return parsed_number

    url_number = parse_doc_number_from_url(registry, document_url)
    if url_number is None:
        return parsed_number
    if doc_base_key(registry, url_number[1]) != doc_base_key(registry, parsed_number[1]):
        return parsed_number
    if doc_revision(registry, url_number[1]) and not doc_revision(registry, parsed_number[1]):
        return url_number
    return parsed_number


def make_catalog_entry(
    *,
    registry: str,
    parsed_number: tuple[str, str, str],
    row: tuple[Cell, ...],
    register_url: str,
    full_row_text: str,
    all_links: list[Link],
    document_url: str | None,
) -> dict:
    display_number, canonical_number, entry_id = parsed_number
    subject = row[1].text if len(row) > 1 else ""
    source = row[2].text if len(row) > 2 else ""
    date = row[3].text if len(row) > 3 else ""
    if not DATE_RE.fullmatch(date):
        date_match = DATE_RE.search(full_row_text)
        date = date_match.group(0) if date_match else date

    status = "available" if document_url else "unposted"
    lowered = full_row_text.lower()
    if "unused" in lowered:
        status = "unused"
    elif "reserved" in lowered:
        status = "reserved"

    related_links = [
        {"text": link.text, "url": link.url}
        for link in all_links
        if link.url != document_url
    ]

    return {
        "entry_id": entry_id,
        "registry": registry,
        "doc_number": canonical_number,
        "display_number": display_number,
        "subject": subject,
        "source": source,
        "date": date,
        "status": status,
        "document_url": document_url,
        "related_links": related_links,
        "register_url": register_url,
    }


def parse_doc_number_from_url(registry: str, url: str) -> tuple[str, str, str] | None:
    basename = Path(urlparse(url).path).name

    if registry == "utc":
        match = UTC_URL_DOC_RE.search(basename)
        if not match:
            return None
        yy, number, revision = match.groups()
        return parse_doc_number("utc", f"L2/{yy}-{number}{revision or ''}")

    if registry == "wg2":
        match = WG2_URL_DOC_RE.search(basename)
        if not match:
            return None
        number, revision = match.groups()
        return parse_doc_number("wg2", f"WG2 N{int(number)}{revision or ''}")

    if registry == "irg":
        match = IRG_URL_DOC_RE.search(basename)
        if not match:
            return None
        number, revision = match.groups()
        return parse_doc_number("irg", f"IRG N{int(number)}{revision or ''}")

    raise ValueError(f"unknown registry: {registry}")


def doc_base_key(registry: str, doc_number: str) -> tuple[str, ...] | None:
    if registry == "utc":
        match = UTC_DOC_RE.search(doc_number)
        return match.group(1, 2) if match else None

    if registry == "wg2":
        match = WG2_DOC_RE.search(doc_number)
        return (str(int(match.group(1))),) if match else None

    if registry == "irg":
        match = IRG_DOC_RE.search(doc_number)
        return (str(int(match.group(1))),) if match else None

    raise ValueError(f"unknown registry: {registry}")


def doc_revision(registry: str, doc_number: str) -> str:
    if registry == "utc":
        match = UTC_DOC_RE.search(doc_number)
    elif registry == "wg2":
        match = WG2_DOC_RE.search(doc_number)
    elif registry == "irg":
        match = IRG_DOC_RE.search(doc_number)
    else:
        raise ValueError(f"unknown registry: {registry}")
    if not match:
        return ""
    return (match.groups()[-1] or "").upper()


def is_version_link(registry: str, link: Link) -> bool:
    if parse_doc_number(registry, link.text) is not None:
        return True
    return bool(VERSION_LINK_RE.search(link.text))


def parse_doc_number(registry: str, text: str) -> tuple[str, str, str] | None:
    if registry == "utc":
        match = UTC_DOC_RE.search(text)
        if not match:
            return None
        yy, number, revision = match.groups()
        revision = revision or ""
        display = f"L2/{yy}-{number}{revision.upper()}"
        canonical = display
        entry_id = f"utc-l2-{yy}-{number}{revision.lower()}"
        return display, canonical, entry_id

    if registry == "wg2":
        match = WG2_DOC_RE.search(text)
        if not match:
            return None
        number, revision = match.groups()
        revision = revision or ""
        display = f"WG2 N{number}{revision.upper()}"
        canonical = display
        entry_id = f"wg2-n{number}{revision.lower()}"
        return display, canonical, entry_id

    if registry == "irg":
        match = IRG_DOC_RE.search(text)
        if not match:
            return None
        number, revision = match.groups()
        revision = revision or ""
        display = f"IRG N{number}{revision.upper()}"
        canonical = display
        entry_id = f"irg-n{number}{revision.lower()}"
        return display, canonical, entry_id

    raise ValueError(f"unknown registry: {registry}")


def write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True))
            fh.write("\n")


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for line_number, line in enumerate(fh, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                rows.append(json.loads(stripped))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
    return rows


def sort_key(entry: dict) -> tuple[str, int, str]:
    doc_number = entry.get("doc_number", "")
    number_match = re.search(r"(\d{2})-(\d{3})", doc_number)
    if number_match:
        return (entry.get("registry", ""), int(number_match.group(1)) * 1000 + int(number_match.group(2)), doc_number)
    number_match = re.search(r"N(\d{3,4})", doc_number, re.IGNORECASE)
    if number_match:
        return (entry.get("registry", ""), int(number_match.group(1)), doc_number)
    return (entry.get("registry", ""), 0, doc_number)


def dedupe_entries(entries: Iterable[dict]) -> list[dict]:
    deduped: dict[tuple[str, str, str | None], dict] = {}
    for entry in entries:
        key = (entry["registry"], entry["entry_id"], entry.get("document_url"))
        deduped[key] = entry
    return sorted(deduped.values(), key=sort_key)
