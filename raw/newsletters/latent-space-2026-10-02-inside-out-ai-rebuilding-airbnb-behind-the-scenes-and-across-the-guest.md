---
source: gmail
newsletter: "latent-space"
message_id: "1a0fcf5fa978c82b"
thread_id: "1a0fcf5fa978c82b"
subject: "Inside-Out AI: Rebuilding Airbnb Behind the Scenes and Across the Guest Experience"
from: "\"Latent.Space\" <swyx@substack.com>"
date: "Fri, 2 Oct 2026 14:04:49 +0000"
ingested: 2026-10-05
sha256: df9abef72cf7213960cb9c8db57e1b3bbb925ddfb63af270b7d63423ac3bb806
---
View this post on the web at https://www.latent.space/p/airbnb

Prior to joining Airbnb as CTO in January, Ahmad Al-Dahle [ https://substack.com/redirect/3137297c-b086-4c82-aef3-6210254a68e6?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] was head of generative AI at Meta and led the launch of its open source Llama models over 2023-2025. Now Al-Dahle is in charge of turning Airbnb into an “AI-native company”.
What that means in practice is using AI internally to speed up product development, then using those same capabilities to transform the customer experience. We’re calling this an “inside-out AI” approach and in this article we’ll dig into the details.
Al-Dahle spoke with Latent Space about Airbnb’s AI transformation. We began by asking him why he made the shift from building frontier models at Meta to deploying them at Airbnb.
“Fundamentally, I like to chase where I believe the hard frontiers live,” he replied, pun perhaps intended. “We kind of knew [at Meta] what the flywheel looks like, we understood how to improve the model capabilities, generation on generation.”
The next challenge, Al-Dahle thinks, is deploying models at scale. At Airbnb, his goals are to “push people to work differently, because these tools are transforming how you work,” and to “take these systems and deploy them in production, in creative ways that actually add value to a core user experience.”
Jumping to prototypes, code is the artifact
From its launch in 2008, Airbnb has been considered a technology company operating in the hospitality industry. The company went public in 2020 and now has a market capitalization of approximately $93 billion (at time of writing). So it’s a big operation to try and make “AI-native.”
Al-Dahle reeled off a few statistics to show that Airbnb is AI-pilled now: 60% of its code is now AI-authored, it has shipped nearly 80% more features and improvements year over year, and pull-request throughput for the average engineer is up about 1.6x.
But how exactly has Airbnb done all this?
Firstly, he said it’s about changing the organizational process for software engineering. Traditionally, you might do product requirements, then design work in Figma, then engineering implementation, and eventually production testing. In the past, these would’ve required handoffs from one team to another. But now, Airbnb has its product, design and engineering teams move directly to working with prototypes.
“Breaking that time down is actually one of the biggest savings that a lot of traditional software companies have to make the leap to do,” said Al-Dahle. “And so we made that leap and it actually ended up adding a ton of tailwind to our product development process.”
A byproduct of this change is that teams deal directly with code, rather than dealing with “artifacts” like a product requirements document.
“We moved away from excessive artifact generation to the code being the artifact that we reason upon, and prototypes,” he said.
AI resolves roughly half of support tickets
Al-Dahle told us that customer support was the first user-facing area that it introduced AI into. He described it as “the hardest problem to deploy,” because “the stakes and the consequences of a mistake are really high.”
Roughly half of Airbnb’s support tickets are now resolved purely by AI, said Al-Dahle (this is in line with the company’s Q2 results [ https://substack.com/redirect/6f22ec6e-2409-4748-83bd-f19d67f39c7e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], which put the figure at nearly 45%).
The key to this, he says, is using synthetic data to thoroughly test the system before taking it to production.
“We start with: build a model, build the agent, and begin to generate a battery of synthetic data before you ever go into production.”
He notes that although agents handle about half of customer support queries, they are careful about what requires human assistance — with safety issues, for example.
“So while we solve 50% of the tickets, we’re actually deliberate about the tickets we don’t choose to solve yet [with agents].”
Everest, Airbnb’s AI context graph
Two Airbnb Services [ https://substack.com/redirect/6ff9ddca-47d1-4a88-8f54-ec63699f2699?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] projects you may not be familiar with yet are grocery deliveries and airport pickups (the grocery service has just been expanded to more cities [ https://substack.com/redirect/c240aeaf-6a39-4d03-bcc3-61606bfb6711?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]). Both were launched earlier this year, thanks in part to Airbnb’s inside-out AI approach.
It was an internal organizational context graph called Everest that helped bring these products to market quickly. Al-Dahle said that Everest uses technologies such as LLMs, embeddings and AI-based retrieval to build and query the graph.
He explained that the grocery delivery and airport pickup services are “kind of similar services — API integrations with partner services [external companies] that integrated onto our platform.” 
The grocery service was built first, and learnings from it were made available in Everest. That enabled the airport pickup team to do its project much more quickly. In its Q2 earnings report [ https://substack.com/redirect/5fb78c64-2641-4bd3-8f8c-9c2fb8c42d87?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], Airbnb states that “groceries took eight months, nine months and airport pickups took about six weeks to develop.”
Additionally, using Everest means its developers don’t necessarily need specialist knowledge to work on projects.
“Because of this context graph that exists across the codebase,” said Al-Dahle, “we’re able to have generalists work across very specialist parts of the code.”
Both of the new services were highlighted by CEO Brian Chesky at Airbnb’s 2026 Summer Release [ https://substack.com/redirect/dd008ce6-373f-4a13-b81f-37911bde0c48?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] in May.
Choosing which models to use and customizing open models
To give more of a sense of Airbnb’s internal AI usage, Al-Dahle described it as a “multi-model company” and says it deploys “a lot of different models” in its production systems.
Airbnb uses a mixture of frontier and open models, but conducts most of its own post-training and reinforcement learning on open models. Al-Dahle said the company deploys at least 10 customized models for production use cases.
It also evaluates models along a Pareto frontier for cost, performance and latency, selecting a different trade-off for each application.
“We run evals specifically for each use case,” he explained. “So if we’re using a model for search, we have a set of search queries that are sampled from production that we measure against. If we’re doing customer support, we also sample all the production queries that we care most about — including edge cases.”
“We try to use the right tool for the right job,” he added. For example, coding can tolerate more latency but mistakes are expensive. So they prefer to use the strongest available frontier model for coding tasks.
“It makes sense to use the absolute most frontier coding model, because for every defect that a model produces, it could easily cost us a lot more.”
On the other hand, search is used at scale by Airbnb’s users and so is very latency-sensitive. So for that job, they prefer smaller specialized models. Al-Dahle claimed that smaller, post-trained models sometimes out-perform frontier models.
“For narrow use cases, we’ve been able to take really small, really nimble models that are very fast and cheap and post-train them beyond the frontier.”
Async agents: the next big shift
Like other AI-native companies [ https://substack.com/redirect/ba503224-c96b-428b-aa7c-35fc69e210d3?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], Airbnb has created an internal agent — in its case called AirChat.
“We have our own internal agent that we call AirChat, which [includes] basically all the necessary MCP organizational context,” said Al-Dahle.
But Airbnb is also starting to implement what Al-Dahle sees as the next development in agents: asynchronous agents running in containers and activated by events.
“A lot of our teams are starting to basically automate their on-calls,” he explained. “So if something trips, if a Grafana limit or whatever monitoring system that you use trips, agents spin up to then triage and run your on-call, your initial on-call.”
A human engineer can review a PR proposed by the agent, while the agent may close the incident itself if it determines that the alert was flaky.
This process reminds us of how open source projects like Vercel’s AI SDK, Astro, Flue and tldraw use software factories — teams of agents — to apply fixes and features [ https://substack.com/redirect/6417cf27-8b4c-4932-9aaa-da33e464520b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Al-Dahle sees this approach eventually being used across its entire marketplace platform; for example to monitor fraud, “trust violations,” marketplace quality, and software defects.
“My vision is large amounts of asynchronous agents that are helping automate and manage the marketplace.”
Maintaining the craft of software engineering
Al-Dahle believes that organizing teams around outcomes rather than features is key to becoming an AI-native company.
“If you’re a company that organizes by feature development, you’re going to struggle in the age of AI,” he said. “If you’re a company that organizes by objectives and missions and results that you’re trying to achieve, you’re going to be fine.”
That said, there’s one thing Al-Dahle worries about during this AI-native transition: whether junior engineers are developing their craft and judgement, given that AI is able to do so much work for them now.
Senior engineers, he says, have acquired their judgement through many years of shipping systems and operating software in production — including the mistakes they made along the way.
Part of the solution, Al-Dahle says, is ensuring all of their engineers can explain the work AI does for them.
“One of the things I’m pushing very strongly is that every engineer must be able to explain, even if an AI generated the PR, must be able to explain what they built. I think if that fundamental premise remains true, then more junior engineers will learn the craft of interface design and architecture, and the importance of testing and unit testing and integration tests. So we’re trying to keep our craft really high.”

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3lOamt3TVRreExDSndiM04wWDJsa0lqb3lNVGcwTURZeU1qZ3NJbWxoZENJNk1UYzVNRGsxTURNM015d2laWGh3SWpveE9ESXlORGcyTXpjekxDSnBjM01pT2lKd2RXSXRNVEE0TkRBNE9TSXNJbk4xWWlJNkltUnBjMkZpYkdWZlpXMWhhV3dpZlEudGtWdnEzNWNWWGtSNWF1djRkN3FnZUx6Ynd4cXBSVWI3RkpWaDRQWUhhUSIsInAiOjIxODQwNjIyOCwicyI6MTA4NDA4OSwiZiI6ZmFsc2UsInUiOjI2OTAxOTEsImlhdCI6MTc5MDk1MDM3MywiZXhwIjoyMTA2NTI2MzczLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.8kBKqUqh6JfA8uoeaqfXOKHeFP2cm5BFXWPLmPRS8Ts?
