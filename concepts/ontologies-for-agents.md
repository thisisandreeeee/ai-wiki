---
title: Ontologies for Agents
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [ai, llm, tooling]
sources: [raw/newsletters/latent-space-2026-07-30-ontologies-are-so-back-why-ai-agents-are-reviving-the-semantic-web.md]
confidence: medium
---

# Ontologies for Agents

**Ontologies for agents** are structured descriptions of domain entities, properties, relationships, and rules used to constrain or validate probabilistic LLM behavior.

## July 2026 signal

Latent.Space highlighted a revival of Semantic Web and ontology ideas for agentic systems. Frank Coyle's AIEWF talk argued that LLM agents need "logical guardrails"; Neo4j described business ontologies, technical metadata ontologies, and execution traces as a shared substrate for agents; and older standards such as Schema.org, RDF/RDFS, OWL, FOAF, and Dublin Core reappeared as practical tools rather than historical curiosities. [raw/newsletters/latent-space-2026-07-30-ontologies-are-so-back-why-ai-agents-are-reviving-the-semantic-web.md:14-24]

The core idea is neurosymbolic: LLMs provide flexible language and probabilistic reasoning, while ontologies provide machine-checkable structure. In agent loops, an ontology or reasoner can validate whether an action, entity relationship, or workflow step is allowed before the system acts.

## Why it matters

This is a direct response to the brittleness of [[software-factories]] and other long-running [[agentic-systems]]. When loops branch, call tools, mutate files, or touch enterprise data, natural-language instructions are not enough. A bounded rule layer can help agents know what exists, what relationships are valid, and which actions violate policy.

The hard part is maintenance. The original Semantic Web struggled because ontologies drifted and were expensive to keep current. The new bet is that agents may help maintain the ontology during normal operation: recording edge cases, updating definitions, and feeding runtime traces back into the shared semantic layer.

## Practical pattern

- model extracts or proposes entities, relationships, and actions;
- ontology/reasoner checks them against domain rules;
- tool gateway enforces schemas and permissions;
- runtime traces update the ontology or reveal missing concepts;
- human reviewers handle contested definitions and high-risk changes.

## Links

- Related concepts: [[agent-reliability-and-operations]], [[agentic-systems]], [[software-factories]], [[retrieval-augmented-generation]]
- Related governance: [[ai-control-roadmaps]], [[ai-cybersecurity]]
