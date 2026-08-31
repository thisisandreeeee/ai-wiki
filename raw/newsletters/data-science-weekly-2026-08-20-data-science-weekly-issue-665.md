---
source: gmail
newsletter: "data-science-weekly"
message_id: "1a02161d68a2aa00"
thread_id: "1a02161d68a2aa00"
subject: "Data Science Weekly - Issue 665"
from: "Data Science Weekly Newsletter <datascienceweekly@substack.com>"
date: "Thu, 20 Aug 2026 22:53:50 +0000"
ingested: 2026-08-31
sha256: 84e29290138bcdccf37478e25a0e4a06fa0002b4e83b7f68292b3f19a237cb9c
---
View this post on the web at https://datascienceweekly.substack.com/p/data-science-weekly-issue-665

Issue #665
Aug 20, 2026
Hello!
Once a week, we write this email to share the links we thought were worth sharing in the Data Science, ML, AI, Data Visualization, and ML/Data Engineering worlds.
And now…let’s dive into some interesting links from this week.
Editor's Picks
Geolocating Random Islet Image Using Geometry & CUDA GPU Programming [ https://substack.com/redirect/ca1a1947-8826-4496-8790-1d95c60a0105?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
This is a photo of a resort located on an island":
a) What is the name of the resort?
b) What are the coordinates of the island?
c) In which cardinal direction was the camera facing when the photo was taken?
In my opinion, solving this challenge with Google Lens is wasting a fun opportunity, so I decided to solve it with math and programming…
Improving heuristics for A* search [ https://substack.com/redirect/59b40b24-4d0c-4e1f-aa10-35cb70d9beb4?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
On my Introduction to A* page I cover the basics of the A* graph search algorithm for finding shortest paths…On this page I’ll show a way to speed up A* by adding “landmark nodes”….At the end of the page are demos of how this technique helps with maps from real games. I use grids for the visualizations on this page, but landmarks work for any type of graph, not only grids. The best part is that it’s not much code, sometimes only 20 lines. It can be combined with most other optimizations…
Everything after training [ https://substack.com/redirect/62a159a1-69a4-411f-b081-ea0d230c1f0c?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Training teaches a model what it knows. Inference is everything that happens afterward, every time somebody uses it, and it is where the bill actually lands. Serving a generative model well means working across a strange range of the stack: attention kernels at one end, GPU procurement across three clouds at the other. This is an interactive companion to Inference Engineering by Philip Kiely. It follows the book’s structure and covers the same ground, with the explanations rewritten and simulators built for the parts that are easier to understand by turning a dial than by reading a paragraph…
.
What’s on your mind
This Week’s Poll:
.
Last Week’s Poll:
.
Data Science Articles & Videos
Git at any scale [ https://substack.com/redirect/99a20de5-61d5-4fd3-bac2-e3ea7edb20a7?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The challenge in hosting Git repositories at scale is inherent in the design of Git itself: a distributed version control system means that all instances of a repository are identical. There’s nothing special about the repository on a Git server that doesn’t apply to a repository on a developer’s laptop. Although at first it may appear that this makes hosting Git repositories straightforward (simply put an HTTP daemon in front of an on-disk copy of a repository and you’ve got a Git server going!), there are many hard scalability and reliability challenges that make this quite the opposite…
What’s the most counterintuitive statistical fact that’s actually true? [Reddit] [ https://substack.com/redirect/0c1da333-faf0-4d76-9e62-c8ef5f4143b8?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I’m looking for examples that completely changed the way you think about probability, statistics, or data analysis…
Harnesses are Situated Agents [ https://substack.com/redirect/ce2f1cbd-dabf-4b12-8797-b29f53bdc3f9?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Harrison Chase once excitedly shared an insight that agents are comprised of 4 things: a system prompt, a planning tool, a file system, and subagents. In the year-plus since he said that, I think this remains largely true. (Though you might tweak it to have general tools, etc.) Lately, we’ve been experiencing a wave of harnesses. It seems like everyday a new coding harness lands. I’m sure we’ll see another few dozen before the month is out…We’ve seen enough at this point that the common patterns are starting to emerge. Each brings something unique, but they’re more alike than different. And that’s great, because that lets us find the metapattern here. Which brings us back to “situated agents.”…
Learning MegaGem, from self-play to price discovery [ https://substack.com/redirect/202f208c-5f4d-4723-814e-81fb46c832f6?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
We study MegaGem, a three-player, general-sum, imperfect-information auction game developed by Jane Street, and train a 4B specialist to play it…MegaGem combines three familiar strategic games. In Figgie, each player observes only part of the supply and must infer fair value from what others are willing to pay and what is revealed over time. In Splendor, public objectives create races while players also need to think about improving their own position, preserving flexibility, and blocking opponents. In poker, hidden hands and previous actions incentivize opponent modeling while position and stack sizes determine which late-game outcomes can still be forced. MegaGem further adds repeated sealed-bid auctions…
No, local models will not win [ https://substack.com/redirect/c09dbe61-3829-4f41-99ff-c1f5e3afc7d0?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Every time a new open-weight AI model is released, people say that local models are the future. Why spend billions of dollars building out datacenters when everyone will just be able to run AI models on their laptops or phones? I think this idea is doomed. No matter how strong open-weight models get, most inference will always happen in AI datacenters….
What Is Reasoning [ https://substack.com/redirect/f9c9c7c7-fc99-43d6-909d-da8a5eb0b3f7?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
A few weeks ago a paper was shared that showed how to extract reasoning traces from closed-weight models. Together with online discussions about tricking models into leaking them, it made me investigate it more out of curiosity. Twitter seems full of half-truths and confusion about how this works, so perhaps this helps some to understand what is happening…
2026: The Year of Dataflow [ https://substack.com/redirect/173ee68a-210e-494d-ab6f-59571de17a8c?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
FlashAttention. Megakernels. Boardfly TPU. Taalas. Extreme co-design. The biggest hardware progressions of the last few years are all converging on dataflow…Deep learning gave hardware an unusually regular workload: large tensor operations, known dependencies, repeated layers, and enough reuse to justify specialized hardware and expensive compilation…Inference pushes this further. The same model may execute billions of times, while latency increasingly depends on where weights and KV cache live, how activations move between stages, and whether communication can overlap with computation. Once those costs matter, optimizing each operation independently is no longer enough. The producer-consumer edges have to stay visible: which operation produces a value, where that value lives, how it moves, and when the consumer can run. That is the version of dataflow this series is about. The clearest way to see it is to watch one algorithm get rewritten around a single boundary…
StanCon 2026 - International Conference on Bayesian Inference and Probabilistic Programming, Conference Videos [ https://substack.com/redirect/c2befed1-c59e-4cca-9837-d0454addcfb1?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Welcome to Uppsala and StanCon 2026. Join us for an exciting week with conference presentations, tutorials and workshops focused on Bayesian modelling and probabilistic programming with Stan. Stan is a Bayesian inference software that is used in both academia and industry for a broad range of applications including pharmacometrics, political sciences, epidemiology, astrophysics, advertising, and more. The conference brings together both veteran and novice Stan users, and serves as a focused event to discuss practical deployment and application of Bayesian modeling…
Protocol-Aware Deterministic Simulation Testing [ https://substack.com/redirect/f7cfe3c1-11e5-43b3-ac70-08c05882beea?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
In this post, we cover the mechanics, method, and merits of going beyond traditional, black-box methods of testing distributed systems – generative testing (for example, Jepsen), and deterministic hypervisors (for example, Antithesis) – to deeply test safety and liveness invariants using protocol-aware DST. If you prefer, watch a talk in which I cover this and more….
Why ACF Is More Than Just a Plot [ https://substack.com/redirect/13375175-fa38-4c92-baa9-96ef646f5377?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Two observations can have the same units, come from the same source, and still require a different kind of reasoning simply because one was recorded before the other….That is the defining feature of time series data: order carries information.
In an ordinary dataset, we often study the correlation between two different variables. In a time series, we can ask a different question: is the series related to an earlier version of itself? The autocorrelation function, or ACF, asks that question repeatedly—one delay at a time…This article revolves around one central question: “What does the ACF actually tell us about how a time series remembers its past?”…
Which Data Repository Should You Use? [ https://substack.com/redirect/8011f06e-d646-4eb5-b828-e4ebd5a779bf?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The Center for Open Science has announced that from November 16, 2026, no new projects can be created on the Open Science Framework. After February 19 all projects will become read-only, and eventually, they anticipate that all private projects will be deleted…Choosing a New Data Repository There are many data repositories, each with their own strengths and weaknesses. Before I compare them, I want to make it clear that the fact that organizations are willing to store your data for free for a very long time is an amazing service. You should be incredibly grateful that any and all of these services exist. As someone who had a free Hotmail email account in 1997 with 2 mb of free storage, the fact that we can now store up to 50GB for every project we create in a data repository blows my mind. Some common data repositories used in psychology are Zenodo, GitHub, ResearchBox, Dataverse, and PsyArchives. I will compare these services on properties that I think are important…
What statistical concepts are commonly misunderstood by the general public? [Reddit] [ https://substack.com/redirect/a6011662-5929-4986-8d5a-f9856d378f3c?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I came across this post explaining what a 70% chance of rain means. I understand the concept, but it got me wondering: what other statistical concepts sound simple but are commonly misunderstood or misinterpreted by the general public?…
Numba in the Browser: Unlocking a New Scientific Python Stack in JupyterLite [ https://substack.com/redirect/b153f75e-3aca-413f-ad25-84e6c27a5c9b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Traditionally, every  notebook requires a Python process running on a server or on the user’s machine. JupyterLite changes this model. Its kernels run locally in the Web browser through WebAssembly, so a static website can provide a complete computational environment without allocating a server to every user. This makes notebooks easier and cheaper to share at scale, whether they are used for documentation, education, or interactive demonstrations. There has, however, been an important piece missing from the browser-based scientific Python ecosystem: Numba. Today, we are excited to share the first working version of the Numba JIT compiler running entirely in the browser with JupyterLite and emscripten-forge!…
Last Week's Newsletter's 3 Most Clicked Links
Eval-driven development: Lessons from evaluating GenAI at scale [ https://substack.com/redirect/14662762-b1aa-451a-b015-6b086c3d7d7e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
City2Graph: Geospatial Graphs for Network Analysis and GNNs [ https://substack.com/redirect/3ea678e5-5d28-48c6-9cfb-b3cf2b98d9f2?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Compression is prediction [ https://substack.com/redirect/ef9586ce-9b5d-460f-aad7-a731198a3473?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
* Based on unique clicks.
** You can find last week's issue #664 here [ https://substack.com/redirect/d9917c53-23f3-48c3-aa31-6c3d7b9a9d5f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Cutting Room Floor
The Shapes of Agent Memory – Files, Stores, and Experience [ https://substack.com/redirect/225be405-a334-4e08-ba70-acddd380403e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Where can your spatial model be trusted? - Reliable validation of spatial machine learning [ https://substack.com/redirect/155be237-36ff-4b2e-95ba-7ede5f37d642?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Creating self-contained R scripts for rendering Quarto documents using the knitr engine – courtesy of the new R package managers ir and uvr [ https://substack.com/redirect/f049f958-dd2a-4cc3-822f-3b3735a7aa9d?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
LLMs reward expertise [ https://substack.com/redirect/5495123d-4e7c-42ce-84df-7d2344325ba3?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
language diffusion pt 1: arithmetic intensity primer [ https://substack.com/redirect/0c81d9d3-f46b-4f23-a87f-7dbf2cdc1471?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Harness Engineering for Self-Improvement [ https://substack.com/redirect/0192eeb7-5834-4f1d-a1a1-7a6be2a023c0?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
Thank you for joining us this week! :)
Stay Data Science-y!
All our best,
Hannah & Sebastian
Data Science Weekly Newsletter is a reader-supported publication. To receive new posts and support our work, consider becoming a free or paid subscriber.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9kYXRhc2NpZW5jZXdlZWtseS5zdWJzdGFjay5jb20vYWN0aW9uL2Rpc2FibGVfZW1haWw_dG9rZW49ZXlKMWMyVnlYMmxrSWpveU5qa3dNVGt4TENKd2IzTjBYMmxrSWpveU1USXdOekkxTnpJc0ltbGhkQ0k2TVRjNE56STJOalExTkN3aVpYaHdJam94T0RFNE9EQXlORFUwTENKcGMzTWlPaUp3ZFdJdE1qSTJPU0lzSW5OMVlpSTZJbVJwYzJGaWJHVmZaVzFoYVd3aWZRLmE4czlrejhhcVZKcWFhZjM1MUNyVldxNXNma0tfSUNkdHBMVHVHTk5ERkkiLCJwIjoyMTIwNzI1NzIsInMiOjIyNjksImYiOnRydWUsInUiOjI2OTAxOTEsImlhdCI6MTc4NzI2NjQ1NCwiZXhwIjoyMTAyODQyNDU0LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.122vkh2oK68KkfE-4vW6m_LPzT1IJhL_5nL6rYZKgCY?
