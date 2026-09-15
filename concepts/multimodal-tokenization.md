---
title: Multimodal Tokenization
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [ai, machine-learning, llm, research]
sources: [raw/learning-resources/multimodal-tokenization-image.md]
confidence: high
---

# Multimodal Tokenization

A Transformer consumes a sequence of vectors, not raw media. **Multimodal tokenization** is the preprocessing layer that converts every input modality — text, images, audio, video, 3D point clouds, and robotic/embodied streams — into the token sequences the model can actually attend over.

Each modality has its own preprocessing pipeline and dedicated encoder, but every encoder emits the same shape: a `[N × D]` vector sequence, where `N` is the number of tokens and `D` the token feature dimension. Once everything is a `[N × D]` sequence, one Transformer can mix information across modalities.

## Modality → token recipes

- **Text** — tokenize into a vocabulary of subword tokens, then look up an embedding (e.g. 768-dim). One output vector per token; `N` ≈ sequence length.
- **Images** — split the image into 16×16 patches (the ViT convention), embed each patch as a token. `N` ≈ number of patches; resolution and patch size set the token budget.
- **Audio** — extract spectrogram features from the raw waveform (e.g. 16 kHz sampling), then encode per-frame features into tokens.
- **Video** — sample frames and space-time patches (**tubelets**), so each token covers a small 3D spatio-temporal region rather than a single frame pixel grid.
- **3D point clouds** — organize the raw points into **points, voxels, or patches**, then encode each region into a token. Geometry has no natural "reading order", so the structure choice is part of the design.
- **Robotics / embodied** — preprocess multiple streams: vision, robot state, tactile sensing, and action commands. Each stream is tokenized separately before fusion.

## From encoders to the Transformer

The per-modality encoders produce `[N × D]` sequences that can be used two ways:

1. **Directly**: feed each sequence into a Transformer (often with a causal or cross-attention wiring between streams).
2. **Fused**: concatenate or otherwise merge all modality sequences into one unified token sequence, and let a single Transformer process tokens from every modality together.

This is why "token" is a universal currency: text tokens, image patches, audio frames, and action tokens all become the same vector-shaped sequence, so one model can attend across them. The cost is the token budget — high-resolution images, long video, or dense point clouds quickly produce very long `N`, with direct consequences for the KV cache and memory footprint in [[llm-inference-on-gpus]].

## Why it matters

- Multimodal models (e.g. [[deepseek-v4-1-flash]], vision-language and embodied systems) all need this interface layer.
- The same Transformer core in [[attention-and-transformer-architecture]] is reused for every modality once inputs are token-shaped.
- [[agentic-robotics]] systems rely on tokenized vision, state, and action streams inside a single policy model.

## Links

- [[attention-and-transformer-architecture]] — the Transformer side of the interface these token sequences feed.
- [[llm-inference-on-gpus]] — token count and sequence length drive memory, KV cache, and prefill/decode cost.
- [[deepseek-v4-1-flash]] — an open-weight multimodal example of per-modality encoders feeding a unified sequence.
- [[agentic-robotics]] — embodied use case combining vision, state, and action tokenization.