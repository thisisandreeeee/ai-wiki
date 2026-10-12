---
title: Stacklok
created: 2026-10-12
updated: 2026-10-12
type: entity
tags: [ai, company, tooling, data-engineering, policy]
sources: [raw/newsletters/latent-space-2026-10-07-can-a-cloud-native-harness-make-agents-reliable-beyond-the-desktop.md]
confidence: medium
---
# Stacklok

**Stacklok** is a cloud-native agent infrastructure company founded by Kubernetes creators Craig McLuckie and Joe Beda. Its reported products separate agent orchestration, execution, session state, memory, identity, and MCP governance.

## Mecatl and ToolHive

Mecatl is an open-source cloud-native harness designed to separate the agent loop from model providers, clients, state stores, and sensitive execution such as shell and tool calls. The goal is to make sessions pauseable, recoverable, centrally governed, and operable across enterprise infrastructure rather than treating a desktop process as the whole runtime.

ToolHive extends the same approach to MCP servers, with Kubernetes-based management, registries, operators, and input/output authorization. Stacklok describes its commercial product as an enterprise control plane for identity, authorization, policy, auditing, budgets, and multi-cluster or multi-cloud operation. [[agent-experience]] [[agent-reliability-and-operations]]

## Significance

The architecture is a concrete expression of [[agentic-systems]]: durable agent work needs an explicit control plane and separate execution environments. The open question is whether cloud-native decomposition improves reliability without making identity transfer, state ownership, and permission boundaries harder to audit.
