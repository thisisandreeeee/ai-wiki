---
title: Xiaomi MiMo-V2.6-Pro
created: 2026-09-28
updated: 2026-09-28
type: entity
tags: [ai, llm, model, machine-learning, research, tooling, trend]
sources: [raw/newsletters/ainews-2026-09-22-ainews-xiaomi-mimo-v2-6-pro-1t-a42b-the-new-top-open-weights-model-tra.md, raw/newsletters/ainews-2026-09-25-ainews-the-future-of-latent-space.md, raw/newsletters/the-neuron-2026-09-23-new-gpt-6-and-claude-models-start-a-price-war.md]
confidence: medium
---

# Xiaomi MiMo-V2.6-Pro

**MiMo-V2.6-Pro** is Xiaomi's reported open-weight, natively omnimodal frontier model. The September batch presents it as a major Chinese open-model release and as a test of whether post-training environments are becoming a strategic asset.

## Model and release

The sources describe a roughly **1.02T-total / 42B-active** model with a 1M-token context window, MIT licensing, and a reported Artificial Analysis Intelligence Index score of 46. Reported API prices vary by task framing, but the consistent signal is unusually low cost relative to closed frontier models. These figures are source-reported and need independent replication. [raw/newsletters/ainews-2026-09-22-ainews-xiaomi-mimo-v2-6-pro-1t-a42b-the-new-top-open-weights-model-tra.md][raw/newsletters/ainews-2026-09-25-ainews-the-future-of-latent-space.md]

Xiaomi released more than weights: the coverage describes technical reports, RL code, task environments, graders, and training recipes spanning coding, general agents, visual/web development, cyber, and music. The complete 7,000-plus task datasets were not released, so the openness is substantial but not complete. [raw/newsletters/ainews-2026-09-22-ainews-xiaomi-mimo-v2-6-pro-1t-a42b-the-new-top-open-weights-model-tra.md]

## Scaling lesson

The reported RL run used large asynchronous batches, 1M-token contexts, multi-task environments, and richer grader computation. One account cited about 130 hours, 75B tokens, and $2.6M for the run; another source framed the release as roughly $3M to train. Treat these as differing newsletter summaries rather than a reconciled cost estimate.

The durable implication is that high-quality, reusable environments may matter as much as pretraining data. Open RL environments lower the barrier for replication, while the missing full task corpus limits independent verification. [[recursive-self-improvement]] and [[ai-benchmarking]] are the relevant lenses.

## Position in the model market

MiMo-V2.6-Pro strengthens the open-weight side of [[closed-vs-open-frontier-models]]: capability is arriving with lower token cost and more inspectable post-training infrastructure, even when serving a trillion-parameter MoE still carries significant memory and systems requirements. [[local-llms]] and [[ai-infrastructure-economics]] capture the deployment tradeoff.

## Links

- Related entities: [[openai]], [[deepseek-v4-1-flash]], [[qwen-3-8-max]]
- Related concepts: [[local-llms]], [[recursive-self-improvement]], [[model-routing]], [[ai-benchmarking]]
