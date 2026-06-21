# Agent Operating Rules

This repository is an Obsidian-compatible LLM wiki.

## Non-negotiables

- Keep `raw/` immutable after ingest. Corrections belong in synthesized pages.
- Every synthesized page must have YAML frontmatter.
- Every synthesized page should use `[[wikilinks]]` for meaningful connections.
- Every new page must be listed in `index.md`.
- Every batch change must be recorded in `log.md`.
- Use provenance: `sources:` frontmatter is required; inline source markers are encouraged for synthesized claims.
- Keep pages crisp and scannable. Split pages over ~200 lines.

## Ingest Workflow

1. Save source emails under `raw/newsletters/` with Gmail metadata and `sha256`.
2. Identify central entities and concepts across the batch.
3. Create/update pages only when they meet the page threshold in `SCHEMA.md`.
4. Update `index.md` once at the end.
5. Run `python3 scripts/lint_wiki.py` before opening a PR.
