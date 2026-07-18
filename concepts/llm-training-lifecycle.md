---
title: LLM Training Lifecycle
created: 2026-07-18
updated: 2026-07-18
type: concept
tags: [ai, machine-learning, llm, research]
sources: [raw/learning-resources/technical-interview-learning-resources.md]
confidence: high
---

# LLM Training Lifecycle

An LLM training recipe is easiest to reason about by separating **stage**, **learning signal**, **data source**, and **update method**. Mixing those categories is the usual reason terms such as CPT, DPO, RLHF, and LoRA become confusing.

```text
pretraining → capability/domain shaping → post-training → deployed system
                 (CPT / “mid-training”)     (SFT, preferences, RL)
```

## The stages

- **Pretraining** learns a general token distribution from broad text, code, and multimodal data, usually by next-token prediction. Its output is a capable *base model*, not necessarily a reliable assistant.
- **Continued pretraining (CPT)** continues that objective on a changed distribution: a language, domain corpus, code, mathematics, or long-context material. It is a way to make the model more fluent in that distribution.
- **Mid-training** is an informal label for targeted capability shaping between broad pretraining and assistant post-training. It is useful as a description, not a universal standardized stage.
- **Post-training** makes a capable model useful in an application: instruction following, style, safety, tool use, and preference trade-offs.

“CPT changes knowledge; post-training changes behaviour” is a useful first approximation, not a hard boundary. SFT can teach facts; CPT can change style. The meaningful difference is the intended distribution, supervision, and evaluation target.

## One engine, different supervision

CPT and SFT may both optimize token-level cross-entropy on the same Transformer. The data format and loss mask tell the model what to learn:

| Method | Typical datum | Main intent |
| --- | --- | --- |
| CPT | domain documents or code | continue text in the target distribution |
| SFT | prompt → desired response | respond to this request in this way |
| DPO | prompt + chosen/rejected responses | prefer one response over another |
| RL | sampled trajectory + scalar reward | discover actions that maximize outcome reward |

For an assistant response $y$ conditioned on prompt $x$, SFT commonly maximizes $\log p_\theta(y\mid x)$ while masking prompt tokens from loss. CPT normally trains across the full document stream. Same mechanics—forward pass, loss, backpropagation—can yield very different behaviour because the supervision differs.

## Post-training primitives

### Imitation: SFT and distillation

**Supervised fine-tuning** teaches demonstrations: the desired answer, tool call, or trajectory is provided. **Distillation** transfers behaviour from a teacher to a student; SFT on teacher-generated answers is one common form. Rejection sampling—generate candidates, score them, then train on the retained ones—is a selection procedure that often supports distillation, but is not synonymous with it.

Use imitation when the desired output is concrete: format compliance, customer-support style, tool schemas, or a known procedure.

### Preferences: DPO

A DPO datum is $(x, y^+, y^-)$, where $y^+$ is preferred to $y^-$. Standard DPO increases the policy's relative likelihood of the chosen response versus the rejected response, compared with a frozen reference policy:

$$
-\log \sigma\left(\beta\left[\log\frac{\pi_\theta(y^+\mid x)}{\pi_{ref}(y^+\mid x)}-\log\frac{\pi_\theta(y^-\mid x)}{\pi_{ref}(y^-\mid x)}\right]\right).
$$

Use DPO when SMEs can rank alternatives more reliably or cheaply than they can author gold answers. **Offline DPO** uses a fixed set of pairs; **online DPO** repeatedly creates fresh pairs from the current policy and a human, AI, or verifier judge. DPO is direct preference optimization—not merely “efficient RLHF”—and its reference model shapes the objective rather than acting as a hard safety constraint.

### Rewards: RLHF and RLAIF

Classic **RLHF** turns human comparisons into a learned reward model, samples new policy outputs, and optimizes expected reward while staying close to a reference policy. PPO is a historical implementation choice, not the definition of RLHF.

$$
\max_\theta\;\mathbb{E}_{y\sim\pi_\theta}[r_\phi(x,y)]-\beta D_{KL}(\pi_\theta\|\pi_{ref}).
$$

Use RL when exploration matters and a trustworthy reward can score new behaviour—especially verifiable code, mathematics, games, tools, and long-horizon trajectories. The central danger is **reward hacking**: optimizing a proxy that is not the desired outcome.

**RLAIF** names the feedback source (AI), not a single optimization method. AI feedback can produce SFT examples, DPO pairs, reward-model labels, or RL rewards. That distinction matters when evaluating bias and validating a judge.

## LoRA is an update method, not a stage

Full fine-tuning changes all selected model weights. **LoRA** freezes a base weight $W$ and learns a low-rank update:

$$W' = W + \frac{\alpha}{r}BA.$$

It can be used for CPT, SFT, DPO, or RL. **QLoRA** additionally quantizes the frozen base to reduce training memory. Choose adapters when iteration cost, GPU memory, or many deployable specializations matter; choose full fine-tuning only when evaluation justifies its additional cost or adapter capacity is insufficient.

## A practical decision tree

1. First ask whether [[retrieval-augmented-generation]], prompting, tools, or a deterministic workflow solve the problem.
2. If the gap is stable domain fluency, consider CPT; if knowledge is private, fresh, or citation-sensitive, prefer retrieval.
3. If ideal examples exist, start with SFT—often with LoRA.
4. If ranking is easier than authoring, evaluate DPO.
5. If success is verifiable across generated or multi-step behaviour, compare online RL against simpler baselines.
6. For consequential tools, add explicit safety, sandbox, and regression evaluation from [[agent-reliability-and-operations]].

## Links

- [[attention-and-transformer-architecture]] explains the model being optimized.
- [[llm-application-interface]] covers the deployed model contract that post-training often targets.
- [[retrieval-augmented-generation]] distinguishes knowledge access from retraining.
- [[agentic-systems]] shows why trajectory-level rewards become useful for tool-using systems.
