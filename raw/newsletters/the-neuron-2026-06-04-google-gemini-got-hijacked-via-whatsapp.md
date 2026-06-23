---
source: gmail
newsletter: "the-neuron"
message_id: "19e92529367e936d"
thread_id: "19e92529367e936d"
subject: "😺 Google Gemini got hijacked via WhatsApp"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Thu, 04 Jun 2026 11:07:27 +0000 (UTC)"
ingested: 2026-06-23
sha256: af52ec51e9e6c92892195243bac0d98bfe90e583144a04db42df9f59eeafcd8c
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f6b7d959-5b51-42ff-b328-50fc9664fefe/image.png?t=1780554618)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/bcce1a46-d66c-497e-a849-b78ba152f86a/In_Partnership_with_outsystems.png?t=1773945239)
Follow image link: (https://www.outsystems.com/Platform/Signup?utm_source=dzone&utm_medium=display&utm_campaign=am-us-dis-2026-02-26-dzone-devrel-ads&utm_term=newsletter&utm_content=personal-environment&utm_campaignteam=community&utm_partner=none)
Caption: 

Welcome, humans. 

Google just [dropped a new app](https://techcrunch.com/2026/06/03/googles-dreambeans-its-weirdest-named-ai-tool-to-date-will-turn-your-life-into-a-cartoon/) from its Labs division called Dreambeans. It scans your Gmail, Photos, and Calendar, then turns your personal data into a short daily set of AI-illustrated stories designed to have a beginning, middle, and end, so you actually stop scrolling.

Somewhere at Google, a product manager pitched this with a straight face and someone said "great, let's call it Dreambeans."

_We genuinely cannot tell if that's the worst product name in tech history or the best. But we respect the chaos._

🔴** LIVE TODAY at 10am PT: Mercury-alpha. GPT-5.6 or just vibes?**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/762501ca-fe38-45fd-a22d-dfbd80288c97/LIVE_Thumbnails__YT___LI___5_.png?t=1780510286)
Follow image link: (https://www.youtube.com/watch?app=desktop&v=iWq6xCSDxVM)
Caption: 

Everyone is talking about Mercury-alpha, the mystery model that many believe could be GPT-5.6. In this live discussion, we're separating fact from speculation and unpacking what would actually matter if OpenAI releases a new flagship model this week.

We'll cover:

* What Mercury-alpha is (and why people think it's GPT-5.6)

* The biggest rumors and evidence so far

* What a new OpenAI model would need to deliver to move the industry forward

* How Mercury-alpha fits into the broader AI agent race

* Codex, Hermes Desktop, and the rise of coding and desktop agents

* What all of this means for AI users, builders, and businesses

Join us live, bring your questions, and help us figure out whether Mercury-alpha is the next major leap in AI or just another chapter in the internet's favorite pastime: model-name archaeology.

**Here’s what happened in AI today: **

* 😺 Researchers found a way to hijack Google Gemini through a WhatsApp message

* 📰 Meta may charge $200/month for its upcoming AI agent called Hatch

* 📰 Meta was forced to stop tracking employees' keystrokes to train AI

* 🍪 Canva now pulls Perplexity research directly into your designs

**Hey: **_Want to reach 700,000+ AI-hungry readers? _[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[ ](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.S: **_Love robots? We’re starting a new robotics newsletter! _[Sign up early here](https://form.jotform.com/260897013570156).

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🙀** ****Someone Figured Out How to Hijack Gemini Through a WhatsApp Message**

Here's a scenario: someone sends you a normal-looking WhatsApp message. You never click anything weird. You never type a suspicious command. But your AI assistant, Google Gemini, reads the notification, follows hidden instructions buried inside it, and quietly exfiltrates your data.

That's exactly what[ SafeBreach Labs researchers](https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/) just demonstrated. This is their second time breaking Gemini this way. Their previous research weaponized Google Calendar invites against it.

The attack type is called indirect prompt injection: hiding malicious commands inside content the AI reads, rather than typing them directly. The novel trick here is a technique called "Fake Context Alignment," which makes attack instructions look like a legitimate part of your ongoing conversation, specifically designed to bypass[ Google's existing defenses](https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini) against this kind of attack.

**Here's what happened:**

* Gemini's Android agent reads incoming notifications from messaging apps to give context-aware responses

* Researchers embedded hidden instructions inside crafted messages; the attack works across WhatsApp, Slack, Signal, SMS, Instagram, and Messenger

* Gemini followed the attacker's commands silently, with no alert to the user

* Five threat categories were demonstrated: data theft, unauthorized actions, phishing relay, account takeover prep, and silent surveillance

* Even without Gemini having external tool access, the poisoned context alone lets attackers make Gemini deliver fake system messages, turning a trusted AI interface into a phishing launcher

The researchers disclosed to Google before publishing.[ Google's layered defense page](https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini) acknowledges indirect prompt injection as a known threat class with active mitigations. The SafeBreach research demonstrates those mitigations were bypassed.

**Why this matters:** The attack surface isn't a bug in one app. It's the design of how AI assistants work. Any notification Gemini reads from any app is now a potential delivery channel. The more access your assistant has, the bigger the blast radius.

**Our take:** Google has defenses. They got bypassed twice by the same team. That's the uncomfortable part. The fix isn't panic; it's permission hygiene. Audit what Gemini can access, and disable anything you don't actively use.[ Here's Google's own guidance](https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini) on how their defenses work, worth reading to understand what's protected and what isn't. _The next researcher is already looking._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS **

# Ready to build AI-powered apps and agents?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/005f316e-7edc-44c3-97bf-8a60d0594617/dzone-ad-640x300.png?t=1780419533)
Follow image link: (https://www.outsystems.com/Platform/Signup?utm_source=dzone&utm_medium=display&utm_campaign=am-us-dis-2026-02-26-dzone-devrel-ads&utm_term=newsletter&utm_content=personal-environment&utm_campaignteam=community&utm_partner=none)
Caption: 

Join the [OutSystems](https://www.outsystems.com/Platform/Signup?utm_source=dzone&utm_medium=display&utm_campaign=am-us-dis-2026-02-26-dzone-devrel-ads&utm_term=newsletter&utm_content=personal-environment&utm_campaignteam=community&utm_partner=none) developer community and start using AI to develop, deploy, and scale your next mission-critical agentic application for free. Go from prompt to production faster, with full control, on a unified, agile, and enterprise-proven platform. 

[Start Now](https://www.outsystems.com/Platform/Signup?utm_source=dzone&utm_medium=display&utm_campaign=am-us-dis-2026-02-26-dzone-devrel-ads&utm_term=newsletter&utm_content=personal-environment&utm_campaignteam=community&utm_partner=none)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# **🎓 ****AI Skill of the Day:  Debug with screenshots, not vibes**

One underrated lesson from Bryce Rattner Keithley’s recent[ no-code iPhone app build](https://www.lennysnewsletter.com/p/how-i-ai-codex-goals-explained-and): when the AI does not understand what you want, stop describing harder.

Show it.

Bryce used screenshots, sketches, and even photos of herself demonstrating exercise positions to give the AI better context. When a prompt went sideways, she often restarted the prompt instead of endlessly patching it.

Try this loop the next time your build gets stuck:

* Screenshot what you see.

* Screenshot or sketch what you wanted.

* Ask the AI to compare the two.

* Restart the prompt if the conversation gets messy.

* Save the working pattern once it solves the bug.

That is less “prompt engineering” and more managing a visual coworker who occasionally needs you to point at the screen.

**Total AI beginner? **[Start here](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/) ([goes with this video](https://www.youtube.com/live/QbFU0UNMVaU?si=skJsgUIDjKjAx3DU)).  

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform) 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🍪 Treats to Try 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2df11868-24bf-4313-8608-8060a065abe7/AI_Image-Dell-Pro-Max-AI-PC-with-GB10__1_.png?t=1780494190)
Follow image link: (https://www.outsystems.com/Platform/Signup?utm_source=dzone&utm_medium=display&utm_campaign=am-us-dis-2026-02-26-dzone-devrel-ads&utm_term=newsletter&utm_content=personal-environment&utm_campaignteam=community&utm_partner=none)
Caption: 

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

1. *Your AI roadmap needs a test course. The [Dell Pro Max with GB10](http://Your AI roadmap needs a test course. The Dell Pro Max with GB10 helps teams experiment before making bigger bets.) helps teams experiment before making bigger bets.

2. [Canva](https://www.canva.com/newsroom/news/perplexity/?utm_source=theneuron) connected to Perplexity so you can pull live research directly into Canva and turn it into editable, on-brand decks and assets in one click, no copy-pasting between tabs.

3. [Ramp Stack](https://ramp.com/stack?utm_source=theneuron) automates bookkeeping, reconciliations, journal entries, and month-end close for accounting firms, with human sign-off built in —free through August.

4. [Reve 2.0](https://x.com/reve/status/2062260665121919101?utm_source=theneuron) generates and edits 4K images with precise layout control and code-like editing for individual objects in a scene, so you can change one element without regenerating everything.

5. [Miso One](https://www.misolabs.ai/?utm_source=theneuron) is an open-source text-to-speech model that clones any voice from 10 seconds of audio and generates expressive speech with 110ms latency —free to try.

6. [Krater](https://krater.ai/?utm_source=theneuron) puts ChatGPT, Claude, Gemini, and 350+ models in one workspace to generate text, images, video, and audio without juggling separate subscriptions or API keys —from $7.50/mo.

7. [Winn.AI](https://Winn.AI) joins your sales calls live, takes real-time notes, fills your CRM automatically, and coaches reps on what to say next, so your team spends more time closing and less time typing.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# **NEW Podcast: Tiago Sada on how to prove you're human online.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5745fea8-8da0-4703-80e4-e522d64e7701/TN_Thumbnail_TiagoSada_2.png?t=1780505471)
Follow image link: (https://www.youtube.com/watch?v=oecqV9-Sh1o)
Caption: 

Sam Altman co-founded Tools for Humanity six years ago with one bet: that AI would eventually make it impossible to tell humans from bots on the internet and that we'd need a new kind of "human passport" before that happened. They raised $240M and built an eyeball-scanning orb to prove the thesis. _It was a weird bet. It looks a lot less weird now._

In our latest episode, Corey sits down with Tiago Sada, Chief Product Officer at Tools for Humanity, to unpack why CAPTCHAs and KYC are already broken, how AI agents can get "digital power of attorney" to act on your behalf, why using AI to detect AI is an unwinnable arms race, and what it means that bots already outnumber humans on the internet.

New episodes air **every week** on: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)** **

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c07a2c16-f40e-42ea-9ed3-3d9854506857/Screenshot_2026-06-03_at_1.36.44_PM.png?t=1780519754)
Follow image link: (https://x.com/OpenAI/status/2062249312839434452)
Caption: To quote Corey: Not to be egotistical or anything, but… _if the OA marketing ppl put this orange cat in this ad to catch our curiosity, fire up that Leo Dicaprio meme because you definitely got our attention!_

* [Meta](https://www.theinformation.com/articles/meta-looks-charge-200-month-planned-hatch-ai-agent) is reportedly considering charging up to $200/month for Hatch, its upcoming consumer AI agent (formerly called OpenClaw), putting it in direct competition with top-tier offerings from OpenAI and Anthropic.

* Meta was forced to [stop its program tracking employee mouse clicks and keystrokes](https://www.reuters.com/world/meta-scales-back-ai-mouse-clicks-tool-citing-employee-concerns-2026-06-02/) to train AI, after over 1,500 workers signed a petition calling it an "Employee Data Extraction Factory."

* [Perplexity](https://thenextweb.com/news/perplexity-ai-split-compute-pc-cloud-inference-cost) built a real-time system that decides whether each AI query runs on your local PC or in the cloud, cutting inference costs without hurting quality; revenue hit $500M on just 34% headcount growth.

* [Google](https://techcrunch.com/2026/06/03/googles-dreambeans-its-weirdest-named-ai-tool-to-date-will-turn-your-life-into-a-cartoon/) launched Dreambeans, a Labs experiment that turns your Gmail, Photos, and Calendar data into a short daily set of AI-illustrated stories, a deliberately finite alternative to infinite scrolling.

* [AI-generated spam](https://sea.mashable.com/tech/48507/ai-is-fueling-reddits-spam-problem) is flooding Reddit faster than moderators can act; Cornell researchers found 67% of mods say it erodes authentic community and 53% call it nearly ungovernable.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

**FROM OUR PARTNERS **

# Your local AI sandbox is ready

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/61aadcbc-322f-4c60-b5ce-c612eff40b3f/image.png?t=1780431305)
Follow image link: (https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro/xcto_fcm1253_usx)
Caption: 

Want a computer you can _actually_ [train your own AI on? Dell Pro Max with GB10](https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro/xcto_fcm1253_usx) brings NVIDIA Grace Blackwell architecture, 128GB memory, and NVIDIA DGX OS 7 to founders, builders, and AI enthusiasts testing agents, demos, and model workflows locally.

[Check out the Dell Pro Max with GB10 here.](https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro/xcto_fcm1253_usx)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 📖** Thursday Trivia**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/acfb3929-8f45-41d7-a642-f33fcd3c948d/image.png?t=1780555691)
Caption: **A**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4f500d8c-288b-4684-8188-7b7a52c3a537/image.png?t=1780555714)
Caption: **B**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# A Cat’s Commentary 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/915c1b3b-e549-4cfe-b715-6426631842cb/A_Cat_s_Commentary_x_2025__2_.png?t=1779161070)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

[A is AI](https://www.reddit.com/r/StableDiffusion/comments/1tc70et/trying_more_serious_tng_content_with_ltx23/), [B is Real](https://screenrant.com/star-trek-tng-enterprise-crew-most-superpowers/)

A was made using LTX 2.3, LoRA fine-tune that recreates the look and feel of 1990s TNG television production



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
https://www.theneurondaily.com/p/google-gemini-got-hijacked-via-whatsapp
