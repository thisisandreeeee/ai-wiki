---
title: Dyna-2
created: 2026-10-19
updated: 2026-10-19
type: entity
tags: [ai, machine-learning, model, research]
sources: [raw/newsletters/latent-space-2026-10-13-dyna-2-general-purpose-physical-agents-with-hour-long-autonomy-jason-m.md]
confidence: medium
---

# Dyna-2

**Dyna-2** is Dyna Robotics' world-action model for physical agents. It combines video, robot state, language instructions, future-state prediction, and executable actions; the reported architecture uses a diffusion transformer and flow matching to produce smooth, reactive motion.

## Reported approach

Dyna reports pretraining on more than one million hours of human video, followed by robot-specific data and short task demonstrations. The stated goal is cross-embodiment transfer: human video supplies broad physical priors, while robot data supplies hardware-specific dexterity and control. Dyna-2.1 is presented as a physical robot agent that can adapt to tasks from roughly 45 minutes of demonstrations. [raw/newsletters/latent-space-2026-10-13-dyna-2-general-purpose-physical-agents-with-hour-long-autonomy-jason-m.md]

The source reports a 99.4% success rate folding restaurant napkins for 24 hours, including recovery after pulling over a stack, and deployments involving thousands of napkins daily. These are company-reported deployment claims; the important evaluation target is sustained, recoverable execution rather than a short demo.

## Constraints

Robotics has no equivalent of the open internet for data. Dyna therefore combines egocentric video, robot demonstrations, synthetic environments, self-generated world-model data, on-device inference, distillation, and custom hardware. Dexterous hands, sensory coverage, latency, and supply chains remain bottlenecks.

## Links

- Related entities: [[standard-bots]], [[modal]]
- Related concepts: [[agentic-robotics]], [[self-driving-labs]], [[real-world-agent-evaluations]], [[agent-reliability-and-operations]]
