---
title: MAI-DxO
created: 2026-10-26
updated: 2026-10-26
type: entity
tags: [ai, llm, model, research, company]
sources: [raw/newsletters/the-neuron-2026-10-23-microsoft-ai-scored-83-where-doctors-got-36.md]
confidence: medium
---

# MAI-DxO

**MAI-DxO** (Microsoft AI Diagnostic Orchestrator) is a reported multi-agent medical-diagnosis system from [[microsoft]]. It combines virtual clinicians that propose diagnoses, choose follow-up questions or tests, challenge one another, and account for test cost.

## Reported evaluation

Microsoft reports 83% accuracy on 304 difficult New England Journal of Medicine cases, compared with 36% for primary-care physicians with textbook and internet access and 22% without. On more typical emergency-room cases, the source reports 80% for MAI-DxO versus 47% for physicians, with roughly half to one-third the diagnostic cost in the NEJM work. [raw/newsletters/the-neuron-2026-10-23-microsoft-ai-scored-83-where-doctors-got-36.md]

The sequential setup is important: SDBench starts with limited information and requires the system to decide what to ask or order next, rather than handing the model a complete case. The panel approach is therefore a workflow and information-acquisition result, not just a model-answer comparison.

## Limits

The evaluation was simulated and used primary-care physicians and general internists working alone, not specialist teams. Microsoft says real-world performance still needs testing. The source also reports that GPT-5 alone scored 78.9%, so the multi-agent orchestration contributed only part of the headline result. A planned study with Beth Israel Deaconess Medical Center is the more consequential test because it compares recommendations with standard care around real patients. [[ai-healthcare]] [[ai-benchmarking]]

## Links

- Related entity: [[microsoft]]
- Related concepts: [[ai-healthcare]], [[ai-benchmarking]], [[agentic-systems]]
- Related query: [[weekly-briefing-2026-10-26]]
