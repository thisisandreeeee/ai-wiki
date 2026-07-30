---
title: Kimi K3
created: 2026-07-20
updated: 2026-07-20
type: entity
tags: [ai, llm, model, company]
sources: [raw/newsletters/ainews-2026-07-17-ainews-kimi-k3-2-8t-a50b-the-largest-open-model-ever-released-opus-4-8.md, raw/newsletters/the-neuron-2026-07-17-kimi-k3-just-shrank-openai-s-moat.md, raw/newsletters/the-neuron-2026-07-19-netflix-is-all-in-on-ai.md]
confidence: high
---

# Kimi K3

**Kimi K3** is Moonshot AI's July 2026 open-weight frontier-class model. The newsletter corpus treats it as the week’s strongest signal that open models are moving from “good for open” toward direct competition with closed frontier systems like [[gpt-5-6]] Sol and [[claude-fable-5]].

## Release profile

- AINews reports official Kimi K3 specs of **2.8T total parameters**, **1M-token context**, native multimodal input, Kimi Delta Attention, Attention Residuals, and open weights promised by July 27, 2026. [raw/newsletters/ainews-2026-07-17-ainews-kimi-k3-2-8t-a50b-the-largest-open-model-ever-released-opus-4-8.md:19-36]
- The Neuron summarizes it as an open 3T-class model with native vision, sparse experts, and full weights due by July 27. [raw/newsletters/the-neuron-2026-07-17-kimi-k3-just-shrank-openai-s-moat.md:50-63]
- Deployment is not casual local inference: sources note Moonshot’s guidance around 64+ accelerators for serious serving and early observations around ~26–30 tokens/s. [raw/newsletters/ainews-2026-07-17-ainews-kimi-k3-2-8t-a50b-the-largest-open-model-ever-released-opus-4-8.md:41-49]

## Capability and benchmark signals

K3’s launch combined strong benchmark claims with useful caveats:

- Arena ranked K3 #1 in Frontend Code Arena, with a reported 1679 score and 76% pairwise win rate, ahead of Claude Fable 5 and GPT-5.6 Sol in that slice. [raw/newsletters/ainews-2026-07-17-ainews-kimi-k3-2-8t-a50b-the-largest-open-model-ever-released-opus-4-8.md:25-30]
- Artificial Analysis scored K3 at 57 on its Intelligence Index, comparable to Opus 4.8 and GPT-5.5 but still behind Fable 5 and GPT-5.6 Sol overall. [raw/newsletters/ainews-2026-07-17-ainews-kimi-k3-2-8t-a50b-the-largest-open-model-ever-released-opus-4-8.md:29-58]
- The same coverage flags weaknesses: hallucination worsened on AA-Omniscience, K3 can be slow/verbose, and benchmark methodology matters, especially for coding partial-credit metrics. [raw/newsletters/ainews-2026-07-17-ainews-kimi-k3-2-8t-a50b-the-largest-open-model-ever-released-opus-4-8.md:62-90]

## Strategic read

K3 matters less as a laptop-local model and more as a pressure point on closed labs:

- It compresses the gap between open-weight and closed frontier capability, especially in frontend/coding tasks.
- It gives enterprises another path toward control, customization, and private deployment—if they can afford the infrastructure.
- It weakens pure model-access leverage for closed providers, pushing competition toward [[software-factories]], product polish, post-training, inference systems, and [[agent-experience]].

The important caveat: **open weights do not make frontier intelligence free**. K3 still requires serious serving infrastructure, strong harness defaults, and follow-up validation on hidden evals and production agent tasks.

## Links

- Related models: [[gpt-5-6]], [[claude-fable-5]], [[grok-4-5]], [[glm-5-2]], [[inkling]]
- Related concepts: [[closed-vs-open-frontier-models]], [[local-llms]], [[ai-infrastructure-economics]], [[coding-agent-evaluation]]
- See also: [[weekly-briefing-2026-07-20]]
