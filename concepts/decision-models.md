---
title: Decision Models
created: 2026-10-05
updated: 2026-10-05
type: concept
tags: [ai, llm, model, tooling, trend]
sources: [raw/newsletters/ainews-2026-09-16-ainews-jev-a-system-one-model-that-only-decides-classifies-routes-scor.md, raw/newsletters/ainews-2026-09-30-ainews-openai-devday-2026-dots-6-1-sol-ultrafast-decisions-api-agents.md, raw/newsletters/latent-space-2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-openai-shipped-its-jev-co.md, raw/newsletters/ainews-2026-10-02-ainews-pi-1-0-pi-durable-and-aie-nyc.md]
confidence: medium
---

# Decision Models

A **decision model** returns a bounded choice, score, route, or probability instead of composing open-ended prose. It is useful when the answer space is known and high-volume decisions need lower latency, lower cost, or more explicit calibration than a general-purpose language-model call.

## Product pattern

[[jev]] established the clearest corpus example: a specialist model for typed decisions, classification, routing, judging, and scoring. OpenAI's Decisions API is a rapid product response built initially on GPT-6 Luna, with vision support and batch-oriented inference. Perplexity's `pplx-decider-v1-27b` and Databricks' `ai_decide()` show the pattern spreading into multimodal endpoints and dataset-scale data workflows. [^1]

The architecture is usually a two-stage route:

1. use a fast decision model for routine, well-defined cases;
2. abstain or escalate uncertain cases to a stronger language/reasoning model or a human;
3. verify downstream effects rather than treating confidence as correctness.

This makes calibration, abstention, class design, and error costs more important than a single latency or token-price number. [[model-routing]] is the natural systems layer; [[ai-benchmarking]] supplies the evaluation discipline.

## What decision models are not

They are not general replacements for models that must explain, plan unconstrained work, write novel content, or choose a sequence of unknown tools. Structured output alone does not create a decision model: the practical distinction is the training objective, latency profile, confidence behavior, and operational contract.

OpenAI's early implementation reportedly wraps Luna rather than introducing a wholly separate architecture. That makes it a useful product primitive even while the research novelty and calibration quality remain open questions. [^2]

## Evaluation

Measure:

- calibration and reliability diagrams;
- abstention quality and escalation rate;
- downstream error and business cost;
- latency under batch and peak load;
- cost per verified decision;
- drift when labels, tools, or class definitions change.

## Links

- Related entities: [[jev]], [[openai]], [[openai-dots]]
- Related concepts: [[model-routing]], [[ai-benchmarking]], [[agent-reliability-and-operations]], [[llm-application-interface]]

[^1]: [raw/newsletters/ainews-2026-10-02-ainews-pi-1-0-pi-durable-and-aie-nyc.md]
[^2]: [raw/newsletters/latent-space-2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-openai-shipped-its-jev-co.md]
