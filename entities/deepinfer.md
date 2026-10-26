---
title: DeepInfer
created: 2026-10-26
updated: 2026-10-26
type: entity
tags: [ai, machine-learning, llm, tooling, research, company]
sources: [raw/newsletters/ainews-2026-10-21-ainews-deepseek-deepinfer-open-source-sota-inference-running-155t-toks.md]
confidence: medium
---

# DeepInfer

**DeepInfer** is DeepSeek's open-source production inference engine, released alongside serving details for [[deepseek-v4-1-flash]]. It is an example of inference infrastructure becoming part of a model lab's public research and competitive strategy.

## Reported capabilities

The source describes distributed inference, speculative decoding, SWA Bounded Replay, structured output, and support for NVIDIA and Huawei Ascend platforms. The companion `deepseek-recipe` layer implements production token processing and API-compatible interfaces. [raw/newsletters/ainews-2026-10-21-ainews-deepseek-deepinfer-open-source-sota-inference-running-155t-toks.md]

DeepSeek reports a cache-heavy production workload reaching 155 trillion served tokens per day from one cluster, with roughly 96% input-cache hits, about 400 ms average time to first token, and roughly 230 tokens/s generation. These are first-party production claims summarized by AINews, not independently audited measurements.

## The important boundary

“Open source” does not mean that the entire production service is reproducible from the initial release. The reporting says the inference engine is public while parts of KV-cache management, load balancing, and internal storage orchestration remain coupled to DeepSeek infrastructure. vLLM reported decode results within 6% of DeepInfer under a matched GB200 setup, but that comparison does not reproduce DeepSeek's whole cache fleet, routing, retention, or traffic mix.

The reported economics are similarly workload-dependent. DeepSeek cites $38 revenue per accelerator-hour at off-peak prices and high serving margins, but the calculations depend on cache hit rates, hardware cost, and omitted storage, networking, staffing, and reserve capacity. Treat the figure as a strong revenue disclosure, not a complete company margin statement. [[ai-infrastructure-economics]]

## Why it matters

DeepInfer makes the serving stack a first-class capability surface: cache lifetime, prefill/decode separation, scheduling, expert parallelism, and model-specific kernels shape the cost of persistent agents as much as the checkpoint does. The result connects [[llm-inference-optimization]] with [[local-llms]] and [[ai-infrastructure-economics]].

## Links

- Related entity: [[deepseek-v4-1-flash]]
- Related concepts: [[llm-inference-optimization]], [[llm-inference-on-gpus]], [[ai-infrastructure-economics]], [[local-llms]]
- Related query: [[weekly-briefing-2026-10-26]]
