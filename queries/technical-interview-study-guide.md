---
title: Technical Interview Study Guide
created: 2026-07-18
updated: 2026-07-18
type: query
tags: [ai, machine-learning, llm, tooling]
sources: [raw/learning-resources/technical-interview-learning-resources.md]
confidence: high
---

# Technical Interview Study Guide

This is a map from the attached question bank to durable concepts. Use it to explain mechanisms, trade-offs, and failure modes in your own words—not to memorize isolated definitions. A strong answer usually follows: **define the mechanism → trace the data/control flow → name the constraint → choose a design for a scenario**.

## Learning order

1. [[attention-and-transformer-architecture]] — embeddings, Q/K/V, softmax, masks, encoder/decoder, MoE.
2. [[llm-training-lifecycle]] — pretraining, CPT, post-training, SFT, DPO, RLHF/RLAIF, LoRA, and distillation.
3. [[llm-application-interface]] — message roles, temperature, structured outputs, tool calling, MCP, and workflow patterns.
4. [[retrieval-augmented-generation]] — ingestion, databases, embeddings, chunking, retrieval quality, and evaluation.
5. [[agentic-systems]] and [[agent-reliability-and-operations]] — loops, harnesses, state, safety, evaluation, incidents, and releases.
6. [[llm-inference-on-gpus]] and [[llm-inference-optimization]] — GPU constraints, KV cache, prefill/decode, batching, kernels, quantization, and parallelism.

## Coverage checklist

### Model and training

- [ ] Explain why CPT and SFT can share cross-entropy mechanics but have different outcomes.
- [ ] Choose SFT, DPO, or RL from the available supervision and explain what each loss encourages.
- [ ] Explain why DPO compares policy likelihoods relative to a reference model.
- [ ] Separate a training stage/objective from an update method such as LoRA.
- [ ] Explain why RL needs an evaluable reward and how reward hacking can occur.

### Architecture

- [ ] Trace $QK^T\rightarrow$ scale $\rightarrow$ softmax $\rightarrow V$, including tensor axes.
- [ ] Explain why scaling and causal masking happen before softmax.
- [ ] Contrast self-attention, cross-attention, FFN, encoder, decoder, decoder-only LLM, and MoE.
- [ ] Distinguish trained parameters from transient forward-pass tensors.

### Applications and retrieval

- [ ] Draw a model/tool loop where the application—not the model—validates and authorizes the action.
- [ ] Distinguish tool calling from MCP, and workflow from agent.
- [ ] Draw RAG from source document to answer, including permission filtering and reranking.
- [ ] Diagnose a wrong answer as retrieval versus generation failure and name layer-specific metrics.
- [ ] Explain why vectors are a derived search index, not a source of truth.

### Agent systems and operations

- [ ] Explain runtime, harness, and control plane as different responsibility scopes.
- [ ] Design durable state and idempotency around a potentially duplicated external write.
- [ ] Evaluate an agent trajectory separately from its final answer.
- [ ] Name controls that must live outside model instructions: permissions, schemas, budgets, approvals, audit, and kill switch.
- [ ] Describe a safe recovery and release pipeline for a changed agent behaviour bundle.

### Inference systems

- [ ] Trace prefill and decode token by token; state why their bottlenecks often differ.
- [ ] Estimate weight and KV-cache memory, including the variables that change the result.
- [ ] Select data, tensor, and pipeline parallelism from model-fit and topology constraints.
- [ ] Explain how continuous batching, PagedAttention, prefix caching, FlashAttention, quantization, and speculative decoding help—and when they do not.
- [ ] Start an optimisation discussion with metrics and a workload profile rather than a universal technique ranking.

## Practice prompts

For each topic, practice three levels of answer:

1. **one sentence** — the core distinction;
2. **whiteboard** — data flow, equation, or state machine;
3. **production scenario** — constraints, failure modes, and the smallest justified design.

If an answer does not mention what is *measured* or what can go *wrong*, it is likely still a definition rather than working understanding.
