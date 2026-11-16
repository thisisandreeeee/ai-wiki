---
source: gmail
newsletter: "data-science-weekly"
message_id: "1a1d24080f5afd70"
thread_id: "1a1d24080f5afd70"
subject: "Data Science Weekly - Issue 677"
from: "Data Science Weekly Newsletter <datascienceweekly@substack.com>"
date: "Fri, 13 Nov 2026 00:12:28 +0000"
ingested: 2026-11-16
sha256: 90dc082a9d356f9c02750d6d40136d24b8c996320d57fdab6990552750b40a45
---
View this post on the web at https://datascienceweekly.substack.com/p/data-science-weekly-issue-677

Issue #677
Nov 12, 2026
Hello!
Every week, we write this email to share links we think are worth sharing in the Data Science, ML, AI, Data Visualization, and ML/Data Engineering worlds.
Now…let’s dive into this week's interesting links.
Editor's Picks
Can GROUP BY still be optimized after all these years? [ https://substack.com/redirect/87616e4d-17cc-4c9e-9017-d76b0444c43b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
One of the things I like the most about the world of databases is how a simple operation can become extremely complex when it’s optimized to its highest levels. As part of that line of thought - I thought it might be interesting and fun to share a novel optimization we recently found that improved Pivot’s performance significantly on GROUP BY queries that find the top K groups by aggregate value. For example, “which 10 items have the most orders?”…
Same Person, Five Records [ https://substack.com/redirect/d3844cf3-133d-4f41-b7eb-d89a1891d330?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I recently wrote about identity resolution for the OneSix blog: Same Person, Five Records: What Actually Works in Identity Resolution. That post covers the basics, build vs. buy, cost, and where AI fits. Here I want to get into some of the other details of the pipeline I built….
The rule of law and economic growth: what three decades of data show [ https://substack.com/redirect/00c9b7cc-5e4b-4cb9-bce5-b872e958b609?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Weighted by population, the rule of law has slipped globally since 1996. India and the United States contributed a large part to this decline, while China’s net impact was negligible thanks to a recovery from the mid 00’s. Countries with a stronger rule of law tend to be wealthier, and those where it improved were more likely to grow faster, but there are plenty of exceptions to the rule, with China experiencing higher growth than might be expected from changes in its rule of law score, alongside Armenia, Bosnia and Herzegovina, Guyana and Myanmar…
What’s on your mind
This Week’s Poll:
Last Week’s Poll:
.
Data Science Articles & Videos
“You’re kind of a hero at my company” [ https://substack.com/redirect/59fccd10-350e-4472-9317-d16318f6f216?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The work I’m proudest of is not necessarily the work that is most useful or best known or that others consider the best. A few years ago I learned that a model I threw together in about 15 minutes, and whose simplicity I had been quietly embarrassed by for years, was used by a successful company. But I just learned that the model is much more widely used and appreciated than I thought. And I’ve just lost my two steady consulting clients, who were together responsible for about 60% of my income each year, so now is the time to do some self-promotion. And I think there are broader lessons here about the virtues of simplicity, and how we sometimes aren’t good judges of our own work, and maybe some other themes besides. So here’s the story…
AMA - Staff DS 9 YOE [Reddit] [ https://substack.com/redirect/73674ca6-07e2-4143-b60d-1e9bf5e7691d?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Around this time last year, I did an AMA and thought it was a pretty good experience. I wanted to do another one. If folks have any questions, maybe we can have some discussion together : )…
Can a Linear Program Do Weight-Space Programming? [ https://substack.com/redirect/c3477b44-90cb-4fe6-998e-c7aa4e494dc4?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Last week, MIT CSAIL published Sparks of Weight-Space Programming. Given the raw weights of a small network, GPT-6 Astra could tell which game it had been trained to play…In another experiment, they asked Astra to make Qwen3.5-0.8B better at math by editing its weights…Looking at Astra’s edit, I realized most of its search was solving a linear program by trial and error. It spent about 8 hours and 28 forward passes choosing which weights to change and by how much. A couple of LP solves, about a minute each, do the same job with 8× fewer changed weights. In this post I’ll walk through the edit, why it’s an LP, and what that says about the fix itself…
Laziness for Bayesian nonparametrics [ https://substack.com/redirect/5eefaa1a-5a45-423f-a7e7-cc96dfd7eca1?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
LazyPPL is a Haskell library for Bayesian probabilistic programming. It supports lazy use of probability, and we provide new Metropolis-Hastings algorithms to allow this. LazyPPL is inspired by recent ideas in synthetic probability theory and synthetic measure theory, such as quasi-Borel spaces and Markov categories. Laziness appears to be a good paradigm for non-parametric statistics.
Does until it doesn’t and doesn’t until it does [ https://substack.com/redirect/2b685db1-6fe4-4366-ace2-8918c9bcf7d1?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The result of high levels of hype about new technologies is that people start to think that:
The world has just been changed forever (which sometimes, but rarely, is true to some extent).
The new technology that is being hyped will continue to change the world in powerful and unimaginable ways.
The new technology is a once in a lifetime, or even once in a millennium, singular event.
[[I think it is no coincidence that these three thoughts are similar to those that found new religions or cults. But my argument below is independent of that correlation.]]
The topic of this post is the following koan applied to new technologies. It is two very general truths that people who think they are powerful ignore at their own peril…
Administration and success [ https://substack.com/redirect/feed77ea-77c0-4626-8b35-883f08fd6237?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The manosphere has it all wrong. If you want to be a successful man in this world, you need to learn to be a good administrator first. The more I go on in my career the more I see this. Let me fill in some details. I’m going to tackle the manosphere first, then I’ll come back around to science careers…
Auditing demographic parity across institutions without sharing individual data [ https://substack.com/redirect/9c99e967-e657-4645-bc3c-86513a0c046c?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Suppose several banks use the same scoring system to evaluate credit applicants. Each bank audits the scores assigned to different demographic groups and finds little or no disparity. Can we conclude that the scoring system is similarly balanced across the entire population? Not necessarily. In fact, every bank may pass its local audit while a substantial disparity emerges when all applicants are considered together. The problem is not necessarily a poor statistical estimate: local and global audits can measure fundamentally different things. This is the starting point of our recent paper, Federated Measurement of Demographic Disparities from Quantile Sketches…We ask a practical question: can we measure population-wide demographic disparities when the relevant score data are held by separate organizations and cannot be pooled?…
Generating Mini-Crosswords [ https://substack.com/redirect/1a4eeb96-63e1-47ab-a1df-ae8936f67247?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The New York Times publishes “mini-crosswords,” which are crossword puzzles on a relatively small grid (usually 5×5), without any black squares, so that every row and column of the grid must spell a word…How hard is it to create these puzzles? This post is motivated by a recent College Mathematics Journal article (see Reference (1) below) that considers this question, and describes an approach using the Metropolis-Hastings algorithm to randomly sample instances of puzzles. But instead of just randomly sampling one puzzle at a time, can we actually enumerate all possible puzzles?…
Stanford / Fall 2026 / CS 312: Deep Learning Alchemy [ https://substack.com/redirect/c13d58b4-d785-4805-b00a-f6576ba76d28?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
This course takes the stance that knowledge or math abilities alone are not enough, and there is no substitute to getting your hands dirty and running many, many experiments. To this end, we will work through computationally tractable domains and take students through the process of obtaining mastery in this domain through efficient experimentation and experiment outcome prediction. The class will alternate between assignments (where students run experiments to understand deep learning phenomena), quizzes (where students are tested for their ability to predict held-out experiment outcomes), lectures, and tutorials…
TinyGPT Visualizer: Tools for Exploring the Souls of Large Language Models [ https://substack.com/redirect/9b78bf09-4499-4fb4-8579-4726fe805096?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
On metaphysics, large language models, and souls. Using TinyGPT Visualizer to decode how large language models think and act…
Faster Retrieval for Better, More Efficient RAG [ https://substack.com/redirect/983c5783-9921-4abd-bede-945ddd46d752?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Maximum inner product search (MIPS) sits at the core of recommendation systems, search, and retrieval-augmented generation (RAG). Given a query vector, MIPS systems search within a database of millions of candidate key vectors for the one that best matches the query. The original data point associated with that best-matching key is then used to handle the query: in RAG, the document that is best suited to answer the question is typically prefixed to the query…In Amortizing Maximum Inner Product Search with Learned Support Functions, a paper presented at ICML 2026, researchers from Apple train small neural networks (NNs) — once, offline, for a fixed database of keys — that learn how to route queries toward their best match faster…
Is traditional research in computer vision and data science still relevant in the age of LLMs? [Reddit] [ https://substack.com/redirect/22a50c0e-15de-4696-b1f4-977d51d2b590?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Why are PhD students still doing research on tasks like image classification, segmentation, and traditional data science problems when we now have powerful LLMs and large pretrained models trained on massive datasets? These models can already achieve impressive results on many benchmarks, sometimes outperforming specialized approaches. So, what is the actual research challenge today? Are researchers still finding meaningful problems that these models cannot solve, or is the focus shifting toward improving efficiency, robustness, interpretability, and performance in specific domains?…
e-means: outperforming k-means in one-tenth the epochs [ https://substack.com/redirect/8f158cba-1b50-4717-bedc-bf483eb4f98a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I’m excited to open-source e-means: a modern, robust k-means algorithm developed at Meta FAIR. A replacement of Lloyd's algorithm, e-means delivers a ~10× speedup in both epochs and wall-clock time while achieving lower loss…
Last Week's Newsletter's 3 Most Clicked Links
Ask HN: What's your current AI agentic setup? [HN] [ https://substack.com/redirect/d4588a7c-49c9-4de9-8d5d-ac1fb410874d?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Exploratory Data Analysis Can’t Be Automated Away [ https://substack.com/redirect/39f4770f-1985-4692-8ca6-7313185ac7cf?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer [ https://substack.com/redirect/869d1170-18e5-4a86-9df4-5a337be4643c?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
* Based on unique clicks.
** You can find last week's issue #676 here [ https://substack.com/redirect/7521cde0-f444-4f4b-a408-f9b81b5fcc57?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Cutting Room Floor
Redefine Statistical Significance Part I: Sleep Trolls & Red Herrings (part 1 of 21) [ https://substack.com/redirect/27215559-9c0a-456b-9c9f-2880240d282f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
How Does Batch Normalization Help Optimization? [ https://substack.com/redirect/007a9663-fa1c-40c0-a515-4b8bae5df2c7?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Computer Networking: a Top Down Approach [ https://substack.com/redirect/55dd8377-635e-485d-92a5-85314cc56b1a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
JUMP Cell Painting chemical dataset: Morphological map of 115,796 compounds in human cells [ https://substack.com/redirect/c70478de-0d0c-4088-9a45-9c7457a339ff?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Dive into Systems [ https://substack.com/redirect/c830245a-7350-4ef3-bfa4-eb284da5acd4?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] is a free, online textbook that serves as a gentle introduction to computer systems, computer organization, and parallel computing [ https://substack.com/redirect/c830245a-7350-4ef3-bfa4-eb284da5acd4?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
Thank you for joining us this week! :)
Stay Data Science-y!
All our best,
Hannah & Sebastian
Data Science Weekly Newsletter is a reader-supported publication. To receive new posts and support our work, consider becoming a free or paid subscriber.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9kYXRhc2NpZW5jZXdlZWtseS5zdWJzdGFjay5jb20vYWN0aW9uL2Rpc2FibGVfZW1haWw_dG9rZW49ZXlKMWMyVnlYMmxrSWpveU5qa3dNVGt4TENKd2IzTjBYMmxrSWpveU1qUTJOemsyTURJc0ltbGhkQ0k2TVRjNU5EVXlPRGd3TkN3aVpYaHdJam94T0RJMk1EWTBPREEwTENKcGMzTWlPaUp3ZFdJdE1qSTJPU0lzSW5OMVlpSTZJbVJwYzJGaWJHVmZaVzFoYVd3aWZRLi1wWDZ3bkdVSUJLX0pfd0V2NE05UnRHR21za3o2MUhZUzQtV1poSU50WWsiLCJwIjoyMjQ2Nzk2MDIsInMiOjIyNjksImYiOnRydWUsInUiOjI2OTAxOTEsImlhdCI6MTc5NDUyODgwNCwiZXhwIjoyMTEwMTA0ODA0LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.oLFgsKdXViKCoYF46404lxittdsupdIcVN8NtE5124A?
