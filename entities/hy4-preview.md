---
title: Hy4-preview
created: 2026-08-31
updated: 2026-08-31
type: entity
tags: [ai, llm, model, research, tooling]
sources: [raw/newsletters/ainews-2026-08-28-ainews-openai-to-reach-agi-bar-by-end-2026.md, raw/newsletters/ainews-2026-08-29-ainews-openai-shuts-off-cursor.md]
confidence: medium
---

# Hy4-preview

**Hy4-preview** is Tencent’s reported open-weight frontier MoE model. The late-August sources describe roughly **770B total parameters**, about **49B active parameters**, and a **1M-token context window**, with early engineering evaluations placing it near the top of open-model coding results.

## Reported profile

AINews reports a blind side-by-side evaluation by 163 internal experts across 203 engineering tasks, where Hy4-preview narrowly led GLM-5.3 and Kimi K3 in the cited comparisons. The same coverage emphasizes that this is an early preview with remaining headroom in training and post-training, plus a tendency to overthink and over-verify. [raw/newsletters/ainews-2026-08-28-ainews-openai-to-reach-agi-bar-by-end-2026.md][raw/newsletters/ainews-2026-08-29-ainews-openai-shuts-off-cursor.md]

## Why it matters

Hy4-preview strengthens the open-weight frontier’s move toward very large, low-active-parameter models. The useful comparison is not total parameters alone: deployment depends on memory capacity, serving kernels, speculative decoding, context reuse, and whether the model’s extra verification improves outcomes enough to justify its token and latency cost.

That places Hy4-preview alongside [[glm-5-3]], [[qwen-3-8-flash-next]], [[model-routing]], and [[local-llms]].

## Links

- Related entities: [[glm-5-3]], [[qwen-3-8-flash-next]], [[kimi-k3]], [[nvidia]]
- Related concepts: [[model-routing]], [[llm-inference-optimization]], [[closed-vs-open-frontier-models]]
