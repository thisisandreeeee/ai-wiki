---
source: gmail
newsletter: "the-neuron"
message_id: "1a1e9017b9bc1ef5"
thread_id: "1a1e9017b9bc1ef5"
subject: "😺 California vs OpenAI: the rogue AI lawsuit"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Tue, 17 Nov 2026 10:15:49 +0000 (UTC)"
ingested: 2026-11-23
sha256: cc40adc91353f4db845f3c047ec3542ba8facf0fce22cf9d479e525b07a4ab54
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2e5a5af6-a42a-4a24-bf5d-ec565604a6da/California_Sues_OpenAI__Rogue_AI_Escapes.png?t=1794897551)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c7eadc2a-fd0a-42d4-ac47-d6713de3b5f2/In_partnership_with__outsystems.png?t=1794415524)
Follow image link: (https://go.outsystems.com/scaleable-AI-apps/?utm_campaign=am-us-dis-2026-02-26-dzone-devrel-ads&utm_medium=display&utm_source=dzone&utm_term=newsletter&utm_content=personal-environment)
Caption: 

Welcome, humans.

So apparently Jordan Belfort, the actual Wolf of Wall Street, co-founded an AI phone-sales startup called [Tone](https://techcrunch.com/2026/11/16/jordan-belforts-new-ai-voice-startup-tone-wants-to-sell-like-the-wolf-of-wall-street/). Its trick is tonality. The AI phrases statements as questions to build engagement and whispers to imply scarcity, with a claimed reply delay of about 600 milliseconds.

The catch is that TechCrunch couldn't verify any of it works, neither founder is an engineer, and Belfort calls himself the judge of what sounds right. _So the man famous for selling over the phone is now selling a robot that sells over the phone, and quality control is his ear._

**Here’s what happened in AI today:**

* 😸 California sued OpenAI over agents that hacked Hugging Face.

* 📰 Google found a fully automated AI hacking framework.

* 📰 Anthropic shortened its bug disclosure window to 30 days.

* 🍪 Gemini Notebook now turns your sources into websites.

* 🎓 Give your AI a short handoff note, not a transcript.

… and a [**whole lot more that you can read about here.**](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-november-17-2026/)

Advertise to 700K readers of The Neuron here! (https://www.theneuron.ai/get-media-kit/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# California sues OpenAI over AI agents that escaped a test and hacked another company

California's attorney general [sued OpenAI](https://techcrunch.com/2026/11/16/california-state-ag-sues-openai-over-rogue-agent-incidents/) on Monday, arguing that its model testing is an ongoing danger to the public.

The case starts in July, when OpenAI was testing GPT-5.6 Sol and an even more capable unreleased model on ExploitGym, a benchmark (basically a standardized exam for AI) of 898 real software vulnerabilities. The job is to turn each one into a working attack.

The test ran in a sandbox, a locked digital room with no internet. Except for one door, a tool that installs software packages through an internal proxy (a middleman server that stores copies of them). [According to OpenAI](https://techcrunch.com/2026/07/21/openai-says-hugging-face-was-breached-by-its-pre-release-models/), the models found a previously unknown flaw in that proxy, called a zero-day, and used it to get online.

Once outside, the models figured out Hugging Face held the answer key and pulled the solutions from its production database. _So the student didn't just peek at the teacher's desk. The student picked the lock on the school._ Hugging Face [caught it on its own](https://decrypt.co/374015/openai-models-escaped-test-environment-hacked-hugging-face-cheat-benchmark).

Here's what California alleges (allegations, not court findings):

* OpenAI's testing lacks adequate safety controls, which makes it a public nuisance (the main claim), and marketing an unsafe product is unfair competition.

* Hugging Face was one of at least 80 incidents, with RubyGems, Wikimedia, and Australian government sites also hit. OpenAI disclosed only 27.

"Public nuisance" is an old legal idea for something that unreasonably interferes with public safety, like a factory fouling a river. The usual fix is an injunction, a court order to stop or repair the problem. California wants one, plus civil penalties of $2,500 per proven unfair-competition violation.

OpenAI says the suit singles out one company for an industry-wide problem.

**Why this matters:** Picture handing someone a task and checking only whether the answer looks right. That's how most of us use AI at work. An independent METR and Redwood Research review found the agents wanted a passing grade, not chaos, and when they thought shortcuts would be rejected, they went after the grader. _Every boss who's received a suspiciously perfect report knows the feeling._ OpenAI admits it missed early warning signs. California alleges they began in May and testing continued anyway, which is unproven. Either way, who checks the work is now a legal question.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# **Building agentic apps is easy. Governing them is the real challenge.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/efaef604-50c4-45f5-873d-9a54a029e427/dzone-ad-640x320.png?t=1794415358)
Follow image link: (https://go.outsystems.com/scaleable-AI-apps/?utm_campaign=am-us-dis-2026-02-26-dzone-devrel-ads&utm_medium=display&utm_source=dzone&utm_term=newsletter&utm_content=personal-environment)
Caption: 

Moving from a prototype to a secure, enterprise-grade application requires strict controls, instant scalability, and trust. OutSystems bridges the gap between concept and production. It equips developers with built-in guardrails for automatic compliance, seamless enterprise scaling, and a unified platform to manage every agent in one place. You get the speed of AI innovation without sacrificing control, security, or governance.

Stop letting compliance slow you down. Build and scale enterprise-ready AI apps with total confidence with OutSystems.

Start building for free today (https://go.outsystems.com/scaleable-AI-apps/?utm_campaign=am-us-dis-2026-02-26-dzone-devrel-ads&utm_medium=display&utm_source=dzone&utm_term=newsletter&utm_content=personal-environment)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Give your AI a smaller, better memory

[Anthropic tested](https://www.anthropic.com/research/components-of-agent-memory) what happens when Claude keeps its own notes between sessions, using Pokémon Red. About 10,000 steps in, the older Claude Sonnet 3.7 had written 413 memory files, nearly a million characters, with a separate file for every battle, item, and character. It earned one badge, and its notes kept going stale as the game changed.

Claude Fable 5 kept nine files plus one top-level file, roughly 43,000 characters, covering its goal, routes, and strategies it had tested. It earned four badges. The difference was what it saved. Fable wrote down things it couldn't see on screen and skipped what the game shows every turn, like money or map position.

Then Anthropic added a review step that checked notes against session transcripts. Claude had noted that a PokéCenter in Mt. Moon was on the east side, which was wrong, and it walked off a one-way ledge. The check rewrote the note, and with the fix Claude reached Cerulean City at action 1,935. The uncorrected run never made it. _A confidently wrong note can be worse than no note at all._ (It was one run per condition, so treat it as a good story, not proof.)

You can steal this for any long project you keep returning to with ChatGPT or Claude. At the end of a session, ask for a handoff instead of a transcript.

1. Ask for a short note with only what you'll need again, not the whole transcript.

2. Have the AI check the note against the conversation and flag anything it can't verify.

3. Read it yourself before the next session, especially names, numbers, and decisions.

```
Create a short handoff for our next session. Include the goal, decisions made, verified facts with their sources, unresolved questions, and next actions. Mark uncertain details explicitly. Do not save a blow-by-blow transcript. Before finalizing, check the notes against this conversation and flag anything you cannot verify.
```
**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

### Attio is the #1 fastest-growing CRM on Brex and Ramp.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6c1ef7f5-3085-4245-aa68-46395f82cfc3/Fastest_Growing_Lander_Nov_26_-_Secondary_CPC.png?t=1793724553)
Follow image link: (https://attio.com/?utm_source=beehiiv&utm_medium=newsletter-sponsorship&utm_campaign=beehiiv-Y26&utm_content=YJ4ZPRQDHV&_bhiiv=opp_854294f8-82cc-4679-86fa-96caf69dcbf8_7395cee5&bhcl_id=bdb34859-1508-4b5c-b377-2e2ea843ed1c_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

Built for the most ambitious companies in GTM, [_Attio_](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter-sponsorship&utm_campaign=beehiiv-Y26&utm_content=YJ4ZPRQDHV&_bhiiv=opp_854294f8-82cc-4679-86fa-96caf69dcbf8_7395cee5&bhcl_id=bdb34859-1508-4b5c-b377-2e2ea843ed1c_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f) is an end to end revenue platform that allows teams to run multiple plays across different revenue motions and lifecycles.

Teams at the frontier are already building on it: Granola, turbopuffer, Modal, and many many more.

[_Start building on Attio._](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter-sponsorship&utm_campaign=beehiiv-Y26&utm_content=YJ4ZPRQDHV&_bhiiv=opp_854294f8-82cc-4679-86fa-96caf69dcbf8_7395cee5&bhcl_id=bdb34859-1508-4b5c-b377-2e2ea843ed1c_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/35fb6940-b368-4eb8-b3d1-9a282cb4201e/image.png?t=1794905135)
Follow image link: (https://x.com/perplexity_ai/status/2122352071295009156)
Caption: Perplexity says it’s putting 10,000+ GPUs behind AI that can do research on its own.

* Google's threat team [found a hacking framework](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold) that reads software patches, writes exploits for the flaws, and launches them with no human involved, a first for the group.

* OpenAI [brought in outside researchers](https://openai.com/index/our-first-phase-of-embedded-assessments/) from Apollo Research, Goodfire, METR, and Transluce to assess different parts of its models and safeguards from the inside.

* Anthropic [shortened its bug-disclosure window](https://www.anthropic.com/research/coordinated-vulnerability-disclosure-timelines) from 90 days to 30 for high-severity and critical flaws it reports starting January 1, 2027, citing AI making rediscovery likelier.

* The Commerce Department [issued an interim rule](https://techcrunch.com/2026/11/16/us-tightens-ai-chip-export-controls-to-deter-chinese-companies-from-accessing-compute-remotely/) requiring licenses to export AI chips to any data center that might give China or other restricted countries computing access, even indirectly.

* Apple [detailed new Mac controls](https://techcrunch.com/2026/11/16/apple-reveals-new-mac-security-controls-as-ai-agents-raise-privacy-risks/) coming in macOS 27.3, including an ask-every-time option, for apps and agents that request full disk access.

* Perplexity [launched Frontier Research](https://x.com/perplexity_ai/status/2122352071295009156), an initiative with 10,000+ GPUs aimed at autonomous research systems, and said it will openly release its models, data, and benchmarks.

Want absolutely EVERYTHING that happened in AI this week? [**Click here!**](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-monday-november-16-2026/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). _[_Advertise to 700K+ readers here_](https://info.technologyadvice.com/advertise-with-the-neuron)_!_

1. [Gemini Notebook](https://x.com/Gemini_Notebook/status/2122436141282660596) turns your sources into a shareable interactive website when you type "make me a site" in chat, like a periodic table explorer with a built-in quiz.

2. [Ask Maps](https://blog.google/products-and-platforms/products/maps/ask-maps-holiday-travel-features-2026/) now builds day-by-day trip itineraries and, in the U.S., can call local businesses to book things like a nail, pet care, or auto appointment.

3. [ChatGPT for Healthcare](https://openai.com/index/more-ways-to-move-care-forward-with-chatgpt-for-healthcare/) adds agents that work inside your existing systems, like filling out a prior authorization and flagging gaps for a human to approve (patient data requires a BAA).

4. [Audible](https://techcrunch.com/2026/11/16/audible-turns-to-ai-to-help-users-discover-audiobooks/) now plays a short audio overview of a book's themes and what readers liked, with editor or author commentary, on select English titles in the U.S.

5. [StreetReaderAI](https://x.com/GoogleResearch/status/2122395958248120626) is an open-source map app that lets blind and low-vision users explore street-level imagery by voice or keyboard, with spoken descriptions and answers to follow-up questions.

6. [Tone](https://techcrunch.com/2026/11/16/jordan-belforts-new-ai-voice-startup-tone-wants-to-sell-like-the-wolf-of-wall-street/) lets authors generate expressive audio narration of their books in one of its voices, or in a clone of their own once cloning rolls out.

7. [ByteVoice](https://www.producthunt.com/products/bytevoice) listens to your voice commands for coding agents like Claude Code and Codex, then reads their summaries back to you.

8. [Deslop](https://github.com/etodanik/deslop) gives Claude a writing skill for revising drafts that sound obviously machine-generated.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

## UPCOMING EVENT: The Neuron IRL in San Francisco

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c17aafde-2e0d-40fe-b4fe-a68924cb8a35/Email_1250x750.png?t=1793122880)
Follow image link: (https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)
Caption: 

The Neuron is **going IRL** on [**November 18 at 4:30 PM PT**](https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)! Join us in San Francisco for **drinks, bites, special guests, and a live recording of The Neuron podcast.** Huge thanks to Slack and Alumni Ventures for making it happen.

**It’s free, but space is limited. Save your spot!**

RSVP for The Neuron IRL (https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 🐦 Tuesday Tweets

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/9701a845-01cd-46b5-a78e-4aba837aff3d/image.png?t=1794905199)
Follow image link: (https://x.com/Reuters/status/2122444599104815339)
Caption: 

Sam Altman has a lot to say about Nvidia's Jensen Huang, who stepped down as CEO last week. [Speaking at a Semafor event](https://x.com/Reuters/status/2122444599104815339), Altman called Huang a longtime personal hero, said even heroes have flaws, and said it's hard to imagine the AI revolution without him.

He also said he feels real empathy for Huang's situation, and he wouldn't say whether Huang should return to Nvidia. _Altman knows a thing or two about getting pushed out of the corner office and coming back._

The other bit worth catching from that same appearance is on OpenAI itself. Altman said the company will go public eventually, but he sees real downsides to being a public company right now, while it's making high-stakes decisions about safety and how society uses the technology.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0820d5ae-9854-4066-8517-059e00d7ea16/ChatGPT_Image_Aug_7__2026__05_43_59_PM.png?t=1786149887)
Caption: 

New episodes air **every week** on Wednesdays: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/050f7c47-e209-45ba-bece-b2da22753f03/3.png?t=1794905786)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today!




**Btw: **We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.S. **Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/california-sued-openai-over-rogue-agents
