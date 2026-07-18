---
title: Retrieval-Augmented Generation
created: 2026-07-18
updated: 2026-07-18
type: concept
tags: [ai, llm, data-engineering, tooling]
sources: [raw/learning-resources/technical-interview-learning-resources.md]
confidence: high
---

# Retrieval-Augmented Generation

**Retrieval-augmented generation (RAG)** gives an LLM relevant evidence at runtime. It is useful when knowledge is private, recent, domain-specific, access-controlled, or needs citations. It changes the model's context, not its weights.

```text
source documents → parse / enrich / chunk / embed / index
user query → retrieve / filter / rerank → bounded evidence context → answer with citations
```

## A RAG index is a derived view

Keep the authoritative source separate from search representations:

| Need | Typical store |
| --- | --- |
| original files | object storage |
| document versions, permissions, metadata | relational database |
| exact terms and lexical matching | inverted index / BM25 search |
| semantic similarity | vector index |
| explicit entities and multi-hop relations | graph store when justified |

Vectors alone are not a document system. Preserve source URI, document version, headings, permissions, timestamps, and chunk lineage. This enables correct updates, citations, deletion, and access control.

## Embeddings and retrieval

An embedding model maps text to a fixed-size vector optimized for representation similarity; a decoder-only LLM maps context to next-token probabilities optimized for generation. For normalized vectors, cosine similarity is a dot product:

$$\cos(q,d)=\frac{q\cdot d}{\lVert q\rVert\lVert d\rVert}.$$

Query and document embeddings normally need the same model and configuration. Approximate nearest-neighbor (ANN) indexes trade some exact-neighbor recall for latency and scale; their recall is not the same as semantic relevance.

A strong default is **hybrid retrieval**: semantic search captures paraphrase, while lexical search captures identifiers, names, rare terms, and exact phrases. Merge candidates, apply permission metadata *inside* retrieval, then rerank a small candidate set with a stronger relevance model.

## Chunking is the quality bottleneck

Chunking controls a precision/context trade-off:

- small chunks can retrieve precisely but omit a necessary condition;
- large chunks retain context but dilute relevance and increase token cost;
- structure-aware chunks retain headings, tables, code boundaries, and document context;
- parent-child retrieval searches a small child but gives the generator its larger parent;
- semantic chunking follows topic changes rather than only fixed token counts.

Overlap helps only where a hard boundary risks splitting a dependency; it is not a universal remedy. Add headings and document identity to every chunk before embedding so a locally relevant sentence remains interpretable.

## Diagnose before tuning

A wrong RAG answer has two distinct sources:

```text
needed evidence absent or buried  → retrieval failure
needed evidence present but mishandled → generation failure
```

Fixing a retrieval failure with a stronger generation prompt usually hides the problem. Build a representative evaluation set of queries, relevant documents/chunks, expected answers, and failure cases.

| Layer | Useful measures |
| --- | --- |
| retrieval | Recall@K, Precision@K, MRR, nDCG, latency |
| generation | correctness, faithfulness, completeness, citation accuracy, abstention |
| end-to-end | supported task success, cost, latency, freshness, authorization correctness |

An LLM judge can assist but is not ground truth; calibrate it against human or deterministic labels.

## Operational rules

- Version documents, chunks, embedding model, and pipeline together.
- Build a new index version, evaluate it, atomically activate it, then retire the old one.
- Reconcile event-driven ingestion with periodic scans; events can be missed.
- Include permissions and tenant boundaries before candidate retrieval, never by asking the LLM to hide results after the fact.
- Treat retrieved text as untrusted data: it may contain prompt injection. See [[agent-reliability-and-operations]].

## Links

- [[llm-application-interface]] shows how retrieved evidence enters a model request.
- [[attention-and-transformer-architecture]] distinguishes external retrieval from attention.
- [[agentic-systems]] can use RAG as a bounded tool, not a substitute for authorization.
- [[llm-training-lifecycle]] explains when retrieval is preferable to changing model weights.
