---
title: Modal
created: 2026-07-13
updated: 2026-07-13
type: entity
tags: [ai, company, tooling]
sources: [raw/newsletters/latent-space-2026-07-08-why-ai-infrastructure-must-evolve-for-agent-experience-akshat-bubna-mo.md]
confidence: high
---

# Modal

**Modal** is an AI cloud platform in the corpus that illustrates how infrastructure is being redesigned for [[agent-experience]] rather than only human developer experience.

## Why it matters

Latent.Space framed Modal's 2026 position as an agent-cloud story: after a $355M Series C, Modal is moving from traditional web-app assumptions toward elastic inference, sandboxes, GPU burst, post-training, background agents, and infrastructure that agents can operate directly. [raw/newsletters/latent-space-2026-07-08-why-ai-infrastructure-must-evolve-for-agent-experience-akshat-bubna-mo.md:14-23]

## Core primitives

The Modal discussion emphasizes infrastructure that fits agent loops:

- serverless functions and decorator-based infrastructure instead of Kubernetes/YAML-heavy workflows;
- sandboxes for code execution, debugging, and iteration;
- elastic inference, GPU snapshotting, speculative decoding, Auto Endpoints, and custom model serving;
- persistent storage, networked containers, private IPv6, RDMA, and multi-node training;
- capacity pooled across 17 cloud providers. [raw/newsletters/latent-space-2026-07-08-why-ai-infrastructure-must-evolve-for-agent-experience-akshat-bubna-mo.md:21-42]

## Agent-experience turn

Modal's CTO described the SDK team as shifting from developer experience to agent experience: an agent should not have to read hundreds of Kubernetes files or write untyped YAML when it can alter typed, co-located infrastructure declarations and observe the result. [raw/newsletters/latent-space-2026-07-08-why-ai-infrastructure-must-evolve-for-agent-experience-akshat-bubna-mo.md:114-123]

The infrastructure bet is that agents need fast, observable loops: write code, run it, inspect output, change environments, debug failures, and try again. That is why Modal connects naturally to [[software-factories]] and [[ai-infrastructure-economics]].

## Links

- Related concepts: [[agent-experience]], [[software-factories]], [[ai-infrastructure-economics]]
- Related entities: [[cognition]], [[openai]]
- Related query: [[weekly-briefing-2026-07-13]]
