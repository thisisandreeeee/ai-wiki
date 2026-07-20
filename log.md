# Wiki Log

> Chronological record of wiki actions. Append-only.  
> Format: `## [YYYY-MM-DD] action | subject`

## [2026-06-21] create | Wiki initialized

- Created repository scaffold for AI/data-science newsletter wiki.
- Added schema, index, log, and operating rules.

## [2026-06-21] synthesize | Last-two-weeks newsletter corpus

- Synthesized The Neuron, Data Science Weekly, AINews/Latent.Space, and Data Elixir items from 2026-06-08 through 2026-06-21.
- Created 17 Obsidian-style wiki pages across entities, concepts, comparisons, and queries.
- Covered Claude Fable/Mythos access controls, OpenAI product/policy strategy, GLM-5.2/open models, coding-agent evaluation, healthcare AI, self-driving labs, agent control, local LLMs, and reliable data workflows.
- Updated `index.md` with all new pages and provenance-linked summaries.

## [2026-06-23] synthesize | Backfill last-30-days newsletter corpus

- Backfilled raw newsletters from 2026-05-24 through 2026-06-07 to complete last-30-days coverage alongside the existing 2026-06-08 through 2026-06-21 ingest.
- Added concise synthesis pages for Anthropic, Claude Opus 4.8, Cognition, Microsoft, GitHub, NVIDIA, real-world agent evals, recursive self-improvement, RL environment quality, and AI infrastructure economics.
- Updated existing pages for coding-agent evaluation, local LLMs, OpenAI, and Google DeepMind.
- Created `queries/two-week-briefing-2026-05-24-to-2026-06-07.md`.

## [2026-07-06] synthesize | Weekly newsletter batch

- Fetched 34 Gmail newsletter items; 30 were new raw newsletter files added to `raw/newsletters/`, with `raw/newsletters/manifest.json` refreshed by the fetch script.
- Created `concepts/software-factories.md` and `queries/weekly-briefing-2026-07-06.md`.
- Updated `entities/anthropic.md`, `entities/claude-fable-5.md`, `entities/openai.md`, `concepts/ai-infrastructure-economics.md`, `concepts/coding-agent-evaluation.md`, `concepts/frontier-model-access-controls.md`, `concepts/local-llms.md`, `concepts/recursive-self-improvement.md`, `concepts/self-driving-labs.md`, and `comparisons/closed-vs-open-frontier-models.md`.
- Updated `index.md`; adjusted `scripts/lint_wiki.py` to validate raw newsletter hashes over raw bytes so CRLF newsletter bodies are checked without false mismatches.
- Ran wiki validation before PR creation.

## [2026-07-13] synthesize | Weekly newsletter batch

- Fetched 33 Gmail newsletter items; 12 were new raw newsletter files added to `raw/newsletters/`, with `raw/newsletters/manifest.json` refreshed by the fetch script.
- Created `entities/gpt-5-6.md`, `entities/grok-4-5.md`, `entities/modal.md`, `concepts/agent-experience.md`, and `queries/weekly-briefing-2026-07-13.md`.
- Updated `entities/openai.md`, `entities/anthropic.md`, `entities/claude-fable-5.md`, `concepts/software-factories.md`, `concepts/ai-infrastructure-economics.md`, `concepts/coding-agent-evaluation.md`, `concepts/recursive-self-improvement.md`, `concepts/ai-control-roadmaps.md`, and `concepts/frontier-model-access-controls.md`.
- Updated `index.md` and preserved previously ingested raw newsletter files unchanged after the fetch script refreshed their `ingested` dates.
- Ran wiki validation before PR creation.

## [2026-07-18] synthesize | Technical-interview learning resources

- Synthesized eight user-provided ChatGPT learning resources and an attached technical-interview question bank into durable notes on LLM training, Transformer architecture, application interfaces, RAG, agent systems, agent operations, GPU inference, and serving optimization.
- Added `queries/technical-interview-study-guide.md` as a coverage map that emphasizes mechanism, trade-offs, failure modes, and production design rather than rote answers.
- Added a source manifest with original share URLs and hashes for the fetched text and attached PDF; preserved the raw newsletter corpus unchanged.
- Updated `index.md` and ran wiki validation before PR creation.

## [2026-07-20] synthesize | Weekly newsletter batch

- Fetched 25 Gmail newsletter items; 13 were new raw newsletter files added to `raw/newsletters/`, with `raw/newsletters/manifest.json` regenerated to include all 120 raw newsletter captures.
- Preserved previously ingested raw newsletter files unchanged after the fetch script refreshed their `ingested` dates.
- Created `entities/kimi-k3.md`, `entities/inkling.md`, and `queries/weekly-briefing-2026-07-20.md`.
- Updated `entities/openai.md`, `entities/gpt-5-6.md`, `concepts/ai-infrastructure-economics.md`, `concepts/software-factories.md`, `concepts/frontier-model-access-controls.md`, `concepts/self-driving-labs.md`, and `comparisons/closed-vs-open-frontier-models.md`.
- Updated `index.md` and ran wiki validation before PR creation.
