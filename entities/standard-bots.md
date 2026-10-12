---
title: Standard Bots
created: 2026-10-12
updated: 2026-10-12
type: entity
tags: [ai, company, machine-learning, tooling, research]
sources: [raw/newsletters/latent-space-2026-10-10-building-ai-for-reliable-execution-lessons-from-industrial-robotics.md]
confidence: medium
---
# Standard Bots

**Standard Bots** is an AI-native industrial robotics company building arms and software for machine tending, welding, and assembly.

## Deployment pattern

The company's reported stack uses a shared base model adapted through demonstrations and fine-tuning. A low-billion-parameter model handles perception, such as locating parts under changing lighting and materials, while conventional programs handle motion and cell logic. Training occurs in the cloud, but inference runs on-premise because factories need predictable uptime and may lack reliable connectivity.

Standard Bots describes a full-stack approach: it controls the arm, end effector, control system, and AI, allowing co-optimization of models and control policies. Failure signals and human corrections can feed fleet learning when customers permit it; air-gapped deployments remain a hard boundary. [[agentic-robotics]] [[agent-reliability-and-operations]]

## Lesson for physical AI

The interview favors targeted, high-quality deployment data over indiscriminate scale. Short-horizon learned behavior, conventional control for deterministic steps, local inference, and human correction are a practical pattern for reliable execution. [[self-driving-labs]] [[real-world-agent-evaluations]]
