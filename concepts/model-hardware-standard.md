---
title: Model Hardware Standard
created: 2026-08-31
updated: 2026-08-31
type: concept
tags: [ai, machine-learning, research, tooling]
sources: [raw/newsletters/the-neuron-2026-08-26-anthropic-s-boldest-number-yet.md, raw/newsletters/the-neuron-2026-08-30-anthropic-taught-ai-agents-to-use-machines.md]
confidence: medium
---

# Model Hardware Standard

The **Model Hardware Standard (MHS)** is an Anthropic and HHMI Janelia research preview for giving AI agents a common interface to programmable laboratory and factory equipment. The late-August sources describe device drivers with read/write commands, plain-language capability and safety tags, and early use at Genentech, Carnegie Mellon, and QuEra.

## Why it matters

MHS attacks the integration bottleneck between agent software and physical equipment. A standard interface can let agents discover devices, sequence work across them, and turn successful procedures into reusable scripts instead of requiring a bespoke integration for every microscope, plate reader, or robot arm. One QuEra example reportedly recovered a quantum laser lock in 695 of 700 trials. [raw/newsletters/the-neuron-2026-08-30-anthropic-taught-ai-agents-to-use-machines.md]

The limits are equally important: this is a research preview, the equipment must be programmable, and Anthropic says expert oversight remains necessary for physical reasoning. The standard belongs beside [[agentic-robotics]] and [[self-driving-labs]], while its safety tags and driver boundary belong in [[agent-reliability-and-operations]].

## Links

- Related concepts: [[agentic-robotics]], [[self-driving-labs]], [[real-world-agent-evaluations]], [[agent-reliability-and-operations]]
- Related entities: [[anthropic]], [[microduck]]
