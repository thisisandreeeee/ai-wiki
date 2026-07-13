---
title: GLM-5.2
created: 2026-06-21
updated: 2026-06-29
type: entity
tags: [ai, llm, model, tooling]
sources: [raw/newsletters/ainews-2026-06-17-ainews-glm-5-2-the-top-frontend-coding-model-in-the-world-indexshare-f.md, raw/newsletters/ainews-2026-06-19-ainews-glm-gpt-glm-5-2-passes-vibe-check-z-ai-forecasts-open-fable-by.md, raw/newsletters/the-neuron-2026-06-18-washington-wants-ai-equity.md, raw/newsletters/ainews-2026-06-25-ainews-it-s-meta-harness-summer.md, raw/newsletters/ainews-2026-06-26-ainews-openai-reports-median-internal-codex-output-tokens-grew-56x-in.md, raw/newsletters/ainews-2026-06-27-ainews-openai-gpt-5-6-sol-terra-luna-restricted-to-trusted-partners.md]
confidence: high
---

# GLM-5.2

**GLM-5.2** was the breakout open-weight model story in the corpus. AINews framed it as an open model that passed the "frontier-adjacent" vibe check rather than another short-lived benchmark-maxed release.

## Signals from the corpus

- Multiple practitioners described GLM-5.2 as plausibly frontier-adjacent in daily use, especially for coding and agentic work.
- AINews highlighted architecture details including MLA/DSA lineage and **IndexShare**, described as reusing sparse-attention indexes for speculative decoding efficiency.
- The model was reported as a very large MoE, with LocalLlama discussion around ~753B total parameters, ~40B active parameters per token, MIT licensing, long-context claims, and large GGUF quantizations.
- Hosted and local access were both important: Hugging Face provider promotions created demand spikes, while Unsloth GGUF quantizations still implied large RAM/VRAM requirements.

## June 24–28: Continued momentum and competitive positioning

The late June corpus shows GLM-5.2 consolidating as the open-model benchmark:

- **Coding benchmarks**: Arena ranked GLM-5.2 Max above Claude Opus 4.8 Thinking on frontend Code Arena. On PostTrainBench, GLM 5.2 Max narrowly ahead of Opus 4.8 Max at 34.29% vs 34.08% with zero failed runs across 84 runs.
- **Infrastructure**: NVIDIA published official NVFP4 checkpoints for Blackwell-class deployment. vLLM added serving support. Databricks pushed throughput to 392 tok/s on Artificial Analysis (up from 201 tok/s on H200s).
- **Real-world parity claims**: Practitioners reported GLM 5.2 "on par with Claude Code powered by Opus 4.8" via OpenClaude. Local Mac Studio workflows for medical-agent orchestration also surfaced.
- **ARC-AGI-2**: GLM-5.2 achieved the strongest ARC-AGI-2 result to date by an open-source model at 22.8%.
- **Pricing**: Luna (OpenAI's cheapest GPT-5.6 tier) roughly matches GLM-5.2 at ~$2/1M tokens blended.

## Why it mattered

GLM-5.2 changed the open-model discussion from "open models are cheaper but clearly behind" to "open models may soon offer Fable-class utility without closed-lab gating." With [[gpt-5-6|GPT-5.6]]'s restricted launch and [[frontier-model-access-controls|frontier access]] increasingly gated, open-weight models like GLM-5.2 gain strategic urgency.

## Open questions

- Does the strongest reported performance survive low-bit quantization and local inference constraints?
- Can Z.ai and other open-model labs sustain progress beyond one launch cycle?
- Will open frontier models remain available if export-control logic spreads internationally?

## Links

- Related concepts: [[local-llms]], [[frontier-model-access-controls]], [[coding-agent-evaluation]]
- Related entities: [[claude-fable-5]], [[gpt-5-6]]
- See also: [[closed-vs-open-frontier-models]], [[weekly-briefing-2026-06-24-to-2026-06-28]]
