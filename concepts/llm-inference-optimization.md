---
title: LLM Inference Optimization
created: 2026-07-18
updated: 2026-08-10
type: concept
tags: [ai, llm, tooling, machine-learning]
sources: [raw/learning-resources/technical-interview-learning-resources.md, raw/newsletters/latent-space-2026-08-03-the-inference-engineering-masterclass-philip-kiely-ali-taha-baseten.md, raw/newsletters/ainews-2026-07-31-ainews-gpt-5-6-price-cut-by-20-80-cost-of-gpt-5-4-intelligence-dropped.md, raw/newsletters/ainews-2026-08-01-ainews-not-much-happened-today.md]
confidence: high
---

# LLM Inference Optimization

Inference optimization is bottleneck removal under a quality and SLO constraint. Profile first: the limiting factor may be compute, HBM bandwidth, memory capacity, inter-GPU communication, CPU launch overhead, queueing, or an upstream service—not “the model” in general.

## Measure the user-visible path

- **TTFT** (time to first token) includes queueing, tokenization, prefill, and transport.
- **TPOT** (time per output token) captures decode responsiveness.
- **End-to-end latency** includes TTFT plus all generated tokens.
- Track p50/p95/p99, queue time, input/output tokens per second, active sequences, HBM by weights/KV/workspace, cache hits/evictions, and **cost per successful task**.

## Scheduling and cache management

Static batching waits for a fixed group and wastes capacity as sequences finish at different times. **Continuous (in-flight) batching** admits and removes sequences between decode iterations, improving utilization and throughput. Its cost is scheduling complexity and potential TTFT/tail-latency trade-offs.

- **PagedAttention** allocates KV cache in blocks/pages, reducing fragmentation for variable-length sequences.
- **Prefix caching** reuses K/V only for an identical token prefix under compatible model/serving settings; stable system prompts and repeated documents benefit most.
- **Chunked prefill** prevents one long prompt from monopolizing a GPU and harming decode responsiveness.
- Prefill/decode disaggregation can isolate their different resource profiles, but adds KV transfer and operational complexity.

Use interactive SLOs to bound batch wait time and prioritize fairness; offline jobs can favor larger batches and throughput.

## Reduce IO before changing algorithms

Naive attention materializes large $T\times T$ score/probability matrices in HBM. **FlashAttention** tiles Q/K/V through on-chip memory and uses online softmax statistics, avoiding materializing that full matrix in HBM. It reduces IO while preserving the attention computation; it is especially valuable for long prefill/training but is not a cure-all for decode latency.

Kernel fusion reduces intermediate reads/writes and launch overhead. CUDA Graphs can reduce CPU launch overhead when shapes and control flow are stable. These gains depend on the actual runtime and workload.

## Quantization

Quantization reduces representation precision to lower memory use and, where supported, bandwidth/compute cost:

- **weight-only** quantization is usually the safest first serving experiment;
- **weight + activation** quantization can offer more benefit but requires careful calibration;
- **KV-cache** quantization targets long-context/high-concurrency capacity and decode bandwidth.

Bits do not translate directly to end-to-end speed: scales, packing, dequantization, kernel support, batch shape, and the current bottleneck matter. Validate task quality, tool-call correctness, structured output, safety, and long-context behavior—not only tokens per second.

## Speculative decoding

A cheap draft model proposes several tokens; the target model verifies them in parallel and accepts a prefix. A correct speculative-sampling implementation preserves the target distribution. It pays off only when draft cost is low, target agreement is high, and verification is efficient; measure acceptance length and TPOT under representative traffic.

## August 2026 update: inference engineering

The Baseten masterclass makes the serving stack more explicit. A 200K-token request may benefit from cache-aware routing, prefill/decode disaggregation, a traffic-specific speculative decoder, and structured-output constraints; dedicated deployments become attractive when traffic or reliability requirements justify custom batching, topology, precision, or kernels. [raw/newsletters/latent-space-2026-08-03-the-inference-engineering-masterclass-philip-kiely-ali-taha-baseten.md]

The new batch also reports model-assisted serving optimization and sharp GPT-5.6 price cuts. Treat the numerical claims as source-reported, but the engineering implication is robust: optimize the whole path—routing, cache reuse, kernels, batching, and workload-specific orchestration—before assuming a new checkpoint is the only route to lower cost. [[baseten]] and [[deepseek-v4-flash]] provide concrete open-serving examples.

## A selection guide

| Observed bottleneck | Candidate moves |
| --- | --- |
| high TTFT | reduce/reuse prefix context, improve prefill kernels, chunk prefill, reduce queueing |
| high TPOT | continuous batching, weight quantization, kernel improvements, speculative decoding |
| OOM / low concurrency | cap context/output, GQA model, quantize weights/KV, page KV, admission control |
| low throughput but acceptable latency | batching, sequence packing, prefix cache, replica scaling |
| long-context slowdown | FlashAttention, retrieval/context reduction, cache controls |
| model does not fit | quantize, TP within node, then hybrid TP/PP; treat CPU/NVMe offload as capacity fallback |
| communication dominates | reduce TP degree, use faster interconnect, evaluate PP/hybrid topology |

Performance is not a win if task success regresses. Re-run end-to-end quality, cost, and tail-latency evaluation after every serving change.

## Links

- [[llm-inference-on-gpus]] provides the memory, parallelism, and prefill/decode model.
- [[attention-and-transformer-architecture]] explains the underlying attention IO pattern.
- [[agent-reliability-and-operations]] turns serving signals into product SLOs and release gates.
- [[retrieval-augmented-generation]] can reduce context length when external evidence is more efficient than prompt stuffing.
