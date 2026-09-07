---
source: gmail
newsletter: "the-neuron"
message_id: "1a0593286af862e7"
thread_id: "1a0593286af862e7"
subject: "😺 OpenClaw 2.0 rebuilt the personal AI agent"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Mon, 31 Aug 2026 19:00:53 +0000 (UTC)"
ingested: 2026-09-07
sha256: 899f304807fc0f3134175026448ad91c3693dec6cda5d8c6f71cd6bb74131e0c
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b47452ee-e987-49c8-a482-3e77ae57b2e2/ChatGPT_Image_Aug_31__2026__11_19_40_AM.png?t=1788200407)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6cd21dfa-285c-45e6-bf78-c5e49964b2d7/In_Partnership_with_Alumni_Ventures.png?t=1780494754)
Follow image link: (https://www.av.vc/blog/ais-infrastructure-moment?utm_medium=email&utm_source=tofu&utm_content=partner-follow-up&utm_campaign=NeuronWebinarAugASend)
Caption: 

Welcome, humans.

Okay, so apparently data centers have become one of the few things Americans are willing to get arrested over.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ea1dbf64-8814-450a-b8b1-ef77ecd5c362/Screenshot_2026-08-31_at_11.33.35_AM.png?t=1788201225)
Follow image link: (https://www.reddit.com/r/Futurology/comments/1w2rcp5/the_number_of_regular_people_being_arrested_for/)
Caption: 

[Futurism counted at least 37 U.S. arrests](https://futurism.com/artificial-intelligence/regular-people-data-center-arrest-protest) tied to data-center protests this year, including a physics teacher from Kansas hauled out of a public meeting after clapping for an anti-data-center speaker. The crowd of those cuffed spans farmers, teachers, suburban parents, plus Zoomers and Boomers alike. 

_Cuffing season came early cause errybody in the club getting cuffed up! _

Also, this is starting to cost real money: [local opposition helped delay or block $130B](https://finance.yahoo.com/technology/ai/articles/59-american-oppose-ai-data-220000798.html) worth of U.S. data-center projects in Q1 alone. _Maybe it’s time we start referring to “the cloud” by its real name: the middle of the desert where nobody will complain about it. Or, y’know: __[actual space](https://www.bcg.com/publications/2026/space-based-data-centers-cost-outlook)__! _

**Here’s what happened in AI today:**

* 😺 OpenClaw 2.0 rebuilt setup, memory, and shared agents.

* 📰 OpenAI bought tens of thousands of Macs for agents.

* 📰 G20 leaders were warned frontier AI could shake finance.

* 📰 DiDi began fully driverless R2 passenger trials.

* 🎓 Build a citation-grounded project brain with Gemini Notebook.

…and a whole lot more that you can read about [here](https://theneuron.ai/digest/everything-that-happened-in-ai-today-friday-august-28-2026/).

Get your product / service in The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😺 OpenClaw 2.0 turns the DIY agent into a real platform

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/719e17b5-6043-414d-9c36-894e3e15ed60/Screenshot_2026-08-31_at_11.10.49_AM.png?t=1788199862)
Follow image link: (https://openclaw.ai/blog/openclaw-2-accidentally)
Caption: 

If OpenClaw, the personal AI agent tool always sounded like something that was too complicated or scary for you (_because you needed a terminal, three API keys, and a Saturday afternoon to pull your hair out trying to learn SSH and Gateways and whatever else_), there’s a new version out aimed at solving ALL THOSE problems.

The open-source personal agent just shipped [v2026.8.1, aka ](https://openclaw.ai/blog/openclaw-2-accidentally)**[OpenClaw 2.0](https://openclaw.ai/blog/openclaw-2-accidentally)**, its largest update yet. The project says 933 contributors, including 569 first-timers, merged more than 16,000 pull requests into this release. _May the vibes be with y’all._

**Here’s what happened:**

* Your first-run setup of OpenClaw 2.0 can actually reuse existing ChatGPT or Claude subscriptions, API keys, or local models.

* The browser app was rebuilt around ongoing conversations, dashboards, progress tracking, and interactive widgets.

* Shared cloud sessions can move work to paired devices or cloud workers, then hand the same session and context to another person.

* Memory adds conversation recall, background consolidation, and reusable-skill learning; Labs adds experimental Swarm and Fleet modes.

**Okay lets talk Swarm vs. Fleet:** [Swarm](https://docs.openclaw.ai/tools/swarm) mode is one OpenClaw task that spawns parallel subagents and collects their results. [Fleet](https://docs.openclaw.ai/gateway/multi-tenant-hosting) produces multiple isolated OpenClaw “cells,” each with its own Gateway, credentials, and state. 

Think of the difference like hiring a temporary team vs. setting up separate offices for different departments. _Remember offices with actual people in them?? _

**How to try OpenClaw 2.0:**

1. Open the [official install guide](https://docs.openclaw.ai/install). Mac, Linux, and WSL2 users can run the recommended installer; Windows users can use the signed Hub app or PowerShell installer.

2. Follow onboarding to choose your model and authentication, create a workspace, and install the Gateway as a background service.

3. Use the browser Control UI or [connect a messaging channel](https://docs.openclaw.ai/quickstart) like Telegram or Discord, then give your Claw one useful recurring workflow.

**Already using OpenClaw 1.0?** Back up `~/.openclaw`, switch to stable with `openclaw update --channel stable`, then run `openclaw doctor --fix`. [This release includes breaking migrations](https://github.com/openclaw/openclaw/releases/tag/v2026.8.1) for OpenProse and older OpenAI routes.

_And if all that’s confusing, just hand these instructions and links to your current agent to help walk you through it! _

**Why this matters:** OpenClaw is trying to move personal agents from hobbyist toy with lots of technical plumbing to navigate towards out of the box software normal people can set up and run themselves. 

The model under the shell of _the claw _can be OpenAI, Anthropic, Google, or your own local or cloud-based open model; OpenClaw 2.0 handles your memory, permissions, tools, channels, recurring work, and now, collaboration with others. 

The test from here is stability. [OpenClaw’s release notes](https://docs.openclaw.ai/releases/2026.8.1) change almost every layer, and its GitHub release explicitly tells existing users to back up before upgrading. _Can OpenClaw’s early adopters survive the transition, and is 2.0 enough to get normal people into the Eclawsystem? I guess it depends on if YOU, dear reader, try this version out or not! _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# Join us Sept 16: Where Private and Public Capital is Betting on AI   

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d8f59941-6842-4703-a083-95dcf43ed98e/Alumni_Ventures.png?t=1787676609)
Follow image link: (https://www.av.vc/blog/ais-infrastructure-moment?utm_medium=email&utm_source=tofu&utm_content=partner-follow-up&utm_campaign=NeuronWebinarAugASend)
Caption: 

Join Meera Oak, Senior Principal at [Alumni Ventures](https://www.av.vc/blog/ais-infrastructure-moment?utm_medium=email&utm_source=tofu&utm_content=partner-follow-up&utm_campaign=NeuronWebinarAugASend), and Corey Noles, Editor of The Neuron, for a fireside conversation on the AI infrastructure landscape — where private and public markets are placing capital, which companies are building the picks-and-shovels of the AI era, and how accredited investors can position themselves for one of the most consequential venture opportunities of the decade.

[Save my seat](https://www.av.vc/blog/ais-infrastructure-moment?utm_medium=email&utm_source=tofu&utm_content=partner-follow-up&utm_campaign=NeuronWebinarAugASend)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Build a Project Brain That Cites Its Sources

Reader request: how do you turn your own docs into a useful project brain without training a model? Our answer: Use [Gemini Notebook (formerly NotebookLM)](https://support.google.com/notebooklm/answer/16164461?hl=en), which answers from the sources you add and gives inline citations.

1. Create one notebook per project and add the official project Docs, PDFs, sites, videos, or Sheets.

2. For each question, select only the sources that should count as truth.

3. Ask for the answer, citations, contradictions, and missing evidence before you act.

```
Answer only from the selected sources. Cite every factual claim. If the sources conflict or do not contain the answer, say so and list the missing evidence.
```
**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

# Upgrade your voice stack with Deepgram Flux TTS

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d51d1af0-7cfa-453e-a366-bbb353b363b5/image__7___1_.png?t=1788105177) [Deepgram Flux TTS]
Follow image link: (https://deepgram.com/product/text-to-speech/flux?utm_source=fnf&utm_medium=newsletter&utm_campaign=september&utm_term=the-neuron&utm_content=flux-tts)
Caption: 

Flux TTS processes entire conversations rather than isolated text strings, keeping agent speech natural across multi-turn calls. You get as low as ~80ms streaming latency and native interruption handling built directly into the engine.

[Test it on your stack now.](https://deepgram.com/product/text-to-speech/flux?utm_source=fnf&utm_medium=newsletter&utm_campaign=september&utm_term=the-neuron&utm_content=flux-tts)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7c50cc1c-2643-430c-8085-3c13621c51e6/Screenshot_2026-08-31_at_11.47.11_AM.png?t=1788202042)
Follow image link: (https://www.reddit.com/r/LocalLLaMA/comments/1w3kppp/glm_53_and_glm_53_flash_ran_locally_on_rtx_pro/)
Caption: Pretty, pretty, pretty… pretty cool

* [OpenAI ](https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads/)said ChatGPT Ads hit a $1B annualized revenue run rate less than 200 days after launch, with tens of thousands of advertisers across 40+ countries.

* [OpenAI](https://www.theinformation.com/articles/apple-stumbled-ai-hardware-success-mac) reportedly bought tens of thousands of Macs for reinforcement learning and computer-use agent training, while Anthropic rents Mac capacity through AWS.

* [SB Energy](https://www.wsj.com/tech/ai/the-5-5-billion-perk-softbanks-data-center-venture-offered-to-land-openai-a5c7fb5e) gave OpenAI warrants now worth about $5.5B to secure the company as an anchor tenant for its planned data centers.

* [The Financial Stability Board](https://www.theguardian.com/business/2026/aug/31/advanced-frontier-ai-financial-stability-andrew-bailey-g20) warned G20 leaders that frontier AI cyberattacks could hit multiple financial firms at once and threaten global stability.

* [Sony and Warner music](https://www.theguardian.com/business/2026/aug/31/aanthropic-sued-alleged-theft-songs-ai-train-claude) publishers sued Anthropic, alleging it pirated tens of thousands of songs to train Claude.

* [DiDi](https://www.prnewswire.com/news-releases/didi-autonomous-driving-begins-fully-driverless-service-trials-with-next-generation-robotaxi-r2-302864755.html), the Chinese robotaxi company, began fully driverless R2 passenger trials in selected Beijing and Guangzhou zones, with rides bookable in the DiDi app.

* [Cloudflare](https://www.cloudflare.com/ru-ru/press/press-releases/2026/cloudflare-introduces-adaptive-intelligence-reverses-the-economics-of-automated-cyber-attacks/) launched Adaptive Intelligence, a bot-defense engine that continuously creates short-lived rules from live traffic to make automated attacks harder to sustain.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a73fabb2-038b-43ba-9c04-5395af635f69/Banner_01.png?t=1787939163) [3 Hours AI Tools Workshop sponsored creative]
Follow image link: (https://links.outskill.com/NEURSEP1)
Caption: 

1. *Outskill’s free 3-hour workshop shows you 15 AI tools and how to build an AI coworker that works 24/7 this Saturday. [Save my free seat](https://links.outskill.com/NEURSEP1).

2. [Fermion Research](https://www.fermionresearch.com/research/phonon-1) released Phonon-1, a 415 MB local English speech-recognition model that can transcribe an hour of audio in roughly 2.5 minutes on a laptop. [Try it here](https://huggingface.co/FermionResearch/Phonon-1).

3. [fal](https://fal.ai/learn/devs/introducing-h3-max-by-fal) released H3 Max, a post-trained MiniMax H3 variant that generates a five-second video in under three seconds in its tests. [Try the playground](https://fal.ai/models/minimax/h3-max/text-to-video).

4. [Google](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash) made Gemini Omni 1.1 Flash generally available for conversational video generation and editing, including extensions, interpolation, and 4K output. [Try it in AI Studio](https://aistudio.google.com/?model=gemini-omni-1.1-flash).

5. [Operant Semantic Firewall](https://www.operant.ai/platform/semantic-firewall) reads intent across prompts, tool calls, code, and data movement, then allows, blocks, or redacts risky agent actions in real time.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 😹 Monday Meme

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/43dd2a80-4496-4ca4-8df4-99547c52bb2d/Screenshot_2026-08-28_at_7.20.04_PM.png?t=1788105177) [Me chillin after vibe coding all day]
Follow image link: (https://www.reddit.com/r/aivideo/comments/1w0tfkq/me_chillin_after_vibe_coding_all_day/)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/73d2a892-f6d2-47e2-b9ba-2672fde8d65a/Noam_AliceAI_082626_A.png?t=1787682492)
Follow image link: (https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/)
Caption: Click the image above to watch on YouTube

**This new episode gets wild:** Noam Schwartz walks us through how hackers could “groom” an AI agent over time, then how a compromised agent could influence other agents almost like human radicalization. 

We also get into why prompt injection may never be fully solved and why agent security gets way scarier once AI can actually take actions. _Buckle up!! _

**Watch / listen:** [YouTube](https://youtu.be/SFBDQzSorRQ) | [Spotify](https://open.spotify.com/episode/40UWH75R7TRaeHS6N1zx6F?si=0xyXhTFfQ6GOj8DfRscWHA) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001)

_This video was sponsored by Dell AI Factory with NVIDIA._ [Learn more.](https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/)

**P.S:** We’re trying to hit** 50K subscribers** **on YouTube** this year. [Click here to help!](https://www.youtube.com/@theneuronai?sub_confirmation=1)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4851ef3d-f6a1-4667-94e5-d73d9795fd71/2026-08-31_-_Cat_s_Commentary.png?t=1786762132)
Caption: want this on my tombstone tbh

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today! 




**P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/openclaw-2-0-is-here
