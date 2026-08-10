---
title: DeepSeek V4 Flash
created: 2026-08-10
updated: 2026-08-10
type: entity
tags: [ai, llm, model, tooling, research]
sources: [raw/newsletters/ainews-2026-08-01-ainews-not-much-happened-today.md, raw/newsletters/ainews-2026-08-05-ainews-megakernels-are-so-dead-and-so-back.md, raw/newsletters/ainews-2026-08-07-ainews-amd-buys-taalas.md, raw/newsletters/ainews-2026-08-08-ainews-zawinski-s-law-of-multiagents.md]
confidence: medium
---

# DeepSeek V4 Flash

**DeepSeek V4 Flash 0731** is presented in the new batch as a cost/performance frontier model with a 284B-total / roughly 13B-active architecture, a 1M context, and an MIT open-weight release.

## Batch signals

- DeepSeek described the update as a post-training improvement without a new architecture or model size; reported gains were concentrated in coding and agent evaluations. [^1]
- The batch cites public-beta API pricing around $0.14/M input and $0.28/M output, with a large cache-hit discount, alongside Responses API and Codex compatibility. These are newsletter-reported launch figures, not an independently verified price sheet. [^1]
- llama.cpp, vLLM, and other runtimes moved quickly to add support, while community reports showed both impressive heterogeneous-hardware experiments and major sensitivity to low-bit quantization. [^2]
- Demand and capacity pressure appeared together: later coverage reported rapid adoption and a possible future API price increase, but no final pricing schedule was available in the sources. [^3][^4]

## Why it matters

DeepSeek V4 Flash makes the open-model tradeoff unusually concrete: a model can be small in active parameters and inexpensive per token while still demanding substantial memory, bandwidth, and serving engineering. That makes it a useful counterpoint to the giant [[qwen-3-8-max]] and [[kimi-k3]] releases.

For production, compare model quality, quantization behavior, cache hit rate, latency, and cost per successful task through [[model-routing]] rather than treating a single benchmark as a verdict. The model's rapid runtime support also reinforces [[local-llms]] as a portability layer, not merely a hobbyist category.

## Links

- Related entities: [[qwen-3-8-max]], [[kimi-k3]], [[baseten]], [[nvidia]]
- Related concepts: [[local-llms]], [[llm-inference-optimization]], [[ai-infrastructure-economics]], [[coding-agent-evaluation]]

[^1]: [raw/newsletters/ainews-2026-08-01-ainews-not-much-happened-today]
[^2]: [raw/newsletters/ainews-2026-08-05-ainews-megakernels-are-so-dead-and-so-back]
[^3]: [raw/newsletters/ainews-2026-08-07-ainews-amd-buys-taalas]
[^4]: [raw/newsletters/ainews-2026-08-08-ainews-zawinski-s-law-of-multiagents]
