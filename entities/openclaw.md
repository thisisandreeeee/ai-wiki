---
title: OpenClaw
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [ai, llm, tooling, company]
sources: [raw/newsletters/the-neuron-2026-08-31-openclaw-2-0-rebuilt-the-personal-ai-agent.md, raw/newsletters/latent-space-2026-09-05-openclaw-power-macbook-simplicity-five-days-with-grok-bot.md]
confidence: medium
---

# OpenClaw

**OpenClaw** is a user-owned agent platform centered on a Gateway, persistent computer, plugins, skills, runtimes, and automations. The September 2026 sources contrast it with managed agent-computer products rather than treating it as only a chatbot wrapper.

## Product direction

OpenClaw 2.0 reportedly narrows setup friction by reusing an existing Claude Code or Codex login, adding a browser app for setup and plugin management, and shipping a native Codex runtime plus routes for other coding-agent harnesses. Its defining tradeoff remains ownership: users choose how and where the Gateway runs and retain more visibility into the host and machinery. [raw/newsletters/the-neuron-2026-08-31-openclaw-2-0-rebuilt-the-personal-ai-agent.md][raw/newsletters/latent-space-2026-09-05-openclaw-power-macbook-simplicity-five-days-with-grok-bot.md]

## Comparison with managed agents

[[grok-bot]] packages the computer, connectors, and persistence as a managed service; OpenClaw exposes more of the configuration and operational burden. That gives OpenClaw more optionality and user control, but also makes uptime, updates, remote access, recovery, credentials, and security the operator’s responsibility. [[agent-experience]] is therefore a control-versus-cognitive-load problem, not a simple usability ranking.

## Links

- Related entities: [[grok-bot]], [[anthropic]], [[openai]]
- Related concepts: [[agent-experience]], [[agent-memory]], [[agent-reliability-and-operations]], [[agent-to-agent-coordination]]
