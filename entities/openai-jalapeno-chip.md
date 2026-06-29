---
title: OpenAI Jalapeño Chip
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [ai, company, tooling, model]
sources: [raw/newsletters/ainews-2026-06-25-ainews-it-s-meta-harness-summer.md, raw/newsletters/the-neuron-2026-06-25-chatgpt-s-secret-advantage.md]
confidence: high
---

# OpenAI Jalapeño Chip

**Jalapeño** is [[openai|OpenAI]]'s first custom AI inference chip, built with Broadcom and designed specifically for LLM inference workloads (ChatGPT, Codex, API traffic, and future agent products). Announced June 2026.

## Specifications and claims

- Purpose-built inference ASIC, not a general-purpose GPU
- Built with Broadcom; described as TPU-like in architecture
- Community estimates: near-reticle die, ~216GB HBM3E, ~7.1–7.4 TB/s bandwidth, ~10 PFLOPS FP4
- 9-month design-to-tapeout cycle — reportedly accelerated by OpenAI's own models, described as unusually fast for a high-performance ASIC
- Already running GPT-5.3-Codex-Spark internally
- Full deployment target: end of 2026, with Microsoft buying 40% of the first batch

## Strategic significance

OpenAI has historically depended on [[nvidia|NVIDIA]] GPUs for inference. Jalapeño represents a vertical-integration play: own the chip, the model, and the product to control compute economics. By designing around exactly how ChatGPT processes tokens, OpenAI can squeeze more efficiency per dollar.

The same day, Qualcomm announced it's acquiring Modular (the Mojo language company), signaling broader competition in vertically integrated inference stacks beyond NVIDIA/CUDA.

## Ecosystem implications

- Hyperscaler-style inference silicon becomes table stakes for frontier labs
- Custom ASICs could let OpenAI outprice competitors who rent NVIDIA hardware
- No performance claims have been independently verified yet
- Fits the broader trend of [[ai-infrastructure-economics|AI infrastructure economics]]: labs moving down the stack to control costs

## Links

- Related entities: [[openai]], [[nvidia]], [[gpt-5-6]]
- Related concepts: [[ai-infrastructure-economics]], [[model-labs-vs-agent-labs]]
- See also: [[coding-agent-evaluation]]
