---
title: Claude Opus 5
created: 2026-07-30
updated: 2026-07-30
type: entity
tags: [ai, llm, model]
sources: [raw/newsletters/ainews-2026-07-25-ainews-claude-opus-5-fable-level-performance-at-opus-price-half-fable.md, raw/newsletters/the-neuron-2026-07-26-nvidia-microsoft-all-in-on-open-source.md]
confidence: medium
---

# Claude Opus 5

**Claude Opus 5** is Anthropic's July 2026 Opus-class model release, framed in the corpus as near-[[claude-fable-5|Fable]] performance at a lower price point and as another stress test for frontier model evaluation.

## Launch read

AINews reports that Anthropic's Opus 5 launch produced a mix of benchmark scrutiny, strong coding-agent anecdotes, and debate over whether aggregate evals captured real-world improvements. Epoch placed Opus 5 at ECI 159, slightly below Fable 5's 161, while matching Fable 5 on SWE-ECI at 161. [raw/newsletters/ainews-2026-07-25-ainews-claude-opus-5-fable-level-performance-at-opus-price-half-fable.md:19-35]

The reception centered less on a clean leaderboard win than on practical agentic competence: coding, browser control, best-of-n sampling, and tool-use workflows. The main caution was evaluation instability, including reports that higher effort was not uniformly better on FrontierCode. [raw/newsletters/ainews-2026-07-25-ainews-claude-opus-5-fable-level-performance-at-opus-price-half-fable.md:37-45]

## Why it matters

Opus 5 makes [[coding-agent-evaluation]] harder. If users experience a model as materially stronger while an aggregate score moves only slightly, the wiki should treat one-number model rankings as weak evidence for operational fit. The useful comparison is task slice, effort setting, latency/cost, and harness behavior.

For [[anthropic]], Opus 5 broadens the premium model lineup around [[claude-fable-5]] rather than replacing it. Fable remains the policy- and capability-flashpoint model; Opus 5 looks like the more accessible frontier workhorse whose value depends on deployment defaults and agent workflows.

## Links

- Related entities: [[anthropic]], [[claude-fable-5]], [[gpt-5-6]], [[kimi-k3]]
- Related concepts: [[coding-agent-evaluation]], [[software-factories]], [[frontier-model-access-controls]]
- Related comparison: [[closed-vs-open-frontier-models]]
