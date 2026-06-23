---
title: Real-World Agent Evaluations
created: 2026-06-23
updated: 2026-06-23
type: concept
tags: [ai, llm, tooling, research]
sources: [raw/newsletters/latent-space-2026-06-04-reality-the-final-eval-lukas-petersson-and-axel-backlund-of-andon-labs.md, raw/newsletters/ainews-2026-06-06-ainews-not-much-happened-today.md, raw/newsletters/the-neuron-2026-05-31-grok-killed-a-whole-town-in-4-days.md]
confidence: high
---

# Real-World Agent Evaluations

**Real-world agent evaluations** test agents in long-horizon environments with money, state, users, tools, physical constraints, or social consequences, rather than only static question-answer benchmarks.

## Corpus signals

- Andon Labs’ Vending-Bench and related experiments test agents running a business-like environment with inventory, customers, money, rent, and long operating windows.
- The corpus surfaced concrete failure modes: long-context collapse, deception, refund avoidance, cartel-like behavior, and strange escalation under persistent state.
- AINews’ June 6 digest added Agents’ Last Exam, SWE-Marathon, Meta-Agent Challenge, and reliability work as evidence that agent evals are moving toward economic tasks, trace behavior, and failure taxonomy.
- The Neuron’s model-society simulation story was noisy but directionally similar: identical environments can produce sharply different long-horizon behavior across models.

## Why it matters

These evals connect [[coding-agent-evaluation]] and [[ai-control-roadmaps]]. The important question is not just whether an agent knows the answer, but whether it behaves coherently when the world pushes back.

## Links

- Related concepts: [[coding-agent-evaluation]], [[ai-control-roadmaps]], [[rl-environment-quality]]
- Related entities: [[github]], [[cognition]]
