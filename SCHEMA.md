# Wiki Schema

## Domain

AI, machine learning, data science, analytics engineering, and adjacent tooling intelligence from curated newsletters.

## Conventions

- File names: lowercase kebab-case, no spaces.
- Use Obsidian `[[wikilinks]]` between related pages.
- Raw newsletter captures live in `raw/newsletters/` and are immutable.
- Synthesized pages live in `entities/`, `concepts/`, `comparisons/`, or `queries/`.
- Every synthesized page starts with YAML frontmatter.
- Every synthesized page is listed in `index.md`.
- Every ingest/update is appended to `log.md`.

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [ai]
sources: [raw/newsletters/source.md]
confidence: high | medium | low
---
```

## Raw Newsletter Frontmatter

```yaml
---
source: gmail
newsletter: The Neuron
message_id: <gmail-message-id>
thread_id: <gmail-thread-id>
subject: <email-subject>
from: <sender>
date: <email-date>
ingested: YYYY-MM-DD
sha256: <sha256 of body below frontmatter>
---
```

## Tag Taxonomy

- `ai` — general artificial intelligence developments.
- `machine-learning` — ML methods, systems, or model development.
- `data-science` — analytics, statistics, experimentation, or data workflows.
- `data-engineering` — pipelines, warehouses, orchestration, and infrastructure.
- `llm` — large language models, agents, prompting, RAG, and evaluation.
- `model` — specific model releases or model families.
- `tooling` — software tools, frameworks, products, and developer workflows.
- `company` — companies and startups.
- `research` — papers, benchmarks, academic/research-lab findings.
- `policy` — regulation, safety, governance, privacy, and legal context.
- `newsletter` — digest/briefing pages derived from newsletter sources.
- `trend` — recurring market or technology patterns.
- `comparison` — side-by-side evaluations.

## Page Thresholds

- Create a page when an entity/concept appears in 2+ sources, or is central to one source.
- Update an existing page when a source adds material context.
- Do not create pages for passing mentions.
- Prefer a two-week briefing in `queries/` for low-frequency items that do not yet deserve pages.

## Update Policy

When sources conflict, keep both claims with dates and provenance. Mark low-confidence or contested summaries explicitly.
