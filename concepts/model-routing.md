---
title: Model Routing
created: 2026-07-30
updated: 2026-08-10
type: concept
tags: [ai, llm, tooling, trend]
sources: [raw/newsletters/ainews-2026-07-21-ainews-not-much-happened-today.md, raw/newsletters/the-neuron-2026-07-23-google-split-gemini-in-three.md, raw/newsletters/ainews-2026-07-29-ainews-ai-is-eating-finance-aie-nyc-now-open.md, raw/newsletters/ainews-2026-08-07-ainews-amd-buys-taalas.md, raw/newsletters/latent-space-2026-08-03-the-inference-engineering-masterclass-philip-kiely-ali-taha-baseten.md, raw/newsletters/latent-space-2026-08-04-unpacking-chatgpt-work-the-agent-for-a-billion-users.md, raw/newsletters/ainews-2026-08-01-ainews-not-much-happened-today.md]
confidence: medium
---

# Model Routing

**Model routing** is choosing among models, effort levels, providers, and harness modes based on task, cost, latency, safety, and context constraints.

## July 2026 signal

AINews described model routing as a first-class systems problem, including OpenAI-compatible routers and broader discussion of open and closed models specializing across cyber, coding, frontend, long-context, and local deployment. [raw/newsletters/ainews-2026-07-21-ainews-not-much-happened-today.md:18-20]

Google's Gemini split gives a product example: Flash for general work, Flash-Lite for speed/high-volume jobs, and Flash Cyber for restricted cyber-defense workflows. [raw/newsletters/the-neuron-2026-07-23-google-split-gemini-in-three.md:20-31]

Kimi K3 harness comparisons add another layer: the same model can show different speed, cost, and success profiles depending on whether it runs through Kimi Code, Hermes, Claude Code-style workflows, or other orchestrators. [raw/newsletters/ainews-2026-07-29-ainews-ai-is-eating-finance-aie-nyc-now-open.md:41-45]

## August 2026 update: routing becomes a learned product layer

Cursor's reported router was trained on millions of weekly in-product interactions and explicitly assigned different models to routine work, planning, execution, and debugging. Baseten's inference account adds cache locality, prefill capacity, traffic shape, and dedicated-vs-shared deployment as routing inputs. [[deepseek-v4-flash]] and [[qwen-3-8-max]] therefore belong in a policy table with quality, quantization, latency, context reuse, availability, and spend—not in a single “best model” slot.

ChatGPT Work adds another routing dimension: plugins, scheduled tasks, browser profiles, and project context determine which tools and memories are available. A model route without a permission and context policy is incomplete. [raw/newsletters/latent-space-2026-08-04-unpacking-chatgpt-work-the-agent-for-a-billion-users.md]

## Why it matters

As capability compresses across frontier and open-weight models, the routing layer becomes part of the product. [[software-factories]] need policies for when to use the strongest model, when to use a cheap executor, when to route to a cyber-specialized model, and when to fall back to [[local-llms]].

## Links

- Related concepts: [[agent-experience]], [[software-factories]], [[ai-infrastructure-economics]], [[frontier-model-access-controls]]
- Related entities: [[kimi-k3]], [[google-gemini]], [[openai]]
