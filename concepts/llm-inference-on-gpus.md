---
title: LLM Inference on GPUs
created: 2026-07-18
updated: 2026-08-10
type: concept
tags: [ai, llm, tooling, machine-learning]
sources: [raw/learning-resources/technical-interview-learning-resources.md, raw/newsletters/latent-space-2026-08-03-the-inference-engineering-masterclass-philip-kiely-ali-taha-baseten.md, raw/newsletters/ainews-2026-08-05-ainews-megakernels-are-so-dead-and-so-back.md, raw/newsletters/ainews-2026-08-01-ainews-not-much-happened-today.md]
confidence: high
---

# LLM Inference on GPUs

LLM inference repeatedly applies model weights while managing memory movement, attention state, and many concurrent sequences. A useful performance model separates **compute**, **memory capacity**, **memory bandwidth**, and **communication**.

## Hardware mental model

A GPU has compute units plus a hierarchy of memory. Registers and shared/cache memory are small and very fast on chip. **HBM** is the GPU's large, high-bandwidth working memory—not persistent storage. CPU RAM and disk sit farther away.

- **Compute** performs matrix multiplications and kernels.
- **Capacity** determines whether weights, KV cache, activations, workspaces, and safety reserve fit.
- **Bandwidth** determines how quickly those bytes reach compute.
- **Arithmetic intensity** is $\text{FLOPs}/\text{bytes moved}$: high intensity tends toward compute-bound operation; low intensity tends toward bandwidth-bound operation.

A rough weight-only capacity estimate is parameter count times bytes per stored parameter: a 7B-parameter model is about 14 GB in FP16 and 7 GB in nominal INT8 before scales, runtime overhead, KV cache, or workspace.

## Prefill and decode

```text
prefill(prompt tokens) → logits for first output token → sample
→ decode(one new token) → logits for next token → repeat
```

**Prefill** processes known prompt tokens through all layers, often using large parallel matrix operations. It computes and stores each token's keys and values in the KV cache. **Decode** processes one new token per active sequence, reads prior cache state, appends the new token's K/V, and repeats autoregressively.

Prefill is often more compute-bound; decode is often more bandwidth-bound because weights and cache are repeatedly read for comparatively little per-sequence work. This is a heuristic, not a law: batch size, context length, model, quantization, kernels, and scheduler can change the bottleneck.

## KV cache

Caching keys and values avoids recomputing them for prior tokens. Approximate KV-cache memory is:

$$2 \times L \times T \times H_{kv} \times d_{head} \times \text{bytes/element} \times B,$$

where $L$ is layers, $T$ cached tokens, $H_{kv}$ KV heads, $d_{head}$ head size, and $B$ active sequences. The factor two is keys plus values.

This makes KV cache grow with context and concurrency. **Grouped-query attention (GQA)** reduces the number of KV heads relative to query heads, reducing cache capacity and decode bandwidth. A cache is per active sequence/token prefix, not permanent conversational memory.

## Parallelism and topology

A **node** is a physical server with CPU, RAM, storage, networking, and one or more GPUs. GPU count is constrained by power, cooling, physical space, PCIe lanes, and high-speed interconnect.

| Strategy | What is split | Main trade-off |
| --- | --- | --- |
| data parallelism | requests across full model replicas | best throughput scaling when the model fits on one GPU |
| tensor parallelism (TP) | work inside layers | frequent high-bandwidth collectives; best within a fast node |
| pipeline parallelism (PP) | groups of layers | less frequent communication but pipeline bubbles and sequential stages |

If a model fits on one GPU, use replicas for throughput first. If it needs sharding, try TP within high-bandwidth NVLink/NVSwitch topology; for larger cross-node placement, consider hybrid TP-within-node and PP-across-node. Profile actual communication rather than treating the rule as universal.

## August 2026 update: topology is part of the model

The new inference coverage reinforces that GPU placement is an application decision. Prefill and decode can use different GPU pools; tensor, expert, and pipeline parallelism must be tuned against the actual interconnect; and identical weights can behave differently across clusters because kernels, scheduling, races, and memory movement differ. [[baseten]] frames this as auto-tuning against representative traffic rather than a one-time hardware choice.

The open-model examples make capacity trade-offs visible. [[qwen-3-8-max]] is strategically important but datacenter-scale, while [[deepseek-v4-flash]] has a smaller active footprint yet still exposes storage, bandwidth, and quantization constraints. “Open weights” changes who can inspect and serve a model; it does not remove the hardware system around it.

## Links

- [[attention-and-transformer-architecture]] explains why attention creates a growing KV cache.
- [[llm-inference-optimization]] covers batching, paging, quantization, kernels, and selection rules.
- [[agent-reliability-and-operations]] connects serving latency/cost to end-to-end task SLOs.
- [[technical-interview-study-guide]] lists the inference questions this note supports.
