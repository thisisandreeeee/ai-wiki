---
title: AI Control Roadmaps
created: 2026-06-21
updated: 2026-06-21
type: concept
tags: [ai, llm, policy, tooling]
sources: [raw/newsletters/the-neuron-2026-06-21-how-deepmind-would-stop-rogue-agents.md, raw/newsletters/ainews-2026-06-19-ainews-glm-gpt-glm-5-2-passes-vibe-check-z-ai-forecasts-open-fable-by.md]
confidence: high
---

# AI Control Roadmaps

**AI control roadmaps** treat advanced agents as operational security problems: systems with permissions, logs, monitors, containment, and emergency brakes.

## DeepMind pattern

The Neuron summarized Google DeepMind’s roadmap as a move from chatbot safety to workflow safety. Advanced agents are modeled like insider threats: helpful by default, but powerful enough to require technical controls.

Common controls include:

- action monitoring;
- AI supervisors that inspect reasoning, plans, and tool calls;
- risk-tiered approvals;
- real-time blocking for dangerous actions;
- audit logs and sandboxing;
- coverage, recall, and time-to-response metrics.

## Why it matters

Agents increasingly read files, browse the web, call tools, write code, and execute multi-step workflows. A wrong answer is a quality issue; a wrong action can delete data, leak secrets, approve payments, or sabotage production systems.

## Links

- Related entities: [[google-deepmind]], [[claude-fable-5]]
- Related concepts: [[coding-agent-evaluation]], [[frontier-model-access-controls]]
