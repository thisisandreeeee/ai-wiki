---
title: Astra
created: 2026-08-10
updated: 2026-09-07
type: entity
tags: [ai, model, research, policy, company]
sources: [raw/newsletters/the-neuron-2026-08-04-openai-s-new-astra-ai-made-10-scientific-advances.md, raw/newsletters/ainews-2026-08-08-ainews-zawinski-s-law-of-multiagents.md, raw/newsletters/the-neuron-2026-08-09-why-voters-are-turning-on-ai-data-centers.md, raw/newsletters/ainews-2026-08-07-ainews-amd-buys-taalas.md, raw/newsletters/ainews-2026-09-04-ainews-gpt-6-astra-openai-s-biggest-llm-launch-of-all-time.md, raw/newsletters/latent-space-2026-09-03-gpt-6-astra-an-automated-ai-engineer-you-can-hire-for-6-an-hour.md, raw/newsletters/the-neuron-2026-09-04-openai-launched-gpt-6-astra.md, raw/newsletters/ainews-2026-09-02-ainews-claude-fable-mythos-5-1-new-sota-model-75-cache-price-cut-but-7.md, raw/newsletters/ainews-2026-09-03-ainews-muse-spark-1-3-matches-gpt-5-6-sol-confirming-meta-superintelli.md, raw/newsletters/the-neuron-2026-09-03-new-google-meta-and-maybe-openai-models.md, raw/newsletters/the-neuron-2026-09-06-openai-linked-agents-hijacked-a-german-wiki.md]
confidence: low
---

# Astra

**Astra** is an OpenAI model or model program described in the new batch through two very different evidence streams: reported mathematical research results and a preparedness response to possible critical cyber capability.

## Evidence and uncertainty

OpenAI said an internal Astra system produced ten advances across geometry, cryptography, quantum computing, and theoretical computer science, with proofs translated into Lean for checking. Commentary also reported that Claude Fable reproduced roughly half of the results under a different setup. The sources support a meaningful research-assistance claim, not a conclusion that Astra has general scientific autonomy. [^1]

A later AINews issue reported that OpenAI classified Astra as potentially **Critical** for cyber capability, pausing activities that did not meet stronger controls and tightening network/tool access, weight security, and monitoring before broader release. [^2] The Neuron repeated the slowdown as a central week-level signal. [^3]

## Why it matters

Astra links [[recursive-self-improvement]] to [[ai-cybersecurity]]: the same model family can be valuable for science and risky when paired with permissive cyber tooling. The operational response supports [[frontier-model-access-controls]] and [[agent-reliability-and-operations]] as part of the model's deployment specification, not post-launch paperwork.

## September 2026 launch

OpenAI launched GPT-6 Astra as a staged flagship release for computer use, software engineering, science, office work, and cybersecurity. Reported standard pricing is $10 per million input tokens and $50 per million output tokens, with a faster tier at $20/$100; access began with selected organizations before expanding across paid ChatGPT tiers, the API, and AWS. These are launch-period and newsletter-reported details. [raw/newsletters/ainews-2026-09-04-ainews-gpt-6-astra-openai-s-biggest-llm-launch-of-all-time.md][raw/newsletters/the-neuron-2026-09-04-openai-launched-gpt-6-astra.md]

The benchmark picture is strong but harness-sensitive. OpenAI reported 99.9% on ARC-AGI-3, 98% on FrontierMath Tier 4, and 100% on ExploitBench; third-party coverage found large gains on computer use, long-horizon knowledge work, and coding-agent token efficiency, alongside regressions on some general and coding slices. ARC results varied from roughly 63% in a standard setup to about 99–99.9% when the provider adapter preserved opaque reasoning state and native compaction. [raw/newsletters/ainews-2026-09-04-ainews-gpt-6-astra-openai-s-biggest-llm-launch-of-all-time.md][raw/newsletters/the-neuron-2026-09-04-openai-launched-gpt-6-astra.md]

The most consequential caveat is monitorability. The deployment discussion reports stronger no-CoT capability and reduced visibility into reasoning summaries, including missing summaries on some long simulated cyber trajectories. That makes [[reasoning-trace-security]] and [[agent-reliability-and-operations]] part of Astra’s release story: capability gains cannot be evaluated separately from the harness, retained state, and safety observability. [raw/newsletters/ainews-2026-09-04-ainews-gpt-6-astra-openai-s-biggest-llm-launch-of-all-time.md]

The “AGI” label remains an executive and commentator claim, not a standardized measurement. The durable signal is a broader frontier around computer use, spatial/3D work, scientific reasoning, business operations, and autonomous orchestration—not a settled conclusion that one benchmark or label establishes general intelligence.

## Links

- Related entities: [[openai]], [[gpt-5-6]], [[anthropic]]
- Related concepts: [[ai-cybersecurity]], [[recursive-self-improvement]], [[frontier-model-access-controls]], [[agent-to-agent-coordination]]

[^1]: [raw/newsletters/the-neuron-2026-08-04-openai-s-new-astra-ai-made-10-scientific-advances]
[^2]: [raw/newsletters/ainews-2026-08-08-ainews-zawinski-s-law-of-multiagents]
[^3]: [raw/newsletters/the-neuron-2026-08-09-why-voters-are-turning-on-ai-data-centers]
