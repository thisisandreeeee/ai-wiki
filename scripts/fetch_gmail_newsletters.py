#!/usr/bin/env python3
"""Fetch recent AI/data newsletters from Gmail via Hermes google_api.py."""
from __future__ import annotations

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

QUERIES = [
    ("the-neuron", '"The Neuron" newer_than:14d'),
    ("data-science-weekly", '"Data Science Weekly" newer_than:14d'),
    ("data-elixir", '"Data Elixir" newer_than:14d'),
    ("ainews", '"AINews" newer_than:14d'),
    ("latent-space", '"Latent Space" newer_than:14d'),
]

MAX_PER_QUERY = 20


def run_api(*args: str):
    cmd = [sys.executable, str(GOOGLE_API), *args]
    proc = subprocess.run(cmd, check=True, text=True, capture_output=True)
    out = proc.stdout.strip()
    if out == "No messages found.":
        return []
    return json.loads(out)


def slugify(text: str, max_len: int = 70) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
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


def main() -> None:
    seen: dict[str, dict] = {}
    for newsletter, query in QUERIES:
        results = run_api("gmail", "search", query, "--max", str(MAX_PER_QUERY))
        for item in results:
            item["newsletter_query"] = newsletter
            seen.setdefault(item["id"], item)

    out_dir = ROOT / "raw" / "newsletters"
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for mid, summary in sorted(seen.items(), key=lambda kv: kv[1].get("date", "")):
        msg = run_api("gmail", "get", mid)
        body = (msg.get("body") or "").strip()
        if not body:
            body = msg.get("snippet", "").strip()
        # Hash exactly what is stored after the closing frontmatter marker.
        stored_body = body + "\n"
        sha = hashlib.sha256(stored_body.encode("utf-8")).hexdigest()
        newsletter = summary.get("newsletter_query") or "newsletter"
        dslug = date_slug(msg.get("date") or summary.get("date", ""))
        sslug = slugify(msg.get("subject") or summary.get("subject", "newsletter"))
        path = out_dir / f"{newsletter}-{dslug}-{sslug}.md"
        fm = "\n".join([
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
        path.write_text(fm + body + "\n", encoding="utf-8")
        manifest.append({
            "id": mid,
            "newsletter": newsletter,
            "subject": msg.get("subject") or summary.get("subject", ""),
            "date": msg.get("date") or summary.get("date", ""),
            "from": msg.get("from") or summary.get("from", ""),
            "path": str(path.relative_to(ROOT)),
            "chars": len(body),
        })

    manifest_path = ROOT / "raw" / "newsletters" / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"count": len(manifest), "manifest": str(manifest_path), "items": manifest}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
