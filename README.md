# AI Wiki

A living, Obsidian-style knowledge base for AI-related news.

I use this repository to organise ideas, companies, models, technical concepts, and recurring themes from the AI ecosystem. The material comes from newsletters I subscribe to but do not have time to read in full due to the sheer volume. I use the repository to consolidate and structure the information so I can review the most relevant ideas in linked Markdown pages over time.

## How it works

This wiki is largely inspired by Karpathy's [llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

At a high level:

```text
Newsletters
    ↓
Raw source archive
    ↓
Extract recurring entities and concepts
    ↓
Consolidate related information
    ↓
Linked Markdown wiki
```

## Newsletter sources

- [The Neuron](https://www.theneurondaily.com/)
- [Latent Space](https://www.latent.space/)
- [AINews](https://www.ainews.com/)
- [Data Elixir](https://dataelixir.com/)
- [Data Science Weekly](https://www.datascienceweekly.org/)

## View in Obsidian

The repository is plain Markdown and can be opened directly as an [Obsidian](https://obsidian.md/) vault.

```bash
git clone https://github.com/thisisandreeeee/ai-wiki.git
```

Then:

1. Open Obsidian.
2. Select **Open folder as vault**.
3. Choose the cloned `ai-wiki` directory.
4. Open `index.md` as a starting point.

Obsidian will automatically resolve the `[[wikilinks]]`, backlinks, and graph relationships between pages.

## Validation

Run:

```bash
python3 scripts/lint_wiki.py
```
