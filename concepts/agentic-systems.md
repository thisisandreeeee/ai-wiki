---
title: Agentic Systems
created: 2026-07-18
updated: 2026-08-10
type: concept
tags: [ai, llm, tooling, data-engineering]
sources: [raw/learning-resources/technical-interview-learning-resources.md, raw/newsletters/ainews-2026-08-08-ainews-zawinski-s-law-of-multiagents.md, raw/newsletters/ainews-2026-08-06-ainews-jeff-sanjay-oriol-and-quoc-depart-deepmind-demis-to-chair-koray.md, raw/newsletters/latent-space-2026-08-04-unpacking-chatgpt-work-the-agent-for-a-billion-users.md]
confidence: high
---

# Agentic Systems

An **AI agent** is an LLM inside a controlled loop with tools and state. It can choose its next action from intermediate observations instead of following a completely prewritten path. That autonomy is useful only when the path is genuinely uncertain and can be bounded, evaluated, and recovered safely.

```text
observe task and durable state
→ propose next action
→ authorize and execute through tools
→ record observation and external effects
→ verify progress
→ continue, replan, escalate, or stop
```

## Workflow versus agent

A workflow has known control flow. An agent chooses control flow under constraints. Tool calling by itself does not make a system agentic; a fixed sequence of tool calls remains a workflow.

Use a workflow when inputs, path, and success criteria are predictable or risk is high. Use an agent when intermediate evidence changes the next step and a deterministic path would be brittle or impractically large. Start with the least autonomous design that works; many production systems use a deterministic outer workflow around a narrow agent loop.

## Runtime, harness, control plane

These terms describe different scopes:

- **Runtime** executes one run: model calls, tools, retries, checkpoints, waits, and state transitions.
- **Harness** is the disciplined operating layer around the model: prompt/context construction, schemas, tool registry, budgets, stopping rules, and guardrails.
- **Control plane** manages runs across time: versions, deployments, identities, policies, schedules, credentials, rollout/rollback, and observability.

A useful hierarchy is `model ⊂ harness ⊂ runtime`; the control plane governs configuration and lifecycle across runtimes. Exact product boundaries vary, so treat these as responsibilities rather than universal taxonomy.

## State makes action recoverable

Conversation history is not sufficient agent state. Persist task goal, plan, observations, artifacts, approvals, budgets, retries, tool arguments/results, and the status of external effects.

For a consequential write, model the uncertainty explicitly:

```text
not attempted → intention persisted → attempting
                              ├→ succeeded
                              ├→ failed
                              └→ outcome unknown
```

A timeout after an API call does not prove failure; retrying blindly can duplicate an email, ticket, payment, or delete. Use an operation ID/idempotency key, store intent before the call, inspect the external state, and reconcile before retrying. [[agent-reliability-and-operations]] expands this into production controls.

## Orchestration patterns

- **Prompt chaining** passes a fixed-stage output onward.
- **Routing** classifies a request to a model, prompt, tool, or workflow.
- **Parallelization** accelerates independent subtasks or generates candidates for selection.
- **Orchestrator-worker** uses a coordinator to decompose work whose subproblems are not known in advance.
- **Evaluator-optimizer** iterates a draft against explicit criteria.

Multi-agent designs are justified by real independence, separate permissions, or distinct specialized context—not by the assumption that more agents automatically create better reasoning.

## August 2026 update: from workers to agent graphs

The batch shows multi-agent systems moving from coordinator-worker demos toward persistent workers and session-to-session communication. Meta's Muse Code, Prime Agent, Claude Code messaging, and ChatGPT Work all emphasize durable context, specialized workers, verification, or scheduled execution. The capability is useful when subtasks are independent or permissions/context differ; otherwise it adds coordination overhead and more failure surface.

Model the graph explicitly: identities, channels, shared state, fan-out limits, budgets, approval edges, and termination conditions. [[agent-to-agent-coordination]] captures the security implication, while [[coding-agent-evaluation]] covers why the graph—not only the model—must be evaluated.

## Verification is layered

A successful tool call does not prove a good action. Verify:

1. **structural validity** — schema and arguments;
2. **execution validity** — did it run;
3. **semantic validity** — was the tool/result interpreted correctly;
4. **goal relevance** — did it reduce uncertainty or meet a requirement;
5. **policy validity** — was it authorized and safe.

Evaluate both the trajectory and outcome. Strong evidence comes from external-world confirmation, deterministic assertions, trusted data, or independent evaluators—not merely the agent declaring success.

## Links

- [[llm-application-interface]] defines message, schema, and tool-call contracts.
- [[agent-reliability-and-operations]] covers authorization, idempotency, incidents, and evaluations.
- [[retrieval-augmented-generation]] provides evidence the agent may retrieve.
- [[llm-training-lifecycle]] covers trajectory rewards and post-training for tool use.
