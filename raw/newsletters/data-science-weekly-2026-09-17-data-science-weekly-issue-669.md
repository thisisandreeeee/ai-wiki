---
source: gmail
newsletter: "data-science-weekly"
message_id: "1a0b184ce7613a1a"
thread_id: "1a0b184ce7613a1a"
subject: "Data Science Weekly - Issue 669"
from: "Data Science Weekly Newsletter <datascienceweekly@substack.com>"
date: "Thu, 17 Sep 2026 22:37:23 +0000"
ingested: 2026-09-21
sha256: e92083fb43440cbdaca2953f95f5fb2d5c14158095a8e7fb5a7aa6407f9bc719
---
View this post on the web at https://datascienceweekly.substack.com/p/data-science-weekly-issue-669

Issue #669
Sep 17, 2026
Hello!
Once a week, we write this email to share the links we thought were worth sharing in the Data Science, ML, AI, Data Visualization, and ML/Data Engineering worlds.
And now…let’s dive into some interesting links from this week.
Editor's Picks
Watch a 14 Byte Neural Network Solve a Maze [ https://substack.com/redirect/4d21fdc0-bee5-41ce-a0ad-7c25e2b6cc4e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
This project was/is an experiment across 47 distinct phases, initially attempting to create a 100% solve rate maze-solving neural network from scratch, then quickly realizing I’m not going to achieve that, so instead trying to solve the highest % of mazes with the most compact neural network representation…
Backups aren’t simple [ https://substack.com/redirect/9fdab17f-aca9-4ffd-a5bd-590ecf67d41d?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I read a comment somewhere that stuck with me, that went something like this: “There are two types of people: those who have suffered a catastrophic loss of data, and those who will.”…Trying to find the source for it for this blog, it turned out that every other sysadmin has his rehashed version of the quote, but the gist of it is the same everywhere. Data loss is something that happens more often than we’d hope, and most of us are woefully unprepared for when it hits us (which is almost always at the worst possible time). I can confirm that I had a similar experience once…
Sample size needed for central limit theorem to kick in [ https://substack.com/redirect/07ac84dc-76d9-4602-82ed-f538286c211f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
It takes a larger sample size than you might hope for the mean of a sample to have a distribution that’s close enough to ‘normal’ for common inference methods to work….
.
What’s on your mind
This Week’s Poll:
.
Last Week’s Poll:
.
Data Science Articles & Videos
I’ve operated petabyte-scale ClickHouse clusters for 5 years [ https://substack.com/redirect/cc149df5-2a7c-430e-b40e-e3723a492b05?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
What I learned operating ClickHouse at scale: the wins, the failures, and the lessons that only come from production experience…
1.5 years of RAG in fintech, what actually worked after screwups [Reddit] [ https://substack.com/redirect/aaafe2c4-a4e4-4924-b4c0-33d25848cdec?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
For the last ~1.5 years, we have been testing RAG in our fintech systems. Initially there were a lot of failures. Some were harmless bad answers, some were actual screwups where a confident wrong answer was much worse than saying “I don’t know.” We were retrieving from a mix of annual reports, news, internal trading strategies, risk documents, rules, research and some codebases. Tried different chunking, indexing, reranking and retrieval methods. A few things worked better than I expected…
Charts built for Chat [ https://substack.com/redirect/f5a9653b-7f03-41c4-a8d9-ebe8794d3e29?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
We’re open sourcing dbt Charts, a declarative language for dashboards, so that even the dashboards you build by chatting with an agent can be governed…
The open houses at the edge of disaster [ https://substack.com/redirect/c6723df5-51cb-49b4-a35c-52ff50848156?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
What are buyers being told about climate risk in Miami? I posed as one to find out…I’m repeating an experiment the writer Sarah Miller performed seven years ago. In 2019, she posed as a prospective homebuyer and toured several properties in Miami Beach’s most climate-threatened areas, asking realtors whether each place might one day flood, or worse, be swallowed by the rising sea…I have no intentions to match Miller’s prose (I could not if I tried). But I did want to rerun the experiment…
Your Model’s MSE Is Lying to You [ https://substack.com/redirect/2a90a264-4727-4f62-aa6d-cf24a133a839?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Imagine you have a sensor recording something you care about, for example seismic background at a detector site, electrical load on a grid, or strain in a bridge cable, and you’ve trained a model to forecast the next value. The model looks at the recent history, thinks for a moment, and gives you a single number: 0.5. There’s a threshold τ = 1.0 that fires an alarm. The question is: should you worry? You can’t answer that…Imagine you actually have two models, both watching the same signal, both predicting x^=0.5 at the same timestep. They even post the same mean squared error on your test set, not approximately, but identically to three decimal places. By every standard ranking metric, they are interchangeable. Except they're not…
Converting between cosine similarity and concentration ratio [ https://substack.com/redirect/8320fa71-6d96-4f76-be90-503697a18287?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I’ve written three posts on cosine similarity lately. The first looked at interpreting cosine similarity. The second looked at an approximation related to the first. The third looked at how ranking according to cosine similarity works better than cosine similarity itself…For this post, I wanted to share a plot of concentration ratio as a function of cosine similarity…
From BirdNET Detections to Ecological Insight: Sunny Tseng on birdnetTools 2.0 [ https://substack.com/redirect/9ba0f132-5c95-44a4-83de-b3385021474e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Sunny Tseng discusses birdnetTools 2.0, an R Consortium–funded package that turns BirdNET detections into reproducible occupancy-modeling workflows…
Neki, sharded Postgres [ https://substack.com/redirect/d5253439-7dd2-426d-8224-3ccfda7fc36c?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Neki is built from lessons we’ve learned over eight years of running some of the largest sharded MySQL clusters in the world. Thousands of production workloads with millions of queries per second for companies where even a few seconds of downtime is a very public event. We know what it means to power the world’s biggest tier 0 workloads…
Slicing in tidyomics [ https://substack.com/redirect/3be9811f-3154-4233-8daa-f80a4fcfd4e5?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
How to use dplyr-style slice operations on omics data objects in the tidyomics project…
p-hacking with Claude [ https://substack.com/redirect/b192cc80-f7c7-40c6-a4a3-63ae778f3726?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
p-hacking is a widespread problem in the literature. AI tools could make it much worse by lowering the bar on trying alternatives…That risk is firmly a reality now with tools like Claude Code. It’s easy to spin up 20 versions of statistical tests for testing the same hypothesis. Examples include comparing different test statistics or different ways of splitting a continuous variable into groups before you do your test…
Training Search Agents with GRPO [ https://substack.com/redirect/bce718e3-be98-4d4d-ae42-a2e12ef3696f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
This post is a hands-on introduction to reinforcement learning through training a search agent with group-relative policy optimization (GRPO). Search is a fun place to learn RL because it has so many levers, and each of them visibly changes how the model searches. It is also a domain where, in my experience, a well-designed reward function can influence how a model searches more effectively than system prompt changes or harness engineering….
Can a small LLM be enough for RAG? [Reddit] [ https://substack.com/redirect/f73c7fb3-ecdc-4124-b69f-3d1b9bd17f07?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
How much does the LLM itself affect the quality of the answer in a RAG system? As I understand it, RAG works roughly like this: we have vector search that retrieves the relevant information, and then we pass the retrieved chunks to the LLM. The model then generates an answer based on those chunks. In that case, it seems like the most important part is the quality of the vector search. If we give different models exactly the same information, I would expect there not to be a huge difference between something like GPT-6 Astra and a small Gemma 4 E2B. What am I missing?…
Analysing seed germination and emergence data with R [ https://substack.com/redirect/98a57fa4-9b8d-4fcc-a25f-ca2b50fe9070?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Germination and emergence assays are pretty straightforward to set up: you grab a sample of seeds, put them in a container under controlled environmental conditions (temperature, humidity, light), and check on them regularly. At each inspection, you count the germinated seeds, remove them, and keep going until the process stops. Simple, right? Well, the lab phase might be, but the data analysis is where things often get messy…A quick look at the literature reveals a wide range of analytical approaches. Some researchers use classic germination indices or non-linear regression, while others lean toward survival analysis. Having options is great for creativity, but not all methods are created equal—especially when basic statistical assumptions are ignored. More importantly: does using dozens of different statistical approaches really help science move forward? Or does it just make it harder to compare results, replicate studies, and speak the same language across research groups?…
Last Week's Newsletter's 3 Most Clicked Links
How are LLMs used in predictive modeling and anomaly detection? [Reddit] [ https://substack.com/redirect/8e2cc04f-051d-4cf4-84f1-e9256caba2b5?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I Made a Real Fly Brain Play Pong. It Didn’t Learn — And That’s the Interesting Part [ https://substack.com/redirect/3f419ac0-a2de-4d7c-89cc-bbbb8e823ad1?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Linear Regression with Gradient Descent: Mathematical Foundations of AI [ https://substack.com/redirect/62fd588e-9df3-4e27-b7b3-fed636f91a6e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
* Based on unique clicks.
** You can find last week's issue #668 here [ https://substack.com/redirect/2ff45507-3e50-4218-a852-7c2a62eae660?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Cutting Room Floor
Scalable near-real-time Bayesian phylogenetics for outbreaks with Delphy [ https://substack.com/redirect/e6a6a25a-9e3e-4cfd-ab2d-21f646b60511?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
5 Methods for Assessing Causality in Statistics [ https://substack.com/redirect/d0d3beef-d4ac-4c01-86e8-85e081f47481?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Browse code by meaning [ https://substack.com/redirect/a692e596-01c7-4cb5-b1ec-91ee50ae5ca8?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Testing low-end, affordable pens [ https://substack.com/redirect/af3bce06-a32f-4f0c-bd13-47338e991e8b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Think Harder: How I (Thorsten Ball) Prompt [ https://substack.com/redirect/557eadc6-2b2b-4c1e-991d-40b325b5cb9b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
engrim: The Universal Cross-Model & Cross-Agent Episodic Memory Standard. [ https://substack.com/redirect/44c45210-e68e-483b-ba2e-b2de8e2e654f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
PipesHub: The Open-Source Workplace AI Platform [ https://substack.com/redirect/3c9b453e-d5dd-4ad7-8105-7f8e50efef23?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
Thank you for joining us this week! :)
Stay Data Science-y!
All our best,
Hannah & Sebastian
Data Science Weekly Newsletter is a reader-supported publication. To receive new posts and support our work, consider becoming a free or paid subscriber.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9kYXRhc2NpZW5jZXdlZWtseS5zdWJzdGFjay5jb20vYWN0aW9uL2Rpc2FibGVfZW1haWw_dG9rZW49ZXlKMWMyVnlYMmxrSWpveU5qa3dNVGt4TENKd2IzTjBYMmxrSWpveU1UWXlNakkwTVRBc0ltbGhkQ0k2TVRjNE9UWTRORFkyTlN3aVpYaHdJam94T0RJeE1qSXdOalkxTENKcGMzTWlPaUp3ZFdJdE1qSTJPU0lzSW5OMVlpSTZJbVJwYzJGaWJHVmZaVzFoYVd3aWZRLkxLUmtrRk9CMzlvNXM0S3JtejVTVGhFM2JzLTl3NVpUZmljRDlvMzdjYnciLCJwIjoyMTYyMjI0MTAsInMiOjIyNjksImYiOnRydWUsInUiOjI2OTAxOTEsImlhdCI6MTc4OTY4NDY2NSwiZXhwIjoyMTA1MjYwNjY1LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.Qz8fcn_fegc5LxJ8im1hrbMm2azwk5BJZujeQtyDVbE?
