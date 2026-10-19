---
title: Muse Spark Open
created: 2026-10-19
updated: 2026-10-19
type: entity
tags: [ai, llm, model, tooling]
sources: [raw/newsletters/ainews-2026-10-16-ainews-agents-disprove-polysemanticity-greatly-improve-interpretabilit.md, raw/newsletters/ainews-2026-10-17-ainews-high-taste-testers-ep-1.md, raw/newsletters/the-neuron-2026-10-16-advertisers-can-target-chatgpt-by-prompt.md]
confidence: medium
---

# Muse Spark Open

**Muse Spark Open** is Meta's October 2026 open-weight multimodal MoE model for coding, long-horizon agents, and multi-step reasoning. The newsletter corpus reports 816B total parameters, 42B active parameters, and a 1M-token context window.

## Reported deployment profile

The release accepts text, image, video, and audio input and returns text. Reported weights are roughly 1.6TB in BF16 and about 530GB in Meta's NVFP4 checkpoint; the corpus describes deployment across multiple high-end accelerators or two 512GB Mac Studios, with day-one support from llama.cpp, vLLM, MLX, and related runtimes. [raw/newsletters/ainews-2026-10-16-ainews-agents-disprove-polysemanticity-greatly-improve-interpretabilit.md][raw/newsletters/ainews-2026-10-17-ainews-high-taste-testers-ep-1.md]

Artificial Analysis reports an Intelligence Index score of 39, first among US open-weight models in that comparison, but the model ranks weakly on the cited agentic evaluations. Pricing is reported at $1.25/$4.25 per million input/output tokens with discounted cached input; these are provider and evaluator measurements, not a universal cost-per-success result. [raw/newsletters/ainews-2026-10-16-ainews-agents-disprove-polysemanticity-greatly-improve-interpretabilit.md]

The custom Muse Model License requires attribution and a separate agreement for Model-as-a-Service businesses above a reported revenue threshold. “Open-weight” therefore does not mean unrestricted commercial use or low-cost local serving.

## Why it matters

Muse Spark Open connects Meta's open-model strategy to [[local-llms]], [[ai-infrastructure-economics]], and [[closed-vs-open-frontier-models]]. The deployment artifacts widen experimentation, while the model's size, license, safety tuning, and weaker agentic scores show that weights alone do not settle practical openness.

## Links

- Related entities: [[meta]], [[muse-spark-1-3]], [[muse-glimmer]], [[reflection-beam]]
- Related concepts: [[local-llms]], [[ai-benchmarking]], [[model-routing]], [[frontier-model-access-controls]]
