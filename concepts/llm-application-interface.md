---
title: LLM Application Interface
created: 2026-07-18
updated: 2026-07-18
type: concept
tags: [ai, llm, tooling, data-engineering]
sources: [raw/learning-resources/technical-interview-learning-resources.md]
confidence: high
---

# LLM Application Interface

An LLM application is not “a model with memory.” It is software that constructs context, requests a probabilistic completion, validates the result, and decides whether to take another action. Important application state belongs in explicit data structures, not only in prose history.

## Messages and sampling

A typical request contains:

- **system/developer messages**: application-level behaviour and constraints;
- **user messages**: the task and supplied information;
- **assistant messages**: earlier model outputs, including tool requests;
- **tool messages**: externally produced observations returned to the model.

A model turns logits $z_i$ into a distribution with temperature $T$:

$$p_i=\frac{\exp(z_i/T)}{\sum_j\exp(z_j/T)}.$$

Lower temperature sharpens the distribution; higher temperature flattens it. Temperature affects sampling variability, not the model's stored knowledge or underlying capability. For routing, extraction, tool arguments, and structured data, prefer the lowest randomness compatible with the task and validate the result.

## Structured output is a contract

Use a schema when model output drives software: classification, extraction, routing, workflow state, or tool arguments. The model may produce a schema-shaped candidate, but the application must parse and validate it, reject or repair invalid data, and enforce authorization separately.

```text
model proposes structured data
→ application validates schema and business rules
→ application authorizes and executes allowed work
→ application records an observation
```

This boundary is central to [[agentic-systems]] and [[agent-reliability-and-operations]]. Model output is untrusted input even when it looks like JSON.

## Tool calling

Tool calling is an interaction pattern, not direct model execution. The application advertises a registry of tool names, descriptions, and argument schemas. The model returns a proposed call; trusted code resolves it, validates arguments and permissions, executes it, then appends the result as a tool message.

```text
model chooses a candidate action
→ tool gateway authenticates, authorizes, validates, and executes
→ result or error becomes new context
→ model continues or finishes
```

A model should never receive unconstrained shell, SQL, payment, or production-write authority merely because its prompt says to be careful. Prefer narrow verbs such as `request_refund(order_id, reason)` over generic “execute anything” interfaces.

## MCP: a portability protocol

The **Model Context Protocol** standardizes how an AI host discovers and communicates with external capability servers. Its three familiar primitives are:

- **tools** for callable operations;
- **resources** for retrievable contextual data;
- **prompts** for reusable templates or workflows.

MCP is not a replacement for APIs, an agent runtime, or an authorization system. Tool calling describes a model/application loop; MCP standardizes the integration surface. An MCP server and its descriptions still cross a trust boundary.

## Workflow patterns and the autonomy ladder

A **workflow** has developer-defined control flow. An **agent** lets a model select the next step from intermediate observations. The choice is not a status hierarchy:

| Pattern | Best use |
| --- | --- |
| prompt chain | fixed transformation stages |
| routing | request categories need different models, prompts, or tools |
| parallelization | independent work or candidate generation |
| evaluator-optimizer | outputs can be iteratively improved against clear criteria |
| agent loop | the next action depends on uncertain intermediate results |

Use the least autonomy that meets the requirement. A deterministic outer workflow with a small bounded agentic loop is often more reliable than a fully open-ended agent. See [[agentic-systems]] for the lifecycle and [[retrieval-augmented-generation]] for a common context-providing workflow.

## Context and memory

Conversation history is one source of context; it is not durable state. Manage recent turns, summaries, retrieved memory, and structured records separately. Important facts such as task status, permissions, completed writes, and budgets must survive model changes, context pruning, and crashes.

## Links

- [[retrieval-augmented-generation]] provides external evidence to the request.
- [[agentic-systems]] turns tool calling into a controlled decision loop.
- [[agent-reliability-and-operations]] supplies the validation, audit, and approval controls.
- [[llm-training-lifecycle]] explains how tool-following behaviour can be trained.
