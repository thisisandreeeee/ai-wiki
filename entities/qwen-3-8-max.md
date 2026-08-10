---
title: Qwen 3.8 Max
created: 2026-08-10
updated: 2026-08-10
type: entity
tags: [ai, llm, model, company, research]
sources: [raw/newsletters/ainews-2026-08-04-ainews-qwen-3-8-max-2-4t-and-27b-new-open-weights-models-for-coding-an.md, raw/newsletters/ainews-2026-08-05-ainews-megakernels-are-so-dead-and-so-back.md, raw/newsletters/ainews-2026-08-06-ainews-jeff-sanjay-oriol-and-quoc-depart-deepmind-demis-to-chair-koray.md, raw/newsletters/ainews-2026-08-08-ainews-zawinski-s-law-of-multiagents.md, raw/newsletters/the-neuron-2026-08-02-why-is-deepseek-so-good-at-this.md, raw/newsletters/the-neuron-2026-08-03-why-mexico-s-top-university-axed-exams.md]
confidence: medium
---

# Qwen 3.8 Max

**Qwen 3.8 Max** is Alibaba Qwen's announced 2.4T-parameter flagship MoE model, paired with a smaller Qwen3.8-27B release. The batch positions it as an open-weight model for coding, long-horizon agentic work, multimodal reasoning, and technical workflows rather than only chat.

## What the batch supports

- Alibaba reported 10+ days of autonomous coding, long-running research, chip-design work, and multimodal agent capabilities; treat these as vendor claims until independently reproduced. [^1]
- Reported pricing was $2/M input, $6/M output, and $0.25/M cached tokens, with a 1M context and 128k maximum output cited by secondary coverage. [^1]
- Third-party summaries placed it near the public frontier on frontend-code, vision, and Vals-style indexes, but community discussion exposed ranking and benchmark-definition disputes. [^1]
- The 27B companion may matter more for broad adoption: the batch cites an estimate near 17 GB VRAM for a quantized/QAT-style release, while the 2.4T flagship remains a datacenter-scale deployment problem. [^2]

## Strategic read

Qwen 3.8 Max extends the [[closed-vs-open-frontier-models]] pattern: releasing a giant open-weight flagship can shift pricing, ecosystem leverage, and evaluation norms even when most users consume it through hosted inference. Its practical value depends on [[model-routing]], [[llm-inference-optimization]], and a reliable agent harness—not on parameter count alone.

The central unresolved question is whether the flagship's capability transfers to the smaller 27B tier without losing the long-horizon verification behavior that made the launch compelling. This is also a useful contrast with [[deepseek-v4-flash]], which appears smaller and more deployment-oriented.

## Links

- Related entities: [[deepseek-v4-flash]], [[kimi-k3]], [[inkling]], [[baseten]]
- Related concepts: [[local-llms]], [[model-routing]], [[coding-agent-evaluation]], [[agentic-systems]]

[^1]: [raw/newsletters/ainews-2026-08-04-ainews-qwen-3-8-max-2-4t-and-27b-new-open-weights-models-for-coding-an.md]
[^2]: [raw/newsletters/ainews-2026-08-05-ainews-megakernels-are-so-dead-and-so-back.md]
