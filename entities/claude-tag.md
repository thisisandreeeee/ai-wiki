---
title: Claude Tag
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [ai, tooling, llm, company]
sources: [raw/newsletters/ainews-2026-06-24-ainews-claude-tag-multiplayer-proactive-persistent-agents-in-slack.md, raw/newsletters/the-neuron-2026-06-24-ai-glasses-are-299-do-you-need-them.md, raw/newsletters/the-neuron-2026-06-25-chatgpt-s-secret-advantage.md]
confidence: high
---

# Claude Tag

**Claude Tag** is Anthropic's Slack-native agent integration that turns Claude into an @mentionable teammate in any Slack channel, with full conversation-thread context, connected app access (Gmail, Calendar, HubSpot, etc.), and shared team visibility. Launched June 2026 for Team and Enterprise plans.

## Core features

- **@Claude in any channel**: Mention Claude with a request; it reads the thread, pulls from connected apps, and responds inline.
- **Ambient Mode**: Claude watches channels it's in and proactively flags things (e.g., spotting a login error in support emails, alerting engineering) without being asked.
- **Agent identity model**: Claude gets its own credentials; actions are auditable under that identity; access can be revoked centrally.
- **Team shared context**: Every team member in the channel sees Claude's work and can pick up where the last person left off.

## Strategic significance

The launch represents Anthropic's bet on **multiplayer, persistent, proactive agents** embedded in existing team software (Slack) rather than standalone chat apps. [[anthropic|Anthropic]] reported 65% of its product team's code is now generated through their internal version of Claude Tag.

Andrej Karpathy argued the significance is underrated: it's "not just a feature" or Slack bot, but an org-level harness. Others described the experiential jump from Claude Code as a "pairing partner" to Tags as "managing a team."

## Concerns raised

- **Identity and permissions**: Per-agent credentialing drew both praise and concern. Some argued explicit per-agent permissioning doesn't scale and advocated capability-based security with fine-grained, task-scoped access.
- **Lock-in risk**: A shared agent that "remembers everything and bills by the thought" creates tacit-knowledge lock-in, prompt-injection risk, and budget opacity once deeply embedded in org workflows.
- **Attribution ambiguity**: Write actions and access control become harder to track outside clean Slack-like boundaries.

## Open/DIY response

Hugging Face described its internal Slack-based coding agent **Moon Bot**, emphasizing self-hosting, custom tools, auditable sessions, and zero lock-in. The pattern: teams want agent-native UX but many prefer owning the harness and memory layer.

## Links

- Related entities: [[anthropic]], [[openai]]
- Related concepts: [[meta-harnesses]], [[coding-agent-evaluation]], [[ai-control-roadmaps]]
- See also: [[frontier-model-access-controls]]
