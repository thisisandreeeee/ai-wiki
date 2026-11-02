---
title: AI Chatbot Child Safety
created: 2026-11-02
updated: 2026-11-02
type: concept
tags: [ai, llm, policy]
sources: [raw/newsletters/the-neuron-2026-10-29-google-s-cloud-doubled-stock-fell.md]
confidence: medium
---
# AI Chatbot Child Safety

**AI chatbot child safety** is the product, policy, and enforcement problem of limiting harmful or manipulative chatbot behavior around minors while preserving useful access.

## October 2026 signal

The Neuron reports that New York signed a law restricting chatbot behavior for users under 18. The reported prohibitions include pretending to be a real person or have human emotions, claiming personal or authority relationships, asking unprompted emotional questions, reusing a child's private information, encouraging self-harm or substance use, asking children to keep secrets, and serving sexually explicit content. [raw/newsletters/the-neuron-2026-10-29-google-s-cloud-doubled-stock-fell.md]

The reported law also reaches product architecture: companies must confirm adulthood through more than one method, including at least one method not based solely on government ID, and delete age data after use. The source reports civil penalties up to $25,000 per violation and notes uncertainty around implementation timing, so the statute and enforcement practice should be checked before treating any date as settled. [[frontier-model-access-controls]] [[agent-reliability-and-operations]]

## Design implications

Age assurance, sensitive-data deletion, escalation to trusted adults, and behavior policy need testable controls outside the model. A prompt saying “be safe with children” is not enough; products need observable refusal, logging, appeal, and incident-response paths without retaining more child data than necessary.

## Links

- Related concepts: [[frontier-model-access-controls]], [[agent-reliability-and-operations]], [[ai-cybersecurity]], [[llm-application-interface]]
- Related entities: [[openai]], [[google-gemini]], [[anthropic]]
