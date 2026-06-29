---
source: gmail
newsletter: "the-neuron"
message_id: "19efe791eff56e8d"
thread_id: "19efe791eff56e8d"
subject: "😺 ChatGPT's secret advantage"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Thu, 25 Jun 2026 11:09:28 +0000 (UTC)"
ingested: 2026-06-29
sha256: 62022a95ef4a562a7c30d771463ebab89bde7f74e8d0caa1b2cb36b05922f007
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c29e903d-0e18-45e9-a035-6b954e15d56a/Gemini_Generated_Image_yi98nyyi98nyyi98.png?t=1782368602)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b2edb76c-e444-4ffa-8be9-21f40e8dc3e8/In_Parntnersip_with_Boldsign_Syncfusion.png?t=1782147583)
Follow image link: (https://boldsign.com/?utm_campaign=boldsign_june2026&utm_medium=newsletter_ad&utm_source=neuron_technology_advice)
Caption: 

Welcome, humans. 

Former Google engineer [Justin Poehnelt says](https://x.com/JPoehnelt/status/2069482265953087602) he was fired for creating the [Google Workspace CLI](https://github.com/googleworkspace/cli), an open-source tool that lets humans and AI agents control Gmail, Drive, Calendar, Docs, Sheets, and other Workspace apps from one command line. It went viral, hit #1 on Hacker News, gained thousands of GitHub stars, and apparently made parts of Google react like someone taught the AI models how to unionize. 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/33bdfcec-793a-445e-acfa-0cb554bb0ef9/Screenshot_2026-06-24_at_12.52.19_PM.png?t=1782331090)
Follow image link: (https://x.com/JPoehnelt/status/2069482265953087602)
Caption: 

The reaction from the AI builder-world on X was basically: _wait, Google fired the guy who made Google Workspace less miserable to use?_ Vercel CEO Guillermo Rauch praised the “agent-native CLI design” and said Vercel rewards that kind of open-source shipping. Peter Steinberger said the Codex team is always looking for high-agency builders. Swyx’s full analysis was “wait wtf,” which, frankly, belongs in the Smithsonian.

The funniest part is that Poehnelt says Google Cloud Next announced an official Workspace CLI two days before he was fired. That makes the whole thing feel like a perfect little Google tragedy: an engineer builds the tool people actually want, the internet loves it, agents can finally use Workspace without spelunking through ten tabs of admin-console archaeology (_which still sucks to use btw_), and somewhere inside the body, the immune system attacks the useful thing.

_Google people: we know ~700 of you read this newsletter. Please stop doing dumb stuff like this. You’re better than that. Reward innovation, make your tools easier to use (spoiler: they are not, and the ones that are, aren’t smart enough, which is why we don’t talk about you as much as we could). In sum: get out of your own way - w/ Love, Grant. _

**Here’s what happened in AI today: **

* 😸 OpenAI and Broadcom just unveiled Jalapeño, their first custom AI chip built from scratch to run ChatGPT cheaper and faster.

* 📰 Noam Shazeer, the co-lead of Google's Gemini model, left for OpenAI. This is the second time he's quit Google for a competitor.

* 📰 Fable 5 might be coming back, and there are breadcrumbs buried inside Claude Code's latest update.

* 📰 GPT-5 Pro helped solve a 3-year immunology mystery about how immune cells fight cancer.

…and a [**whole lot more that you can read about here**](https://theneuron.ai/explainer-articles/everything-that-happened-in-ai-today-monday-june-22-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=fugu-ultra-beat-models-at-blindfold-chess&_bhlid=d872a8fa2b55deb876044b544dd41f8b713c3cff).

**Hey: **_Want to reach 700,000+ AI-hungry readers? _[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[ ](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.S: **_Love robots? We’re starting a new robotics newsletter! _[Sign up early here](https://form.jotform.com/260897013570156).

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😺**OpenAI's First Chip Is Here (And It Runs on 🌶️)**

Every month, OpenAI pays Nvidia an eye-watering amount of money to run ChatGPT. That's about to change.

Yesterday, OpenAI and Broadcom unveiled[ Jalapeño](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/): OpenAI's first custom-built AI chip, designed from scratch to run large language models (i.e. the AI brains behind ChatGPT) faster and cheaper than anything on the market. Sam Altman himself was in the room when it landed.

**Here's what happened:**

* Jalapeño is a purpose-built **inference chip** (that means it runs AI models in real time in response to your questions, not trains them from scratch, which is a different, more expensive process)

* It went from concept to working chip in **just 9 months** (OpenAI says that may be the fastest-ever advanced semiconductor development cycle)

* Early tests show it beats current state-of-the-art chips on **performance per watt** (meaning: more output, less electricity cost)

* The chip is already running **GPT-5.3-Codex-Spark** in OpenAI's lab right now

* Full deployment is set for **end of 2026**, with Microsoft buying 40% of the first batch

Oh, and OpenAI's own AI models helped design the chip. The robots are building themselves now. _Cool and definitely fine._

**Why this matters:**

OpenAI has historically depended on Nvidia for its compute (the raw computing power to run AI). Nvidia GPUs are powerful but expensive and general-purpose, and they weren't built for LLM inference specifically.

Jalapeño is designed around _exactly_ how ChatGPT thinks. That means OpenAI can squeeze far more efficiency out of every dollar of compute, which directly lowers the cost of running ChatGPT for you.

**Our take:** This is OpenAI's most important infrastructure move yet. By owning the chip, the model, and the product, they're building a vertically integrated AI stack that could let them outprice and outperform competitors who still rent Nvidia hardware. The risk? None of these performance claims have been independently verified yet. Broadcom says it's faster; we'll see the benchmarks later. _Jensen Huang, call your office._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS **

# A smarter way to get documents signed

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/43ed5f3b-a8c7-4ae7-a1d5-36a6322c7438/Syncfusion_Ad_Image_BoldSign_640X320.png?t=1782224581)
Follow image link: (https://boldsign.com/?utm_campaign=boldsign_june2026&utm_medium=newsletter_ad&utm_source=neuron_technology_advice)
Caption: 

[BoldSign](https://boldsign.com/?utm_campaign=boldsign_june2026&utm_medium=newsletter_ad&utm_source=neuron_technology_advice) helps growing teams simplify document signing from start to finish. Send contracts, track signing progress, manage reminders, and store completed documents securely in one place.

Easy to use, cost-effective, and built for businesses that want faster agreement workflows without unnecessary complexity.

**Move agreements forward with **[**BoldSign**](https://boldsign.com/?utm_campaign=boldsign_june2026&utm_medium=newsletter_ad&utm_source=neuron_technology_advice)**.**

[Start your free trial](https://boldsign.com/?utm_campaign=boldsign_june2026&utm_medium=newsletter_ad&utm_source=neuron_technology_advice)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 **AI Skill of the Day**: **Use Claude Directly Inside Slack (with Your Whole Team)**

In[ this tutorial](https://www.youtube.com/watch?v=WsD4NkD_swE) from Brock Mesarich's YouTube channel (AI for Non Techies), host Brock shows how to use Claude with your entire team inside Slack, not just as a solo chatbot, but as a shared second brain everyone in the channel can access.

The tool is called[ Claude Tag](https://www.anthropic.com/claude-tag), and it just launched for Team and Enterprise plans.

Here's how to try it:

1. Go to Claude's Slack integration page and click **Add to Slack** (requires a Team or Enterprise plan)

2. In any Slack channel, type **@Claude** followed by your request (it auto-adds itself when you first mention it)

3. Claude pulls from any apps you've already connected (Gmail, Google Calendar, HubSpot, etc.) and responds in a thread

4. Every team member in that channel can see Claude's work and pick up where the last person left off

The killer feature is **Ambient Mode**: Claude watches the channels it's in and proactively flags things it thinks you need to know, like spotting a login error in your support emails and alerting your engineering Slack channel automatically, without anyone having to ask.

```
Example: 
@Claude I'm meeting Acme at 2pm. What do I need to know?

→ Claude pulls your calendar, the client's recent Slack messages, 
  any open CRM notes, and gives you a pre-meeting briefing.
```
_Anthropic says 65% of their product team's code is now generated through their internal version of Claude Tag. Which explains why Claude keeps getting better._

**Total AI beginner? **[Start here](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/) ([goes with this video](https://www.youtube.com/live/QbFU0UNMVaU?si=skJsgUIDjKjAx3DU)).  

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform) 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🍪 Treats to Try 

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

1. *With Wrike, you get award-winning tools that empower collaboration, visibility, and adaptability. [Try for free](https://link.technologyadvice.com/r/cpl_wrike_project-management_newsletter_neuron_tertiary) 

2. [Relay](https://www.zhukauai.com/?utm_source=theneuron&utm_medium=newsletter&utm_campaign=june-26-thursday) sets up a fully working AI phone receptionist for your business in one click: paste your website, and it reads the site, writes the agent, and starts answering calls, booking appointments, and handling reschedules automatically, with no dashboards or prompt engineering required.

3. [AgenticCalling](https://agenticcalling.ai/?utm_source=theneuron&utm_medium=newsletter&utm_campaign=june-26-thursday) lets you send your Claude or ChatGPT agent out to make real phone calls on your behalf, so you can tell it "call 50 hotels in Miami and find me the best rate" and it handles the whole conversation autonomously; 3 free minutes to start.

4. [Asmi](https://www.asmiai.com/?utm_source=theneuron&utm_medium=newsletter&utm_campaign=june-26-thursday) is an AI that makes real phone calls for your personal errands (scheduling appointments, following up with businesses, dealing with customer service lines) so you never have to sit on hold again.

5. [ai-coustics](https://ai-coustics.com/?utm_source=theneuron&utm_medium=newsletter&utm_campaign=june-26-thursday) cleans up background noise and voice quality in real time for any voice AI product, so your speech-to-text and voice assistants actually work in noisy environments like a car or a busy office.

6. [LocalClicky](https://github.com/dikshantrajput/LocalClicky?utm_source=theneuron&utm_medium=newsletter&utm_campaign=june-26-thursday) is a fully offline Mac voice assistant that controls your computer by voice (open apps, move files, edit videos, click things on screen), with zero data leaving your machine (open source, free).

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# Trending: FOUR popular Neuron podcast eps…

Did you know we have a podcast (_The Neuron: AI Explained)_ where we talk to fascinating people in the industry who teach us how it actually works?  Check it out: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ba00aebe-a1b9-4651-b3fa-78bc48fd4d66/Screenshot_2026-04-27_at_10.18.22_AM.png?t=1777310341)
Follow image link: (https://www.youtube.com/@theneuronai/videos)
Caption: Click to view these episodes on YouTube!

New episodes air **every week** on: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)** **

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/602eb0de-4605-42e4-8f39-c0f6e66f12f0/image.png?t=1782368252)
Follow image link: (https://x.com/nvidiahealth/status/2069434100054962567?s=46&t=T4ASCAO-x6EzmRSTvpSgEg)
Caption: _NVIDIA just released its BioNeMo Agent Toolkit, a framework for building AI agents that can act like a junior scientist: reading papers, generating hypotheses, writing code, and iterating on results, all without a human in the loop. It's aimed at life sciences and drug discovery teams who want to automate the early, repetitive parts of research. Somewhere, a PhD student is both relieved and mildly concerned._

* [Noam Shazeer](https://www.cnbc.com/2026/06/18/google-gemini-co-lead-noam-shazeer-leaves-for-openai.html) left Google, where he co-led Gemini development, to join OpenAI less than two years after Google paid $2.7B to bring him back from [Character.AI](https://Character.AI).

* [GPT-5 Pro](https://openai.com/index/gpt-5-immunology-mystery/) helped immunologist Derya Unutmaz crack a 3-year-old mystery about how T cells (the immune cells that fight cancer and viruses) specialize, opening new doors for cancer and autoimmune research.

* [Fable 5](https://x.com/synthwavedd/status/2069813760622043483) may be returning: strings discovered in Claude Code v2.1.190 hint at the game being permanently included in subscriptions with weekly usage limits, though nothing is confirmed.

* [Nabla Bio's JAM-2](https://x.com/nablabio/status/2069405121084281260) became the first AI model to design drug-quality antibodies directly from a computer, hitting binding success rates that match or beat traditional lab discovery, including against notoriously hard-to-target cancer-relevant proteins.

* [Arc Institute](https://x.com/arcinstitute/status/2069500411476885914) released Proto, an open framework that wires together multiple AI biology tools so researchers can design proteins, RNA, and gene regulators in combination rather than one at a time.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

**FROM OUR PARTNERS **

# One tool. Projects, docs, chat, AI

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c0c817bb-c84e-4c66-8da8-442be34220d8/Clickup_Ad.png?t=1782152074)
Follow image link: (https://link.technologyadvice.com/r/clickup-nl-the-neuron-sponsorship)
Caption: 

We tried treating PM, docs, chat, and AI as four separate purchases. It cost more and worked worse. Then we switched to [ClickUp](https://link.technologyadvice.com/r/clickup-nl-the-neuron-sponsorship). Now 18 spaces and 48 lists run from one workspace, with Brain AI on top.

[→ Try ClickUp free](https://link.technologyadvice.com/r/clickup-nl-the-neuron-sponsorship)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🧩 **Thursday Trivia**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c080e458-e31b-4c35-ba69-ea0093c02ab6/image.png?t=1782370935)
Caption: **A.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1bde7afd-967f-41a5-b192-2dbeb4e7f693/image.png?t=1782370937)
Caption: **B.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# A Cat’s Commentary 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/fc38dde2-0afa-49c5-b986-34b11f6b58ff/A_Cat_s_Commentary_x_2025__39_.png?t=1781818796)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

Trivia Answer: A is [AI](https://www.reddit.com/r/aivideos/comments/1ubmniv/pretty_unrealistic_but_looks_awesome/), B is [Real](https://www.instagram.com/reel/DPZQFppDRw2/)

That’s all for now. 




**P.S: **Before you go… have you [subscribed to our YouTube Channel](https://www.youtube.com/@theneuronai?sub_confirmation=1)? If not, can you?  

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a24710a5-002e-463c-b79d-f5754a0e8e59/Gemini_Generated_Image_c6yadmc6yadmc6ya.png?t=1764928014)
Follow image link: (https://www.youtube.com/@theneuronai?sub_confirmation=1)
Caption: Click the image to subscribe! 

**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).  


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/chatgpt-s-secret-advantage
