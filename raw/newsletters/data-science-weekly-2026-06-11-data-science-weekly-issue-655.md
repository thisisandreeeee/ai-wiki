---
source: gmail
newsletter: "data-science-weekly"
message_id: "19eb8cab5eeaa9cd"
thread_id: "19eb8cab5eeaa9cd"
subject: "Data Science Weekly - Issue 655"
from: "Data Science Weekly Newsletter <datascienceweekly@substack.com>"
date: "Thu, 11 Jun 2026 22:25:19 +0000"
ingested: 2026-06-24
sha256: e2a2c8bb3523e30d1d031f5c18ae139ac46918def80add8b5f8ac302d047b4a7
---
View this post on the web at https://datascienceweekly.substack.com/p/data-science-weekly-issue-655

Issue #655
June 11, 2026
Hello!
Once a week, we write this email to share the links we thought were worth sharing in the Data Science, ML, AI, Data Visualization, and ML/Data Engineering worlds.
And now…let’s dive into some interesting links from this week.
Editor's Picks
An Overview of Modern AI Robotics from First Principles [ https://substack.com/redirect/4a6276d2-4a23-493d-9c54-1a9f84980406?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
There is a deceptively simple way to describe what physical AI is all about, a way in which anyone with a STEM background will intuitively understand. Like all other AI models, a model which controls a robot is also a function. It takes in observations (camera pixels, joint angles, the felt resistance of a gripper, etc) and it outputs actions, the next set of positions and torques for its motors…If you’ve ever trained a model that maps inputs to outputs, you can already grasp the shape of the problem. The interesting part is what happens when you take this familiar shape and drop it into a moving, active world…This sounds like ordinary machine learning, and for a while you can pretend it is. But robotics introduces a third axis that classic ML never had to respect: inference time…
My unvarnished guide to solution engineering [ https://substack.com/redirect/8e4d86c5-cb79-47a4-b0b8-7b98293d1e3a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Nowadays I feel more or less comfortable interacting with customers. But I was awful at first. I know because one of the cofounders gave me harsh feedback after a call with our first serious customer. I still remember slamming the lid of my computer when we debriefed. What I perceived as harsh feedback at the time turned out to help me grow quickly…I used to be a regular data scientist assigned to internal projects. Talking to prospects and customers got me out of my comfort zone. You owe them a service, and they expect you to deliver something. If something goes wrong they’ll go above your head to your founders, at which point you start feeling the heat. It can be quite harsh. But it can also be rewarding when things go well…
Navier-Stokes fluid simulation explained with Godot game engine [ https://substack.com/redirect/5496da06-f0ac-4923-8f91-b29066e2a24b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Let me start with the mathematical description of what we will do in this blog post. This description might sound daunting, but don’t worry - we’ll explain everything as we go. Here goes: we will simulate fluid flow by moving a scalar density field through a vector velocity field. We’ll simulate velocity diffusion and advection as well as density diffusion and advection. Then we will add velocity projection with the goal of making the fluid obey the law of mass conservation - which will happen by balancing divergence with a pressure field. We will use bilinear interpolation and Gauss-Seidel relaxation for approximating values where needed…
What’s on your mind
This Week’s Poll:
.
Last Week’s Poll:
.
Data Science Articles & Videos
The Anti-Scaling Law in Biology, and Why AI Could Make Crowding Worse Before Making Drug Development Better [ https://substack.com/redirect/33523272-3124-446d-a5bd-92355e6f8f63?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
One of the main reasons for the tech community’s optimism is the scaling-law. Once you demonstrated 0-1, you can do 1-100 much quicker. The internet, social media, and so on…In biology and drug development, I think there is a mirror image, the anti-scaling law. Because of that, here’s my contrarian view: AI could make crowding in drug development worse, before making it better. And that’s my perspective as a genuine believer in the transformative power of AI, and an AI practitioner who used $14,000 worths of AI tokens in the past 2 months…
What is there besides Frequentist and Bayesian stats? [Reddit] [ https://substack.com/redirect/27bd8988-4307-4890-a7d1-0f3b1692fdbe?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I am wondering whether there are lesser known statistical paradigms. like most people, I was first acquainted with the Frequentist framework, and later got introduced to Bayesian stats. I really like the way this made me reconsider some of what I thought were basic assumptions, so now I’m wondering what the next thing could be? Are there any other branches/frameworks which are not as well known?…
Forecasting: Principles and Practice, the Pythonic Way [ https://substack.com/redirect/afebe2c4-ded4-49d6-b2dc-72f4007e38d7?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
This textbook is based on Forecasting: Principles and Practice (3rd ed) and is intended to provide a comprehensive introduction to forecasting methods and to present just enough information about each method for readers to be able to use them sensibly. We don’t attempt to give a thorough discussion of the theoretical details behind each method, although the references at the end of each chapter will hopefully fill in many of those details…
The Simplest Learning Machine, Pt.2 [ https://substack.com/redirect/bfd0a60c-35bb-4239-83dd-b8e06f855de7?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
In the previous article I outlined the concept of the Simplest Learning Machine. It’s an imaginary algorithm that uses one byte of persistent memory and learns to predict something about a stream of binary events…Can we actually write something like that? How would it work?…One semi-obvious thing we can learn is the rate of positive events in the stream. This would give us some predictive power, as long as that rate is different from 50%. A bit of a stretch to call this “machine learning”, sure, but I’ll get to the questions of usefulness later…
On Training Data for Bio AI Models [ https://substack.com/redirect/f031e7d1-1e5b-41fb-929f-2488f8a9104e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
As we advance biological foundation models, which lessons from LLM data curation transfer, and which need rethinking?…
Our goodpractice Package Has New Superpowers [ https://substack.com/redirect/a34d679e-1eca-4950-bddc-b1be4d8bca0b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The goodpractice package has been recommended by rOpenSci since it was first started just over 10 years ago by Gábor Csárdi. We used to ask our editors to manually run goodpractice on all packages submitted to software peer-review, and then to ask authors to fix any notable issues flagged by the package…We’re really pleased to share that we’ve recently rolled out a host of updates and extensions to the package. These make it both easier to use, and more powerful…I think that is the aspect that I found most surprising: That the use of Claude made our collaboration feel less technical, and therefore somehow even more human. And that gave us the ability to work though 70 pull requests representing over 100 new checks, all ready for everybody to use…
The Warehouse [ https://substack.com/redirect/a10c104d-9764-49a6-bf44-8a3ffab0d89b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The Problem
With over 23,000 packages on CRAN alone, finding the right package for your task is overwhelming:
Searching by keywords often misses relevant packages
No easy way to compare similar packages
Quality indicators are scattered or missing
GitHub-only packages are hard to discover
The Warehouse Solution provides:
Function-first search: “estimate serial interval” → find all relevant packages
Quality scores: Automated assessment of tests, documentation, and maintenance
All sources: CRAN, GitHub, Bioconductor in one place
Community reviews: Real user experiences and recommendations
Smart categorization: Browse by what packages actually do…
Robot Learning: From Fundamentals to Foundation Models [ https://substack.com/redirect/4be92f5c-01e2-4c00-b930-89d9c3db0315?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
This course provides a comprehensive introduction to modern robot learning, combining classical techniques with the latest advances in large-scale models: Students will start by learning the fundamentals of imitation learning, reinforcement learning, and policy optimization, and gradually progress to advanced topics including Vision-Language-Action (VLA) models and foundation models for robotics The objectives of this course are:
Understand the core principles of imitation learning, reinforcement learning, and policy learning.
Implement basic robot learning systems in simulation and on real robots.
Explore state-of-the-art Vision-Language Action and foundation models for robotics.
Design and evaluate scalable robot learning pipelines integrating perception, control, and multi-modal reasoning…
ML Job Interviews: The Ultimate Guide [ https://substack.com/redirect/ac9d54cc-1a52-4169-acaa-e34dc1a3e5ca?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
How I found a Research Scientist role after a PhD in Machine Learning…My process was, overall, successful: I received offers from every company I completed interviews with including: DeepMind (which I accepted), Isomorphic Labs, Cohere, Meta, and a startup in stealth. A few caveats to the first claim: Anthropic, Mistral, and TeslaAI got back to me too late and I didn’t complete those processes. ReflectionAI, the one genuine rejection: they didn’t like me for the RS role but switched me to their Engineering track instead…
stata-mpl - Give your matplotlib and seaborn charts the Stata 19 look [ https://substack.com/redirect/ed5eda5b-8f5b-4192-9f27-904bea42d327?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Give your matplotlib and seaborn charts the look of Stata 19 (the stcolor scheme, Stata’s colorblind-friendly default). Calibrated against the official SVG files exported by Stata 18/19…
Avian Visitors [ https://substack.com/redirect/2f47621f-4a9b-408d-bc1e-d88cde081307?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I mounted a tiny microphone on my apartment balcony to listen for any birds passing by and built a site to collage them as they’re heard…so I’ve thrown together this short writeup for any of you who want to monitor any avian visitors that may be passing by your own place. It’s short and sweet for now in an attempt to get something out quickly, but this work is part of a longer chain of bird-tangent projects i’ll write something up about soon!…
Ask HN: What are tools you have made for yourself since the advent of AI? [ https://substack.com/redirect/897afb4c-8cac-478e-9097-d6b032a86149?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Ask HN: What are tools you have made for yourself since the advent of AI?…
Why Academics Should Use AI for Writing: A Case Study [ https://substack.com/redirect/0ab21058-2b75-4cca-9ed8-114dec55dd88?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I violently dislike the idea of AI taking over my writing. My writing is my own, and having it done by AI makes the final product lose its soul. Also, whenever I have used AI to write several paragraphs independently (which I admit to doing for bureaucratic tasks) I ended up rewriting most of it anyway. However, over the past year or so I have become increasingly impressed with what AI can do, and rather than talk about this in abstract terms I would like to present you with a concrete demonstration that shifted my opinion a great deal…
.
Last Week's Newsletter's 3 Most Clicked Links
How to Build a Simple, Bulletproof Data Pipeline [ https://substack.com/redirect/5ecbf974-7ac2-4a09-a34c-40ef3b3d169a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
supertree - Interactive Decision Tree Visualization [ https://substack.com/redirect/70d3158e-b4b5-4fe0-ae0f-636fb9e91738?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Beyond the Semantic Layer: Building a Context Layer for the Agentic Era [ https://substack.com/redirect/8824d2c5-c7c1-478b-8727-22b9a2f7f484?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
* Based on unique clicks.
** Please take a look at last week's issue #654 here [ https://substack.com/redirect/ce1e5fd5-72b8-417f-a2d5-b83e7b1e5c53?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Cutting Room Floor
When is detecting AI-generated text worthwhile? [ https://substack.com/redirect/75cd1181-f4f3-451c-9879-27edf261f26e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Lines of Code Got a Better Publicist [ https://substack.com/redirect/a5df9370-fd0f-45f7-a0bf-ccfd02f52597?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
BayesMultiMode: Bayesian Mode Inference in R [ https://substack.com/redirect/2a46d49e-86a9-475c-8c3d-002ba60db1af?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Cognitive Endurance as Human Capital [ https://substack.com/redirect/814e3568-c813-4619-9126-60d1460f56ad?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
DiffusionBlocks: Training Neural Networks One Block at a Time [ https://substack.com/redirect/96119691-ff98-4479-a3cf-7f1a450b5283?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Data from 66,000+ practice sessions. How much does the typical musician actually practice? [Reddit] [ https://substack.com/redirect/c419ef33-999a-4990-9b5c-0d4a56c29a11?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
What is the most common reason data science projects fail to deliver business value? [Reddit] [ https://substack.com/redirect/effa06fa-afd2-4cdd-ad06-6365927fea26?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
Whenever you're ready, 3 ways we can help:
Go deeper each week (paid subscription)
Get 3 additional posts per week designed to help you:
Statistics → understand the math behind ML
AI Agents → build with modern AI tools
Career → become more valuable at your job
👉 Upgrade for $10/month — cancel anytime [ https://substack.com/redirect/46dd6d3d-c9cd-444f-9417-90f193d607dd?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Looking to get a job?
A practical guide to landing your first (or next) data science role, based on thousands of reader questions.
👉 Check out our  [ https://substack.com/redirect/33929ed0-0bb4-4fc2-80b0-530521873f5f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]“Get A Data Science Job” [ https://substack.com/redirect/33929ed0-0bb4-4fc2-80b0-530521873f5f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] Course [ https://substack.com/redirect/33929ed0-0bb4-4fc2-80b0-530521873f5f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Promote your organization/project/event to ~68,500 subscribers
Sponsor this newsletter and reach a highly engaged data science audience (30–35% open rate).
👉 Reply to this email to learn more
Thank you for joining us this week! :)
Stay Data Science-y!
All our best,
Hannah & Sebastian
Data Science Weekly Newsletter is a reader-supported publication. To receive new posts and support our work, consider becoming a free or paid subscriber.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9kYXRhc2NpZW5jZXdlZWtseS5zdWJzdGFjay5jb20vYWN0aW9uL2Rpc2FibGVfZW1haWw_dG9rZW49ZXlKMWMyVnlYMmxrSWpveU5qa3dNVGt4TENKd2IzTjBYMmxrSWpveU1ERTJNVFl4TWpJc0ltbGhkQ0k2TVRjNE1USXhOamMxTWl3aVpYaHdJam94T0RFeU56VXlOelV5TENKcGMzTWlPaUp3ZFdJdE1qSTJPU0lzSW5OMVlpSTZJbVJwYzJGaWJHVmZaVzFoYVd3aWZRLjR2SUVRbEYzcURtWjJLQjdwUERBQTNIaE9UN3VqNEx3WVRCMi1ZX1NTeWsiLCJwIjoyMDE2MTYxMjIsInMiOjIyNjksImYiOnRydWUsInUiOjI2OTAxOTEsImlhdCI6MTc4MTIxNjc1MiwiZXhwIjoyMDk2NzkyNzUyLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.uZPTvSxQgUgk-MlQ9mBR8A0lA1hhzcKehmI9g4xUAVk?
