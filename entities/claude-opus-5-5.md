---
title: Claude Opus 5.5
created: 2026-09-28
updated: 2026-09-28
type: entity
tags: [ai, llm, model, tooling, research]
sources: [raw/newsletters/ainews-2026-09-23-ainews-claude-opus-5-5-the-new-default-model-for-ainews-and-everybody.md, raw/newsletters/the-neuron-2026-09-23-new-gpt-6-and-claude-models-start-a-price-war.md, raw/newsletters/the-neuron-2026-09-24-what-950-claude-agents-found.md, raw/newsletters/the-neuron-2026-09-25-meta-is-bringing-tomogotchi-back.md]
confidence: medium
---

# Claude Opus 5.5

**Claude Opus 5.5** is Anthropic's September 2026 Opus-class model, positioned as a cheaper, highly capable workhorse for coding, agents, and creative production.

## Release signal

AINews reports that Opus 5.5 performs near Claude Fable 5.1 for many tasks while costing about 40% less to run than Opus 5. The Neuron reports API pricing of **$4 / million input tokens** and **$20 / million output tokens**, placing it above GPT-6 Sol on raw price but below the prior Opus tier. These are newsletter-reported launch figures, not independent measurements. [raw/newsletters/ainews-2026-09-23-ainews-claude-opus-5-5-the-new-default-model-for-ainews-and-everybody.md][raw/newsletters/the-neuron-2026-09-23-new-gpt-6-and-claude-models-start-a-price-war.md]

Reported results vary with effort. On Terminal-Bench-Science, one AINews summary placed Opus 5.5 at 24% on low effort, 62% at xhigh, and 59% at max, suggesting that a nominally stronger setting is not automatically the best operating point. [[ai-benchmarking]] should therefore track effort, latency, retries, and total task cost.

## What the batch adds

The most concrete capability signal is orchestration. Community examples describe Opus 5.5 writing JavaScript production systems, delegating art, audio, and review to other models, and exporting complete short videos or interactive worlds. These are compelling demonstrations, but they are anecdotal and should not be treated as a production benchmark. [raw/newsletters/the-neuron-2026-09-24-what-950-claude-agents-found.md][raw/newsletters/the-neuron-2026-09-25-meta-is-bringing-tomogotchi-back.md]

The model also anchors an emerging two-tier pattern: use a frontier model for planning, architecture, review, and synthesis, then delegate bounded implementation or media-generation steps to cheaper models. [[model-routing]] and [[software-factories]] provide the systems frame.

## Links

- Related entity: [[anthropic]]
- Related models: [[claude-fable-5]], [[gpt-5-6]]
- Related concepts: [[coding-agent-evaluation]], [[model-routing]], [[agent-reliability-and-operations]]
