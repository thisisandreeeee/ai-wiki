---
source: gmail
newsletter: "latent-space"
message_id: "1a116b6285816562"
thread_id: "1a116b6285816562"
subject: "Can a Cloud-Native Harness Make Agents Reliable Beyond the Desktop?"
from: "\"Latent.Space\" <swyx@substack.com>"
date: "Wed, 7 Oct 2026 14:10:45 +0000"
ingested: 2026-10-12
sha256: fcd2ba9b94d336a00468c6769c9c471dc3dc2ff073a763e07f55a6be71e9559b
---
View this post on the web at https://www.latent.space/p/stacklok

At a high level, coding agents have a basic architecture: an LLM calls tools in a loop, while carrying forward the required context. Since that’s easiest to implement locally, many coding agents started out as terminal tools and then desktop apps (Claude Code famously began as a CLI tool). But as the open laptop meme illustrates, modern agent harnesses have frustrating limitations if they’re not able to be managed in the cloud.
Since 2025, both OpenAI and Anthropic have been trying to shift their harnesses more into the cloud — but with varying levels of success. The challenges include keeping sessions reliable, isolating tool execution and preserving context.
This sounds a lot like container orchestration in the early 2010s, from which emerged the open source Kubernetes in 2014. Kubernetes, developed by Google, became the dominant open source system for deploying and managing cloud applications at scale — it kickstarted the “cloud native” era of computing.
Kubernetes uses control loops to keep applications running, recover from failures, and scale when needed. What if coding agents could be managed in the same way?
That’s the bet that two Kubernetes creators, Craig McLuckie [ https://substack.com/redirect/45261eea-f546-4cb8-848a-e767c9c2c260?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] and Joe Beda [ https://substack.com/redirect/32ff3828-bc00-4600-b0a0-2354fdee41a4?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], are making with Stacklok [ https://substack.com/redirect/57120505-7de5-40c1-8a04-fafb3bafcfa8?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Stacklok raised a $17.5 million Series A [ https://substack.com/redirect/b4083b7e-bdbc-4ab6-afb8-c66099ff95e7?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] back in 2023 from Accel, Madrona and Bain Capital. Initially focused on software supply chain security [ https://substack.com/redirect/45be8da8-a014-4bda-ae82-00846a6661db?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], the company recently pivoted to Kubernetes-based agentic solutions.
Mecatl: a harness built for the cloud
The most interesting product of Stacklok is Mecatl, a “cloud-native harness” begun in June as an open source project on GitHub [ https://substack.com/redirect/28cf442c-a125-40a9-8084-3b4bb12e2373?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]. At first, I thought the name was pronounced “me-cattle” — a play-on-words referencing the ‘cattle vs. pets’ concept of Kubernetes, where you treat your servers, pods and clusters like cattle rather than pets. But no, the name is actually pronounced “MEH-kah-tl” and is an Aztec word meaning a cord or rope!
In any case, what does cloud-native mean in the context of a harness?
It’s primarily about “moving the locus of value from the desktop to the cloud,” said McLuckie. He’s talking about “value” from an enterprise perspective — that the code and context are often derived from local environments. “That’s where the IP sits,” Beda chimed in. “And if you want to be able to actually bring that under management, it’s that much more difficult when it’s sitting on a desktop.”
McLuckie added that a cloud native approach also allows Stacklok to ask some deeper questions about agentic coding.
“Why is the agent loop so intricately coupled to the tool calling subsystems? Why is agent identity being reasoned about through the lens of human identity systems?”
When it comes to open source agent harnesses, there are already well-regarded solutions — such as Pi [ https://substack.com/redirect/83f88491-c65e-47de-9f74-cc81718a4929?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], a “minimal agent harness” that projects like Flue have built on top of [ https://substack.com/redirect/95342d64-b876-4ae5-96ef-bb5aee4fdc5b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]. We asked the Stacklok pair what makes their harness different?
Beda didn’t mention Pi specifically, but he did say that in desktop-first harnesses, the loop, local execution and session state often begin inside the same process.
“There are a ton of solutions in this space, but they’re all focused to essentially run on the desktop,” he said. “So even if they have pluggability, the architecture is still one process, or one set of tightly coupled processes, that are built to run on the desktop.”
But can’t enterprises use VMs, containers, or one of many different sandbox products to move their harness to the cloud?
Beda says this “lift and shift” approach tends to create issues around the lifecycle of an agent or being able to quiesce it (safely pause it while it waits for human input).
“Our thinking is, well, what if we rethought the harness from the ground up to actually run in the cloud?”
Separating the agent loop from execution
One of the intriguing approaches of Mecatl is that it keeps the agent loop independent of the client, model provider, state store and execution environment.
“This is an application that we know how to run in the cloud well,” said Beda, regarding the loop application. “What if we take that and we separate that out from the more sensitive operations, like tool calling and bash, and then also separate out things like session management and memory, so that these things are no longer stored as JSONL files sitting on disk, but can natively be put into manageable systems”
A lot of you reading this will probably have very opinionated harnesses, customized for your own requirements. But Mecatl is designed to extend beyond a single-user, local harness into infrastructure that enterprises can operate centrally. Beda likened this to how enterprises manage email.
“We think, in the future, interactions that you have with an agent while you’re working for an enterprise belong to that enterprise; and they’re going to want to manage that and govern that like they do email.”
Decoupling AI agents from frontier labs
One of the main motivations of Stacklok is to help large enterprises lessen their dependency on frontier labs and hyperscalers, such as Codex, Claude Code and GitHub Copilot. This, suggested McLuckie, is similar to how Kubernetes helps companies reduce dependency on the big cloud providers.
For McLuckie, the term “cloud native” came to represent a way to “run in a cloud that is decoupled from the specifics of the cloud provider. So a lot of what we’re trying to do [at Stacklok] is more or less what we did in the Kubernetes time.”
After its pivot into agent infrastructure, Stacklok built ToolHive — an open-source platform for running and governing MCP servers. It initially began as a way to manage MCP servers running in Docker containers on the desktop. Then, said Beda, they expanded it into a “Kubernetes-based gateway and other associated services — a registry and an operator helper for running and managing MCP servers and getting some of the input-output auth stuff right with those things.”
The idea, as McLuckie put it, was to enable enterprises that already ran on Kubernetes to “start to bring agentic workloads into those environments.”
Beda claims that many other agent tools were designed for individuals or small startup teams, which doesn’t fly for enterprise-scale companies.
“We talk to larger organizations and they’re struggling with like, how do I take this thing that was built for a team of six people and deploy it for an engineering task force in the thousands or tens of thousands.”
Stacklok’s LLM gateway
MCP was the first step. Next was building an LLM gateway, or “AI Gateway” as it’s called on the Stacklok’s website, to help companies control access and costs.
“Most of our customers are banks, semiconductor companies, telcos…you know, people operating in relatively regulated industries,” McLuckie said.
The AI Gateway is the one main product Stacklok hasn’t open sourced yet, but Beda says it’s “on our roadmap and we’re going to get there soon.”
Unlike Glean’s solution [ https://substack.com/redirect/1e8b58df-09ba-4c36-b13a-2ba1bf3304be?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], Stacklok’s AI Gateway does not currently choose a model based on the task. Instead, it focuses on access control, budgets, reporting and provider routing.
“We prefer to see the semantic-routing model choice happening in an intelligent system that’s honed in the harness, because there’s just more context there,” McLuckie explained.
The enterprise spine
Since both ToolHive (MCP platform) and Mecatl (the harness) are open source, what’s the business model for Stacklok?
McLuckie replied that ToolHive and Mecatl are both intended to be independently useful, but that the company offers things like consistent identity, authorization, policy and auditing across the open source parts.
“Our commercial product is the enterprise spine, the control plane that ties them all together,” he said.
“The open source projects are relatively easy to get up and running for a small team,” Beda added. “But once you start scaling these things out to multiple clusters, multiple clouds, [...] all sorts of new problems crop up there. And that’s what we’re focused on solving.”
The cloud native era for AI?
Amazon introduced S3 and EC2 — the beginnings of the cloud era — in 2006 [ https://substack.com/redirect/76a974d3-3f1c-48cf-a6e1-e86c3b22ce72?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], but at first these products were mainly used by startups and individuals. It took several years for enterprise solutions like Windows Azure to emerge, and then in 2014 Kubernetes arrived to manage containerized applications at scale.
We’re starting to see that same pattern play out with agentic technology. Enterprises don’t necessarily want to allow their employees to customize an open source harness, or even use frontier lab harnesses that run on their personal computers. Stacklok — built by two kings of cloud native — aims to solve those problems by bringing agent harnesses fully to the cloud.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3lOamt3TVRreExDSndiM04wWDJsa0lqb3lNVGt5TmpnMk1UVXNJbWxoZENJNk1UYzVNVE00TWpNNU9Dd2laWGh3SWpveE9ESXlPVEU0TXprNExDSnBjM01pT2lKd2RXSXRNVEE0TkRBNE9TSXNJbk4xWWlJNkltUnBjMkZpYkdWZlpXMWhhV3dpZlEuQkNKeDNfQm1DbE1pSzdpUE5URkZXVnlKY1NaSnNuMTRrZk0wdDNvU0szNCIsInAiOjIxOTI2ODYxNSwicyI6MTA4NDA4OSwiZiI6ZmFsc2UsInUiOjI2OTAxOTEsImlhdCI6MTc5MTM4MjM5OCwiZXhwIjoyMTA2OTU4Mzk4LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.EpQibYlJQrSKpPAHoYJHHbt1rPdi0_A3KGTFEn600NU?
