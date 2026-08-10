---
title: Baseten
created: 2026-08-10
updated: 2026-08-10
type: entity
tags: [ai, company, tooling, machine-learning]
sources: [raw/newsletters/latent-space-2026-08-03-the-inference-engineering-masterclass-philip-kiely-ali-taha-baseten.md, raw/newsletters/ainews-2026-08-07-ainews-amd-buys-taalas.md]
confidence: medium
---

# Baseten

**Baseten** is an inference platform used in the batch as a concrete example of inference engineering becoming its own discipline: turning model weights into fast, reliable, affordable APIs at scale.

## Inference engineering lessons

The Baseten discussion describes cache-aware routing, prefill/decode disaggregation, speculative decoding, structured-output constraints, model parallelism, kernel work, and traffic-specific tuning. A long request may be routed to a replica with a reusable prefix, prefilled on one GPU group, and decoded on another; a small draft model can accelerate generation when its tokens are accepted often enough. [^1]

The episode also distinguishes shared APIs from dedicated deployments. Dedicated capacity becomes attractive when traffic is high or a customer needs custom batching, parallelism, precision, or a traffic-specific speculative decoder. Supporting a new open model on day zero is therefore an operational integration problem, not merely a model download.

## Strategic context

Baseten's support for Kimi K3, DeepSeek V4 Flash, and GLM-5.2 connects the platform to the open-weight frontier. [^2] The broader pattern is captured by [[llm-inference-optimization]]: model quality is only one input to latency, cost, and reliability; routing, kernels, memory movement, and topology can change the product outcome.

## Links

- Related entities: [[deepseek-v4-flash]], [[qwen-3-8-max]], [[kimi-k3]], [[nvidia]]
- Related concepts: [[llm-inference-optimization]], [[llm-inference-on-gpus]], [[model-routing]], [[ai-infrastructure-economics]]

[^1]: [raw/newsletters/latent-space-2026-08-03-the-inference-engineering-masterclass-philip-kiely-ali-taha-baseten]
[^2]: [raw/newsletters/ainews-2026-08-07-ainews-amd-buys-taalas]
