---
title: Claude Duet
created: 2026-10-26
updated: 2026-10-26
type: entity
tags: [ai, llm, tooling, company, policy]
sources: [raw/newsletters/the-neuron-2026-10-22-claude-duet-just-launched-what-s-the-catch.md, raw/newsletters/the-neuron-2026-10-25-walmart-wants-ai-shoppers-on-an-allowance.md]
confidence: medium
---

# Claude Duet

**Claude Duet** is Anthropic's research-preview proactive agent for U.S. Pro and Max subscribers. It runs background checks on a cloud computer, sends a morning brief, watches connected applications, and interrupts the user when it believes attention is needed.

## Operating model

Duet runs on a virtual machine with a browser rather than depending on the user's laptop or phone remaining online. The source says it carries over Claude memory, skills, and connected apps, with more than 6,000 connectors advertised. Background work uses the subscriber's existing plan limits. [raw/newsletters/the-neuron-2026-10-22-claude-duet-just-launched-what-s-the-catch.md]

The product's key boundary is approval for consequential actions. It is reported to ask before sending messages, making payments, signing documents, or deleting data; securities trading and moving money between accounts are prohibited. Managed-agent credentials are designed to keep passwords and tokens away from the model, and a classifier blocks or requires explicit confirmation for sensitive information.

## Open questions

The safety design is promising but incomplete. Duet can misread a thread, misjudge urgency, and spend usage quota while working in the background. It also reportedly cannot yet show the user its browser, which makes inspectability and user trust important product questions. [[agent-experience]] [[agent-reliability-and-operations]]

The shopping coverage places Duet in a wider dispute over whether external agents should be allowed to act on retailer sites. Walmart's planned spending limits and approval controls are a more constrained pattern than unrestricted card entry, while Amazon is favoring its own assistant. [raw/newsletters/the-neuron-2026-10-25-walmart-wants-ai-shoppers-on-an-allowance.md]

## Links

- Related entity: [[anthropic]]
- Related concepts: [[agent-reliability-and-operations]], [[agent-experience]], [[browser-agents]]
- Related query: [[weekly-briefing-2026-10-26]]
