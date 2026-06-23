---
source: gmail
newsletter: "the-neuron"
message_id: "19e63f82477a116d"
thread_id: "19e63f82477a116d"
subject: "😺 Meta vs a random GitHub repo (GitHub won)"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Tue, 26 May 2026 11:06:56 +0000 (UTC)"
ingested: 2026-06-23
sha256: 5e6db3b51dbfed98e81ec02d1e787c5ccb6667f482cc3866df63f13e0fc68943
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0e23cc2a-41c6-4bf1-864b-2aaf89631482/image.png?t=1779775921)
Caption: 

Welcome, humans. 

Researchers just found that hackers can hide[ inaudible sounds](https://futurism.com/artificial-intelligence/hackers-inaudible-recordings-hijack-ai-voice-chatbots) in a podcast or YouTube video (i.e., sounds you literally cannot hear) that silently take over your phone's AI assistant.

Once the attack runs, hackers can access your photos, bank accounts, and anything else connected to your voice AI. You don't have to interact with the infected audio at all. It just plays in the background.

The attack takes about 30 minutes to build and is “context-agnostic,” meaning it doesn't matter what you're saying when it hits you. _Your move, Siri._

**Here’s what happened in AI today: **

* 😸 A free GitHub tool bypassed key safety guardrails on Meta and Google's AI models in under 10 minutes.

* 📰 ClickUp fired 22% of its staff and replaced them with 3,000 AI agents.

* 📰 Grok's next model finished training. Elon Musk says it's 2-3 weeks from going public.

* 📰 California's biggest university system doubled down on a $13M/year OpenAI deal, even as its own faculty and students push back.

**Hey: **_Want to reach 700,000+ AI-hungry readers? _[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[ ](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.S: **_Love robots? We’re starting a new robotics newsletter! _[Sign up early here](https://form.jotform.com/260897013570156).

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😸 Meta Spent Millions on AI Safety. A Free GitHub Tool Bypassed Much of It in 10 Minutes.

The AI industry's uncomfortable open secret just got a lot harder to ignore.

Meta and Google have spent hundreds of millions of dollars building safety guardrails into their AI models (the filters that stop those models from explaining how to make weapons, generate malware, or produce harmful content). Last week, a [Financial Times investigation](https://www.ft.com/content/5630ed79-a263-41ed-9a1a-321617ae310e?syn-25a6b1a6=1) found that a free tool called Heretic, available on GitHub, bypassed key safeguards in one of those models in under 10 minutes. On a regular laptop.

The modified model then answered questions about biological weapons it had previously refused to discuss.

**Here's what happened:**

* The FT used Heretic to strip safety filters from Meta's Llama 3.3 (one of the most widely used open-source AI models) in under 10 minutes, no special hardware needed

* A separate test on Google's Gemma 3 model produced similarly alarming outputs, including instructions the original model would have refused

* Heretic's creator told the FT the tool has already been used to build **3,500+ "decensored" model versions**, downloaded 13 million times

* He also bypassed Google's newer Gemma 4 model within 90 minutes of its public release

Here's the key thing to understand: this technique (called "abliteration") only works on **open-source models**, meaning models where anyone can download and modify the underlying code. Proprietary models like Claude or ChatGPT are harder targets because outsiders can't access those core files directly.

Meta declined to comment. Microsoft, whose products are built on some of these open-source models, said something about "additional layers of protection."

**Why This Matters:** The FT investigation is the most visible example yet of a pattern researchers have been documenting for months. A[ Nature Communications study](https://www.nature.com/articles/s41467-026-69010-1) found that reasoning-capable AI models could autonomously talk other AI models into producing harmful outputs through multi-turn conversations, with a 97% success rate across major commercial models. An[ ICLR 2026 paper](https://openreview.net/forum?id=qlf6y1A4Zu) described a more surgical approach: identify and silence the specific internal components responsible for a model's refusals, then steer it elsewhere. Up to 99% bypass rate on some models.

The uncomfortable lesson isn't that one GitHub tool is uniquely dangerous. It's that open-weight AI changes the safety equation completely. Companies can spend months training a model to refuse harmful requests, but once the weights are public, anyone can try to remove those refusals. Safety stops being a locked door and becomes more like a sticker that determined users can peel off.

**Our Take:** Meta and Google will tell you this is a known tradeoff of open-source AI, and that the benefits outweigh the risks. _That argument holds right up until someone uses a 13-million-download tool to do something catastrophic._ The real question is whether governments start treating open-weight AI the way they treat other dual-use technologies, and whether that conversation moves faster than the next model release.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS **

### The IT strategy every team needs for 2026

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0f7e9fb9-d2e5-4fb4-9f28-bf633d912ad3/1200x600_2x.png?t=1771458224)
Follow image link: (https://www.deel.com/resources/it-strategy-toolkit-2026-guide-hr-leaders/?utm_medium=sponsored-newsletter&utm_source=beehiiv&utm_term=YJ4ZPRQDHV&utm_campaign=ww_engage_download_beehiiv_sponnewsletter_it-ttrends2026-feb26_it_all&utm_content=engage_it_sponnewsletter_ittrends2026-sponnews400-it_en&_bhiiv=opp_73df69cf-373b-4015-88e5-d3f6c236f10f_28664f41&bhcl_id=df8e98f1-55a8-4a8b-805f-cb0b30a8f9c7_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

2026 will redefine IT as a strategic driver of global growth. Automation, AI-driven support, unified platforms, and zero-trust security are becoming standard, especially for distributed teams. This [toolkit](https://www.deel.com/resources/it-strategy-toolkit-2026-guide-hr-leaders/?utm_medium=sponsored-newsletter&utm_source=beehiiv&utm_term=YJ4ZPRQDHV&utm_campaign=ww_engage_download_beehiiv_sponnewsletter_it-ttrends2026-feb26_it_all&utm_content=engage_it_sponnewsletter_ittrends2026-sponnews400-it_en&_bhiiv=opp_73df69cf-373b-4015-88e5-d3f6c236f10f_28664f41&bhcl_id=df8e98f1-55a8-4a8b-805f-cb0b30a8f9c7_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f) helps IT and HR leaders assess readiness, define goals, and build a scalable, audit-ready IT strategy for the year ahead. Learn what’s changing and how to prepare.

[Download the Toolkit](https://www.deel.com/resources/it-strategy-toolkit-2026-guide-hr-leaders/?utm_medium=sponsored-newsletter&utm_source=beehiiv&utm_term=YJ4ZPRQDHV&utm_campaign=ww_engage_download_beehiiv_sponnewsletter_it-ttrends2026-feb26_it_all&utm_content=engage_it_sponnewsletter_ittrends2026-sponnews400-it_en&_bhiiv=opp_73df69cf-373b-4015-88e5-d3f6c236f10f_28664f41&bhcl_id=df8e98f1-55a8-4a8b-805f-cb0b30a8f9c7_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Stop Asking Which AI Is Best. Ask Which One Fits Your Workflow.

Most AI debates miss the point. The question isn't "Copilot vs. Gemini vs. Claude." It's "which one lives where you already work?"

[Patrick Giwa](https://www.linkedin.com/posts/patrickgiwa_copilot-may-not-trend-on-linkedin-but-its-activity-7393988407804452865--CEK) laid out a clean framework for this, and it's more useful than any benchmark:

* **Use Copilot** if your team runs on Microsoft 365. It's native inside Word, Excel, Outlook, Teams, and GitHub, so it can generate reports, summarize meetings, automate spreadsheets, and draft proposals without you ever leaving the app you're already in. Bonus: many enterprise companies block ChatGPT but allow Copilot, making it the most-adopted AI tool in corporate settings whether anyone admits it or not.

* **Use Gemini** if your work lives in Google Workspace. Gmail, Docs, Sheets, Drive: Gemini is built into all of it. Best for summarizing email threads, drafting slides and reports, and handling the async collaboration and meeting prep that knowledge workers spend half their day on.

* **Use Claude** when the task requires real thinking across large amounts of material: legal review, research synthesis, long-document analysis, or anything where you need the model to reason carefully rather than just execute quickly. It's not the default enterprise assistant, but it's the specialist you want for heavy lifting.

Patrick's actual point, and it's a good one: "the best AI isn't always the most popular one." It's the one that integrates into how your team already works. Routing the right task to the right model is itself a skill, and most people aren't doing it.

**Total AI beginner? **[Start here](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/) ([goes with this video](https://www.youtube.com/live/QbFU0UNMVaU?si=skJsgUIDjKjAx3DU)).  

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform) 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🍪 Treats to Try 

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

1. [Dell Pro Max with GB10](https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro/xcto_fcm1253_usx) helps teams turn AI ideas into pilots, demos, and workflows with NVIDIA Grace Blackwell power and 128GB memory. [See it here.](https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro/xcto_fcm1253_usx)

2. [Crade](https://crade.ai/?utm_source=theneuron) is a desktop assistant for Mac and Windows that already sees what's on your screen, so you can ask it questions about your Excel formulas, error messages, or PDFs without taking screenshots or switching tabs.

3. [Chert](https://www.trychert.com/?utm_source=theneuron) lets you build and deploy AI directly on iMessage, so you can reach customers at scale through the app they already use every day (YC-backed).

4. [Dodocs](https://dodocs.ai/?utm_source=theneuron) automatically captures, reads, and files your financial documents (invoices, receipts, statements) so your accounting records stay organized without anyone having to touch them.

5. [Maia](https://maia.is/?utm_source=theneuron) is a business automation teammate that connects your apps and runs repeatable workflows for you, so tasks that normally require someone to manually copy data between tools just... happen.

6. [Winn.ai](https://Winn.ai) helps sales reps run better calls by taking notes, tracking talking points, and updating the CRM automatically while the conversation is still happening.

7. [PollyReach](https://pollyreach.ai/?utm_source=theneuron) gives your AI agents their own phone numbers so they can make and receive real calls to handle lead qualification, customer support, and appointment booking automatically.

8. [Frontdesk](https://www.myaifrontdesk.com/?utm_source=theneuron) answers every inbound call, qualifies leads, books appointments, and syncs your CRM 24/7 so no customer ever hits voicemail again (free to try, then $79/month).

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

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/fc331d97-0467-4e24-85b8-a1d0d6b5ee6b/image.png?t=1779776561)
Follow image link: (https://x.com/sattyyouneed/status/2058945920151302224)
Caption: _Yes. Claude Code did this. The contractor is fine. Probably._

* [ClickUp](https://techcrunch.com/2026/05/25/what-clickups-mass-layoff-tells-us-about-the-future-of-work/) cut 22% of its workforce (about 290 people) and replaced them with 3,000 AI agents, framing the cuts as building a "100x org"; surviving employees are being offered salary bands up to $1M if they create "outsized impact using AI."

* [Elon Musk](https://x.com/elonmusk/status/2058787384364265734) announced that Grok's next foundation model, V9-Medium (a 1.5 trillion parameter model), finished training with strong early results; fine-tuning is underway with a public release about 2-3 weeks out.

* [California State University](https://www.npr.org/2026/05/25/nx-s1-5772820/artificial-intelligence-education-technology-california-state-university) renewed its $13M/year OpenAI deal (a 3-year, $39M+ commitment) to become the first AI-powered university system in the US, even as a majority of its own students and faculty said in a survey they're skeptical of AI's educational value.

* [Cybersecurity job postings](https://www.thestar.com.my/tech/tech-news/2026/05/25/one-job-that-is-growing-in-the-ai-era-cybersecurity-experts) jumped 11% year-over-year in Q1 2026 as AI-generated code flooded the market with new vulnerabilities, making it one of the few job categories actively growing because of AI, not despite it.

* [LA's sidewalk delivery robots](https://www.theguardian.com/us-news/2026/may/25/los-angeles-delivery-robots) expanded to 40 neighborhoods (up from just 2 in 2023) as Serve Robotics grew its fleet elevenfold since last year; local restaurants describe the bots as a daily fixture that "everyone films."

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

**FROM OUR PARTNERS **

# The Future of AI: Generative Media Report

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/37542dba-666b-4d7a-8b13-365cadf96272/Google_Startups.jpeg?t=1779297139)
Follow image link: (https://cloud.google.com/resources/content/future-of-ai-genmedia?utm_source=gfs&utm_medium=newsletter&utm_campaign=FY26-Q2-GLOBAL-GCP40293-website-dl-StartupGenMedia-168368&utm_content=neuron2)
Caption: 

Is your startup ready for the generative media boom? The new [Future of AI report](https://cloud.google.com/resources/content/future-of-ai-genmedia?utm_source=gfs&utm_medium=newsletter&utm_campaign=FY26-Q2-GLOBAL-GCP40293-website-dl-StartupGenMedia-168368&utm_content=neuron2) gives founders the inside track on what’s next for the creative economy.

Discover actionable perspectives on synthetic media, multimodal models, and the infrastructure powering next-gen apps. 

[Stay ahead of the curve.](https://cloud.google.com/resources/content/future-of-ai-genmedia?utm_source=gfs&utm_medium=newsletter&utm_campaign=FY26-Q2-GLOBAL-GCP40293-website-dl-StartupGenMedia-168368&utm_content=neuron2)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🔧 Tuesday Tool Tip: Use Audio Tags in ElevenLabs to Make Your Voiceovers Actually Perform

If your ElevenLabs voiceovers still sound like a robot narrating a terms-of-service agreement, the fix isn't a better model. It's a technique ElevenLabs calls[ Audio Tags](https://elevenlabs.io/docs/eleven-agents/best-practices/prompting-guide) and their own team says it's now "an essential skill" with Eleven v3.

Here's how it works: instead of just writing the words you want spoken, you embed small direction cues directly inside the script. Tags like [excited], [whispers], or [sighs] tell the model _how_ to perform the line, not just what to say. Think of it as stage directions for your AI voice actor.

ElevenLabs is straightforward about the tradeoff: v3 requires more prompt engineering than older models, but gives you far more expressive control in return. The key is using tags with intent and not sprinkling them randomly, but placing them where a real performer would actually change their delivery.

**Basic approach:**

1. Write your script normally first

2. Read it out loud and mark every line where tone, pacing, or emotion should shift

3. Layer in tags at those exact moments and only those moments

**Example:**

Instead of:

```
We did it. I can't believe it.
```
Write:

```
[happily][shouts] We did it! [laughs] I can't believe it.
```
You can stack tags, place them mid-sentence, and use them to direct emotional shifts, dialogue beats, and nonverbal reactions (sighs, laughs, pauses) without switching models or re-recording anything. ElevenLabs specifically recommends this for videos, audiobooks, interactive characters, and any dialogue-heavy content where plain text underspecifies the performance.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# A Cat’s Commentary 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/eb667955-446d-43e9-af7b-467b978da02f/A_Cat_s_Commentary_x_2025__9_.png?t=1778566914)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. 




**P.S: **Before you go… have you [subscribed to our YouTube Channel](https://www.youtube.com/@theneuronai?sub_confirmation=1)? If not, can you?  

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a24710a5-002e-463c-b79d-f5754a0e8e59/Gemini_Generated_Image_c6yadmc6yadmc6ya.png?t=1764928014)
Follow image link: (https://www.youtube.com/@theneuronai?sub_confirmation=1)
Caption: Click the image to subscribe! 

**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).  


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/a-free-tool-just-broke-meta-s-guardrails
