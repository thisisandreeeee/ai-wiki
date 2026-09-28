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

## Python environment

Run every script in this repository with its dedicated virtualenv interpreter:

```bash
/home/janet/.hermes/venvs/ai-wiki/bin/python scripts/lint_wiki.py
```

Do not use bare `python3`. On this machine it resolves to a Hermes-managed toolchain
interpreter that has no Google API libraries, so `scripts/fetch_gmail_newsletters.py`
fails immediately with `ModuleNotFoundError: No module named 'googleapiclient'` — and
because that script re-invokes `scripts/google_api.py` through `sys.executable`, the
entire Gmail path dies with it.

The venv deliberately lives outside this repository so no machine-specific path is
tracked. To recreate it on a fresh clone:

```bash
uv venv ~/.hermes/venvs/ai-wiki --python /usr/bin/python3
uv pip install --python ~/.hermes/venvs/ai-wiki/bin/python \
  google-api-python-client google-auth-oauthlib
```

Apply the same interpreter to validation commands, for example
`/home/janet/.hermes/venvs/ai-wiki/bin/python -m py_compile scripts/*.py`.

## Ingest Workflow

1. Save source emails under `raw/newsletters/` with Gmail metadata and `sha256`.
2. Identify central entities and concepts across the batch.
3. Create/update pages only when they meet the page threshold in `SCHEMA.md`.
4. Update `index.md` once at the end.
5. Run `/home/janet/.hermes/venvs/ai-wiki/bin/python scripts/lint_wiki.py` before opening a PR.
