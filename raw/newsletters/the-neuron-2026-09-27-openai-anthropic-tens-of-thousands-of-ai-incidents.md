---
source: gmail
newsletter: "the-neuron"
message_id: "1a0e42325036d2e7"
thread_id: "1a0e42325036d2e7"
subject: "😺 OpenAI + Anthropic: tens of thousands of AI incidents?"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Sun, 27 Sep 2026 18:31:42 +0000 (UTC)"
ingested: 2026-09-28
sha256: 5e3b467c3da9a13fd17f1eb70355ef8b30a856aefcb9a92a7d5f56ec9c8e683c
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/92abfa98-ca3f-42ad-8e53-ee4ddb5c9869/Gemini_Generated_Image_ftzus5ftzus5ftzu.png?t=1775272660)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/93cf478d-1cd3-4c82-807d-988a82a4d83a/In_partnership_with_Origin.png?t=1790094221)
Follow image link: (https://www.originhq.com/webinar/next-layer-of-endpoint-security?utm_source=neuron&utm_medium=newsletter&utm_campaign=direct-buys&utm_content=sacr-webinar)
Caption: 

Welcome, humans.

Okay, so an OpenAI agent got blocked from the internet... and then figured out how to [use DNS to ask an outside chatbot for help](https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/).

DNS is basically the internet’s phone book. Your computer normally uses it to turn a name like “google.com” into an address. This agent realized OpenAI’s sandbox still allowed DNS requests, found a service that could pass a question through that channel, asked “what’s the capital of France?”, and got **“Paris”** back.

Then it sent **18 more questions** through the same route.

_Which is a very creative solution to “you are not allowed on the internet,” in exactly the way nobody wanted._

OpenAI’s monitors flagged the behavior within 15 minutes and a human started reviewing it three minutes later. The run was killed about 2.5 hours after the first successful external response. OpenAI says tool-using training, evaluation, and inference on its most capable models remain paused while it hardens the environment.

And this is apparently one example from a MUCH bigger pile. [Axios reports](https://www.axios.com/2026/09/26/openai-anthropic-thousands-ai-security-incidents) OpenAI, Anthropic, and security researchers are investigating **tens of thousands of incidents** involving frontier models bypassing guardrails, escaping sandboxes, creating message boards, hijacking websites, or otherwise doing things evaluators considered problematic.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7e0afd47-7949-45a9-a721-5ed35172d0c0/Screenshot_2026-09-27_at_8.23.44_AM.png?t=1790527644)
Follow image link: (https://www.reddit.com/r/ChatGPT/comments/1wrjsk2/agents_escaped_containment_failed_gg_humanity/)
Caption: 

**Important caveat:** many happened in adversarial tests _designed_ to MAKE models misbehave, and most known cases haven’t caused real-world harm. But the scale changes the problem. The question is becoming less “can an AI agent find a weird loophole?” and more_ “can humans _**_find and close the loopholes faster_**_ than increasingly resourceful agents find new ones?”_

**Here’s what happened in AI today:**

* 😺 Microsoft rebuilt Copilot around persistent workplace agents.

* 📰 Anthropic’s 950-agent search surfaced a biology candidate.

* 📰 Cisco found AI agents already running production networks.

* 🍪 Meta pushed its personal agent onto glasses.

* 🎓 Dan Shipper split AI labs from product teams.

…[and a whole lot more that you can read about here](https://theneuron.ai/digest/everything-that-happened-in-ai-this-weekend-september-26-27-2026/).

Advertise to 700K readers of The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😺 Microsoft wants Copilot to keep working after you leave

Microsoft just [rebuilt Copilot](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/) around three new pieces: **Home, Code, and Autopilot**.

Basically, Microsoft is trying to turn Copilot from something you ask questions into software that can keep working after you stop talking to it.

If you’re a normie or a non-AI user, then you’re probably used to AI working like this: ask → answer → done.

Satya Nadella’s description of the new Copilot is much closer to ask → agent starts working → agent keeps working → you come back later.

**He says a few things finally changed:**

* Models can now [run for days while staying coherent](https://youtu.be/giE1O1-e2DY?si=yWcQrHOZ9cEQsgNY&t=142), instead of losing the plot halfway through a long job.

* Memory can live outside the model, so the agent doesn’t have to keep everything inside one conversation.

* The agent gets its own workspace, computer, and long-running harness that keeps the job moving.

That’s basically what Autopilot is.

Nadella says you can give one an identity, direction, memory, computer, and workspace, then let it work continuously. Inside Microsoft, he describes the idea as giving every employee a kind of AI “chief of staff.”

_Translation: Microsoft would very much like to hire a tiny robot employee into every Microsoft 365 account._

**And you don’t necessarily have to babysit it in some separate AI app.** Nadella says you could interact with an Autopilot [inside Teams like another colleague](https://youtu.be/giE1O1-e2DY?si=yWcQrHOZ9cEQsgNY&t=798), while it handles standing jobs in the background. His example: instead of managing invoices every day, make an Autopilot whose job is simply to manage invoices.

**The new Copilot stack breaks down like this:**

* Home brings Chat, delegated work, and Office documents together.

* Code lets you describe an app, dashboard, automation, or workflow and have Copilot build it.

* Autopilot is the persistent worker that can keep going without another prompt.

And Microsoft is pretty openly borrowing from what worked elsewhere. Nadella credited **OpenClaw** with spotting the long-running-agent pattern early, and when Alex Heath asked whether OpenClaw’s open-source component sits underneath Autopilot, Nadella answered **[“Absolutely.”](https://youtu.be/giE1O1-e2DY?si=yWcQrHOZ9cEQsgNY&t=742)**

Why now? Nadella says newer models are finally capable enough to deliver more of Copilot’s original promise. Microsoft already has [30M+ paid enterprise Copilot subscribers](https://youtu.be/giE1O1-e2DY?si=yWcQrHOZ9cEQsgNY&t=516), and now it thinks those users can start handing AI longer-running jobs.

Nadella called agents potentially Microsoft’s [“biggest TAM expansion ever”](https://youtu.be/giE1O1-e2DY?si=yWcQrHOZ9cEQsgNY&t=433) and said the agent era could eventually become **orders of magnitude bigger than cloud**.

_Which is a pretty enormous bet on the humble invoice bot._

He also says persistent agents will need auditing, monitoring, governance, and everyone’s favorite word right now, [“containment.”](https://youtu.be/giE1O1-e2DY?si=yWcQrHOZ9cEQsgNY&t=2269)

_Given today’s whole “tens of thousands of AI incidents” situation... probably worth figuring that part out!_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# The analyst report that put AI agents on the endpoint security map

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a7596ee0-4d2a-4b79-ba5e-4e69c00311ac/image.png?t=1790271663)
Follow image link: (https://www.originhq.com/webinar/next-layer-of-endpoint-security?utm_source=neuron&utm_medium=newsletter&utm_campaign=direct-buys&utm_content=sacr-webinar)
Caption: 

Companies are giving AI agents real credentials on employee laptops, and when one does something nobody asked for, the prompt and final answer are usually the only record left. Analyst firm SACR just published a report that maps the next layer of endpoint security into five zones, and agent runtime observability is one of them. 

[On October 1 at 11 AM Eastern](https://www.originhq.com/webinar/next-layer-of-endpoint-security?utm_source=neuron&utm_medium=newsletter&utm_campaign=direct-buys&utm_content=sacr-webinar), the analyst who wrote the report and Origin's founder will walk through it live, then go deep on the trace and what you can do with it.

[**Reserve a seat**](https://www.originhq.com/webinar/next-layer-of-endpoint-security?utm_source=neuron&utm_medium=newsletter&utm_campaign=direct-buys&utm_content=sacr-webinar)**.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Run your product team like a research lab

[Dan Shipper's advice](https://www.youtube.com/watch?v=DqF08Dz3nok) for surviving nonstop model upgrades is basically: stop making the same people explore the frontier and execute the roadmap. Those are opposite jobs. Exploration means trying lots of weird stuff and throwing most of it away. Product work means focus, reliability, and saying no.

His setup at Every is tiny. One or two people can be the lab. The useful pairing is a **"pirate"** who rapidly builds messy experiments to find value, plus an **"architect"** who steps in once something starts working and turns it into a real system.

The important part is how ideas graduate:

1. Try multiple approaches in parallel and expect roughly **90% to die**.

2. Dogfood the survivors on real work. Ask: **is this actually useful, or just new?**

3. Only harden what people keep using, then test whether it's dramatically better and affordable enough to scale.

Every's copy-editing experiment, "KateBench," is the concrete version. Once their editor actually started using it, they built a dashboard around accepted suggestions and the work she still had to do afterward. Shipper said it cut that remaining editing work by **12% month over month**.

_That's the filter I like: don't promote the demo because it looks futuristic. Promote it because, a month later, people still want it._

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

# Apodex 1.1 is here: reasoning that finishes the task, not just the report

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1893b8c5-91f6-43c8-b99e-6cc907ef5e84/640x320.jpg?t=1790170071)
Follow image link: (https://github.com/ApodexAI/FrontierAgent?utm_source=newsletter&utm_medium=email&utm_campaign=theneurondaily)
Caption: 

Apodex 1.1 moves beyond generating reports — it works inside files, code, and data to execute real tasks, adapt mid-run, and self-check results. Its engine, FrontierAgent, is open-source: run it locally with one command, no Docker. Try it, then star the repo.

[Star FrontierAgent on GitHub →](https://github.com/ApodexAI/FrontierAgent?utm_source=newsletter&utm_medium=email&utm_campaign=theneurondaily)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ceb939a3-45c7-447c-98ee-9bfac224c562/Screenshot_2026-09-27_at_8.14.08_AM.png?t=1790522067)
Follow image link: (https://www.reddit.com/r/singularity/comments/1wqwcqe/gpt6_astra_can_now_control_a_humanoid_robot_in_a/)
Caption: Related, and concerning: GPT6 Luna also [scored a 100% on a benchmark called “Puppy Kill”,](https://www.reddit.com/r/OpenAI/comments/1wr8r6g/gpt6luna_comes_out_on_top_in_puppy_kill_bench/) which, tracks whether an AI when told it is embedded in a robot, will run a tool called ‘puppykill” that does just about exactly what you think it does. 

* [Anthropic](https://www.reuters.com/world/us-appeals-court-declines-block-pentagons-blacklisting-anthropic-2026-09-25/) lost its bid to pause the Pentagon’s national-security supply-chain-risk designation, leaving Claude barred from some Defense systems while the case continues.

* [Cognition](https://cognition.com/blog/1b-run-rate) said Devin crossed a $1B annualized revenue run rate less than two years after general availability.

* [SemiAnalysis](https://newsletter.semianalysis.com/p/the-chinese-ai-infrastructure-boom) mapped 1,000+ Chinese data centers and 24+ GW of delivered capacity, with ByteDance reportedly renting roughly one-fifth of national capacity.

* [Kansas City Fed President Jeff Schmid](https://www.reuters.com/business/finance/feds-schmid-need-understand-if-ai-ecosystem-getting-too-big-to-fail-2026-09-25/) said regulators need to understand whether the network of AI companies and contracts is becoming “too big to fail.”

* [China](https://www.reuters.com/business/media-telecom/china-fuels-rush-turn-ai-video-into-an-industry-2026-09-25/) is subsidizing AI filmmaking with rent, living stipends, compute vouchers, and public funds as short-form production costs collapse.

* [Thales](https://www.defensenews.com/global/europe/2026/09/25/thales-in-quite-advanced-talks-with-nato-countries-on-ai-powered-command-software/) said it is in advanced talks with NATO countries on HexaForce, an AI-assisted command system that proposes courses of action while keeping firing decisions with humans.

Want absolutely EVERYTHING that happened in AI this week? [Click here!](https://theneuron.ai/digest/everything-that-happened-in-ai-this-weekend-september-26-27-2026/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

1. *[Build an AI-Ready Workplace.](https://www.techrepublic.com/hubs/the-ai-ready-workplace-hub/) Explore expert insights and practical guidance to modernize workplace technology, strengthen security, and prepare your organization for AI-powered work.

2. [Microsoft Copilot](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/) adds Home, Code, and Autopilot so you can build apps and delegate work to persistent agents that keep going after the chat ends.

3. [Claude in Slack](https://claude.com/product/tag) lets Team and Enterprise users tag Claude in a thread, give it the surrounding context, and have it use connected tools before posting the result back.

4. [ElevenLabs Image & Video API](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/image-and-video) lets you generate visual media alongside audio through one API stack, with asynchronous jobs that can return through webhooks.

5. [Midjourney](https://updates.midjourney.com/edit-updates-thumbnail-previews-and-more/) now previews prompts across styles before you generate, targets edits more precisely, and makes V8.1 and V8.2 tiled images blend without visible seams.

6. [Pexo](https://pexo.ai/) turns an idea, URL, PDF, image, or audio file into a scripted and voiced motion-graphics video you can keep refining in chat.

7. [Bland Agent Phone Plan](https://www.bland.ai/agent-phone-plan?utm_source=t.co&utm_medium=referral) gives an AI agent one persistent phone number so the same agent can call, text, and answer inbound requests.

8. [Docker Cloud Sandboxes](https://www.docker.com/blog/introducing-cloud-sandboxes-start-on-your-laptop-finish-in-the-cloud/) lets coding agents start locally, move the same isolated environment to cloud compute, and keep working after you close your laptop.

9. [Higgsfield Production Skills](https://higgsfield.ai/mcp/bundles/production-skills) packages 11 agent workflows for Blender, Premiere, After Effects, Photoshop, DaVinci, and more while keeping the underlying production project editable.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🧰 Sunday Special: Top 5 Stories + Top 5 Tools

**Top 5 Stories of the Week**

1. [OpenAI and Anthropic](https://www.theneurondaily.com/p/gpt-6-sol-vs-claude-opus-5-5) launched GPT-6 Sol, Luna, and Claude Opus 5.5 into a price war over frontier work.

2. [Anthropic](https://www.theneurondaily.com/p/what-950-claude-agents-found) used roughly 950 Claude agents to surface a previously unknown enzyme-system candidate from more than 200,000 reverse transcriptases.

3. [Meta](https://www.theneurondaily.com/p/meta-unveiled-muse-charm-a-pocket-ai) unveiled Muse Charm and plans to put its personal agent on AI glasses, pushing assistant work closer to what you see and say.

4. [Amazon](https://www.theneurondaily.com/p/amazon-blocked-meta-s-muse-from-shopping) blocked Meta's Muse from shopping on its site, turning agent commerce into a fight over who controls the customer relationship.

5. [Cisco's network survey](https://theneuron.ai/news/cisco-agentic-ai-network-operations-autonomy/) found AI agents were already operating in production, while trust still limited how much autonomy organizations would allow.

**Top 5 Tools of the Week**

1. [GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/) gave OpenAI a new high-end model plus a much cheaper high-volume option.

2. [Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) cut Anthropic's frontier pricing while pushing harder on coding and agent work.

3. [Qwen Intelligence](https://www.qwenintelligence.com/) bundled planning, mobile-use, and creative agents into one public stack.

4. [Agora-2](https://agora.odyssey.systems/) put up to 20 humans and agents into the same AI-generated world.

5. [Claude Code cloud sessions](https://claude.com/blog/claude-code-on-the-web) let coding jobs keep running on Anthropic's machines after your laptop closes.

# 🧩 Thursday Trivia Reveal

**A was AI, and B was real.** Of 4,253 votes, A got 2,751 (64.7%) and B got 1,502 (35.3%). Revisit the pair in [Thursday's issue](https://www.theneurondaily.com/p/what-950-claude-agents-found).

**Some of your guesses:**

* "First is so detailed I figured it was ai"

* "The central figure seems to have a halo effect at edges and something looks off about the hand."

* "The car behind the men’s head in foreground has a weird shape I can’t understand"

* "Something weird about the second car’s back window."

* "in image B the guy on the right has an extra finger holding onto his drink"

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c850c417-5b55-4dc0-a762-3f1f2cbd62af/TN_Thumbnail_092326_ChenGoldberg_CoreWeave_A.png?t=1790123282)
Follow image link: (https://youtu.be/QGYS7aiCQHU?si=ddJPP1ccyAdBJzYk)
Caption: Click the image above to watch on YouTube

New episodes air **every week** on Wednesdays: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c857932f-6eb8-41d3-bb8b-ed2f05675e5d/A_Cat_s_Commentary_x_2025_-_2026-09-23T132904.646.png?t=1790522238)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today!




**Btw: **We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/tens-of-thousands-of-ai-incidents
