#!/usr/bin/env python3
"""Backfill a fixed Gmail newsletter date window into raw/newsletters."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOOGLE_API = Path(os.environ.get("HERMES_HOME", str(Path.home() / ".hermes"))) / "skills/productivity/google-workspace/scripts/google_api.py"

SOURCES = [
    ("the-neuron", '"The Neuron"'),
    ("data-science-weekly", '"Data Science Weekly"'),
    ("data-elixir", '"Data Elixir"'),
    ("ainews", '"AINews"'),
    ("latent-space", '"Latent Space"'),
]


def run_api(*args: str):
    proc = subprocess.run([sys.executable, str(GOOGLE_API), *args], check=True, text=True, capture_output=True)
    out = proc.stdout.strip()
    if out == "No messages found.":
        return []
    return json.loads(out)


def slugify(text: str, max_len: int = 70) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", (text or "").lower()).strip("-")
    return text[:max_len].strip("-") or "newsletter"


def date_slug(date_text: str) -> str:
    try:
        dt = parsedate_to_datetime(date_text)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.date().isoformat()
    except Exception:
        return datetime.now(timezone.utc).date().isoformat()


def yaml_quote(value: str) -> str:
    return json.dumps(value or "", ensure_ascii=False)


def parse_raw_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text:
        return {}
    fm, body = text[4:].split("\n---\n", 1)
    data = {"chars": len(body.strip())}
    for line in fm.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        try:
            data[key.strip()] = json.loads(value)
        except Exception:
            data[key.strip()] = value.strip('"')
    return data


def rebuild_manifest(out_dir: Path) -> int:
    items = []
    for path in sorted(out_dir.glob("*.md")):
        data = parse_raw_frontmatter(path)
        items.append({
            "id": data.get("message_id", ""),
            "newsletter": data.get("newsletter", ""),
            "subject": data.get("subject", ""),
            "date": data.get("date", ""),
            "from": data.get("from", ""),
            "path": str(path.relative_to(ROOT)),
            "chars": data.get("chars", 0),
        })
    (out_dir / "manifest.json").write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf-8")
    return len(items)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--after", required=True, help="Gmail after: date, e.g. 2026/5/24")
    parser.add_argument("--before", required=True, help="Gmail before: date, e.g. 2026/6/8")
    parser.add_argument("--max", type=int, default=30)
    args = parser.parse_args()

    seen: dict[str, dict] = {}
    source_hits: dict[str, int] = {}
    for newsletter, base_query in SOURCES:
        query = f"{base_query} after:{args.after} before:{args.before}"
        results = run_api("gmail", "search", query, "--max", str(args.max))
        source_hits[newsletter] = len(results)
        for item in results:
            item["newsletter_query"] = newsletter
            seen.setdefault(item["id"], item)

    out_dir = ROOT / "raw" / "newsletters"
    out_dir.mkdir(parents=True, exist_ok=True)
    created = []
    skipped = []
    for mid, summary in sorted(seen.items(), key=lambda kv: kv[1].get("date", "")):
        msg = run_api("gmail", "get", mid)
        body = (msg.get("body") or "").strip() or (msg.get("snippet") or "").strip()
        # Hash exactly what is stored after the closing frontmatter marker.
        stored_body = body + "\n"
        sha = hashlib.sha256(stored_body.encode("utf-8")).hexdigest()
        newsletter = summary.get("newsletter_query") or "newsletter"
        dslug = date_slug(msg.get("date") or summary.get("date", ""))
        sslug = slugify(msg.get("subject") or summary.get("subject", "newsletter"))
        path = out_dir / f"{newsletter}-{dslug}-{sslug}.md"
        rel = str(path.relative_to(ROOT))
        if path.exists():
            skipped.append(rel)
            continue
        frontmatter = "\n".join([
            "---",
            "source: gmail",
            f"newsletter: {yaml_quote(newsletter)}",
            f"message_id: {yaml_quote(msg.get('id') or mid)}",
            f"thread_id: {yaml_quote(msg.get('threadId') or summary.get('threadId', ''))}",
            f"subject: {yaml_quote(msg.get('subject') or summary.get('subject', ''))}",
            f"from: {yaml_quote(msg.get('from') or summary.get('from', ''))}",
            f"date: {yaml_quote(msg.get('date') or summary.get('date', ''))}",
            f"ingested: {datetime.now(timezone.utc).date().isoformat()}",
            f"sha256: {sha}",
            "---",
            "",
        ])
        path.write_text(frontmatter + body + "\n", encoding="utf-8")
        created.append({
            "id": mid,
            "newsletter": newsletter,
            "subject": msg.get("subject") or summary.get("subject", ""),
            "date": msg.get("date") or summary.get("date", ""),
            "from": msg.get("from") or summary.get("from", ""),
            "path": rel,
            "chars": len(body),
        })

    manifest_count = rebuild_manifest(out_dir)
    print(json.dumps({
        "source_hits": source_hits,
        "unique_hits": len(seen),
        "created_count": len(created),
        "skipped_count": len(skipped),
        "manifest_count": manifest_count,
        "created": created,
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
