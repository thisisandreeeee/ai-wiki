---
source: gmail
newsletter: "latent-space"
message_id: "1a12628bd64230e0"
thread_id: "1a12628bd64230e0"
subject: "Building AI for Reliable Execution: Lessons From Industrial Robotics"
from: "\"Latent.Space\" <swyx@substack.com>"
date: "Sat, 10 Oct 2026 14:04:11 +0000"
ingested: 2026-10-12
sha256: 6717f30e63bb1677b52b434fea88d3fa98a24e15c0acb827f924d1e624e42c12
---
View this post on the web at https://www.latent.space/p/standard-bots

When you think of robotics and AI, you probably first think of full humanoid robots like Figure’s AI-powered machines [ https://substack.com/redirect/f1d524da-2ee6-45f5-af33-25abe3e8eda7?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] and 1X’s NEO home robots [ https://substack.com/redirect/2687cdf9-ae09-43b8-86b6-a3e123598638?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]. Those may well be the future, but arguably more important in 2026 is industrial robots — which are typically not humanoids.
Standard Bots [ https://substack.com/redirect/03833180-728d-45eb-9a78-f98e82fa9128?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] claims to be “America’s largest AI-native industrial robot manufacturer.” It recently raised $200 million [ https://substack.com/redirect/58f457d9-1292-4927-9a63-1f6058bb3f3c?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] at a $1 billion valuation, in a series C round led by General Catalyst and RoboStrategy, a fund focused on robotics. Its customers include NASA, Amazon and Lockheed Martin.
We spoke to Evan Beard [ https://substack.com/redirect/1db773a3-203f-4c61-8661-59b94a658653?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], co-founder and CEO, and Leif Jentoft [ https://substack.com/redirect/c6db13a9-4505-4a30-a28a-e2c414566ab6?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], Head of AI, to find out more about Standard Bots’ AI stack and how its models work.
To set the scene, Standard Bots’ industrial robot arms are designed for tasks such as machine tending, welding, and assembly. Here’s a quick demo by Jentoft:
Pretrained models and task-specific adaptation
According to Beard, Standard Bots has a shared base model that customers adapt through demonstrations and fine-tuning. Jentoft added that Standard Bots runs a range of models, including a zero-shot perception system for machine tending.
Beard says its largest model is in the low billions of parameters — so it’s not that large by frontier lab standards.
“We believe data quality matters far more than raw volume,” said Jentoft,  “and we focus on getting the most out of targeted data rather than chasing the largest possible dataset.” (This matches the “bitterest lesson” of Jev creator Diogo Almeida [ https://substack.com/redirect/254d9ead-8c10-47f8-9790-330ba6ae7587?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], who told us recently that the right task and the right data can matter more than compute.)
“Our market access gives us unique access to the highest value data,” he added. “In-situ interventions can fix an edge case with a few dozen examples.”
Beard notes that Standard Bots focuses on short-horizon tasks to meet production requirements for cycle time and reliability. The company uses conventional programming for parts of a workflow that don’t require learned behavior.
Model training happens in the cloud but inference runs locally, said Beard.
What does the model do exactly?
I asked Jentoft what the learned model does in a typical robot routine, and which parts of the workflow use conventional programming?
As an example, he brought up its machine-tending solution for high-mix manufacturing.
“We’ve built a zero-shot system that lets a user tell the robot which parts to look for on a given task. The model handles perception — locating and identifying the parts — while conventional programming handles the motion and the cell logic around it.”
Here’s a demonstration of the machine-tending:
“Our backbone for this task is trained on over a billion images, which is what lets the robot distinguish between lighting conditions, material types, and an object versus its background,” Jentoft said.
The Full AI Stack
Back in April, we had Applied Intuition on the podcast [ https://substack.com/redirect/7379003d-33f7-4a58-be04-eac0e5203a3e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] to talk about “Physical AI” and how it differs from on-screen AI. One of the learnings was that the Physical AI isn’t just constrained by model intelligence: the hard part is deploying models onto real hardware, under safety, latency, power, cost, and reliability constraints.
But for Standard Bots, that can also be a strength, since it controls the “full stack” from software to hardware. Jentoft points out that it controls the robotic arm, end effector, control system, and AI.
“That lets us co-optimize the models and the control policies,” he said. “Despite claims elsewhere, no model today is truly hardware-agnostic, and co-optimizing low-level control and higher-level functions is a major advantage for both performance and iteration speed.”
Skild, a company aiming to build “general purpose robotic intelligence,” might quibble with the hardware-agnostic claim — its goal is to achieve cross-hardware generalization [ https://substack.com/redirect/dbf242db-33ee-4cea-8fcc-a78b33543281?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
On-prem inference: sensors, edge GPUs, and ‘action chunks’
Beard had mentioned that inference is done locally, which is especially important for its core customers: factories.
“For factories, which is most of what we’re doing right now — and certainly so much opportunity that we see there — this is something where you need to do inference on-premise,” he said.
For machine tending, the model identifies parts while conventional programming handles motion. Jentoft also described how models can generate actions that feed into the robot’s control system.
“Wrist cameras and other sensors feed raw pixels and signals into the system over internal gigabit Ethernet, routed internally so no cables tangle,” he explained. “GPUs at the edge process that data to generate action chunks, which stream to low-level control.”
He reiterated that inference is run on-premises deliberately.
“Cloud compute for robotics is operationally extremely hard — most factories and warehouses don’t have reliable internet, and that’s even more true for mobile robots. Uptime is crucial to customer acceptance, so we keep the loop local.”
Production failures and fleet learning
Standard Bots uses simulation where it can, but Beard says some production tasks — including those involving liquids, suction, or cutting flexible material — are difficult to reproduce in current simulators.
Real-world demonstrations are another part of the learning process. Here’s a demo of teaching a robot using a handheld touch device:
So how does it deal with failure in a robot task, and do those kinds of learnings flow back to the model?
“We capture failure signals and human corrections from deployments, and how we use that data depends on the customer,” Jentoft replied.
He noted that many of its defense customers “deploy in air-gapped environments, where nothing comes back.” But for customers that aren’t air-gapped, “fleet learning delivers enough benefit to their own applications that we typically don’t see pushback on contributing data in exchange for that performance.”
StandardOS: an AI robotics dev platform
Standard Bots has already expanded its platform so that external developers can use it. With StandardOS [ https://substack.com/redirect/f4ae3082-6f38-47cd-a12b-e503a5c19fd8?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], it offers a set of APIs and SDKs.
According to Beard, developers can use Standard Bots’ APIs to build robotics applications with whichever parts of its stack they need, including bringing their own models. He cited NVIDIA Cosmos [ https://substack.com/redirect/aa1570be-8100-44ea-b63e-de8503766257?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], an open family of omnimodal world models for physical AI, as an example (version 3 was released late-May [ https://substack.com/redirect/e6e56d69-eec2-4476-9394-f0b92f0c3c36?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]).
Today, this requires developers to write their own integration code. But Standard Bots plans to make collecting data, training models, and deploying them onto its robots easier.
Focus on targeted data
Standard Bots isn’t the sexiest robotics company out there, but it is already being deployed for industrial automation at NASA, Amazon, Lockheed Martin, and others.
For AI engineers, perhaps the most useful lesson is how Standard Bots adapts AI to a specific job. It keeps the model’s role focused and uses corrections from real deployments to fix edge cases. You can, of course, apply that same approach to software agents.
As Jentoft said — and it was a recent lesson from Jev too — it’s all about “getting the most out of targeted data rather than chasing the largest possible dataset.”

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3lOamt3TVRreExDSndiM04wWDJsa0lqb3lNVGsxT1Rrek1EZ3NJbWxoZENJNk1UYzVNVFkwTVRVMk15d2laWGh3SWpveE9ESXpNVGMzTlRZekxDSnBjM01pT2lKd2RXSXRNVEE0TkRBNE9TSXNJbk4xWWlJNkltUnBjMkZpYkdWZlpXMWhhV3dpZlEucHE4eElSX2xfMTAxS3BhQU1JdXV4dEtMbDFOV3dyN3JmME1FRzQ0RmlRVSIsInAiOjIxOTU5OTMwOCwicyI6MTA4NDA4OSwiZiI6ZmFsc2UsInUiOjI2OTAxOTEsImlhdCI6MTc5MTY0MTU2MywiZXhwIjoyMTA3MjE3NTYzLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.MNpahxA7FKs1HSViiMEs3ehcOBT9fCAwj3xkGSUqLsI?
