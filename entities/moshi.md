---
title: Moshi
created: 2026-10-26
updated: 2026-10-26
type: entity
tags: [ai, data-science, llm, tooling, company]
sources: [raw/newsletters/latent-space-2026-10-22-the-recommendation-engine-for-commodity-traders-anekha-sokhal-moshi.md]
confidence: medium
---

# Moshi

**Moshi** is Anekha Sokhal's recommendation engine for commodity, energy, and macro traders. It is designed to connect a trader's portfolio to the market information, private documents, and second-order signals that matter for current decisions.

## Product model

The interview describes Moshi as combining structured time series, technical indicators, market fundamentals, news, social and audio data, and user-specific sources such as analyst subscriptions and internal records. The system cleans and transforms the data, applies statistics and machine learning, tags it with an ontology, and stores relationships in an n-dimensional graph. It then pushes portfolio-relevant recommendations rather than presenting only a passive dashboard. [raw/newsletters/latent-space-2026-10-22-the-recommendation-engine-for-commodity-traders-anekha-sokhal-moshi.md]

A practical trust pattern is to identify trusted sources, surface divergent reports as information rather than silently resolving them, and attach confidence to signals. Moshi also uses document extraction for private PDFs and favors keeping customer data away from third-party processing when the team can build the relevant model itself.

## Why it matters

Moshi illustrates a domain-specific agent product whose defensibility is in workflow fit, data integration, provenance, and interface—not necessarily a proprietary foundation model. The “recommendation engine” framing also connects to [[ai-in-finance]] and [[semantic-layer-for-ai]]: useful AI must map heterogeneous evidence to the user's book and decision context. [[agentic-knowledge-work]] captures the broader shift from answering questions to pushing relevant work.

## Links

- Related concepts: [[ai-in-finance]], [[semantic-layer-for-ai]], [[agentic-knowledge-work]], [[model-routing]]
- Related entities: [[modal]], [[openai]]
- Related query: [[weekly-briefing-2026-10-26]]
