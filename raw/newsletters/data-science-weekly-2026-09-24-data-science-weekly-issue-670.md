---
source: gmail
newsletter: "data-science-weekly"
message_id: "1a0d3777bf30dcd6"
thread_id: "1a0d3777bf30dcd6"
subject: "Data Science Weekly - Issue 670"
from: "Data Science Weekly Newsletter <datascienceweekly@substack.com>"
date: "Thu, 24 Sep 2026 12:49:24 +0000"
ingested: 2026-09-28
sha256: 63ff7aba106fb020965762f1465abadd20c6b64f0dd8698d4971480e2e449e3b
---
View this post on the web at https://datascienceweekly.substack.com/p/data-science-weekly-issue-670

Issue #670
Sep 24, 2026
Hello!
Once a week, we write this email to share the links we thought were worth sharing in the Data Science, ML, AI, Data Visualization, and ML/Data Engineering worlds.
And now…let’s dive into some interesting links from this week.
Editor's Picks
An Interactive Introduction to Fourier Transforms [ https://substack.com/redirect/5d846420-948c-4966-94f9-e697569bf9bc?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Fourier transforms are a tool used in a whole bunch of different things. This is an explanation of what a Fourier transform does, and some different ways it can be useful. And how you can make pretty things with it, like this thing: I’m going to explain how that animation works, and along the way explain Fourier transforms! By the end, you should have a good idea about: a) what a Fourier transform does; b) some practical uses of Fourier transforms; and c) some pointless but cool uses of Fourier transforms. We’re going to leave the mathematics and equations out of it for now. There’s a bunch of interesting maths behind it, but it’s better to start with what it actually does, and why you’d want to use it first. If you want to know more about the how, there’s some further reading suggestions below!…
Can gzip be a language model? [ https://substack.com/redirect/6680fddc-336b-4373-a6cd-2864be6d8586?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
A while back I wrote about language modeling without neural networks, where I generated Shakespeare with an unbounded n-gram model: no weights, no training, just counting. Fortuitously, I came across the paper Language Modeling is Compression, which mentioned the compression–prediction equivalence: “every prediction model is inherently a compressor, and all compression algorithms are prediction models”. This led to the natural question: can gzip do language modeling?…
Why fitting a logistic is nearly impossible from early data [ https://substack.com/redirect/e2bccc51-33d2-492f-a3a5-58beb14f992e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Nothing grows exponentially forever. What appears to be an exponential curve often turns out to be some sort of S curve, such as a logistic curve…Suppose you’re collecting data on the left side of the curve. If there’s even a small amount of error in your data, you won’t be able to predict the asymptotic value with any accuracy. But if you have data on both sides of the inflection point, you can make a good prediction of the limiting value. I’ve written about this before, explaining that the problem is hard, but I didn’t say why it’s hard. Here I’d like to give an idea why it’s hard…
.
What’s on your mind
This Week’s Poll:
.
Last Week’s Poll:
.
Data Science Articles & Videos
Data Science in the Age of AI [ https://substack.com/redirect/e87337aa-01fe-4f1f-94ba-5456c609ca40?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Data scientists apply the best tools and technology to maximise the value of data. I’ve been in the profession for over a decade, and in retrospect it’s surprising how slowly things changed over most of that period. The tools evolved, but ultimately my day-to-day work looked similar in 2013 and 2023. The rise of LLMs has been the biggest shakeup to the profession that I have experienced. The work has changed radically. I used to spend most of my time programming, but in the last year I’ve barely written a single line of code…
Those who have gotten a new job in the last 6 months - 1 year, how’s it going? [Reddit] [ https://substack.com/redirect/fcc6d1e5-1726-4546-b2b6-2b905d78d3c2?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Those who have changed roles, how has it gone for you? Interested in hearing from folks who’ve moved into the tech industry specifically…
Making Plot Sketchy [ https://substack.com/redirect/cfc369a0-16a5-4774-bc41-4177f309c04f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Way back in 2010, I created a plugin for Processing called handy that allowed it to render in a sketchy hand-drawn style. This formed part of some research into the effects of sketchy styling on people’s understanding of data visualization (Wood et al., 2012). Handy was subsequently ported to JavaScript and extended by Preet Shihn as Rough.js. This page describes a plugin for Observable Plot that allows high level Plot specifications to render in Rough.js sketchy style with minimal additional specification details. It builds on Gordon Tu’s plugin approach but with greater Plot coverage and some bug-fixes…
Make the Invisible Tangible: Turning Time Gaps into Distance [ https://substack.com/redirect/2445700e-274b-42f8-a814-eb46800f48ce?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
At the 2026 Hungarian Grand Prix, Lewis Hamilton qualified second, 0.012 seconds behind pole. On the broadcast, that flashes up as “+0.012s,” and then it’s gone. Do you feel anything? I don’t. I can’t picture 12 thousandths of a second, and neither can you, because nobody has a sense for it. So let me tell you the same fact a different way. Hamilton was 1.1 metres behind. About a car’s nose. Now it’s real. You can see the two cars almost level, one just edging the other over the line. Nothing about the fact changed. Only the unit did. That distance between a number and a feeling is one of the most common problems I encounter in data visualisation, and it has a pleasingly simple fix. When a quantity won’t land, stop trying to make it more precise and start translating it into something the reader’s body already understands. Usually, that something is distance…
English: a vs an [ https://substack.com/redirect/8e64eda0-0ec7-41af-ab6c-77c27c3829d4?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
n English, there is an “indefinite” article a that can go before a word. For example, a raccoon. But for some words, we use an. For example, an apple.
When procedurally generating text, I want a function a_or_an("apple") that tells me which article to use. That seems like it’d be easy. We can check the first letter to see if it’s a vowel. But that would mean we output an unicorn, not a unicorn…I was curious how often these exceptions occurred, and whether they can be grouped together, so I spent a day looking at the data and building some visualizations and wrote up the results. I was surprised that only 129 of the 32,455 words in my list needed exceptions…
A study of sequence weighting at scale [ https://substack.com/redirect/dd868f3f-053b-4bd1-99d9-e11e60d511a5?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
We study the scaling laws of data weighting across in-house and open-weight LMs, finding non-monotonic behavior across scales. We vary the weight assigned to sequences during training and measure how strongly the model’s loss reduction on a sequence depends on the sequence’s weight. Taken together, our results are consistent with a general trend: as models transition from small to medium scale, they transition from learning general patterns independent of data weight to learning data-specific patterns proportional to the data weights. As models then transition from medium to large scale they are able to learn all patterns present in the data, once again independent of data weight…
From Words to Vectors: What Happens in Between? [ https://substack.com/redirect/ef32b049-a4a4-4b64-b89b-7b0963543318?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
A Journey through TF-IDF, vector space, and text classification…
mnemiq: text-to-SQL you can tune to your database [ https://substack.com/redirect/a5281655-9db0-4be3-9c3c-be1568e03893?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Text-to-SQL vendors publish accuracy numbers, but those numbers do not transfer across databases. They tell you little about how a system will perform on your data — and when it underperforms, the black box gives you little ability to understand why or fix it. We built mnemiq, an open-source text-to-SQL engine that opens up that black box. You can change the model, retrieval, semantic layer, verifier, and other parts of the pipeline, then benchmark those choices on your own database…
GPUs: Rent vs Buy [ https://substack.com/redirect/caa6e170-ef03-4f76-90f8-b47f93e94e04?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
GPU prices have been going up. At the same time, smaller LLMs have become much more powerful, making local inference accessible on less capable hardware. This article lays out the trade-offs between renting and buying hardware (mostly GPUs) for LLM inference…This article will cover hardware with a total cost of up to $20k, with most setups under consideration in the $4k-$12k range. That enables running open models up to around 300B parameters…
Bootstrap v traditional asymptotic normal assumptions [ https://substack.com/redirect/55514d8d-fd8d-4e8b-bb2f-6dc9c1a44140?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Bias-corrected and adjusted bootstrap does an ok job at confidence intervals of the mean from some example skewed distributions. Better than does relying on the traditional methods of just assuming normality from the central limit theorem. But for particularly awkward distributions, sample sizes are still needed in the thousands to get coverage that resembles the claimed coverage…
An Agentic Data Science Story [ https://substack.com/redirect/2a72c0a4-614e-4182-8494-23651d3341f5?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
For a recent collaboration with AIBM, I found myself working with data from the National Survey of Family Growth (NSFG), which I used in several examples in Think Stats. I was reminded of the technical debt I have accumulated while working with this data, and the dread I feel getting back to it. So I decided to make it a case study in agentic data science. I asked Claude Code to take inventory of the repository, reorganize it, and rebuild the analysis pipeline. Then I asked it to generate a blog post about the process, which is what follows, with my revisions…
FlexViz: 1 billion data points, interactive exploration, in 0.25s [ https://substack.com/redirect/7a828df7-8e2a-4508-8706-7231608c5fd0?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
FlexViz is a visualization library for exploring datasets that are too big for conventional Python dashboarding tools. Charts stay interactive (zoom, pan, cross-filter) at 100M+ rows because every interaction is answered by lazy Polars aggregations and Rust kernels instead of by shipping raw data to the browser. The same engine serves a coding agent: it builds the dashboard, hands you the URL, and reads back what you zoomed and brushed. You explore the data together, and neither of you loads it…
The last mile of a long road: faster NumPy in the browser [ https://substack.com/redirect/1a6de9ee-095a-4469-9127-88703e70e317?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
For a long time, running NumPy in the browser meant running it without an accelerated BLAS. Matrix multiplications fell back to plain loops (portable, but blind to cache and SIMD). That just changed. The Emscripten-forge NumPy package now links OpenBLAS in WebAssembly, and at n = 1024 square np.matmul jumps to about 30.92× faster (float32) and 14.90× faster (float64). The next OpenBLAS release, already available as an experimental package on Emscripten-forge, with kernels contributed by QuantStack, pushes it further, and an optional Relaxed SIMD build adds another step on engines that support it…
Last Week's Newsletter's 3 Most Clicked Links
1.5 years of RAG in fintech, what actually worked after screwups [ https://substack.com/redirect/54a72122-3557-415d-9eaf-0105c54661f7?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Sample size needed for central limit theorem to kick in [ https://substack.com/redirect/1519143f-65a1-43d3-8311-4a77a143e267?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Watch a 14 Byte Neural Network Solve a Maze [ https://substack.com/redirect/101ef82f-2fe9-4441-93f5-4092788198ad?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
* Based on unique clicks.
** You can find last week's issue #669 here [ https://substack.com/redirect/558e4e09-2487-414b-8a2e-62a88e4f30c0?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Cutting Room Floor
Are carrots becoming less nutritious? [ https://substack.com/redirect/24b6fc63-baed-46b7-91c1-a513436549d3?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
3 EDA Problems to Catch Before Fitting a Regression Model [ https://substack.com/redirect/25757aab-7100-4461-8986-9c83bba0e5b6?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Transformers Explained Visually [ https://substack.com/redirect/69f73fed-981e-4755-8d2a-afbe75c7412d?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
A data scientist walks into a GxP conference [ https://substack.com/redirect/847671e1-f333-459e-8466-d04239511126?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Relationship matrices without the matrix: fast pedigree computation in R with visPedigree [ https://substack.com/redirect/68b1686c-cbd5-4df1-9238-e8e742029952?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
RAM: the forgotten history [ https://substack.com/redirect/11c5e90b-d2c8-44e3-8d8e-ba79d1db4e32?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Faster JSON parsing with SVE2 on ARM processors [ https://substack.com/redirect/3680bbe9-62d9-449c-a27e-72eb33893233?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
Thank you for joining us this week! :)
Stay Data Science-y!
All our best,
Hannah & Sebastian
Data Science Weekly Newsletter is a reader-supported publication. To receive new posts and support our work, consider becoming a free or paid subscriber.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9kYXRhc2NpZW5jZXdlZWtseS5zdWJzdGFjay5jb20vYWN0aW9uL2Rpc2FibGVfZW1haWw_dG9rZW49ZXlKMWMyVnlYMmxrSWpveU5qa3dNVGt4TENKd2IzTjBYMmxrSWpveU1UY3lNamc1TWpFc0ltbGhkQ0k2TVRjNU1ESTFOREl4Tml3aVpYaHdJam94T0RJeE56a3dNakUyTENKcGMzTWlPaUp3ZFdJdE1qSTJPU0lzSW5OMVlpSTZJbVJwYzJGaWJHVmZaVzFoYVd3aWZRLkJJaUxlUlFBUzNaVEc5MVZfcUdtSU03NFlfNzhUUHoyRVI5cTRtRVNEZ00iLCJwIjoyMTcyMjg5MjEsInMiOjIyNjksImYiOnRydWUsInUiOjI2OTAxOTEsImlhdCI6MTc5MDI1NDIxNiwiZXhwIjoyMTA1ODMwMjE2LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.hOPs9n6WDWCWfSTkAX8iVzMm6lDFiTHeWtwC7QOjHKM?
