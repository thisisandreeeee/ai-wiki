---
title: Physics Foundation Models
created: 2026-08-31
updated: 2026-08-31
type: concept
tags: [ai, machine-learning, research, model]
sources: [raw/newsletters/latent-space-2026-08-26-we-have-foundation-models-for-language-not-for-physics-anima-anandkuma.md]
confidence: medium
---

# Physics Foundation Models

**Physics foundation models** are AI systems intended to simulate or design across physical phenomena such as weather, fluids, fusion, heat flow, materials, and biology. The late-August source argues that these systems cannot simply copy language-model scaling because physical data is sparse, multi-scale, and often too large to fit into a conventional token context.

## Structure beats brute-force context

The source highlights neural operators as a way to learn evolving functions across scales while incorporating physical priors. Fourier and spherical-harmonic representations help weather models remain stable on a globe, where naive grid-based modeling can become unwieldy. In fusion, the reported opportunity is to predict disruptions from thousands of samples and accelerate simulation dramatically compared with traditional solvers. [raw/newsletters/latent-space-2026-08-26-we-have-foundation-models-for-language-not-for-physics-anima-anandkuma.md]

This is not an argument against scale. It is an argument that useful scale in physical AI may come from architecture, inductive bias, and simulator/data design rather than ever-larger token corpora. Formal verification of neural networks, as discussed through TorchLean, is especially relevant when a model enters a safety-critical control loop.

## Links

- Related concepts: [[self-driving-labs]], [[agentic-robotics]], [[real-world-agent-evaluations]], [[recursive-self-improvement]]
- Related entities: [[radical-ai]], [[simile-ai]], [[nvidia]]
