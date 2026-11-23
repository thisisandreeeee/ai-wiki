---
title: AI for Science
created: 2026-09-28
updated: 2026-11-16
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

## October 2026 update: experiment, verification, and absorption

OpenAI's reported 722 mathematical manuscripts show a new bottleneck shape: generation can produce a large corpus quickly, but only some results are formalized and independent reviewers still need to verify, understand, and connect them. The relevant unit is verified and reusable knowledge, not raw output volume. [[ai-benchmarking]] [raw/newsletters/ainews-2026-10-07-ainews-quasi-riemann-hypothesis-openai-publishes-722-math-papers-solvi.md][raw/newsletters/the-neuron-2026-10-07-722-math-manuscripts-one-openai-model.md]

[[periodic-labs]] describes the physical analogue. Materials discovery needs synthesis, characterization, multimodal measurements, negative results, and reasoning under noisy and incomplete observations. Experiments are the ground truth because a model can otherwise exploit memorized answers or an imperfect simulator. [[self-driving-labs]] [raw/newsletters/latent-space-2026-10-08-synthesis-superintelligence-from-semiconductors-to-superconductors-per.md]

The AlphaFold discussion adds a scope warning: useful structure prediction is not the same as solving protein dynamics, function, whole-cell biology, or disease. A good scientific model therefore needs calibrated uncertainty and behavioral characterization even when internal interpretability is incomplete. [raw/newsletters/latent-space-2026-10-10-why-alphafold-didn-t-solve-protein-folding-pushmeet-kohli-google-deepm.md]

## November 2026: cell-specific genomics and formal proofs

DeepMind's AlphaGenome 2 models how a DNA variant changes gene regulation by cell type. The Neuron reports a 1-million-letter DNA input, more than 100 million cell profiles across 68 tissues, stronger results on variant discovery and effect direction in DeepMind's evaluations, and adaptation to new cell states without retraining. The model is research-only and not clinically or diagnostically validated; external replication on unseen cells and regions is the relevant next test. [[google-deepmind]] [raw/newsletters/the-neuron-2026-11-12-dna-isn-t-one-recipe-says-google-s-new-ai.md]

Two math stories sharpen the verification bottleneck. PSI reported an unreleased Anthropic model helping prove the Aaronson–Ambainis conjecture, with Lean checking the formal proof; Anthropic reported formalizing an existing Fermat proof; and DeepMind reported Lean-checked security properties for Signal code. These are checkable artifacts, not automatic guarantees that the formal statement matches the intended real-world claim. [[formal-verification-for-ai]] [[third-party-ai-evaluation]] [raw/newsletters/the-neuron-2026-11-09-would-you-trust-ai-math.md][raw/newsletters/the-neuron-2026-11-10-anthropic-released-claude-fable-5-2.md][raw/newsletters/the-neuron-2026-11-11-will-claude-join-your-meeting.md]

## November 2026: proof-producing physics and biological modeling

The Neuron reports that OpenAI and physicist Nathaniel Craig published a candidate lattice construction for the Standard Model that GPT-6 Astra helped develop and prove. As with other model-assisted mathematics in the corpus, a formal artifact is stronger evidence than fluent prose but does not by itself establish that the statement captures the intended physical claim; independent expert review remains necessary. [[astra]] [[formal-verification-for-ai]] [raw/newsletters/the-neuron-2026-11-16-nvidia-reportedly-supplied-china-via-asia.md]

Data Science Weekly's virtual-cell item offers a complementary framing: instead of simulating every molecule, a model might learn how cells respond to perturbations from enough training examples. The proposal is an intuition for a difficult predictive-biology problem, not evidence that a general virtual cell has been achieved. The relevant tests are held-out perturbations, causal validity, uncertainty, and experimental feedback. [[self-driving-labs]] [[ai-benchmarking]] [raw/newsletters/data-science-weekly-2026-11-19-data-science-weekly-issue-678.md]

## Links

- Related concepts: [[self-driving-labs]], [[recursive-self-improvement]], [[ai-benchmarking]], [[reliable-data-pipelines]], [[ai-cybersecurity]]
- Related entities: [[recursive]], [[radical-ai]], [[anthropic]]
