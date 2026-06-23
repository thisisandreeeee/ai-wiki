---
source: gmail
newsletter: "data-science-weekly"
message_id: "19e701b4044b912c"
thread_id: "19e701b4044b912c"
subject: "Data Science Weekly - Issue 653"
from: "Data Science Weekly Newsletter <datascienceweekly@substack.com>"
date: "Thu, 28 May 2026 19:41:05 +0000"
ingested: 2026-06-23
sha256: f3e057cd829468357370508253b8530e127926aa78f2392a131ba9afcd831268
---
View this post on the web at https://datascienceweekly.substack.com/p/data-science-weekly-issue-653

Issue #653
May 28, 2026
Hello!
Once a week, we write this email to share the links we thought were worth sharing in the Data Science, ML, AI, Data Visualization, and ML/Data Engineering worlds.
And now…let’s dive into some interesting links from this week.
Editor's Picks
The quadratic sandwich [ https://substack.com/redirect/d0108c61-607b-4eef-b9f6-f981fa4b2b43?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
If you have ever tried to minimize a function with gradient descent, you probably noticed that some functions are a joy to optimize and others are a nightmare. The difference often boils down to two properties: strong convexity and L-smoothness. These two concepts define a “sandwich” of quadratic bounds around your function that tells you exactly how well-behaved it is. If the sandwich is tight, life is good. If one slice of bread is missing, things get ugly fast…In this post we’ll build up both concepts from scratch, see how they combine into the quadratic sandwich, understand what happens at the level of the Hessian’s eigenvalues, and pick up a neat trick to verify L-smoothness without ever computing an eigenvalue…
What it takes to transpose a matrix [ https://substack.com/redirect/7c24bb59-1ee2-4f01-8643-b45dc1139304?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
In this article we are going to gradually build a sequence of progressively more efficient implementations of matrix transpose, with the most sophisticated implementation being up to x25 times faster than the naive one. During each step we will locate the bottleneck, figure out what has caused it, and think of a solution to overcome it. This article is intended to serve as an introduction to optimizing matrix algorithms for x86_64, presented from the perspective of a real-world problem…
Why is Kullback-Leibler divergence not a distance? [ https://substack.com/redirect/0e4df9ec-468f-40cb-955d-8dbdbadc3521?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The Kullback-Leibler divergence between two probability distributions is a measure of how different the two distributions are. It is sometimes called a distance, but it’s not a distance in the usual sense because it’s not symmetric. At first this asymmetry may seem like a bug, but it’s a feature. We’ll explain why it’s useful to measure the difference between two probability distributions in an asymmetric way. The Kullback-Leibler divergence between two random variables X and Y is defined as…
What’s on your mind
This Week’s Poll:
.
Last Week’s Poll:
.
Data Science Articles & Videos
Friday Pins vs Sunday Pins or: How to Illustrate Something Completely Obvious [ https://substack.com/redirect/3de14ff4-1101-47ac-a9a6-21d62ff3a831?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
In my previous article, I Spent the Last Month and a Half Building a Model that Visualizes Strategic Golf, I laid out the very basics of the golf model I built, the underlying reason that compelled me to work on it, and novel maps it could create. However, I barely scratched the surface of what this model can illustrate about golf course architecture. Here, I want to talk about how we can specifically look at one kind of dynamic architectural interest. That is, features of golf architecture that appear as we change the course setup. Specifically, I want to look at how different hole locations change the architectural interest for players, how we can show that, and what it looks like…
What DS job market trends are you seeing? [Reddit] [ https://substack.com/redirect/22ade66e-f468-48a3-8cc6-0ee6cd6e4884?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I have 20 YOE, but I do a generic “data science” search on LinkedIn every 3 months to see how the job market is trending. Here are my latest observations. I would love to hear what others think.
The number of AI postings is going down. ML and DE skills are back in fashion.
Salaries are down across the board.
Non-technical responsibility is up. I see “Data Scientist” roles being asked to create a roadmap and drive organizational change. That used to be the responsibility of the manager or maybe the lead.
I haven’t applied for any of these jobs, so I don’t know what’s actually real. I wonder if Data Science is no longer the hot keyword and I should be searching for something else…
Thoughts About the Roles of AI for Statistics [ https://substack.com/redirect/c1c824fc-7460-4d17-b98f-487ffb319448?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
This talk covers what I’ve learned from using large language models in my work for the past two years. For statistical programming, success has come when I play the role of specification writer and comprehensive tester. For statistical methodology, AI has been successful serving me as a mathematical statistical assistant and a critic. Instead of avoiding AI we should embrace it, but we should always set a higher bar for the quality of our work as a result…
Evaluating detection & classifier algorithm accuracy [ https://substack.com/redirect/99aa551e-e622-4d36-80a0-d92e8baf0f4a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Let’s say i have images with a mixture of normal cells and sick cells on each image. Humans can reliably distinguish normal cells from sick cells, however it takes a lot of time to mark up the images as there are hundreds of cells in one field of view. I have an algorithm that can also distinguish normal and sick cells. The outputs from both manual markup and my algorithm is 2 lists of (x, y) coordinates -- one list for sick cells, one for healthy. What are the best practices for comparing and reporting the accuracy of my algorithm against manual markup?…
Do Most TV Shows Stick the Landing? [ https://substack.com/redirect/2df6aff5-a244-411b-b36c-d15b6a983686?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Four decades later, television has changed dramatically, reshaped by streaming and a clearer understanding of what makes for a satisfying conclusion. But has this institutional knowledge led to better endings? Have showrunners learned from the mistakes of St. Elsewhere, Game of Thrones, and other finale fiascos? So today, we’ll investigate whether omniscient showrunner Tommy Westphall has gotten any better at sticking the landing, how finale quality has changed in recent decades, and whether finality is simply a structural weakness of television itself…
NYED Data Explorer Shows 15 Years of Charter School Success [ https://substack.com/redirect/8e16f3d5-acf0-4f13-b0d1-b32dac355d94?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
When I discovered 15 years of NYED assessment data, the interest to clean and free this data for others to discover in a Shiny app, was immediate. The opportunity to also feature Classical’s stand-out performance didn’t hurt my motivation, although this post and the app were built in my spare time, and do not represent the opinions of South Bronx Classical Charter Schools. Unlike many past Redwall posts, this one will not have code, and will be primarily to explain the data and show how to use the app…
Luck vs. skill in poker [ https://substack.com/redirect/8791f031-5b9c-4927-8c41-3dd63f07a79b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
The thread of our recent discussion of quantifying luck vs. skill in sports turned to poker, motivating the present post…Can good poker players really “read” my cards and figure out what’s in my hand?…
Speeding up Stan model builds for R package developers [ https://substack.com/redirect/e9184e8b-8d14-4468-994e-fbfbe48307b4?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
My PhD student was interested in Bayesian methods and we put together an R package which included some Stan models. I was always frustrated by how slowly these compiled on our Windows machines…A few years later, when I got a MacBook Air I was shocked how much faster they compiled. On my Windows machine our mrbayes package takes 3 minutes 55 seconds to compile and install. On my M4 MacBook Air it takes 1 minute 16 seconds. The following tips show how to improve those timings…
How unfair is the coin? [ https://substack.com/redirect/7a616776-a632-4b2c-845a-d82eb5908af6?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
In February 2024, Reverie Labs, the startup I co-founded in 2017, was acquired by Ginkgo Bioworks. I’m now on leave from Ginkgo and I’ve joined Y Combinator as a Visiting Partner, giving me the chance to work with the next generation of companies. Especially in this new role, I’ve been thinking a bit about what worked, what didn’t work, and what lessons I can take forward…We had quite the journey – 6+ years of building at the intersection of AI and drug discovery. We began as a machine learning driven software company selling SaaS tools and consulting services to pharma companies, and at acquisition we were a pharmaceutical company, developing our own in-house pipeline of drug assets and advancing them rapidly using our machine learning technology…
Functions over Idioms - Writing R in Python with rfuns [ https://substack.com/redirect/a2e21126-f8c3-4257-9ce0-b3611f4179a4?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Sometimes a problem calls for a particular language to be used, and with that comes adjusting one’s brain to thinking in that language and using the appropriate idioms to leverage that language’s features…But what if I don’t want to?…The line between R and Python has been heavily blurred the last few years, particularly with {reticulate} (rstudio.github.io) enabling us to use Python within R code, RStudio rebranding as Posit (posit.co) and taking on a strong Python development effort, releasing Positron (posit.co) as a multi-language IDE, and Quarto (quarto.org) being a multi-language rethink of Rmarkdown…
LLM Prompting Techniques for Data Scientists and Engineers in 2026 [ https://substack.com/redirect/8dee2d86-bee5-4e32-8435-2530f2e920fe?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Six techniques matched to six failure modes, including inconsistent output formats, shallow reasoning, instruction drift, and more…
I am faking my way through a Data Analyst role with AI, how do I actually learn before I get caught? [Reddit] [ https://substack.com/redirect/a398e44c-4646-473d-8545-04f208f3ff1b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I graduated with a CS degree, but I spent my undergrad years grinding part-time jobs instead of actually studying. Now I am a Data Analyst at a small business, and the job is nothing like the theory I slept through in school. I am just winging it every day tbh. I rely heavily on openclaw for data scraping and acciowork to handle the processing and archiving. If these AI tools ever went down, I would be fired within an hour. I am terrified of being exposed as a fraud. Where do I even start fixing this? Should I grind python, or is mastering excel still the first step for survival?…
50 Hours to Draw Some Lines [ https://substack.com/redirect/b30f79a3-058a-4dc1-965e-b00945d740eb?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
"What are you working on these days?"
"Data visualizations." I told him.
"Ah, you using algorithms, machine learning, cloud computing, things like that?"
"No." I said. "I'm just trying to draw a line graph."….What do I mean by drawing data by hand? I made this data visualization (data viz) about a coffee maker computer by hand, using rulers, pencils, ink, and a lettering kit. Along with my flubs, flukes, and acclimation with tools - it took me 50 hours to make. It’s statistically accurate, carefully crafted, and like Hackaday said “right out of a 1970’s college textbook”. It’s how professionals might visualize data before computers could do it for them….
.
Last Week's Newsletter's 3 Most Clicked Links
Are there any small, quick things I can do everyday to keep my skills sharp? [Reddit] [ https://substack.com/redirect/692c2c8b-0277-4ed8-880a-e4ed93a8769d?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
After 5 years in data science, I’m starting to realize most “insights” we deliver are completely ignored. Is this normal? [Reddit] [ https://substack.com/redirect/dd7bc20b-9de8-49f5-942a-7e70390250c2?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Is logistic regression regression? [ https://substack.com/redirect/90cd73a6-f6f9-4055-8989-75bf19d367f7?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
* Based on unique clicks.
** Please take a look at last week's issue #652 here [ https://substack.com/redirect/a90309e9-8110-42f1-a978-316e68e4e46a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Cutting Room Floor
Lahman Baseball Database, created by SABR member Sean Lahman, contains complete major league batting and pitching statistics back to 1871 [ https://substack.com/redirect/137346c3-60da-415c-8609-f41a5ccc122f?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
A Data-Driven Survey of MLB Franchise Management [ https://substack.com/redirect/69a8a0b1-b4cc-4baa-a1db-c72c14d015ba?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Behavior-Driven Development in R Shiny: Modeling User Behavior with When Steps [ https://substack.com/redirect/94fb3b70-d6cd-494c-aa5e-bdbee80e3dec?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
I dont understand Standard Deviation [Reddit] [ https://substack.com/redirect/363485a0-650f-4fe8-a1d3-703dcc79e18c?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Good practices in data scripts [Reddit] [ https://substack.com/redirect/67961724-1c1b-4515-9ec6-eff39912b936?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
.
Whenever you're ready, 3 ways we can help:
Go deeper each week (paid subscription)
Get 3 additional posts per week designed to help you:
Statistics → understand the math behind ML
AI Agents → build with modern AI tools
Career → become more valuable at your job
👉 Upgrade for $10/month — cancel anytime [ https://substack.com/redirect/e906466a-944b-4321-80f1-dcd9d3316bc5?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Looking to get a job?
A practical guide to landing your first (or next) data science role, based on thousands of reader questions.
👉 Check out our  [ https://substack.com/redirect/453f1d98-8ddc-4a43-8454-94c0b5d8f78a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]“Get A Data Science Job” [ https://substack.com/redirect/453f1d98-8ddc-4a43-8454-94c0b5d8f78a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] Course [ https://substack.com/redirect/453f1d98-8ddc-4a43-8454-94c0b5d8f78a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
Promote your organization/project/event to ~68,500 subscribers
Sponsor this newsletter and reach a highly engaged data science audience (30–35% open rate).
👉 Reply to this email to learn more
Thank you for joining us this week! :)
Stay Data Science-y!
All our best,
Hannah & Sebastian
Data Science Weekly Newsletter is a reader-supported publication. To receive new posts and support our work, consider becoming a free or paid subscriber.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9kYXRhc2NpZW5jZXdlZWtseS5zdWJzdGFjay5jb20vYWN0aW9uL2Rpc2FibGVfZW1haWw_dG9rZW49ZXlKMWMyVnlYMmxrSWpveU5qa3dNVGt4TENKd2IzTjBYMmxrSWpveE9UazJNakUwTmpBc0ltbGhkQ0k2TVRjM09UazVOekk1TkN3aVpYaHdJam94T0RFeE5UTXpNamswTENKcGMzTWlPaUp3ZFdJdE1qSTJPU0lzSW5OMVlpSTZJbVJwYzJGaWJHVmZaVzFoYVd3aWZRLklzWk4wLVJSRjVkdkNSYWRfaFp2VDZObUItOTZDeUVwNHVtTDdBaHdvRFEiLCJwIjoxOTk2MjE0NjAsInMiOjIyNjksImYiOnRydWUsInUiOjI2OTAxOTEsImlhdCI6MTc3OTk5NzI5NCwiZXhwIjoyMDk1NTczMjk0LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.VyUO1zxiwXM_zjbkE35KSjfgJ9zOIBV6r-Q4uMMGZv4?
