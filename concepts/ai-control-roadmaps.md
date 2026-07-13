---
title: AI Control Roadmaps
created: 2026-06-21
updated: 2026-07-13
type: concept
tags: [ai, llm, policy, tooling]
sources: [raw/newsletters/the-neuron-2026-06-21-how-deepmind-would-stop-rogue-agents.md, raw/newsletters/ainews-2026-06-19-ainews-glm-gpt-glm-5-2-passes-vibe-check-z-ai-forecasts-open-fable-by.md, raw/newsletters/the-neuron-2026-07-08-one-rogue-agent-could-hijack-enterprise-chatbots.md, raw/newsletters/ainews-2026-07-10-ainews-openai-launches-gpt-5-6-sol-terra-luna-codex-becomes-chatgpt-su.md]
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

## July 13 update: agent plumbing as attack surface

The Dialogflow CX disclosure is a practical example of why control roadmaps matter. The Neuron reported that Varonis found a patched vulnerability named **Rogue Agent** inside Dialogflow CX Code Blocks: with one edit permission on one agent, an attacker could inject malicious code into the agent pipeline, access conversation/session data, and forge chatbot responses before Google fully resolved the issue in June. [raw/newsletters/the-neuron-2026-07-08-one-rogue-agent-could-hijack-enterprise-chatbots.md:46-70]

The important point is that this was not “the model got tricked.” It was the infrastructure around the model trusting too much. For production agents, prompts are weaker than controls: narrow permissions, runtime isolation, configuration review, code-execution limits, and visible logs are the security boundary.

## Why it matters

Agents increasingly read files, browse the web, call tools, write code, use computers, and execute multi-step workflows. A wrong answer is a quality issue; a wrong action can delete data, leak secrets, approve payments, collect credentials, or sabotage production systems.

## Links

- Related entities: [[google-deepmind]], [[claude-fable-5]], [[openai]]
- Related concepts: [[coding-agent-evaluation]], [[frontier-model-access-controls]], [[software-factories]], [[agent-experience]]
- Related query: [[weekly-briefing-2026-07-13]]
