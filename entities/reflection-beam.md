---
title: Reflection Beam
created: 2026-10-12
updated: 2026-10-12
type: entity
tags: [ai, llm, model, machine-learning, research]
sources: [raw/newsletters/ainews-2026-10-06-ainews-reflection-beam-501b-a23b-american-open-model.md, raw/newsletters/ainews-2026-10-07-ainews-quasi-riemann-hypothesis-openai-publishes-722-math-papers-solvi.md]
confidence: low
---
# Reflection Beam

**Reflection Beam** is a reported US-trained open-weight mixture-of-experts model from Reflection AI, aimed at coding, agentic, and scientific work.

## Reported release

- The announced architecture is 501B total parameters with 23B active, text-only, trained from scratch, with Apache 2.0 weights expected in October 2026.
- The source reports 23.8T pretraining tokens and a large reinforcement-learning run on roughly 10,000–10,500 GB300s, with more than 100M rollouts across about 1M tasks.
- Reflection claims 80.9 on SWE-bench Verified and 3–4x the inference efficiency of GLM 5.2. Independent early commentary places it around GLM-5.2 level and below stronger Chinese open models on some benchmarks.

The numbers are a mixture of company claims, early-access analysis, and commentary. The weights, technical report, reproducible evaluations, and real deployment data are the durable watch points. [[ai-benchmarking]] [[local-llms]]

## Strategic significance

Beam broadens the US open-weight supply, but it does not remove the infrastructure burden of large MoEs. Its positioning also reinforces the corpus trend that open weights improve control and customization while leaving memory, serving, and verification economics unresolved. [[ai-infrastructure-economics]] [[model-labs-vs-agent-labs]]
