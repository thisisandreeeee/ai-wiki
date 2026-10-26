---
source: gmail
newsletter: "data-science-weekly"
message_id: "1a163af6f495ee42"
thread_id: "1a163af6f495ee42"
subject: "Data Science Weekly - Issue 674"
from: "Data Science Weekly Newsletter <datascienceweekly@substack.com>"
date: "Thu, 22 Oct 2026 12:56:22 +0000"
ingested: 2026-10-26
sha256: 19ed71917c3de0f7d2699eb320d6d15989680c8a0f043411742821240cf00c46
---
View this post on the web at https://datascienceweekly.substack.com/p/data-science-weekly-issue-674

Issue #674
Oct 22, 2026
Hello!
Every week, we write this email to share links we think are worth sharing in the Data Science, ML, AI, Data Visualization, and ML/Data Engineering worlds.
Sponsor Message
Online Data Science Programs from Drexel University [ https://substack.com/redirect/b3c40124-60d9-4f6e-b874-deb72f35c87e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Find your algorithm for success with an online data science degree [ https://substack.com/redirect/2040de6f-6f70-4b9b-a34e-1263d512ffc2?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] from Drexel University. Gain essential skills in tool creation and development, data and text mining, trend identification, and data manipulation and summarization by using leading industry technology to apply to your career.
Learn more [ https://substack.com/redirect/b3c40124-60d9-4f6e-b874-deb72f35c87e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]. [ https://substack.com/redirect/b3c40124-60d9-4f6e-b874-deb72f35c87e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
Now…let’s dive into this week's interesting links.
Editor's Picks
How to build a custom R graphics device [ https://substack.com/redirect/7d9ed018-4927-4ffc-ab17-a627dae41a46?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Did I need to write a graphics device to output plots to an HTML canvas? No I did not. Did anyone ask for this? Oh hells no. Ah, but did I have fun? Hahahahahahahaha. No…For the longest time, graphics devices in R have been a mystery to me…I decided to use the master’s tools to build my own goddamn house: I shamelessly used Claude to teach me how these things are constructed, so that I could do it myself if I bloody well wanted to. This is that story….
Building Open GeoAI for Humanitarian Response [ https://substack.com/redirect/40c7808f-dbcf-48e1-ac13-09300d963786?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
In this episode I sat down with Petya Kangalova and Kshitij Sharma from the Humanitarian OpenStreetMap Team (HOT) to discuss how GeoAI and community-driven mapping are being combined to support disaster response and humanitarian action…
Ask HN: How to deal with shipping AI-written code you don't understand? [HN] [ https://substack.com/redirect/6797612d-ee41-41df-afee-8cfef1aff033?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I’m an engineer at Meta and I never felt this uncomfortable doing my job. I’m writing code these days and it all feels like a black box. This new standard of shipping with AI is moving so fast that if we’re going to spend our time checking each line of code, it’s going to take forever. That means you can end up with systems you’ve built where you don’t truly understand how all the code works. You understand the high level, but not every detail. And maybe this is becoming the new standard. It goes against every instinct of being a software engineer. I’m used to understanding what I’m building. Now I’m trying to figure out how much I need to understand before I’m comfortable moving forward. Are other engineers feeling this too?
How are you handling this?…
.
What’s on your mind
This Week’s Poll:
.
Last Week’s Poll:
.
Data Science Articles & Videos
One Hash Bloom Filters [ https://substack.com/redirect/15a13bca-ca3b-4f9b-98f1-8391a4fe825b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
As part of our research on bloom filter techniques, we came across this paper from Lu et al. that uses even more math to show how to do bloom filters using only a single hash…Here’s an overview of how it works:
Instead of one big bit array, split that into k array partitions of fixed sizes
Each partition has a different size, and all the sizes are pairwise coprime, meaning that no two sizes share a common factor other than one
You hash the given key once to get hash
The bit position in partition p is hash%size_p (the size of the partition)
Since you have k partitions, you get k bit positions to check out of that single hash
You can use those k bit positions as you would with other bloom filter types!
With this technique in hand, I made jcalabro/gloom, a one-hash bloom filter (OHBF) implementation in go…
Everyone at my company can hook Claude up to source systems and build their own dashboards. Anyone dealt with this as an analytics team? [Reddit] [ https://substack.com/redirect/ea79e5f8-5084-484e-9197-ff789cf6e981?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Our company gave pretty much everyone Claude hooked up straight to our source systems. And yeah, it’s fast, people love it. But now there are reports everywhere built off raw data, all with slightly different logic, and a few of them get passed around as “the” number. Meanwhile we (the analytics team) mostly find out about this stuff after the fact. What’s bugging me is who owns what…
safespace - A Safe Space to Experience Pull Requests [ https://substack.com/redirect/b870fa43-1155-4d1b-af40-c9d681df9600?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The goal of the safespace repository and package is to provide a safe space for new developers to try out a pull request (particularly for Hacktoberfest) for an R package where they will definitely not break any in-production code…
Jarl: just another R linter [ https://substack.com/redirect/56ac3442-749a-4a8b-ae0c-b62e36d061eb?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I’m very excited to introduce Jarl1Jarl stands for “Just Another R Linter”., a new R linter. A linter is a tool that statically parses code (meaning that it doesn’t run the code in question) and searches for patterns that are inefficient, hard to read, or likely bugs. Jarl can parse dozens of files and thousands of lines of code in milliseconds. Here is an example of Jarl running on r-source (approximately 1000 files and 200k lines of R code) in about 700 milliseconds..
Ruby Jacquemin: Arizona Public Health Statistician [ https://substack.com/redirect/fd6ae9e1-30c8-4f12-b73e-8c29f49d50d8?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
As described in Part 1 [ https://substack.com/redirect/415dfcbe-b497-4d92-8f89-7ab92842ebec?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], September 2026 marked the 100th anniversary of Arizona’s entry into the federal registration areas for vital statistics. The woman who piloted Arizona to this milestone was Ruby Loy Jacquemin, a Prescott native who, after early widowhood, became the statistician for the State Board of Health. Who was Ruby Jacquemin, and what did she do?…
drinkR: Estimate your Blood Alcohol Concentration (BAC) [ https://substack.com/redirect/d570af9c-c885-4b35-bb55-423bcf533029?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Estimate your BAC, now 100% in the browser…Thanks to the awesomeness of webR and Shinylive, the tool I made in back in 2014 to estimate your blood alcohol concentration (BAC) now runs 100% in the browser, no server needed!…
Pele - Renders Mermaid diagrams faster than you'd run from a volcano [ https://substack.com/redirect/86432c3a-98b5-4d1f-be74-88b7a585127a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Pele is a lightweight open source library that renders Mermaid diagrams to SVG, themed with CSS variables. How it works: Write Mermaid syntax, Pele renders it to SVG….
Principles and Practice of Deep Representation Learning [Book] [ https://substack.com/redirect/c2c725a8-da12-4c58-b2ba-dd4d5dc17ced?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
This book is an attempt to "open the black box" and understand the mechanisms of large deep networks, through the perspective of representation learning, which is a major factor — arguably the single most important one — in the empirical power of deep learning models….
How to Learn ML in 2026 (Vicki Boykis Interview) [ https://substack.com/redirect/326ce3c9-5e0e-4552-bf8d-d18b40742067?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I had the pleasure of being interviewed by Yacine of Deep Learning with Yacine. He posed a lot of very thoughtful questions and I had a great time…
Can we trust the correlation coefficient in designed field experiments? [ https://substack.com/redirect/d50c1a59-06f1-4319-af3e-4117599af903?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Spoiler: no, we cannot…is it correct? Can we trust the conclusions? The answer is no, not completely. And here is why. Please, note that in this post I am following the point made by Bland and Altman (1994), by using an example that is more closely related to plant/crop science…
Chain of Thought For Humans [ https://substack.com/redirect/c43fc711-205f-4a6a-81cc-488a465714fc?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
These past few weeks, I’ve been conducting interviews, and I often open with “make sure you articulate your thoughts out loud, so I can follow along with your thinking”. This is primarily because I’m not a mind reader, but it does also help ensure candidates avoid freezing up. It’s a very “interviewy” skill though – artificial and unlike real development…But, inspired by my interviews, I’ve started narrating my own thought process out loud to myself. I look like a bit of a loon, but I tell myself I’m just a streamer with an audience of one. And to my surprise, it’s working really well…
Diplomatic Ways to Critique AI Slop [ https://substack.com/redirect/1fd2b2c5-702c-4282-bd61-8059d705a5e8?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
What do you say when a collaborator sends you AI slop to edit? You can’t accuse them of AI slop, because you never really know. But the thing is, we know that readers are suspicious of slop and will stop reading if they suspect that, whether its warranted or not. So here’s a live list of coded ways I have of telling people to reduce the AI slop in their writing…
You could have invented transformers from memory [ https://substack.com/redirect/c82c05c8-6091-4a68-8026-e5c9270ecc57?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
How do models remember so much information? And how much can they store? In this post, I’ll go through an intuitive way to look at linear maps, MLPs, and self-attention as different kinds of memory stores. From this intuition we can derive some heuristics for how much memory each layer can store…
Last Week's Newsletter's 3 Most Clicked Links
Are .ipynb notebooks already outdated in the agentic era? [Reddit] [ https://substack.com/redirect/49128678-892b-432b-a684-96b3bccddd7e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Claude Dashboards: The Jupyter Notebooks of Agent Age [ https://substack.com/redirect/8d501329-9017-4f50-a562-7e2dfa976994?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Validating data analyses written by coding agents [ https://substack.com/redirect/0afc5ab7-7521-4eb9-8d32-442dabc736cf?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
* Based on unique clicks.
** You can find last week's issue #673 here [ https://substack.com/redirect/473fad5c-3d25-43ed-b154-2d6d9448668a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Cutting Room Floor
Redis now has compressed bitmaps (Roaring) [ https://substack.com/redirect/77d91a6a-c787-49e1-9252-c09c5ece1dd0?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Engaging figures - How we guide understanding, without misleading [ https://substack.com/redirect/d6853e2a-f2a0-4fe7-b25a-64d9034bdecc?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
How Do I Contribute to R? A Guide to Getting Involved with R Core [ https://substack.com/redirect/a5d0ead0-55aa-4d32-9978-2ff4e011250c?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Parametric Models vs. Empirical Distributions and Ordinal Regression [ https://substack.com/redirect/0c663eb6-c8a9-4fa7-9ecb-14b642b3a376?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Expressing and Visualizing Model Uncertainty in Bayesian Variable Selection Using Cartesian Credible Sets [ https://substack.com/redirect/1e5dd064-3247-4f64-a474-8640e187c297?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Active inference as a unified model of collision avoidance behavior in human drivers [ https://substack.com/redirect/c32f48b0-6bc5-4d05-85b0-3763c71c0644?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Asking LLM for confidence [ https://substack.com/redirect/2fa81a54-e4b6-4917-bd2e-58df857d9f01?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
A Trip from Covariance to Correlation and Back [ https://substack.com/redirect/a6865691-aba0-434b-bf01-cd855003fd6c?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Going back to the basics: the correlation coefficient [ https://substack.com/redirect/4652f33e-5040-4cf2-baba-26536055836f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
Thank you for joining us this week! :)
Stay Data Science-y!
All our best,
Hannah & Sebastian
Data Science Weekly Newsletter is a reader-supported publication. To receive new posts and support our work, consider becoming a free or paid subscriber.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9kYXRhc2NpZW5jZXdlZWtseS5zdWJzdGFjay5jb20vYWN0aW9uL2Rpc2FibGVfZW1haWw_dG9rZW49ZXlKMWMyVnlYMmxrSWpveU5qa3dNVGt4TENKd2IzTjBYMmxrSWpveU1qRTJNall6TlRjc0ltbGhkQ0k2TVRjNU1qWTNNemd3TXl3aVpYaHdJam94T0RJME1qQTVPREF6TENKcGMzTWlPaUp3ZFdJdE1qSTJPU0lzSW5OMVlpSTZJbVJwYzJGaWJHVmZaVzFoYVd3aWZRLjhFWVFvQVBwbGRQSmRXXzRHOWRmaU1ZRzJiMFprS3R4YUdicm9MVVg5TDQiLCJwIjoyMjE2MjYzNTcsInMiOjIyNjksImYiOnRydWUsInUiOjI2OTAxOTEsImlhdCI6MTc5MjY3MzgwMywiZXhwIjoyMTA4MjQ5ODAzLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.dAOe3ap1iBUxfsglGbaIKdVa7w2N_Amc2zwu2MMdoUg?
