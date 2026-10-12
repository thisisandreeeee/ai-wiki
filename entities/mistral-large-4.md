---
title: Mistral Large 4
created: 2026-10-12
updated: 2026-10-12
type: entity
tags: [ai, company, llm, model, machine-learning]
sources: [raw/newsletters/ainews-2026-10-07-ainews-quasi-riemann-hypothesis-openai-publishes-722-math-papers-solvi.md]
confidence: medium
---
# Mistral Large 4

**Mistral Large 4**, nicknamed “Le Chonk” in AINews coverage, is a reported multimodal sparse MoE release from Mistral AI.

## Reported profile

- 1T total parameters and 49B active parameters.
- Pre- and post-trained on roughly 3,800 Grace Blackwell GPUs in Europe.
- API availability preceded promised open-weight release at the end of October 2026.
- Reported pricing was $1.36/$4.18 per million input/output tokens, with discounted cached input and an introductory discount.
- Sources disagree on context length, citing 512K and 1M variants, so the capability should be treated as provisional.

Mistral's benchmark claims place it ahead of selected open models on STEM, CAD, finance, and agentic coding. Independent reports cited in the newsletter place it around GPT-6 Luna on one intelligence index and note that heavy context can raise cost substantially. The benchmark and openness claims need independent, reproducible evaluation. [[ai-benchmarking]] [[local-llms]]

## Why it matters

Large open MoEs make the open-model tradeoff concrete: weights and customization can broaden access, while inference remains constrained by memory, interconnect, power, and serving quality. [[ai-infrastructure-economics]] [[model-routing]]
