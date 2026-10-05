---
title: OpenAI Dots
created: 2026-10-05
updated: 2026-10-05
type: entity
tags: [ai, llm, tooling, company]
sources: [raw/newsletters/ainews-2026-09-30-ainews-openai-devday-2026-dots-6-1-sol-ultrafast-decisions-api-agents.md, raw/newsletters/the-neuron-2026-09-30-dots-is-here-openai-s-bigger-bet.md, raw/newsletters/latent-space-2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-openai-shipped-its-jev-co.md]
confidence: medium
---

# OpenAI Dots

**Dots** is OpenAI's always-on agent product: an agent with its own cloud computer, browser, persistent projects, and access to thousands of app integrations. The October 2026 launch is best understood as a bet that ChatGPT becomes an action layer rather than only a conversational interface.

## Product shape

- Each Dot runs on a cloud computer and can keep working after the user closes their laptop.
- The product connects to 4,000+ apps plus Slack and Teams, with user-defined boundaries and approval gates.
- OpenAI positioned Dots alongside hosted computer use, Plugin Extensions, Sign in with ChatGPT, a Marketplace, and Codex cloud environments.
- Private Safety Processing is described as a way to run automated safety checks without creating a new path for OpenAI personnel to read protected customer content.

The product thesis is persistent delegation: the user states an outcome, while the agent chooses tools, models, and intermediate steps. That makes identity, permissions, context, and budget central product primitives. [^1]

## Strategic significance

Dots competes with [[grok-bot]], Meta's Muse direction, and other persistent-agent products, but OpenAI's wider platform bundle matters as much as the agent itself. A ChatGPT subscription, app marketplace, identity layer, and AI budget could make OpenAI the default aggregator for software actions. [^2]

This is also a test of [[agentic-knowledge-work]] and [[agent-reliability-and-operations]]. The useful adoption question is not whether Dots can perform a demo, but whether people will trust it with invoicing, scheduling, research, purchases, software maintenance, and coordination without constant supervision.

## Open questions

- Can approval gates remain understandable as tasks span many tools and ongoing projects?
- Does the cloud-computer abstraction expose enough state, cost, and permission information for meaningful oversight?
- Will Dots become a primary agent that delegates to specialist agents, or mainly a branded interface around existing OpenAI APIs?
- How much of the reported value comes from the model versus the harness, integrations, and persistent state?

## Links

- Related entities: [[openai]], [[grok-bot]]
- Related concepts: [[agentic-systems]], [[agent-reliability-and-operations]], [[model-routing]], [[agent-experience]]

[^1]: [raw/newsletters/ainews-2026-09-30-ainews-openai-devday-2026-dots-6-1-sol-ultrafast-decisions-api-agents.md]
[^2]: [raw/newsletters/the-neuron-2026-09-30-dots-is-here-openai-s-bigger-bet.md]
