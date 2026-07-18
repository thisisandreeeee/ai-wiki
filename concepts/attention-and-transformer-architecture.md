---
title: Attention and Transformer Architecture
created: 2026-07-18
updated: 2026-07-18
type: concept
tags: [ai, machine-learning, llm, research]
sources: [raw/learning-resources/technical-interview-learning-resources.md]
confidence: high
---

# Attention and Transformer Architecture

A Transformer repeatedly alternates two operations: **attention moves information between token positions**, while an **FFN transforms each position independently**. Stacking these blocks turns token embeddings into increasingly contextual representations.

## Attention is learned retrieval

For hidden states $X$, learned projections create queries, keys, and values:

$$Q=XW_Q,\quad K=XW_K,\quad V=XW_V.$$

- A **query** represents what this token needs.
- A **key** represents how another token can be matched.
- A **value** is the information returned after that match.

$$\operatorname{Attention}(Q,K,V)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V.$$

The score $q_i\cdot k_j$ is an unnormalized relevance score, not an attention weight. Dividing by $\sqrt{d_k}$ avoids increasingly extreme logits as key dimension grows; softmax over the *key-token axis* creates a distribution for each query token. The output is a weighted mixture of values—a new context-aware representation.

This resembles [[retrieval-augmented-generation]] only at a high level. Attention retrieves within the model's current sequence and learned weights; RAG retrieves external evidence at application runtime.

## Shapes prevent most implementation bugs

A common batched multi-head convention is:

```text
X:       (B, T, D)       batch, token positions, model dimension
Q/K/V:   (B, H, T, Dh)   H heads, Dh dimensions per head
scores:  (B, H, Tq, Tk)  each query position against every key position
context: (B, H, Tq, Dh)
```

```python
scores = Q @ K.transpose(-2, -1) / sqrt(Dh)
weights = softmax(scores + mask, dim=-1)
context = weights @ V
```

Name axes before transposing. A dot product yields one scalar; matrix multiplication applies many dot products. Heads are a separate representation axis, not duplicate token positions.

## Multi-head attention and masking

Multiple heads run attention in parallel on different learned projections. Their outputs are concatenated and remixed through an output projection $W_O$. Heads are not guaranteed to become named concepts such as “syntax head” or “fact head”; they are learned relation spaces.

A **causal mask** is applied *before* softmax in decoder self-attention, assigning forbidden future positions $-\infty$. Thus position $i$ can attend only to positions $j\le i$. Applying a mask after softmax leaks future information during training.

## Encoder, decoder, and cross-attention

An encoder reads its input bidirectionally. A simplified block is:

```text
X1 = LayerNorm(X + SelfAttention(X))
X2 = LayerNorm(X1 + FFN(X1))
```

A decoder writes autoregressively. It uses masked self-attention, and in encoder-decoder architectures also **cross-attention**:

```text
query: decoder states
key/value: encoder states
```

Cross-attention lets generated positions retrieve from a different source sequence. Decoder-only LLMs instead use token and position representations, repeated causal decoder blocks, then an LM head that projects hidden states to vocabulary logits.

The position-wise FFN is normally one shared network applied independently at every token. It adds nonlinearity; it does not mix token information. Residual connections preserve a path for existing representations, while layer normalization stabilizes optimization.

## Mixture of Experts

A **Mixture of Experts (MoE)** often replaces a dense FFN with many expert FFNs and a router. For each token, the router selects a small top-$k$ subset and combines their outputs. This increases total parameter capacity while keeping active compute lower than an equally large dense model. Its real systems costs are routing, load balance, and cross-device expert communication—not free scale.

## Training and inference

Trainable parameters include embedding tables; Q/K/V/output projections; FFN, normalization, and vocabulary-head weights. Q, K, V, attention scores, and context vectors are transient forward-pass values, not model parameters.

During training, causal masking lets the model process shifted target tokens in parallel. During autoregressive inference, it must produce one token at a time; this shift explains the prefill/decode split in [[llm-inference-on-gpus]] and [[llm-inference-optimization]].

## Links

- [[llm-training-lifecycle]] describes how these parameters are adapted.
- [[llm-inference-on-gpus]] explains the memory and compute consequences of attention.
- [[retrieval-augmented-generation]] is the external-retrieval counterpart.
- [[technical-interview-study-guide]] maps this note to answerable questions.
