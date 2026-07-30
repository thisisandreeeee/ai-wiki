---
source: gmail
newsletter: "latent-space"
message_id: "19f862e08b79c3d8"
thread_id: "19f862e08b79c3d8"
subject: "Causal Models Need Causal Data - Xaira’s X-Cell model for Drug Discovery (Bo Wang & Ci Chu, Chief Discovery Office…"
from: "\"Latent.Space\" <swyx@substack.com>"
date: "Tue, 21 Jul 2026 19:34:07 +0000"
ingested: 2026-07-30
sha256: bcac24903efa9aad18c8d2550f55d7b8cd4f330777546861bef95deca94fc9f5
---
View this post on the web at https://www.latent.space/p/xaira

Bet on information
If test loss flatlines after 1.5B parameters while training loss continues to drop as you scale, that tells you that your model is limited by the amount of information in your data.
Training on a single, smallish data set exposed an information gap: the 3.1B model falls off the scaling trend. Neither parameters nor compute will improve performance past this wall. For predicting changes to gene expression, you need more information rich data.
This is what Chu and Bo’s teams have done, and here is what ~30x the information buys you:
Now we can scale with parameters and training compute! We don’t know how much this effort costed, but we can guess that data collection experiments and infrastructure was a few tens of millions, and compute + headcount + research was a few million. The budget looks like a RL rollout budget, rather than a data rich pre-training one.
We were lucky enough to have the two central figures in this story on our podcast. Taking the lead from Ci Chu and Bo Wang, Xaira Therapeutics is betting that information rich data is the key to AI-driven drug development. Chu was recently promoted [ https://substack.com/redirect/682a14a3-1aef-4217-934e-c3e527ca20f7?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] to Chief Discovery Officer and Bo to Chief AI Scientist, underscoring just how strategic Xaira considers this bet.
Reverse engineering the human cell
If you had to figure out how a human cell works, what would you do? A good place to start might be by documenting what genes are expressed (e.g. what RNA is floating around) in different kinds of cells, in different circumstances.
That is CELLxGENE [ https://substack.com/redirect/06aea3f1-a446-4409-b0bf-6652629190f7?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], a database of 168M cells built by Chan Zuckerberg Institute that maps each cell to a count of how many times 20K-30K genes were detected in that cell, plus detailed metadata about every cell. A ~4 trillion-entry matrix.
If the Protein Data Bank (PDB) unlocked structural biology models [link Boltz, BioHub], CellXGene has done the same thing for Virtual Cell models. Like PDB, CELLxGENE has inspired a zoo of AI models of RNA expression; so much so that RNA expression models have become synonymous with Virtual Cell models. Bo Wang built one of the most influential, scGPT [ https://substack.com/redirect/ab6148d7-7f58-4800-be0f-6207d8b978a6?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], that became the starting point for Xaira’s new model.
RNA expression ≠ Virtual Cell
Models trained on CELLxGENE describe the relationship between cell types and cell states, but they are not good at predicting what will happen if we make changes to RNA expression. Changes in gene expression are highly correlated, and its is difficult (impossible) to figure out what causes what in most cases.
If you could “turn the dial down” on one gene at a time, however, then you would be able to observe what is upstream and downstream of a given gene. You could tell if A → B & C or B → A & C or B → A, C → B → … If you did this for all of the genes, then maybe you could train a model that could predict what would happen to a cell if you change a gene (e.g. with a drug or a gene edit). Or maybe you could figure out the least invasive way to change a particular gene’s expression.
X-Atlas → X-Cell
This is exactly what Chu and Bo’s teams have done. The data set is called X-Atlas and the model is called X-Cell.
In this episode, we discuss:
Why the team abandoned autoregression for diffusion
The CRISPR-based experiments that run millions of tests in parallel, and generate the raw data for X-Atlas and X-cell
Generalization to real lab experiments in real human cells
Beating the linear baseline that has outperformed previous models
Justifying a kitchen-sink of priors, and how that stacks up vs. data and architecture
Bo also shared with us some of the (major) advantages he has as an academic vs. industry leader, and how his labs keep up with the breakneck pace of AI innovation.
Check out the full episode on YouTube, or your favorite podcasting platform!

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3lOamt3TVRreExDSndiM04wWDJsa0lqb3lNRGM1TkRFMk1EY3NJbWxoZENJNk1UYzRORFkyTWpVNU1Dd2laWGh3SWpveE9ERTJNVGs0TlRrd0xDSnBjM01pT2lKd2RXSXRNVEE0TkRBNE9TSXNJbk4xWWlJNkltUnBjMkZpYkdWZlpXMWhhV3dpZlEuT1JXOS1xc3pySjZDdGFlaFFUZXg3NkNGNXgyVmVWZ0kwVXoxbEZqdGV0QSIsInAiOjIwNzk0MTYwNywicyI6MTA4NDA4OSwiZiI6ZmFsc2UsInUiOjI2OTAxOTEsImlhdCI6MTc4NDY2MjU5MCwiZXhwIjoyMTAwMjM4NTkwLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.Xp_Px_DNpJQP1g0yHsWLecl0Dh_G5LdyiPpl2CEp9h4?
