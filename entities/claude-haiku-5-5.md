---
title: Claude Haiku 5.5
created: 2026-10-12
updated: 2026-10-12
type: entity
tags: [ai, company, llm, model, tooling]
sources: [raw/newsletters/ainews-2026-10-08-ainews-claude-haiku-5-5-better-than-gpt-6-luna-at-the-same-pricing.md, raw/newsletters/the-neuron-2026-10-08-gpt-6-builds-your-calculator-check-its-math.md]
confidence: medium
---
# Claude Haiku 5.5

**Claude Haiku 5.5** is Anthropic's small model positioned for fast, high-volume work inside [[agentic-systems]] and multi-model coding harnesses.

## Reported release signals

- Input/output pricing is reported at $0.10/$0.50 per million tokens below 100K tokens, matching GPT-6 Luna's sticker price; prompts above 100K have a higher tier.
- Anthropic reports roughly 75% lower average operating cost than Haiku 4.5. It positions Haiku as the worker for summaries, compaction, database queries, and subagents while [[claude-opus-5-5]] handles harder reasoning.
- The model adds effort controls, adaptive thinking, a 1M-token context window, and computer/browser-use SDK support.
- Artificial Analysis reports an Intelligence Index score of 43 at maximum effort, slightly above several low-cost peers, but also reports much higher token use than Luna at similar scores. Its AutomationBench score was depressed by a reported over-refusal bug, and cost-per-task estimates were not yet final.

These are launch and early-evaluation signals, not a settled leaderboard. The relevant production measure is cost per verified task after token use, retries, tool latency, and escalation. [[ai-benchmarking]] [[model-routing]]

## Why it matters

Haiku 5.5 strengthens the specialist-first pattern: a strong model can delegate routine, bounded work to a cheaper worker while preserving a frontier model for difficult decisions. That makes model selection part of the harness rather than a one-model default. [[anthropic]] [[decision-models]]
