---
title: Google DeepMind
created: 2026-06-21
updated: 2026-06-29
type: entity
tags: [ai, company, research, policy]
sources: [raw/newsletters/the-neuron-2026-06-21-how-deepmind-would-stop-rogue-agents.md, raw/newsletters/ainews-2026-06-11-ainews-open-models-model-labs-vs-agent-labs-and-what-s-untrainable-sar.md, raw/newsletters/latent-space-2026-06-18-the-professor-of-outputmaxxing-anjney-midha-amp.md, raw/newsletters/the-neuron-2026-06-25-chatgpt-s-secret-advantage.md, raw/newsletters/ainews-2026-06-26-ainews-openai-reports-median-internal-codex-output-tokens-grew-56x-in.md, raw/newsletters/the-neuron-2026-06-26-ai-is-making-your-next-apple-device-cost-more.md, raw/newsletters/the-neuron-2026-06-28-openai-vs-washington-over-gpt-5-6.md]
confidence: high
---

# Google DeepMind

**Google DeepMind** appeared in the corpus as both a safety roadmap author and a research lab whose unpublished work is increasingly viewed as strategically consequential.

## Agent safety roadmap

The Neuron covered DeepMind's AI Control Roadmap for powerful internal agents. The roadmap treats advanced agents as potential insider threats and layers security controls on top of alignment.

Core ideas:

- Monitor agent reasoning, plans, and actions.
- Scale controls by risk, from delayed review to real-time blocking.
- Track operational metrics such as coverage, recall, and time-to-response.

This connects directly to [[ai-control-roadmaps]].

## Model and research context

AINews also covered Google/DeepMind's DiffusionGemma release, a non-autoregressive diffusion text model that revived interest in iterative refinement and fast text generation.

Latent.Space's AMP interview raised a separate concern: much high-value DeepMind research may be delayed, embargoed, or never productionized. That made research hoarding and compute allocation part of the broader frontier-lab debate.

## Backfill: May 24–June 7

The earlier corpus adds broader Google signals around Gemini, Gemma, and agent security:

- Gemini notification ingestion created an indirect prompt-injection risk via third-party app messages.
- Gemma 4 coverage strengthened the local/open model thread connected to [[local-llms]].
- Gemini Omni and AI Search coverage show Google pushing multimodal generation and search-as-agent-infrastructure while also creating user-trust backlash.

## June 24–28: Computer use launch, talent loss, Gemini 3.5 Pro rumors

### Gemini 3.5 Flash computer use

Google baked computer use directly into Gemini 3.5 Flash — a first-class built-in capability across browser, desktop, and mobile. Developers can build agents that see, click, and control software without separate model calls. Safety controls include explicit user confirmation for sensitive actions and automated task stopping. This is a meaningful product shift: not just model APIs, but a standardized action interface with human-in-the-loop affordances.

### Noam Shazeer leaves for OpenAI

Noam Shazeer, co-lead of Gemini development, left Google to join [[openai]] — the second time he's quit Google for a competitor, less than two years after Google paid $2.7B to bring him back from Character.AI.

### Gemini 3.5 Pro rumors

Unverified rumors of a "Gemini 3.5 Pro" release circulated, claiming stronger vision, multimodal reasoning, better memory, agent workflows, and a 2.5M context window. Commenters were skeptical, noting the lack of coding benchmark claims and the implausible context-window number.

### BioNeMo Agent Toolkit

NVIDIA released its BioNeMo Agent Toolkit for life sciences: a framework for building AI agents that read papers, generate hypotheses, write code, and iterate on results — functioning as a junior scientist.

## Links

- Related concepts: [[ai-control-roadmaps]], [[frontier-model-access-controls]], [[coding-agent-evaluation]]
- Related entities: [[openai]], [[claude-fable-5]], [[amp]]
- See also: [[weekly-briefing-2026-06-24-to-2026-06-28]]
