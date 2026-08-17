---
title: Grok 4.6
created: 2026-08-17
updated: 2026-08-17
type: entity
tags: [ai, llm, model, tooling]
sources: [raw/newsletters/ainews-2026-08-13-ainews-spacexai-grok-4-6-and-grok-bot.md, raw/newsletters/the-neuron-2026-08-13-elon-releases-grok-4-6-says-grok-4-7-is-weeks-away.md]
confidence: medium
---

# Grok 4.6

**Grok 4.6** is xAI/SpaceXAI's August 2026 model for long-running agents, coding, research, and interactive work. The batch presents it as a cost-efficient frontier contender rather than simply a larger checkpoint.

## Launch and training signals

- xAI describes a longer supplemental training run, regenerated SFT trajectories, model-based filtering, and agentic RL across knowledge work, coding, web development, CAD, and kernel optimization. [raw/newsletters/ainews-2026-08-13-ainews-spacexai-grok-4-6-and-grok-bot.md]
- The model is reported as roughly 1.5T parameters and available through the API, Cursor, Grok Build, OpenRouter, Vercel, and Cloudflare. [raw/newsletters/ainews-2026-08-13-ainews-spacexai-grok-4-6-and-grok-bot.md]

## Evaluation and economics

Artificial Analysis placed Grok 4.6 at 61 on its Intelligence Index, roughly level with [[gpt-5-6]] Sol, with strong agentic results including a reported 88.4% Terminal-Bench v2.1 score. The more durable signal is cost per completed task: reported API pricing is $2 per million input tokens and $6 per million output tokens, while AA-Briefcase coverage describes materially fewer turns and input tokens than Opus 5 on a comparable run. These are third-party and vendor/ecosystem reports, so benchmark conditions and task mix matter. [raw/newsletters/ainews-2026-08-13-ainews-spacexai-grok-4-6-and-grok-bot.md][raw/newsletters/the-neuron-2026-08-13-elon-releases-grok-4-6-says-grok-4-7-is-weeks-away.md]

## Strategic significance

Grok 4.6 strengthens the [[coding-agent-evaluation]] argument that quality, turn count, latency, and price must be measured together. A near-frontier model that completes long jobs with fewer retries can be more valuable than a higher-scoring model with a heavier trajectory. That makes it a natural candidate for [[model-routing]] and [[software-factories]].

## Caveats

- The corpus reports a planned Grok 4.7 in three to four weeks, with additional SpaceX data; this is a forward-looking claim, not an independently verified release plan. [raw/newsletters/the-neuron-2026-08-13-elon-releases-grok-4-6-says-grok-4-7-is-weeks-away.md]
- Cost-per-task comparisons depend on harness, context, tool latency, and retry behavior. They should not be read as a universal model ranking.

## Links

- Related entities: [[grok-4-5]], [[gpt-5-6]], [[openai]]
- Related concepts: [[coding-agent-evaluation]], [[model-routing]], [[ai-infrastructure-economics]], [[agentic-knowledge-work]]
