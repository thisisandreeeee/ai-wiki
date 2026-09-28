---
title: AI for Science
created: 2026-09-28
updated: 2026-09-28
type: concept
tags: [ai, machine-learning, data-science, research, tooling, trend]
sources: [raw/newsletters/latent-space-2026-09-22-an-oscar-two-asteroids-and-the-algorithm-in-your-sklearn-john-platt-on.md, raw/newsletters/newsletter-2026-09-24-foundries-vs-navigators-lowering-the-cost-of-science.md, raw/newsletters/the-neuron-2026-09-24-what-950-claude-agents-found.md, raw/newsletters/latent-space-2026-09-23-bio-security-is-an-ai-arms-race-eric-nguyen-ceo-radical-numerics.md]
confidence: medium
---

# AI for Science

**AI for science** is the use of models, search, software, and experiments to generate and test scientific hypotheses. The central constraint is not only model intelligence; it is the speed, quality, and cost of verification in the physical world.

## Scoreable search and verification

Google's Empirical Research Assistance (ERA) frames many scientific problems as scoreable tasks: define a useful objective, then search over code and experiments that improve it. ERA keeps a tree of prior notebooks, uses an optimistic selection rule related to Monte Carlo Tree Search, mutates promising branches, and shares history across leaves. The source also warns that a score can be gamed; scientific validation must establish that the metric describes the phenomenon rather than merely winning the benchmark. [raw/newsletters/latent-space-2026-09-22-an-oscar-two-asteroids-and-the-algorithm-in-your-sklearn-john-platt-on.md]

## Foundries and navigators

The batch distinguishes **foundries**, which industrialize measurement through sequencing, multiplexing, microscopy, or physical automation, from **navigators**, which use AI inside ordinary company workflows to choose questions, build analysis tools, and triage possibilities. Endura's reported workflow used agents to screen roughly 500 disease targets, then research about 100 in greater depth, while retaining human checks against primary sources and selected programs. [raw/newsletters/newsletter-2026-09-24-foundries-vs-navigators-lowering-the-cost-of-science.md]

This distinction complements [[self-driving-labs]]. Foundries make the experimental loop faster; navigators make more hypotheses and decisions feasible before the next experiment. The moat is often the verified experimental data and the team's ability to convert it into the next useful action.

## Agentic discovery and biological risk

Anthropic's reported ART discovery used roughly 950 Claude agents to search more than 200,000 reverse transcriptases, nominate about 3,500 candidate systems, and narrow them to 20 for human review. Wet-lab work confirmed transcription into short RNAs, but the system's function and any programmable gene-editing utility remain unknown. The strongest claim is methodological: agents can widen search and surface an unusual candidate for human validation, not that Claude discovered “CRISPR 2.” [raw/newsletters/the-neuron-2026-09-24-what-950-claude-agents-found.md]

Genomic language-model coverage adds a dual-use warning. Long-context DNA models can represent long sequences and optimize sequence-level scores, but the same biological capability can improve both defense and harmful design. Human-in-the-loop validation does not remove the need for access controls, provenance, and biosecurity review. [[ai-cybersecurity]] and [[frontier-lab-governance]] are part of the science stack.

## Open questions

- Which scientific objectives are truly predictive rather than reward-hackable?
- How should agent-generated hypotheses be attributed, reproduced, and independently reviewed?
- Does faster hypothesis generation overcome slow wet-lab and clinical feedback loops?
- Which biological capabilities require staged access, monitoring, or dual-use restrictions?

## Links

- Related concepts: [[self-driving-labs]], [[recursive-self-improvement]], [[ai-benchmarking]], [[reliable-data-pipelines]], [[ai-cybersecurity]]
- Related entities: [[recursive]], [[radical-ai]], [[anthropic]]
