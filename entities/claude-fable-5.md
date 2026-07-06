---
title: Claude Fable 5
created: 2026-06-21
updated: 2026-07-06
type: entity
tags: [ai, llm, model, policy]
sources: [raw/newsletters/the-neuron-2026-06-10-claude-fable-most-controversial-ai-yet.md, raw/newsletters/the-neuron-2026-06-14-us-gov-shuts-down-claude-fable.md, raw/newsletters/ainews-2026-06-11-ainews-open-models-model-labs-vs-agent-labs-and-what-s-untrainable-sar.md, raw/newsletters/ainews-2026-06-13-ainews-fable-and-mythos-officially-too-dangerous-to-release.md, raw/newsletters/the-neuron-2026-06-19-your-doctor-may-ask-chatgpt-next.md, raw/newsletters/ainews-2026-07-01-ainews-sonnet-5-today-and-fable-5-tomorrow.md, raw/newsletters/the-neuron-2026-07-01-fable-5-is-back-baby.md, raw/newsletters/the-neuron-2026-07-02-fable-5-first-reviews.md, raw/newsletters/the-neuron-2026-07-05-build-something-real-with-fable.md]
confidence: high
---

# Claude Fable 5

**Claude Fable 5** is the public, safeguarded variant of Anthropic's Mythos-class model in the June–July 2026 corpus. It is the clearest example of frontier AI as a gated capability system rather than a simple model release.

## What happened

- Anthropic launched Fable 5 as a generally available version of a Mythos-class system, while **Claude Mythos 5** was described as a less-restricted variant for vetted cyber and biology partners.
- The June corpus reported pricing at **$10 / million input tokens** and **$50 / million output tokens**, with temporary inclusion in paid Claude subscriptions.
- The launch mixed strong capability reports with confusion around fallback behavior, biology/cyber restrictions, and invisible interventions for frontier AI research.
- A U.S. export-control directive then forced Anthropic to disable Fable 5 and Mythos 5 for customers because it could not enforce foreign-national access restrictions in real time.

## July redeployment

By July 1, the corpus reported that export controls had been lifted enough for Fable 5 to return globally while Mythos 5 access expanded through approved partners. The relaunch came alongside Sonnet 5 becoming Anthropic’s default mid-tier model for Claude, Claude Code, API, and ecosystem partners.

The first-review coverage framed Fable 5 as usable but still operationally unstable: builders were stress-testing it, Anthropic had added safeguards after the shutdown, and capacity/plan availability remained messy. The Neuron’s July 5 advice was to treat Fable like a scarce “weekend contractor”: plan cheaply, give it a concrete goal and finish line, then spend the expensive model run on work that genuinely needs it.

## Why it mattered

Fable 5 made three themes concrete:

1. **Capability**: reports emphasized long-horizon coding, agent loops, research synthesis, game generation, CAD-like work, and multi-hour tasks.
2. **Trust**: AINews captured backlash over alleged silent degradation on AI R&D tasks; users argued explicit refusals are safer than hidden steering.
3. **Policy risk**: the shutdown and redeployment showed that frontier-model availability can depend on government directives, export controls, nationality gates, provider compliance systems, and capacity allocation.

## Operating lesson

Treat Fable-class models as unstable strategic dependencies. Teams should keep evals, fallbacks, [[local-llms]], and procurement risk reviews in place before building critical workflows around any one frontier API. Where Fable is available, it fits best into bounded [[software-factories]] with explicit review, cost limits, and rollback plans.

## Links

- Related concepts: [[frontier-model-access-controls]], [[coding-agent-evaluation]], [[ai-control-roadmaps]]
- Related entities: [[anthropic]], [[glm-5-2]], [[openai]]
- See also: [[closed-vs-open-frontier-models]], [[weekly-briefing-2026-07-06]]
