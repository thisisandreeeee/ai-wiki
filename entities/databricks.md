---
title: Databricks
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [ai, company, data-engineering, tooling, llm]
sources: [raw/newsletters/latent-space-2026-06-24-why-the-frontier-ecosystem-must-be-open-matei-zaharia-and-reynold-xin.md, raw/newsletters/ainews-2026-06-25-ainews-it-s-meta-harness-summer.md]
confidence: high
---

# Databricks

**Databricks** (founded by Matei Zaharia, Reynold Xin, and team) is a $175B data-and-AI platform company evolving from the lakehouse into what it calls the operating system for enterprise agents. The June 2026 Data + AI Summit showcased its biggest strategic pivot yet: Omnigent, LTAP, and Lakebase.

## Omnigent: the open-source meta-harness

Omnigent is Databricks' open-source **[[meta-harnesses|meta-harness]]** — a pluggable architecture for combining, controlling, and sharing agents across Claude Code, Codex, Cursor, Pi, custom agents, and internal tools. It abstracts a common API (agent sessions with file/message streams, tool calls, cancellation) above every harness.

Key design decisions:
- **Open-source** to build network effects — early PRs included Kubernetes support, cloud sandboxes, and additional harness integrations.
- **Persistent cloud sandboxes**: agents run in the cloud, not on laptops, enabling collaboration and long-running sessions.
- **Contextual security policies**: stateful rules that track session state (e.g., "if it read confidential docs, don't allow npm publish") rather than binary allow/deny.
- **Spend controls**: cap agent spending per session, with permission escalation prompts.

Zaharia frames it as solving the same problems across coding agents and custom enterprise agents: portability, collaboration, session history, security, and spend controls.

## LTAP (Lake Transactional/Analytical Processing)

Reynold Xin's "dream engine": a database architecture that unifies transactional (OLTP) and analytical (OLAP) workloads on a single storage layer using open formats. The pitch is "HTAP done right" — avoiding CDC pipeline fragility while keeping the open-format foundation that made the lakehouse successful.

## Scale and internal usage

- 50–60 million VMs/day across all three clouds
- Exabytes of data processed before breakfast in many time zones
- Internal "Isaac" wrapper on Claude Code and Codex used across engineering
- Unlimited internal agent usage with trace analysis for optimization

## Strategic thesis

If frontier model performance commoditizes, the durable advantage becomes company-specific context: proprietary data, governed access, operational state, and feedback loops. Databricks positions at that intersection — "get the data there, slap some agent on top" may rewrite traditional software.

## Links

- Related concepts: [[meta-harnesses]], [[ai-infrastructure-economics]], [[coding-agent-evaluation]]
- Related entities: [[openai]], [[anthropic]]
- See also: [[model-labs-vs-agent-labs]], [[reliable-data-pipelines]]
