---
source: gmail
newsletter: "data-science-weekly"
message_id: "1a18a09d1fcef130"
thread_id: "1a18a09d1fcef130"
subject: "Data Science Weekly - Issue 675"
from: "Data Science Weekly Newsletter <datascienceweekly@substack.com>"
date: "Thu, 29 Oct 2026 23:40:40 +0000"
ingested: 2026-11-02
sha256: 1f42cda4d18ba10fb7a7f4d965c3a12721e55e3f14008d7ede8f36a9f5a619b1
---
View this post on the web at https://datascienceweekly.substack.com/p/data-science-weekly-issue-675

Issue #675
Oct 29, 2026
Hello!
Every week, we write this email to share links we think are worth sharing in the Data Science, ML, AI, Data Visualization, and ML/Data Engineering worlds.
Now…let’s dive into this week's interesting links.
Editor's Picks
Life with hazard ratios [ https://substack.com/redirect/9a5c0c88-7c70-4a52-be9d-da2823464df2?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
If you read anything about health or longevity, you’ll soon find yourself in a world of hazard ratios. Some study might say that eating more fiber might change your risk of dying by a factor of HR = 0.90. Another might say that occasional smoking might change it by HR = 1.30…But how much should you care about that? Is HR = 0.90 or HR = 1.30 a lot? What if you don’t want to eat more fiber? What if you like smoking?…
When Do Causal ML Models Beat LM / GLM / GBM? [ https://substack.com/redirect/2abaf8e6-9d82-46fe-805f-e406295a5f2e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Nine simulated toy cases with a known true effect: A simulation study with nine toy cases and a known true effect: when do causal forests, Double ML, AIPW and meta-learners beat plain LM, GLM and GBM, and how can you tell without knowing the truth?…
AI Promised Less Work. I Have Never Worked More. [ https://substack.com/redirect/2d3fae35-434e-4c5e-8bd0-e37fac38eb63?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The pitch was that AI would give us our time back. Write less boilerplate, delegate the boring parts, go home earlier. I am not complaining about the tools. I use agents for all of my engineering work now, and I wrote about how that setup evolved and why I still read the code. I can investigate and ship things that would not have been worth starting two years ago. But somewhere this year I noticed that I am working more than I ever have, and that it feels heavier than it used to. Not because any single task is harder. Because there are so many more of them, all at once. This post is me trying to understand that, with some data from my own GitHub history…
.
What’s on your mind
This Week’s Poll:
Last Week’s Poll:
.
Data Science Articles & Videos
Battles and space-filling curves [ https://substack.com/redirect/35405e1d-429c-4a20-93b5-7ede28974a01?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I recently learned about an interesting way of reducing the dimension of a data set. I’d like to illustrate it with a data set of about 550 historical battles in the UK, extracted from Wikidata using a SPARQL query…One way to visualise battles over time is to make a 2D graph with time on one axis and location on another axis. But how do you plot a 2D location on a 1D line? One answer is to use a space-filling curve, which in this case will be a curve which snakes all over the map, visiting every location once. This won’t necessarily preserve the relationship between points (points which are close together in 2D could be far apart in 1D) but at least points which are close together in 1D are guaranteed to be close together in 2D. One example of a space-filling curve is the Hilbert curve…
Screwed up a model in production, feeling super anxious [Reddit] [ https://substack.com/redirect/65416d18-d2f9-4223-9a58-1e0120cc8576?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I’m a junior data scientist and I have 1 yoe at a medium sized company. Recently my job has made me so anxious I cannot even sleep. Basically, I deployed a model for the first time, and I cited great improvements, but due to holes in my QA, the QA person did not find that the model actually improved that much in production. Im already anxious enough, but my manager made me even more anxious. He got pretty pissed that this happened…
A (lukewarm) defense of Minsky and Papert: On paradigm shifts in the history of AI [ https://substack.com/redirect/0eef352b-7a1b-4cb4-a845-602c533f3028?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
In the history of AI as told in “Introduction to Neural Networks”-kind of courses, Minsky and Papert usually play the villains. The story goes that Frank Rosenblatt’s first training of a Perceptron in 1957 generated quite the enthusiasm about AI’s possibilities, with large public and private capital investments and increased research interest. But this changed after Minsky and Papert’s publication of their book Perceptrons in 1969, which supposedly caused the first AI winter, a period when neural network research stalled because of reduced interest and funding. I want to challenge this view by showing how the type of AI they opposed was already faltering because of its own theoretical limitations, and interest in neural networks had already declined by the time Perceptrons came out…
Growing trees [ https://substack.com/redirect/c09b52f5-65b5-401d-bdb5-1fc3e1c3a7f3?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I’ve been playing with procedural tree growth recently. The method I am using is based on Self-organizing tree models for image synthesis, by Palubicki et al. (SIGGRAPH 2009). The idea is beautifully simple: buds compete for light, the tree distributes a growth resource among them, and the successful ones produce new shoots. Those shoots change the light available for the next round. The crown shape emerges from this feedback loop. Here is a quick breakdown, with some visualizations from my implementation…
We studied 1,584 data centers – and found the buildings full of machines are tied to modest local job growth [ https://substack.com/redirect/23fe053c-18c7-4881-b71c-123d913a8cf5?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
We are professors who study real estate and urban economics, including how large place-based investments shape local economies. So we set out to answer a question at the center of these fights: Do data centers actually create jobs where they are built? To find out, we teamed up with four colleagues to study what happens to local employment after data centers open. We found that new data centers that opened from 2000-2023 created 1,000 to 1,300 jobs in the counties where they are located, on average. But those jobs, which are for work performed outside data centers rather than inside them, take a few years to appear…
H.264 is Magic [ https://substack.com/redirect/27246a77-5f3c-47f1-b9c4-b5e6a5409a07?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
H.264 is a video compression codec standard. It is ubiquitous - internet video, Blu-ray, phones, security cameras, drones, everything. Everything uses H.264 now. H.264 is a remarkable piece of technology. It is the result of 30+ years of work with one single goal: To reduce the bandwidth required for transmission of full-motion video. Technically, it is very interesting. This post will give insight into some of the details at a high level - I hope to not bore you too much with the intricacies. Also note that many of the concepts explained here apply to video compression in general, and not just H.264….
Much Ado About None: Sentinel Values in Python [ https://substack.com/redirect/ba7a56d2-347c-473f-bf7a-6a755d9f98d1?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
None is probably the most overloaded value in Python. We use it as a Swiss Army knife to express that something is missing, unset, that an error occurred, or simply as an actual value. In my talk about sentinel values, which I presented this year at PyConDE/PyData Berlin 2026, EuroPython 2026 and, most recently, the Swiss Python Summit 2026, I take a closer look at why this ambiguity bites us and what to use instead…
A Primer for Earth Data Embeddings [ https://substack.com/redirect/91748e6d-170d-4d93-982f-1147263eba2b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Embeddings are one way we make use of the rich representations learned by geospatial foundation models, supporting everything from search and retrieval to natural language interfaces. Yet for many practitioners, the concept remains opaque. This primer explores how embeddings are generated, the kinds of questions they help answer, and why they’re useful across the geospatial ecosystem…
Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation [ https://substack.com/redirect/cf70c6be-97ca-4ace-af89-f97d05756391?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Diffusion language models (DLMs) offer parallel sampling for faster generation than autoregressive models, an increasingly important advantage as inference becomes a dominant computational workload. However, DLMs degrade quickly with fewer sampling steps, process the full sequence at every step, and require many passes over the dataset to reach good quality. We introduce Next-Concept Modeling (NCM), a two-stage, coarse-to-fine framework: a multiscale residual VQ-VAE encodes text into a hierarchy of discrete codes, and a transformer generates one level at a time, predicting all codes within a level in parallel…
Twelve years of distributed SQLite [ https://substack.com/redirect/e0c54801-5c59-44df-a80b-0aba68155335?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
In September 2014 I published a short post announcing rqlite. The idea was simple: take SQLite, put a Raft log in front of it, and replicate every write to a cluster so that the loss of a node did not mean the loss of the data. The source went on GitHub that same weekend. As far as I can tell, that was the first open-source system to combine Raft and SQLite. Nobody else was doing it, and for several years nobody else tried. Today “distributed SQLite” is a category with a dozen projects in it, a few of them venture-funded, two of them acquired. Since the people now writing about the category tend to start the story around 2021, I thought I should write down the version that starts in 2014. I was there for all of it…
There’s No Such Thing as Society in the Objective Function [ https://substack.com/redirect/b3fb90f1-ecf7-40d7-b364-d4f33fc96f82?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Governments, like the rest of us, optimise the number in front of them. I followed the formulas behind Britain’s bills, rivers and public services. Here’s what they leave out and how to fix it…
Here Be Monsters: What Do You Still Need to Know When Agents Do the Work? [ https://substack.com/redirect/b2577187-5d8d-47d5-8307-16ccdd72357a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The traditional wisdom is that in order to develop and maintain a non-trivial system you need to have a proper working model of it. I think few people would argue with that. And in software engineering you would acquire that working model by working directly with the code…In order to figure out a viable path for achieving some measure of mastery, we have to look at what it means to own a non-trivial software system. If you think about your typical architect/lead/CTO and how they operate, it becomes clear that to be successful they need to have a model of the system in their head, a chart of the waters. The real question is at what level of granularity?…
Where should my family meet? [ https://substack.com/redirect/1cdd5e75-1067-40fe-9944-9343bbae84fd?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Like many others, my family is quite split geographically: some are in Europe but in different countries, and some are in other continents. Given this distance between us, we don’t gather in a single place that often. This got me thinking: in which place should we meet if we wanted to minimize the total distance, i.e the sum of the distances made by each one?…This question is frequent in a lot of optimal location problems. For example, where should a factory be built so that it minimizes the sum of distances to a list of warehouses?…I thought a bit more about that, searched online, asked to other members of my family more comfortable with maths, and this blog post summarizes what I learnt from that…
Last Week's Newsletter's 3 Most Clicked Links
Ask HN: How to deal with shipping AI-written code you don't understand? [ https://substack.com/redirect/546dec27-2ff5-4106-9d3a-4142e00a41af?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Everyone at my company can hook Claude up to source systems and build their own dashboards. Anyone dealt with this as an analytics team? [Reddit] [ https://substack.com/redirect/269c5db1-4ff2-4928-b7f6-8e9839d1d14e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Diplomatic Ways to Critique AI Slop [ https://substack.com/redirect/88320722-d67e-48a1-8498-ccbc55502525?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
* Based on unique clicks.
** You can find last week's issue #674 here [ https://substack.com/redirect/3e498630-50df-4e78-b8ba-1875bda5d8b3?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Cutting Room Floor
Bayes Theorem, the Geometry of Changing Beliefs: The 3Blue1Brown Demonstration as Another Interactive App [ https://substack.com/redirect/2d31bf5a-fa52-4111-a2ef-ae138433660e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Longitudinal data and conditioning [ https://substack.com/redirect/f4e84240-9aa9-4815-82a5-ceb9f24c2a88?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Characteristic NYC Neighborhood Complaints [ https://substack.com/redirect/98df4fb7-3333-495b-932c-d240b7009b0c?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The Probability Playground: 5,138,680 Simple Exercises on Probability Theory [ https://substack.com/redirect/4e78dd9d-2162-4ecf-874a-ce329cea74c1?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Some notes about improving base R code [ https://substack.com/redirect/0136bf5c-0c50-4c6a-b80b-394ec6088d6e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Local Wikipedia - Local Wikipedia is Wikipedia, but only for things a half hour walk from you [ https://substack.com/redirect/db85554b-df27-4b04-9816-1d56e7d75f4b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Make Your Own LLM Agent in R [ https://substack.com/redirect/b3c77a5b-6957-46d3-b5c9-4631e15cb8e8?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The future of scholarly books [ https://substack.com/redirect/9e468649-462e-4eb6-8d97-0b1557a98eef?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
Thank you for joining us this week! :)
Stay Data Science-y!
All our best,
Hannah & Sebastian
Data Science Weekly Newsletter is a reader-supported publication. To receive new posts and support our work, consider becoming a free or paid subscriber.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9kYXRhc2NpZW5jZXdlZWtseS5zdWJzdGFjay5jb20vYWN0aW9uL2Rpc2FibGVfZW1haWw_dG9rZW49ZXlKMWMyVnlYMmxrSWpveU5qa3dNVGt4TENKd2IzTjBYMmxrSWpveU1qSTJOamd6Tmpnc0ltbGhkQ0k2TVRjNU16TXhOekkyTVN3aVpYaHdJam94T0RJME9EVXpNall4TENKcGMzTWlPaUp3ZFdJdE1qSTJPU0lzSW5OMVlpSTZJbVJwYzJGaWJHVmZaVzFoYVd3aWZRLnNwSTFLX3BBY0dfaEF0NlBfdTRoMnRYbmtOS2FNLThZZHV1dERaQzhpYXciLCJwIjoyMjI2NjgzNjgsInMiOjIyNjksImYiOnRydWUsInUiOjI2OTAxOTEsImlhdCI6MTc5MzMxNzI2MSwiZXhwIjoyMTA4ODkzMjYxLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.1ayzxGCj2dMxm_4n00HNGHnjMpJPTI3U2SKXZ1eHO1Q?
