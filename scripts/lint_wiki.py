#!/usr/bin/env python3
"""Sanity checks for the Obsidian-compatible AI wiki."""
from __future__ import annotations

import ast
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIRS = ["entities", "concepts", "comparisons", "queries"]
REQUIRED_FIELDS = ["title", "created", "updated", "type", "tags", "sources", "confidence"]


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5 :]


def parse_scalar(value: str):
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        try:
            return ast.literal_eval(value)
        except Exception:
            inner = value[1:-1].strip()
            if not inner:
                return []
            return [part.strip().strip('"\'') for part in inner.split(",")]
    return value.strip('"\'')


def parse_frontmatter(fm: str) -> dict:
    data = {}
    for line in fm.splitlines():
        if not line.strip() or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = parse_scalar(value)
    return data


def page_name(path: Path) -> str:
    return path.stem


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    schema = (ROOT / "SCHEMA.md").read_text(encoding="utf-8")
    allowed_tags = set(re.findall(r"^- `([^`]+)`", schema, flags=re.MULTILINE))
    index = (ROOT / "index.md").read_text(encoding="utf-8")

    wiki_pages = []
    for d in WIKI_DIRS:
        wiki_pages.extend((ROOT / d).glob("*.md"))
    name_to_path = {page_name(p): p for p in wiki_pages}

    for path in sorted(wiki_pages):
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if fm is None:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        data = parse_frontmatter(fm)
        for field in REQUIRED_FIELDS:
            if field not in data or data[field] in ("", []):
                errors.append(f"{rel}: missing required frontmatter field `{field}`")
        tags = data.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        for tag in tags:
            if tag not in allowed_tags:
                errors.append(f"{rel}: tag `{tag}` not declared in SCHEMA.md")
        sources = data.get("sources", [])
        if isinstance(sources, str):
            sources = [sources]
        for source in sources:
            source_path = ROOT / source
            if not source_path.exists():
                errors.append(f"{rel}: source does not exist: {source}")
        if f"[[{path.stem}]]" not in index:
            errors.append(f"{rel}: missing from index.md")
        links = re.findall(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]", body)
        for link in links:
            if link not in name_to_path:
                errors.append(f"{rel}: broken wikilink [[{link}]]")
        if len(set(links)) < 2 and path.parent.name != "queries":
            warnings.append(f"{rel}: fewer than 2 outbound wikilinks")

    for raw in sorted((ROOT / "raw" / "newsletters").glob("*.md")):
        rel = raw.relative_to(ROOT)
        text = raw.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if fm is None:
            errors.append(f"{rel}: missing raw frontmatter")
            continue
        data = parse_frontmatter(fm)
        expected = data.get("sha256")
        actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if expected != actual:
            errors.append(f"{rel}: sha256 mismatch")

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
    if errors:
        print("Errors:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"OK: {len(wiki_pages)} wiki pages, {len(list((ROOT/'raw/newsletters').glob('*.md')))} raw newsletter sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
