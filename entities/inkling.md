---
title: Inkling
created: 2026-07-20
updated: 2026-07-20
type: entity
tags: [ai, llm, model]
sources: [raw/newsletters/ainews-2026-07-16-ainews-thinky-s-inkling-975b-a41b-multimodal-new-best-american-apache.md, raw/newsletters/the-neuron-2026-07-16-chatgpt-may-get-a-body.md, raw/newsletters/the-neuron-2026-07-17-kimi-k3-just-shrank-openai-s-moat.md]
confidence: high
---

# Inkling

**Inkling** is Thinking Machines Lab’s first open-weight model family, released in July 2026 with a customization-first pitch. In this corpus it is important because it pairs a large American open-weight model with the same week’s [[kimi-k3]] release, making open frontier-adjacent models a two-sided U.S./China competition rather than a single-lab anomaly.

## Model profile

AINews reports Inkling as a sparse multimodal Mixture-of-Experts transformer with **975B total parameters**, **41B active parameters**, a **1M-token context window**, and pretraining over **45T tokens** spanning text, images, audio, and video. [raw/newsletters/ainews-2026-07-16-ainews-thinky-s-inkling-975b-a41b-multimodal-new-best-american-apache.md:14-18]

The same source highlights **Inkling-Small**, a preview sibling with 276B total parameters and 12B active parameters. Discussion framed it as potentially more attractive for lower-latency or high-end local/home inference than the full 41B-active model, depending on benchmarks and serving support. [raw/newsletters/ainews-2026-07-17-ainews-kimi-k3-2-8t-a50b-the-largest-open-model-ever-released-opus-4-8.md:174-180]

## Positioning

Thinking Machines positions Inkling around customization through Tinker rather than pure leaderboard dominance. The Neuron’s Kimi K3 coverage notes that Thinking Machines used open models, including older Kimi systems, to bootstrap early post-training data, making open models part of the supply chain for other model companies. [raw/newsletters/the-neuron-2026-07-17-kimi-k3-just-shrank-openai-s-moat.md:72-82]

That matters for [[closed-vs-open-frontier-models]]: open weights are not just end-user alternatives to closed APIs. They can become upstream ingredients for post-training, specialization, evals, and private model development.

## Caveats

- AINews discussion notes skepticism because Inkling did not clearly outperform competing open models such as [[glm-5-2]] in the cited leaderboard context. [raw/newsletters/ainews-2026-07-17-ainews-kimi-k3-2-8t-a50b-the-largest-open-model-ever-released-opus-4-8.md:174-180]
- Parameter scale complicates comparisons: a near-1T total-parameter model may be operationally harder to adopt than smaller open-weight systems even if it is technically strong.
- Its durable impact will depend on licensing, serving recipes, fine-tuning workflow, and whether Tinker makes customization materially easier than standard open-model tooling.

## Links

- Related models: [[kimi-k3]], [[glm-5-2]], [[gpt-5-6]], [[claude-fable-5]]
- Related concepts: [[local-llms]], [[closed-vs-open-frontier-models]], [[ai-infrastructure-economics]]
- See also: [[weekly-briefing-2026-07-20]]
