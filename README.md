# AI Wiki

An Obsidian-compatible LLM wiki compiled from AI and data-science newsletters.

## Purpose

This repository captures newsletter issues as immutable raw sources, then compiles them into a navigable markdown wiki using `[[wikilinks]]`.

## Structure

- `raw/newsletters/` — immutable Gmail newsletter captures.
- `entities/` — notable companies, products, people, models, labs, and projects.
- `concepts/` — recurring ideas, technical themes, and methods.
- `comparisons/` — side-by-side analysis when useful.
- `queries/` — synthesized briefs and reusable answers.
- `SCHEMA.md` — conventions, frontmatter, and tag taxonomy.
- `index.md` — catalog of wiki pages.
- `log.md` — append-only change log.

## Validation

Run:

```bash
python3 scripts/lint_wiki.py
```
