---
title: Runway WorldPrompt
created: 2026-09-28
updated: 2026-09-28
type: entity
tags: [ai, model, research, tooling]
sources: [raw/newsletters/latent-space-2026-09-25-runway-s-worldprompt-and-the-engineering-of-real-time-worlds.md]
confidence: medium
---

# Runway WorldPrompt

**WorldPrompt** is Runway's proposed input format for GWM Worlds 2, a research-preview world model that turns video and audio generation into a real-time interactive simulation.

## How it works

WorldPrompt fixes selected parts of a generated environment, including an initial frame, then describes timestamped events or actions. Events can also be supplied during the simulation, making the prompt a state-and-event interface rather than a one-shot text description. The source calls the underlying approach “autoregressive diffusion”: generation unfolds over time while retaining a diffusion-based visual process. [raw/newsletters/latent-space-2026-09-25-runway-s-worldprompt-and-the-engineering-of-real-time-worlds.md]

The engineering target is not only visual quality. Runway describes a system where a user or agent can act inside a persistent world, so temporal continuity, state, latency, controllability, and action semantics become first-class evaluation dimensions. That connects WorldPrompt to [[agentic-robotics]], [[ai-benchmarking]], and [[real-world-agent-evaluations]].

## Why it matters

WorldPrompt is a concrete step from generative media toward interactive simulation. It complements Runway's earlier [[runway-solaris]] story: Solaris treats rendered screens as an interface, while WorldPrompt treats generated audiovisual state as an environment. Neither should be treated as reliable software or a physical-world simulator without repeated trajectory and state-consistency tests.

## Links

- Related entity: [[runway-solaris]]
- Related concepts: [[agentic-robotics]], [[ai-benchmarking]], [[real-world-agent-evaluations]]
