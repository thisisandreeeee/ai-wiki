---
title: Poolside
created: 2026-07-30
updated: 2026-07-30
type: entity
tags: [ai, company, llm, model]
sources: [raw/newsletters/latent-space-2026-07-23-inside-the-model-factory-eiso-kant-poolside-ai.md, raw/newsletters/ainews-2026-07-23-ainews-laguna-s-2-1-released-cheaper-than-deepseek-v4-flash-better-tha.md, raw/newsletters/ainews-2026-07-22-ainews-ai-cybersecurity-becomes-top-of-mind.md]
confidence: medium
---

# Poolside

**Poolside** is an AI lab focused on code models, open-weight releases, and a high-throughput internal "Model Factory" for rapidly training and improving models.

## Corpus signals

Latent.Space's Eiso Kant interview frames Poolside as an engineering-first model lab: fewer than 70 researchers reportedly run roughly 10,000–20,000 experiments per month, with streaming data, reproducible experiments, low-precision compute, and agents increasingly writing code, launching jobs, evaluating results, and modifying model-training pipelines. [raw/newsletters/latent-space-2026-07-23-inside-the-model-factory-eiso-kant-poolside-ai.md:16-18]

The Laguna S 2.1 release made that strategy concrete: AINews described it as an open-weight 118B-parameter MoE with about 8B active parameters per token, positioned around agentic coding, persistence on long-horizon tasks, and single-DGX-Spark-scale deployment. [raw/newsletters/ainews-2026-07-22-ainews-ai-cybersecurity-becomes-top-of-mind.md:27-29]

## Why it matters

Poolside is the model-lab analogue of [[software-factories]]: it treats model development itself as an industrial loop with experiment throughput, reproducibility, evaluation, and agent-assisted pipeline work. The key claim is not simply that one model is strong; it is that the organization can compress model cycles from months to weeks.

Its open-weight stance also fits the strategic pressure around [[closed-vs-open-frontier-models]]. Poolside argues for many foundation-model companies rather than a small oligopoly, while also acknowledging that very capable open models may eventually raise release-policy questions.

## Model-factory thesis

Poolside's recurring themes:

- model building is mostly engineering and systems work;
- persistence, verification, and backtracking can outperform raw one-shot intelligence;
- harness/model co-design determines agent capability;
- RL may move earlier into training and become a bottleneck in wall-clock experimentation;
- smaller or more efficient models may cover more knowledge work than expected.

## Links

- Related models: [[kimi-k3]], [[glm-5-2]]
- Related concepts: [[software-factories]], [[recursive-self-improvement]], [[coding-agent-evaluation]], [[local-llms]]
- Related comparison: [[closed-vs-open-frontier-models]]
