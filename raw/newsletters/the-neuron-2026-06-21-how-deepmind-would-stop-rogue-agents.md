---
source: gmail
newsletter: "the-neuron"
message_id: "19eeb75744bf4c66"
thread_id: "19eeb75744bf4c66"
subject: "😼 How DeepMind would stop rogue agents"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Sun, 21 Jun 2026 18:32:54 +0000 (UTC)"
ingested: 2026-06-21
sha256: 67f97ea5664db0521979f7f2d4cfce05abff0c09276ea34f7685e5ea75cda26c
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ed375032-633c-4d6e-b34a-b2795bf9fc92/Gemini_Generated_Image_k9l4fik9l4fik9l4.png?t=1781875743)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f6d5e087-4753-47b0-9ec8-112c7341669b/In_Partnership_with_Outskill.png?t=1781798150)
Follow image link: (https://links.outskill.com/NEURON4?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=new-codex-copilot-hermes-and-microst-build-2026-ai-updates)
Caption: 

Welcome, humans. 

So apparently Americans are now spending **more than twice as much time with AI companions as dating apps**. That’s according to data from[ Sensor Tower’s State of AI 2026 report](https://sensortower.com/report/state-of-ai-2026) _(page 57)_ shared by[ Justine Moore](https://x.com/venturetwins/status/2066977528133415350). U.S. users reportedly spent around **700M hours** on apps like [Character.AI](https://Character.AI) and Talkie in Q1, while Tinder, Bumble, and friends held steady around** 300-400M.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c152285b-d22b-4049-91e6-7a68c5552146/Screenshot_2026-06-18_at_3.02.59_PM.png?t=1781820289)
Follow image link: (https://x.com/venturetwins/status/2066977528133415350)
Caption: 

Okay, despite it being _horrifying _news, this actually makes sense… in the bleakest possible way: Dating apps ask you to be charming, attractive, emotionally available, geographically convenient, unreasonably comfortable with constant rejection, or the reverse, _unreasonably comfortable with rejecting others__, _and willing to answer (or dodge) the “what are you looking for?” question for the 900th time. 

AI companions ask you to open the app… and chat (_no strings attached). _Whenever you want to stop the convo, you stop. And when you come back, it’ll be like you never left: _AI have no sense of time (at least not now). _

**Both stats show us the obvious:** people want connection. _Congrats to AI. It has discovered the killer app: responding back!_ The uncomfortable part? People also want no strings attached, _convenient,_ connection; connection without ghosting, rejection, calendar coordination, awkward first dates, or any effort whatsoever. As [X user Signüll calls it](https://x.com/signulll/status/2066990366029459933): _frictionless intimacy. _

Could this trend also correlate with [the new paper](https://www.nber.org/papers/w35310) that tracks the rise of smartphones against the fall of birth rates? _Certainly not because of AI companions, as those are too new to be reflected in the data. But smartphone use and the drop in in-person socialization and increased desire for and access to frictionless experiences in general that followed? Probably! _Anyway, the whole [SensorTower report](https://sensortower.com/report/state-of-ai-2026) is epic. Check it out. 

**Here’s what happened in AI today: **

* 😼 Google DeepMind published an AI Control Roadmap for securing powerful internal agents.

* 📰 Anthropic said Claude completed shared robot tasks 18-37x faster than earlier human teams.

* 📰 Dean Ball joined OpenAI to lead a Strategic Futures team focused on frontier AI policy.

* 🌟 This week's best skill: make your agents prove their work before they touch the real workflow.

…and a [**whole lot more that you can read about here**](https://www.theneuron.ai/explainer-articles/-everything-that-happened-in-ai-today-friday-june-19-2026/).

**Hey: **_Want to reach 700,000+ AI-hungry readers? _[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[ ](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😼** ****Google DeepMind is preparing for the AI agent that goes off-script**

The next phase of AI safety looks less like philosophy and more like IT security. Passwords. Logs. Permissions. Monitors. Emergency brakes.

[Google DeepMind](https://deepmind.google/blog/securing-the-future-of-ai-agents/) published an AI Control Roadmap for securing powerful internal AI agents. The basic assumption is refreshingly practical: even if a model is trained to be helpful, the system around it still needs controls for the day it behaves badly.

**Here's what happened:**

* DeepMind framed advanced agents as potential insider threats, similar to employees with access to sensitive systems.

* The roadmap adds system-level security on top of alignment, meaning training the model to behave well is only one defense.

* Trusted AI supervisors would monitor an agent's reasoning, actions, and plans.

* Controls would scale by risk, from delayed review for low-risk actions to real-time blocking for dangerous ones.

This matters because agents are no longer just answering questions. They are reading files, browsing the web, calling tools, writing code, and carrying out multi-step work. Anthropic's robotics update made the same shift concrete from another direction: Claude is starting to coordinate physical tasks, not just screen work. That makes agent safety less theoretical and much harder to fake.

**Why this matters: **The hard problem is moving from chatbot safety to workflow safety. A wrong answer is bad. A wrong action can delete data, leak a file, approve a payment, or quietly sabotage a project.

DeepMind's roadmap borrows from cybersecurity because cybersecurity already knows a painful truth: trusted systems can still be compromised. The future agent stack will probably look like a mix of model evals, access control, audit logs, sandboxing, and AI supervisors watching other AIs.

DeepMind also named the metrics that make this more than hand-waving: coverage (how much agent traffic is monitored), recall (how much bad behavior gets caught), and time-to-response (how fast the system can stop it). That is safety as operations, not a blog-post promise.

**Our take: **The companies winning agents may be the ones that make autonomy boring. The magic demo matters less than the permission system that keeps the magic from touching payroll at 2 a.m., or quietly emailing a customer before a human sees the plan.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS **

# Make Claude Your 2nd Brain That works 24/7 By Mastering In It 16 hours- Here’s How

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/64c7c1dd-d2b8-454c-b9d3-e973f5c7bff8/Outskill.png?t=1781798182)
Follow image link: (https://links.outskill.com/NEURON4?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=new-codex-copilot-hermes-and-microst-build-2026-ai-updates)
Caption: 

Claude is currently the most powerful tool of 2026. It's been launching new features every week- Skills, Connectors, Cowork, vibe coding. Yet almost no one knows how to actually use them.

Our expert mentors have condensed 800+ hours of Claude research, articles, YouTube content and real-world practice into a focused 16-hour curriculum. Join the [**2-Day Claude AI Mastery Workshop**](https://links.outskill.com/NEURON4?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=new-codex-copilot-hermes-and-microst-build-2026-ai-updates): a live, end-to-end deep dive into Claude plus 10+ AI tools, LLMs and workflows.

It would be silly not to **[SIGN UP](https://links.outskill.com/NEURON4?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=new-codex-copilot-hermes-and-microst-build-2026-ai-updates)**

The professionals who master Claude right now will design carousels in seconds, ship code without being developers, and have AI working for them while they sleep. 

You will learn how to:

* master Claude's three modes : Chat, Cowork and Code. 

* Set up Skills, Connectors and Plug-ins to automate your desktop, Notion and files. 

* Vibe code apps and dashboards without writing code & 10+ AI tools and workflows that pair with Claude.

🧠 Saturday & Sunday

 🕜 10 AM – 7 PM EST

[Register NOW!](https://links.outskill.com/NEURON4?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=new-codex-copilot-hermes-and-microst-build-2026-ai-updates)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Make ChatGPT judge its own work before you see it

When using /goal with any task (knowledge work or coding), a smart fix comes from [Matt Berman](https://x.com/MatthewBerman/status/2067458261285241227): use an LLM-as-a-judge loop, which means asking one AI pass to create the “goal” you want to achieve. 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/301beeec-6b0e-4865-b367-7d1867a7a1e6/Screenshot_2026-06-19_at_9.17.15_AM.png?t=1781885932)
Caption: 

**Try it like this:** ask Codex to optimize a slow dashboard “until the page loads as fast as possible without changing what users see,” or clean up a messy internal process doc “until a teammate could follow it without Slacking you three questions.” Here’s the prompt:

```
/goal

Work toward this outcome:
[describe the task]

Before starting, define what “good enough” means for this task.

Create 3-5 success criteria Codex can keep checking while it works. Include any hard requirements, tests, files, constraints, style rules, performance targets, or user-facing behavior that must be preserved.

Then work in a loop:
1. Make the next useful improvement.
2. Judge the result against the success criteria.
3. Identify the biggest remaining gap.
4. Continue until the work meets the goal.

Return:
- The final result
- The success criteria you used
- The biggest change you madeoved.
```
**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform) 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🍪 Treats to Try 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/17883aad-3fc9-4324-9eb3-a643ead15fd7/Creai.png?t=1781796116)
Follow image link: (https://www.creai.mx/lets-build-together)
Caption: 

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

* *Discover what the right AI implementation can do for a company like yours. [→ Let's build it together.](https://www.creai.mx/lets-build-together)

* [Poolside](https://huggingface.co/collections/poolside/laguna-m1) released Laguna M.1 as open weights under Apache 2.0 with 226B parameters and 256K context.

* [Viktor](https://viktor.com/) lives inside Slack and Microsoft Teams as a work agent that can run reports, build dashboards, write code, and connect to 3,200+ tools - free to start.

* [Adapt](https://adapt.com/) gives your company a shared brain in Slack and on the web so people and agents can answer questions and act across tools - $100 free credits.

* [Juno](https://github.com/Cassini-Research/Juno) turns your Mac voice notes into clean text inside Mail, Slack, Notes, Cursor, and the apps you already use - free/open source.

* [VoiceOS](https://www.voiceos.com/) lets you dictate, search, send messages, and automate desktop tasks by voice on Mac and Windows - no pricing details.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# **NEW interview: Andrew Dai on why AI still can’t really see.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a0757820-427b-44da-939b-ca5fceeec8a3/TN_Thumbnail_AndrewDai_1.png?t=1781718367)
Follow image link: (https://www.youtube.com/watch?v=hMS-2l-p9tM)
Caption: 

Andrew Dai, former Google Brain / DeepMind researcher and now CEO of[ Elorian](https://elorian.ai/), joined us to explain why today’s AI can write code, read docs, and build apps, but still misses visual problems a grade-schooler could spot in seconds. 

In our latest episode, Andrew unpacks why image description is not the same as visual reasoning, why models may need a “visual scratchpad,” and why better vision could unlock stronger coding agents, robotics, design review, and physical-world engineering.

🎧 **Watch / Listen:**[ YouTube](https://youtu.be/hMS-2l-p9tM) |[ Spotify](https://open.spotify.com/episode/5xHGFl9oM2qhLWzsmXnU21?si=hn0tvPVRSGuf2XUqlxP0Ng) |[ Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001)

_Special shout out to this episode’s sponsors, _[_Dell Technologies and NVIDIA_](https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-elorian-wants-to-fix-ai-s-toddler-vision&_bhlid=47159c0785d7a7c82b378a9d68c66153269848d3)_ and _[_Outshift_](https://outshift.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-elorian-wants-to-fix-ai-s-toddler-vision&_bhlid=b896ab3790a28113a458f9e45affa599051e539d)_! _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn 

* [Anthropic](https://www.anthropic.com/research/project-fetch-phase-two) said Claude completed shared robotics tasks more than 18-37x faster than human teams in the original Project Fetch experiment.

* [Dean Ball](https://www.axios.com/2026/06/18/dean-ball-openai) joined OpenAI to lead a Strategic Futures team focused on frontier AI policy and governance.

* [Kobi Hackenburg](https://x.com/KobiHackenburg/status/2066890518009708839) reported that frontier AI nearly tripled donations versus professional canvassers in one persuasion campaign.

* [Google DeepMind](https://deepmind.google/research/publications/239142/) explored four possible paths from AGI to superintelligence in a new research report.

* [Snap](https://techcrunch.com/2026/06/18/snap-spins-off-ai-video-team-into-new-company-dotmo-due-to-costs/)⁠ is spinning off an internal generative-AI video team into Dotmo, a separate company focused on AI models for interactive gaming experiences, with Snap licensing technology to Dotmo, taking a large equity stake, and citing the high cost of doing the work internally as one reason. 

* [Meta Platforms](https://news.bloomberglaw.com/tech-and-telecom-law/meta-strikes-new-ai-computing-deals-with-data-center-firm-crusoe)⁠ is under contract, according to Bloomberg, to buy roughly 1.6 GW of AI computing capacity from Crusoe across data centers in Childress, Texas, and Warrenton, Missouri, with the spending amount and delivery timing not yet clear. 

* [Amazon Web Services](https://www.bloomberg.com/news/articles/2026-06-18/amazon-is-in-talks-to-sell-nvidia-rival-chips-to-other-companies)⁠ is in early talks to sell Trainium AI chips for use in other companies’ data centers, per AWS AI chief Peter DeSantis, after Andy Jassy said Amazon may sell chip racks to third parties and estimated a standalone chips run rate of about $50 billion if sold to AWS and outside buyers. 

[Want absolutely EVERYTHING that happened in AI this week? Click here!](https://www.theneuron.ai/explainer-articles/-everything-that-happened-in-ai-today-friday-june-19-2026/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

**FROM OUR PARTNERS **

# AWS Summit Washington DC - June 30-July 1

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0f01d754-a93d-45b0-bd64-8ab5290ff612/AWS_Summitpng.png?t=1781632357)
Follow image link: (https://aws.amazon.com/events/summits/washington-dc?trk=5c54fc37-736e-4e42-9c92-2b9268232627&sc_channel=el)
Caption: 

[AWS Summit DC](https://aws.amazon.com/events/summits/washington-dc?trk=5c54fc37-736e-4e42-9c92-2b9268232627&sc_channel=el) is bringing together cloud leaders, developers, and innovators for two days of expert-led sessions, keynotes, and public sector insights. Explore AI-driven workflows and modernization at scale. 

[Register for free.](https://aws.amazon.com/events/summits/washington-dc?trk=5c54fc37-736e-4e42-9c92-2b9268232627&sc_channel=el)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🌟** ****Sunday Special: Top of the Week**

* [OpenAI](https://openai.com/index/diagnose-rare-childhood-diseases/) helped researchers reopen 376 unsolved rare childhood disease cases and find 18 new diagnoses, while [Google](https://blog.google/innovation-and-ai/models-and-research/google-research/amie-for-disease-management-in-nature/) pushed their AMIE from diagnosis into ongoing care. Medical AI had a rare week where the story was not “look at this benchmark,” but “look at the families who finally got an answer.”

* [SpaceX reportedly bought Anysphere](https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/), the company behind Cursor, for $60B. The deal turns one of the most important AI coding work surfaces into strategic infrastructure for SpaceX, xAI, and the broader developer-agent race.

* [Anthropic’s Fable and Mythos fight](https://www.axios.com/2026/06/15/anthropic-white-house-fable-mythos) turned model access into a national-security, cyber-defense, and market story all at once. The messy part: cutting off powerful U.S. models may also make cheaper open models from China look a lot more attractive.

* [Z.ai](https://Z.ai)[ launched GLM-5.2](https://z.ai/blog/glm-5.2), an MIT-licensed open-weight model with a 1M-token context window and strong coding / agent results. Translation: the open-model race is no longer a side quest, and companies now have a serious reason to ask whether they want rented intelligence or something they can run themselves.

* [Salesforce signed a deal to acquire Fin](https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/?bc=OTH) for $3.6B, bringing Intercom’s customer-service agent platform deeper into the Salesforce machine. Enterprise agents are moving from “neat demo” to “which giant platform owns this workflow?”

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# A Cat’s Commentary 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/02fcf59f-6242-458d-a0ea-eb33ca993705/A_Cat_s_Commentary_x_2025__36_.png?t=1781818797)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. 




**P.S: **Before you go… have you [subscribed to our YouTube Channel](https://www.youtube.com/@theneuronai?sub_confirmation=1)? If not, can you?  

**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).  


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/deepmind-mapped-ai-agent-controls
