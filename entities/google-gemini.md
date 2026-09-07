---
title: Google Gemini
created: 2026-07-30
updated: 2026-09-07
type: entity
tags: [ai, llm, model, company]
sources: [raw/newsletters/the-neuron-2026-07-23-google-split-gemini-in-three.md, raw/newsletters/ainews-2026-07-22-ainews-ai-cybersecurity-becomes-top-of-mind.md, raw/newsletters/ainews-2026-08-14-ainews-gemini-3-7-flash-brings-gdm-back-to-the-forefront.md, raw/newsletters/the-neuron-2026-08-14-why-gemini-3-7-flash-just-got-half-price.md, raw/newsletters/ainews-2026-09-02-ainews-claude-fable-mythos-5-1-new-sota-model-75-cache-price-cut-but-7.md, raw/newsletters/ainews-2026-09-03-ainews-muse-spark-1-3-matches-gpt-5-6-sol-confirming-meta-superintelli.md, raw/newsletters/the-neuron-2026-09-03-new-google-meta-and-maybe-openai-models.md, raw/newsletters/ainews-2026-09-04-ainews-gpt-6-astra-openai-s-biggest-llm-launch-of-all-time.md]
confidence: medium
---

# Google Gemini

**Google Gemini** is Google's model family in the corpus, increasingly split into specialized variants rather than a single one-model-fits-all product.

## July 2026 split

The Neuron reported Google releasing Gemini 3.6 Flash, Gemini 3.5 Flash-Lite, and Gemini 3.5 Flash Cyber. The product split separates a cheaper workhorse model, a high-throughput lightweight model, and a restricted cyber-defense model for governments and vetted partners. [raw/newsletters/the-neuron-2026-07-23-google-split-gemini-in-three.md:20-31]

AINEws adds the systems detail: Gemini 3.5 Flash Cyber is used inside CodeMender-style pipelines with multiple calls and output aggregation, where a smaller specialized model can beat larger general systems on practical vulnerability workflows. [raw/newsletters/ainews-2026-07-22-ainews-ai-cybersecurity-becomes-top-of-mind.md:24-26]

## August 2026: Flash resets the workhorse tier

Gemini 3.7 Flash arrived roughly three weeks after 3.6 Flash with reported gains on coding, autonomy, and agent benchmarks, a 1M context window, and introductory pricing at half the later rate. It rolled quickly into Google's products and external coding tools, reinforcing Gemini's strategy of frequent, specialized, high-volume releases. [raw/newsletters/ainews-2026-08-14-ainews-gemini-3-7-flash-brings-gdm-back-to-the-forefront.md][raw/newsletters/the-neuron-2026-08-14-why-gemini-3-7-flash-just-got-half-price.md]

The launch strengthens the model-routing interpretation of Gemini: Flash handles broad workhorse traffic while other variants can serve lightweight, restricted, or higher-quality needs. Reported results are promising but remain benchmark- and harness-dependent; the batch also flags the absence of a recent Pro update as an unresolved product signal.

## Why it matters

Gemini's July split reinforces a broader model-routing trend: agent systems increasingly need portfolios of specialized models, not just a single frontier endpoint. That connects [[google-gemini]] to [[ai-cybersecurity]], [[agent-experience]], and [[frontier-model-access-controls]].

## September 2026: Gemini 3.8 Flash

Gemini 3.8 Flash entered the same workhorse tier as [[muse-spark-1-3]], with coverage emphasizing coding, reasoning, long-running tasks, search-heavy work, and agent use at low latency. Reported pricing was $0.75 per million input tokens and $3.75 per million output tokens. Independent coverage said it was faster than the prior Flash release and competitive on several agentic, legal, finance, vision, biology, and reasoning slices, while heavier coding benchmarks still favored premium frontier models. [raw/newsletters/the-neuron-2026-09-03-new-google-meta-and-maybe-openai-models.md][raw/newsletters/ainews-2026-09-02-ainews-claude-fable-mythos-5-1-new-sota-model-75-cache-price-cut-but-7.md]

The useful comparison is completed-task economics. Coverage reported that Gemini’s token price stayed low but its extra work could make cost per completed task about 40% higher than Spark on one comparison. That is a routing signal, not a universal ranking: model choice must include expected turns, tool latency, verification, and failure recovery. [[gemini-3-8-flash]] therefore belongs in [[model-routing]] and [[ai-benchmarking]]. [raw/newsletters/the-neuron-2026-09-03-new-google-meta-and-maybe-openai-models.md]

## Links

- Related entity: [[google-deepmind]]
- Related concepts: [[ai-cybersecurity]], [[agent-experience]], [[frontier-model-access-controls]], [[software-factories]]
