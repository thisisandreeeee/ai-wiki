---
source: gmail
newsletter: "data-science-weekly"
message_id: "1a08b718e04ad16e"
thread_id: "1a08b718e04ad16e"
subject: "Data Science Weekly - Issue 668"
from: "Data Science Weekly Newsletter <datascienceweekly@substack.com>"
date: "Thu, 10 Sep 2026 13:03:29 +0000"
ingested: 2026-09-14
sha256: 34489f6b91f23bb266e38e15d0a719851c8a5ee6ccc5f2bb534ab6b79beafca1
---
View this post on the web at https://datascienceweekly.substack.com/p/data-science-weekly-issue-668

Issue #668
Sep 10, 2026
Hello!
Once a week, we write this email to share the links we thought were worth sharing in the Data Science, ML, AI, Data Visualization, and ML/Data Engineering worlds.
And now…let’s dive into some interesting links from this week.
Editor's Picks
I Made a Real Fly Brain Play Pong. It Didn’t Learn. That’s the Interesting Part [ https://substack.com/redirect/cf2cf118-4f10-41d9-b60b-1a30fdb65cb8?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The question is whether the behavior is being driven by the fly’s actual wired-in visual and motor circuits, or whether we’re mostly watching neurons fire and a game engine turn that into something that reads as alive because open worlds and rhythm games are forgiving environments to watch. I picked the least glamorous test bed available to check: Pong….
Line: Draw a pot profile, design a family of vessels [ https://substack.com/redirect/4885fcc7-7fca-4f7d-b1e5-f766cb9329a8?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Potters don’t design bowls and vases, they design one curve. That single line, rotated around the axis, becomes the entire form. In Line, you draw that curve. One side, shaped with a handful of control points, and the app grows a family of proportions around it: each variant keeping the radii and angles that make your line recognizably yours. Taller, wider, slender, grand: different vessels, same gesture. Find the line. The rest is proportion…
How I Turned My Security Cameras Into an Automatic Bird Identification System with BirdNet-Go [ https://substack.com/redirect/813064ef-34a5-4099-9d5d-281d9312e0ae?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I turned three security cameras into an automatic bird identification system using BirdNet-Go…My wife loves listening to the birds and identifying them using an app on her phone. I thought I'd take this a step further and see if there was something that can identify the birds based on their song. Looking around I found BirdNet and BirdNet-Go, then discovered you can run this on Docker and use the security cameras you already have outside to identify the birds. Awesome! So I took 3 of the cameras around my house and used their microphones to identify the birds…
.
What’s on your mind
This Week’s Poll:
.
Last Week’s Poll:
.
Data Science Articles & Videos
Python sets and dictionaries can have quadratic-time performance [ https://substack.com/redirect/431873ed-3423-49d7-85a1-0fe02599457c?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
In Python, the dict data structure is the conventional key-value structure. E.g., you might store a list of names as keys and have their phone numbers as values. Valentin Ignatev wrote this amusing post on X:
It is indeed widely believed that, in the strict sense, the dict data structure and its companion, the set data structure, are O(1), meaning that as you increase the size of the data structure, the time to insert or query a key remains constant.
Let us examine the claim…
Squill: my canvas for writing SQL [ https://substack.com/redirect/359fb72f-dd0b-48c5-8760-b344ea3f3ff0?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
It’s 2026, and I’m not convinced there’s one place people flock to for writing SQL…There are excellent tools like DataGrip, Count.co, and Hex, but you have to pay for them…There are some great free generalist tools, such as Beekeeper Studio, DBeaver, and QStudio. There are also apps that cater to specific databases like Postico for PostgreSQL. For CLI aficionados there’s Harlequin and the more recent sqlit…Last but not least dbt and SQLMesh both have official VSCode plugins, which have some great features…
Object storage is all you need [ https://substack.com/redirect/871ff315-a71d-49db-a9a1-d41ed8c7cefe?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Last time on the Ampbase blog I talked about all the database engines that we don’t use and promised to follow up explaining what we actually do. We don’t use a relational database. We use Tigris as the storage layer directly, and implement the few database behaviors we actually need on top of the two primitives it gives us. Yeah, yeah, I know; “we didn’t need a database” is a catchy title that usually happens about 8 months before the inevitable next post being “how we tucked our tail between our legs and moved to Postgres”. In practice, when you reach for a database engine you’re actually reaching for four basic features: unique constraints, transactions, indices, and history tables. In order to use Tigris’ global object storage as a database, we had to implement all of these primitives ourselves. Today I’m going to peel back the curtain and show you how those primitives work so you can understand what actually goes into your database engine of choice…
Linear Regression with Gradient Descent: Mathematical Foundations of AI [ https://substack.com/redirect/1debaca2-f5ff-4e4d-877e-f3f0bbadac39?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Why bother with linear regression, a model that has been around for more than a century? After all, ChatGPT or Claude are not linear regressions. They are large Transformer-based neural networks, also called Large Language Models (LLMs). You may be able to understand such models without knowing linear regression. But you may find yourself struggling when reading terms like cross-entropy or gradient descent. By developing an intuitive understanding of linear regression, we will cover the concepts at the core of the current AI revolution…
You Could Have Come Up with Speculative Decoding [ https://substack.com/redirect/0b7510fc-308c-4fec-b5c5-663f81997749?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Speculative Decoding is a great example of how good systems understanding can lead to performance increases; in some case around 2 − 3 × decode throughput. It is kind of a perfect study since it involves knowing the entire inference stack from batch scheduling, hardware limitations to the model internals to make it work well…Lets dive into how you could have also come up Speculative Decoding. Whenever you think of optimization, you might imagine various axes of freedom the problem has e.g. to get a specific result you might be able to add more compute, this is a variable you could change; although the relation might not be linear, but the idea is there is a relation…
Navigating Challenges in Spatial Machine Learning [ https://substack.com/redirect/f06be8bb-7654-4802-8d19-cb51d5366a11?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
A short note about our perspective paper on validation, uncertainty, algorithms, software, and reproducibility in spatial machine learning…Spatial machine learning has become a standard tool for producing environmental and geographic prediction maps. It is now relatively (technically) easy to combine field observations with remote sensing, climate, terrain, or other predictor layers and fit a strong machine learning model. The harder question is whether the resulting map is reliable, transferable, and reproducible…
Evaluating Polynomials Fast [ https://substack.com/redirect/dd5b4414-cf2b-4462-b236-099b505405b8?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
You may have heard about Horner's method, which evaluates a polynomial of degree n in n multiplications (n−1 if it is monic). But did you know that with a bit of preprocessing of the coefficients, ⌊n/2⌋+1 multiplications suffice for any monic polynomial, one more for a general one? You can use this to approximate functions like exp, sin, cos, or to evaluate polynomials in cryptography, hashing, and coding theory. Simply type a polynomial below, pick your field, and we'll preprocess it for you…
Which tools do Claude Code, Codex and Cursor choose? We measured 16,893 sessions to find out. [ https://substack.com/redirect/4de227ed-1ed6-4536-96c4-703936c75a8e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
As agents take over more and more parts of the coding journey, there is one specific part everyone outsources to their agent, from vibe coders with no software background to senior engineers: selecting which service to implement for a specific need in an existing codebase…
Can Guitar Frets Perform Multiplication? [ https://substack.com/redirect/a30ebdf0-c5cf-44b9-89c7-1896c600ef0f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I’m sure that some pictures are worth a thousand words, but others trigger a whole lot of puzzlement. Such was the case with the cover of a book I recently bought entitled Calculating with Tones: The Logarithmic Logic of Music:
The Lost Art of Logarithms [ https://substack.com/redirect/6bb32dbe-57ec-4370-9bee-2bc70bb73fa0?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
A web-book-in-progress by Charles Petzold wherein the utility, history, and ubiquity of that marvelous invention, logarithms, including what the hell they are, are explored; with some demonstrations of their primary historical application in plane and spherical trigonometry; plus, that extraordinary tool known as the slide rule is fully explored in theory and use…
Color Scales: the Birth of Viridis [ https://substack.com/redirect/19049659-78db-4220-8345-9c8ea7d2c02f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Why color scales are not just for beauty but determine the precision of data visualization…“Color Scales and the Birth of Viridis” tells the story of viridis, one of the most influential scientific color scales of the last decade. Designed as a perceptually uniform and colorblind-friendly alternative to rainbow color maps, viridis has become a standard tool for visualizing quantitative data across many fields of science. The piece explores how it was developed and why seemingly simple choices such as color scales can profoundly influence how we interpret data…
How are LLMs used in predictive modeling and anomaly detection? [Reddit] [ https://substack.com/redirect/e53cc968-1034-4eaa-bbe3-a1b3ea02f642?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I am DS with 20 YOE but I’ve been managing lately and know very little about using LLMs. Does the DS just feed the data into LLM then ask it to predict something or find anomaly? Or does the DS ask the LLM to build a model which is then deployed?…
How science gets by with a little help from the Beatles: Detecting cultural wordplay in scientific literature using large language models [ https://substack.com/redirect/62e83792-934b-4d84-a6f3-ff7ce77d4b26?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
This study documents how often Beatles song titles and lyrics appear in academic article titles, identifying 2,237 exact references and 963 instances of creative wordplay in data from Scopus…We report which titles and lyrics are referenced most often, trace how their use has grown over the decades, and show that this growth has outpaced the expansion of the scientific literature as a whole while varying systematically across disciplines. The result is the first large-scale, cross-disciplinary account of how the Beatles have left their mark on scientific writing…
Last Week's Newsletter's 3 Most Clicked Links
What is an (agent) Harness? [ https://substack.com/redirect/4cb59214-58f3-41a5-87ac-a0b0b17c79f0?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The Harness Is the Thing [ https://substack.com/redirect/bb69bf24-e9d9-4849-beba-20e988b45032?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
ROC, Paper, Scissor, Shoe [ https://substack.com/redirect/f69b36fa-46f4-4790-aace-d3c7a199aab2?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
* Based on unique clicks.
** You can find last week's issue #667 here [ https://substack.com/redirect/8d04179c-7cee-494f-bfd5-cf31cb3e0e10?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Cutting Room Floor
Is my degree useless because of AI? [Reddit] [ https://substack.com/redirect/190d48f6-b0a9-4384-84e7-f47f46426f84?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
How to use dplyr-style slice operations on omics data objects in the tidyomics project [ https://substack.com/redirect/2c8e8034-7fc1-4915-be56-14bd4757469d?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
What are some examples of truly independent things that are relatable to people? [ https://substack.com/redirect/cb2561e8-89cd-4602-844a-595b92d7b402?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Most of us are writing with AI, but no one likes reading AI writing [ https://substack.com/redirect/779273e6-4eb3-4d8d-a6da-589ce6310552?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Revealing the Strategies Hidden in Variance [ https://substack.com/redirect/fdc7872d-3f4a-4851-9078-01cd119021c2?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
A 50-year-old computer-assisted proof [ https://substack.com/redirect/c24cc2e8-fc0d-4e85-a4df-b2a129ffec3f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Ashby’s Law of Requisite Variety [ https://substack.com/redirect/f89f1e0f-b7da-43e3-b5df-dcbd025a8d81?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
Thank you for joining us this week! :)
Stay Data Science-y!
All our best,
Hannah & Sebastian
Data Science Weekly Newsletter is a reader-supported publication. To receive new posts and support our work, consider becoming a free or paid subscriber.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9kYXRhc2NpZW5jZXdlZWtseS5zdWJzdGFjay5jb20vYWN0aW9uL2Rpc2FibGVfZW1haWw_dG9rZW49ZXlKMWMyVnlYMmxrSWpveU5qa3dNVGt4TENKd2IzTjBYMmxrSWpveU1UVXdNelU0TVRJc0ltbGhkQ0k2TVRjNE9UQTBOVGcyT0N3aVpYaHdJam94T0RJd05UZ3hPRFk0TENKcGMzTWlPaUp3ZFdJdE1qSTJPU0lzSW5OMVlpSTZJbVJwYzJGaWJHVmZaVzFoYVd3aWZRLk03b1h1ZC1wQW5hRGxDZ1dmTWNoMzI5Sm5RYjZ3NE1heDJwV1FYek41QzAiLCJwIjoyMTUwMzU4MTIsInMiOjIyNjksImYiOnRydWUsInUiOjI2OTAxOTEsImlhdCI6MTc4OTA0NTg2OCwiZXhwIjoyMTA0NjIxODY4LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.K8BdCWSAU1xHtNbmunUdeTdAP-zE4rHvo_lcF27vqu0?
