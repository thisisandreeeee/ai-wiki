---
source: gmail
newsletter: "the-neuron"
message_id: "1a159038c4cc22e4"
thread_id: "1a159038c4cc22e4"
subject: "😸 AI hackers left the door open"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Tue, 20 Oct 2026 11:12:08 +0000 (UTC)"
ingested: 2026-10-26
sha256: 9c3db82d99cbbdf108850be6c8d7f3a68b765b02116138482fbd55443b3a8e2b
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/dba7fb12-b7de-4d9e-bc8a-a191799910ac/AI_Hackers__Open_Dashboard_Mystery.png?t=1792483755)
Caption: 

Welcome, humans.

So apparently Eugenia Kuyda just built the AI assistant she pitched on stage at TechCrunch Disrupt in 2014. Back then, her startup Luka showed off IO, a chat concierge that helped people book restaurants and vacations years before the breakthroughs behind today's chatbots (here's [the IO launch video](https://x.com/ekuyda/status/2107652765904478407) from 2015). She told [TechCrunch](https://techcrunch.com/2026/10/19/replikas-founder-built-the-ai-assistant-she-pitched-at-disrupt-12-years-ago/) it worked, but it was nowhere near what's possible now.

Luka later became Replika, and Kuyda left as CEO last year to start Wabi, which opened to everyone on Monday. Connect your email and Wabi decides which mini apps to build for you, each inside its own chat thread. In her family thread, one app tracks her daughter's schedule and another quizzes her daughter on Japanese. With her boyfriend, there's a daily relationship question. _The 2014 version helped you book dinner. The 2026 version quizzes your kid on Japanese._

Her pitch against assistants like Meta's Muse is that one endless chat gets worse as context piles up, so Wabi splits everything into threads you can share like group chats. _Twelve years later, the technology finally RSVP'd._

**Here’s what happened in AI today:**

* 😺 Hackers' AI agents hit real sites, dashboards left open

* 📰 Homeland Security ordered agencies to remove DeepSeek products

* 📰 Anthropic reportedly neared a second $45B Nscale deal

* 🍪 fal released FLUX 3 Max video generation

* 🛠️ Corey Noles tested Mercury 3 for about four cents

…and a [**whole lot more that you can read about here**](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-october-20-2026/)**.**

Advertise to 700K readers of The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😺 Hackers' AI Agents Are Breaking Into Real Websites, and Their Control Panels Were Left Open

[NorForge](https://norforge.com/blog/inside_cairn), a security startup, found more than 20 exposed control panels for an AI hacking tool called Cairn that appear to belong to criminals. The dashboards give a rare look at crooks using AI agents to break into real businesses. (An agent is an AI that takes actions on its own, like browsing sites and running code, instead of just answering questions.)

First, how Cairn works. Picture a team of AI workers sharing a whiteboard. You give it a target and a goal, like breaking into one particular online store, and that job becomes a project. As the agents work, they post what they've learned (facts) and what they plan to try next (intents) on the shared board, and a human can add hints. Because the board remembers everything, one project can keep running for hours, or even days.

**Here's what happened:**

* One cluster of 14 panels, driven by Chinese-language instructions, held more than 1,100 attack projects aimed mostly at online stores in the US, Japan, and Australia.

* NorForge estimates about 10% of projects hit their goal, and the successful ones in that cluster averaged just under 23 hours start to finish.

* A typical attempt cost roughly $5 in model fees once failures are counted, by NorForge's own rough guess.

* [The Verge reported](https://www.theverge.com/ai-artificial-intelligence/1013643/ai-agents-hack-john-deere-shark-ninja-cummins) that the panels named targets including John Deere, SharkNinja, and Cummins, and that one operator appeared to have compromised more than 100 sites.

Is any of this real? NorForge checked one claimed break-in, at a large hardware parts vendor, and found the back door (a hidden page that lets attackers upload files to a site's server) still sitting live on the vendor's website.

Here's the part worth repeating: the attackers left their dashboards open to the public internet, no password needed. NorForge could read target lists, the agents' running notes, and stolen logins. Scanning that data turned up hundreds of exposed passwords and access keys, and 11% were still valid. One group even posted the login for its own staging server. _These are the people threatening your company's security, and they forgot to lock their own command center._ A bug in one group's pipeline also kept chopping a leading w off site names, so wholesale became holesale, which made related panels easy to spot.

What were the agents running on? Worker names in the panels suggest off-the-shelf coding agents powered by DeepSeek's cheap V4.1 Flash model, though NorForge calls that its reading, not a confirmed fact. If its estimates hold, the math is striking: about $5 per try and a 10% hit rate works out to roughly $50 in model fees per successful break-in (our math, so treat it as a ballpark).

**Why This Matters:** If you run a website, store, or client portal, the agents' to-do list was the boring stuff: login flaws, pages that skip the login check, and file uploads. Old, known holes get found faster when software can work through more than 1,100 projects in a single cluster. And if you hire outside security testers (a red team, meaning hired hackers), ask how they protect their own AI dashboards. NorForge says apparently legitimate red team setups were left exposed too, which can leak a client's secrets.

A grain of salt: NorForge builds sandboxing tools for AI agents, the 10% figure is its own reasonable assumption, success varies by group, and this is a snapshot of tools that change fast.

**What to watch next:** NorForge says it's working with Reuters to notify victims and trying to get the panels taken down, though that depends on the hosting companies. Then watch whether that 10% climbs as the models behind these agents improve.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

### A deal has two sides. Your stack only sees one.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b1af3a70-26f3-4f6d-adf0-8427df9ac698/meet-aligned.jpg?t=1789074760)
Follow image link: (https://alignedup.com/sign-up/?utm_campaign=YJ4ZPRQDHV&utm_source=beehiiv&_bhiiv=opp_c6b6a33e-5ccc-497d-bc77-5dcc32cfde57_fd271d4f&bhcl_id=6d5f593e-5e0c-4adf-9ceb-50ac623c6f4d_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

[Aligned](https://alignedup.com/sign-up/?utm_campaign=YJ4ZPRQDHV&utm_source=beehiiv&_bhiiv=opp_c6b6a33e-5ccc-497d-bc77-5dcc32cfde57_fd271d4f&bhcl_id=6d5f593e-5e0c-4adf-9ceb-50ac623c6f4d_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f) shows you the other half. See what buyers actually do between meeting. See what they open, revisit, and share; so you know the exact next step to move things forward. And your champion gets everything they need to win internally when you're not in the room.

[Win More Deals With Aligned](https://alignedup.com/sign-up/?utm_campaign=YJ4ZPRQDHV&utm_source=beehiiv&_bhiiv=opp_c6b6a33e-5ccc-497d-bc77-5dcc32cfde57_fd271d4f&bhcl_id=6d5f593e-5e0c-4adf-9ceb-50ac623c6f4d_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🎓 AI Skill of the Day: Make Gemini 4 Argon show its receipts

Two versions of a vendor contract land in your inbox with no redline, and someone wants to know what changed by lunch. Two guides published last week on Google's Gemini 4 Argon, [one from iWeaver's Liana](https://www.iweaver.ai/blog/how-to-use-gemini-4-argon/) and [one from PrompTessor's Rizki Murtadha](https://promptessor.com/blog/gemini-4-argon-prompting-guide), take on this kind of document comparison with the same core move: tell the model what counts as evidence, then make it show its work.

Here's the recipe, adapted from both:

1. Label each document (Version A, Version B), add dates, and say which one wins if they conflict.

2. Tell Argon to use only your documents, cite the section behind each finding, keep what the documents say separate from its interpretation, and flag anything missing instead of guessing.

3. Paste the documents first and put your question last, which PrompTessor recommends for long inputs.

The order matters because of how Argon's memory works. Its context window (how much text it can hold in view at once) is 1,048,576 tokens (word-sized chunks of text), but that budget is shared across what you paste in, the model's thinking, and its answer. A giant pile of documents leaves less room to reason, so both guides say to start with only the sources the question needs and add more if the first pass reveals a gap.

Neither guide shares test results, so treat this as a starting template:

```
Compare Version A and Version B of the attached [contract / policy]. Use only the supplied documents. If they conflict, Version B (the newer one) wins.

Focus on [payment terms, termination, data access, liability, approval authority].

For each change, give: the section in each version, what changed in practice, who is affected, and what we should review. Keep what the documents say separate from your interpretation. If a clause is missing or unclear, say so instead of guessing. This is not legal advice.

Finish with a comparison table, a 300-word summary, and the three questions we should settle before signing.
```
Then check it like a skeptic. Trace a few claims back to the cited sections, and fix errors with a specific correction (for example, Version B has no termination clause, so revise that row) instead of starting over. iWeaver adds a smart test: run the same documents and prompt through Gemini 3.8 Flash too, so you can see what Argon adds.

You'll need Google AI Pro or Ultra to use Argon in the [Gemini app](https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-availability), and iWeaver offers a free trial. Check your company's policy before uploading client documents.

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

# Put your meetings to work

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c95904a1-602d-4b09-9e19-00714faad0f2/Granola_Meetings-to-work_02_1920x1080.png?t=1791558336)
Follow image link: (https://www.granola.ai/?utm_source=affiliate&utm_medium=TheNeuron&utm_campaign=general-htn&via=theneuron-q4&dub_id=U0YAaZ1CxGhSwSwv)
Caption: 

Granola, the AI notepad for people with back-to-back meetings, turns your notes and the meeting transcript into clear summaries with actual next steps. Share them with your team before the next call starts. 

Download Granola and try it in your next meeting.
3 months on us with the code **THENEURON**.

[Try Granola](https://www.granola.ai/?utm_source=affiliate&utm_medium=TheNeuron&utm_campaign=general-htn&via=theneuron-q4&dub_id=U0YAaZ1CxGhSwSwv)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0b3a0f6d-59a8-4b9b-bf03-a6c670e8c466/SwitchTrust_Newsletter_Image_640x320px.jpg?t=1792177002)
Follow image link: (https://www.switchagents.ai/trust?utm_source=theneuron&utm_medium=newsletter&utm_campaign=Tertiary102026)
Caption: 

1. *Your AI agents are doing work, but are they doing it well? Evaluate risks, track costs, and measure results with [Switch AI](https://www.switchagents.ai/trust?utm_source=theneuron&utm_medium=newsletter&utm_campaign=Tertiary102026).

2. [FLUX 3 Max](https://fal.ai/models/blackforestlabs/flux-3-max/text-to-video) on fal turns a text prompt or still image into a 5- to 20-second video with audio, and fal says a 10-second clip took about 12 seconds to make.

3. [Wabi](https://wabi.ai/) connects to your email, then builds mini apps and separate chat threads for you (think a kid's schedule tracker), and you can invite others into any thread.

4. [MiniMax M3.1 Flash](https://www.minimax.io/blog/minimax-m31f) is a cheaper, faster model for running AI agents, with open weights planned for October 23, though one test found it tends to make things up when it's wrong.

5. [TorchNeuron](https://www.aboutamazon.com/news/innovation-at-amazon/torchneuron-pytorch-aws-trainium-chips-ai) runs your existing PyTorch code (a popular framework for building AI models) on Amazon's Trainium chips after a settings change instead of a rewrite.

6. [Wally](https://www.producthunt.com/products/willow-voice) from Willow turns your spoken or typed rough ideas into an editable draft in your own tone, and learns your style over time.

7. [Kai Resolve](https://www.producthunt.com/products/gleap) from Gleap reads a customer's screen recordings, logs, and account details to answer the problem or hand engineers a diagnosis.

8. [Maali](https://maali.app/) is a personal finance app for Mac and Windows that keeps your bank data on your computer, with an optional on-device AI analyst to explore your spending.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/66a9982c-8e24-463f-9690-806164da2061/image.png?t=1792482868)
Follow image link: (https://x.com/OpenAI/status/2112310345863930168)
Caption: OpenAI says its newest models can now handle COBOL, the 1950s-era language still running bank and government software. _Somewhere, a retiree who still maintains it just got a very polite LinkedIn message._

* Homeland Security ordered federal civilian agencies to [stop buying DeepSeek](https://public-inspection.federalregister.gov/2026-21447.pdf) and remove it from their systems, including third-party tools built on it, in a notice made public Monday.

* Microsoft [argued AI agents are insider risks](https://blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/) and pitched Guardian Agents that watch every agent action before it happens.

* Anthropic and Nscale [neared a second $45B deal](https://techcrunch.com/2026/10/19/nscale-and-anthropic-are-reportedly-in-talks-for-yet-another-45-billion-compute-deal/) for computing capacity, Bloomberg reported, a little over a month after the first.

* OpenCode said a [breach exposed API keys](https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/) for about 1.4% of Console users, and some reported charges topping $1,000.

* Ex-OpenAI engineer Abdulrahman Alfozan, charged with hiding a recording device in an executive meeting room, was [kept in custody](https://apnews.com/article/9fc401a1be248c2b966814040d13c0f6) before trial and pleaded not guilty.

* Tenstorrent [raised $1.5B](https://techcrunch.com/2026/10/19/tenstorrent-hits-6-2b-valuation-to-scale-open-weight-ai-chips/) at a $6.2B valuation to scale its open-architecture AI chips, a rival to Nvidia's.

* Anthropic [reported junior staff fell](https://www.theneuron.ai/news/anthropic-junior-technical-hiring-ai/) from 27% to 9% of its technical hires, though the report doesn't show whether junior hiring itself dropped.

* Anthropic [consulted lawyers](https://www.theneuron.ai/news/anthropic-ai-agents-negotiation-lawyers/) about AI agents that negotiate for users, the Financial Times reported, though no product has been announced.

Want absolutely EVERYTHING that happened in AI this week? **[Click here!](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-october-20-2026/)**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

## UPCOMING EVENT: The Neuron IRL in San Francisco

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ffcec634-8d32-4117-b1be-c04c45a0f74c/NeuronLive_Social_1200x675.png?t=1791478412) [The Neuron Live San Francisco event]
Follow image link: (https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)
Caption: 

The Neuron is **going IRL** on **[November 18 at 4:30 PM PT](https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)**! Join us in San Francisco for **drinks, bites, special guests, and a live recording of The Neuron podcast.** Huge thanks to Slack and Alumni Ventures for making it happen.

**It’s free, but space is limited. Save your spot!**

RSVP for The Neuron IRL (https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 🛠️ Tuesday Tool Tip: Test a new AI model on your own work for about four cents

Corey Noles, host of The Neuron: AI Explained podcast, ran Inception's brand-new Mercury 3 through eight API runs, and the whole bill came to about four cents. _You can't even buy a gumball for that._ [His review](https://www.theneuron.ai/news/mercury-3-review-diffusion-language-models/) doubles as a ready-made test kit for any model you're sizing up.

Mercury is an odd duck. Most chatbots write one token (a word-sized chunk of text) at a time, left to right. Mercury is a diffusion model, which drafts and refines several parts of an answer at once, more like an editor revising a whole draft. Inception, which [launched Mercury 3](https://www.inceptionlabs.ai/blog/introducing-mercury-3) on October 19, claims it generates 1,068 tokens per second on NVIDIA GPUs and rivals GPT-6 Luna and Claude Haiku 5.5 on quality. Corey did not independently reproduce that speed.

Here's what he ran through OpenRouter: a constrained sci-fi story, a coffee-shop math problem, an explain-AI-to-three-audiences prompt, a single-file dungeon-crawler game, a made-up NASA mission to see if it would invent facts, and a classic logic puzzle. How it did:

* Math: nailed the $900 daily gross profit, $756 monthly savings, and $576 net benefit, and questioned the problem's assumptions (one small margin mix-up aside).

* Coding: produced a full dungeon-crawler game in one HTML file, and its code passed a syntax check and 2,000 randomized map-generation checks with zero failures. Corey didn't play through every combat scenario.

* Writing: a funny story about a maintenance machine worshipped by roaches, but about 274 words against a 250-word limit.

* Fake NASA mission: it flagged the fabrication, but it used web searches and added an unrelated error of its own.

How to run your own version:

1. Try it in [Mercury Chat](https://chat.inceptionlabs.ai/) with no setup, or through [OpenRouter](https://openrouter.ai/inception/mercury-3). Corey says new accounts on Inception's API platform get 100 million free tokens.

2. Copy his kit with tasks from your actual work: one with strict limits, a math word problem, a coding request, and a question with a fake premise.

3. Grade the misses instead of the vibes: count the words, check the math, and see whether it invents facts.

These were spot checks, not a controlled benchmark, and the comparison charts are Inception's own. Corey says he wants independent comparisons and more proof on long, complicated tasks.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5bad3347-cf0a-4c9b-9868-45bcf260caff/TN_Thumbnail_101326_AnastasisGermanidis_Runway_B.png?t=1791882337)
Follow image link: (https://www.youtube.com/watch?v=DbfWxmGsh2M&list=PLgNkxzbxQR_FEau-nc6OZ5DBD4GoZ7s2l)
Caption: Click the image to watch the video.

New episodes air **every week** on Wednesdays: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ac4d061e-4ac1-4707-a6cd-a2edbe4a655a/A_Cat_s_Commentary_x_2025_-_2026-09-28T162704.628.png?t=1790640264)
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
https://www.theneurondaily.com/p/ai-hackers-left-the-door-open
