---
title: Model Routing
created: 2026-07-30
updated: 2026-08-31
type: concept
tags: [ai, llm, tooling, trend]
sources: [raw/newsletters/ainews-2026-08-17-ainews-stripe-buys-openrouter-for-7b.md, raw/newsletters/latent-space-2026-08-18-frontier-model-cost-and-open-weights-popularity-is-driving-demand-for.md, raw/newsletters/the-neuron-2026-08-21-claude-allegedly-speedran-a-31k-loss.md, raw/newsletters/ainews-2026-07-21-ainews-not-much-happened-today.md, raw/newsletters/the-neuron-2026-07-23-google-split-gemini-in-three.md, raw/newsletters/ainews-2026-07-29-ainews-ai-is-eating-finance-aie-nyc-now-open.md, raw/newsletters/ainews-2026-08-07-ainews-amd-buys-taalas.md, raw/newsletters/latent-space-2026-08-03-the-inference-engineering-masterclass-philip-kiely-ali-taha-baseten.md, raw/newsletters/latent-space-2026-08-04-unpacking-chatgpt-work-the-agent-for-a-billion-users.md, raw/newsletters/ainews-2026-08-01-ainews-not-much-happened-today.md, raw/newsletters/ainews-2026-08-13-ainews-spacexai-grok-4-6-and-grok-bot.md, raw/newsletters/the-neuron-2026-08-13-elon-releases-grok-4-6-says-grok-4-7-is-weeks-away.md, raw/newsletters/ainews-2026-08-14-ainews-gemini-3-7-flash-brings-gdm-back-to-the-forefront.md, raw/newsletters/the-neuron-2026-08-14-why-gemini-3-7-flash-just-got-half-price.md]
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

## August 17 update: price, latency, and trajectory shape the route

Grok 4.6 and Gemini 3.7 Flash sharpen the routing table. Grok is positioned around cost per completed long-running task, while Gemini emphasizes high-throughput workhorse traffic, rapid iteration, and low introductory pricing. GPT-5.6 Sol Ultrafast and DeepSeek V4 Pro add hardware and time-of-day dimensions. The route should therefore include expected turns, cache reuse, tool latency, context length, failure recovery, and total task cost—not only input/output token price. [raw/newsletters/ainews-2026-08-13-ainews-spacexai-grok-4-6-and-grok-bot.md][raw/newsletters/ainews-2026-08-14-ainews-gemini-3-7-flash-brings-gdm-back-to-the-forefront.md][raw/newsletters/the-neuron-2026-08-14-why-gemini-3-7-flash-just-got-half-price.md]

## August 24 update: routing becomes the economic control plane

The reported Stripe–[[openrouter]] acquisition, Glean's enterprise router, and AT&T's reported shift toward open models make routing a budget and reliability control plane. Routine work can move to cheaper open models, while difficult or high-stakes tasks escalate; the policy only works when “good enough” is measured on real workloads. [raw/newsletters/ainews-2026-08-17-ainews-stripe-buys-openrouter-for-7b.md][raw/newsletters/latent-space-2026-08-18-frontier-model-cost-and-open-weights-popularity-is-driving-demand-for.md][raw/newsletters/the-neuron-2026-08-21-claude-allegedly-speedran-a-31k-loss.md]

## Late August: route by task cost and state

The new model wave makes routing more heterogeneous. GLM-5.3-Flash and Hy4-preview offer open, large-MoE options; Qwen 3.8 Flash Next adds n-gram memory and heterogeneous offload; and vLLM’s speculative-decoding comparison reports no universal winner across model families and workloads. A useful route therefore includes expected turns, cache reuse, KV-cache policy, tool latency, verification cost, hardware placement, and failure recovery—not merely token price. [raw/newsletters/ainews-2026-08-28-ainews-openai-to-reach-agi-bar-by-end-2026.md][raw/newsletters/ainews-2026-08-29-ainews-openai-shuts-off-cursor.md]

## Why it matters

As capability compresses across frontier and open-weight models, the routing layer becomes part of the product. [[software-factories]] need policies for when to use the strongest model, when to use a cheap executor, when to route to a cyber-specialized model, and when to fall back to [[local-llms]].

## Links

- Related concepts: [[agent-experience]], [[software-factories]], [[ai-infrastructure-economics]], [[frontier-model-access-controls]]
- Related entities: [[kimi-k3]], [[google-gemini]], [[openai]]
