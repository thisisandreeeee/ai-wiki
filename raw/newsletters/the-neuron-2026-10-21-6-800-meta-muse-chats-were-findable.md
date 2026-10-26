---
source: gmail
newsletter: "the-neuron"
message_id: "1a15e06cf212e2cf"
thread_id: "1a15e06cf212e2cf"
subject: "😺 6,800+ Meta Muse chats were findable"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Wed, 21 Oct 2026 10:34:24 +0000 (UTC)"
ingested: 2026-10-26
sha256: 554a98039d83756b18582c5a54f79c75c5588b6d6946eece0827a34adfde6965
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2be99e51-52aa-47a1-b6ad-64015675db45/Meta_s_Public_Chat_Trail.png?t=1792566720)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/574d176c-9d5a-4253-9876-6dc2348b2e18/In_partnership_with_fingerprint.png?t=1792436034)
Follow image link: (https://fingerprint.com/blog/how-to-detect-meta-muse-ai-agent/?utm_campaign=Primary102126&utm_source=theneuron&utm_medium=newsletter)
Caption: 

Welcome, humans.

So guess what: SpaceX is now basically an AI company that also launches rockets. The company [reported third-quarter revenue of $14.6B](https://techcrunch.com/2026/10/20/spacexs-ai-business-is-beating-expectations/), and its new "Super Intelligence" division brought in $7.5B of it. That's about half.

That division bundles three things: Grok (Elon's chatbot), Cursor (the AI coding tool SpaceX recently acquired), and a "neocloud" business. A neocloud is a landlord for AI computing power: it fills data centers with chips and rents them to whoever needs them. SpaceX now has 1.7 GW of compute, which measures how much electricity those chips can draw.

The bill for all this is steep. SpaceX spent $19.6B on capital expenditures this quarter, mostly on data centers like Colossus II plus Starship rockets, and its [filing forecasts](https://www.sec.gov/ix?doc=/Archives/edgar/data/1181412/000162828026066482/spcx-20261020.htm) $35B to $40B of investment next quarter. _The rockets are officially the side hustle._

**Here’s what happened in AI today:**

* 😸 Meta's Muse shared chats were findable without the link

* 📰 OpenAI bought Orchestra Bio to push into drug development

* 📰 Anthropic pitched a federal bill to gate risky model releases

* 🍪 ChatGPT added PIN-locked chats with separate memory

* 🎓 Spreadsheet tricks using Claude

Advertise to 700K readers of The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😼 Shared Meta Muse Chats Were Findable Through Public Web Records, Researchers Say

A security firm says anyone could find chats people shared from Meta's Muse app without ever being sent the link. Claroc [found 6,800+ share addresses](https://blog.claroc.io/ghostshares-muse-passive-dns/) using public internet records, and The Verge reports Meta [paused Muse's sharing feature](https://www.theverge.com/tech/1014627/meta-muse-ai-sharing-ai-chats) while it looks into how that happened.

Here's how sharing works. When you tap share in Muse, it publishes your chat as a web page that opens for anyone with the link, no login needed. That's by design, since it's how your coworker reads it. Plenty of AI apps share this way.

The twist is the address. Muse builds each page's address from the chat's title plus a random code, so a chat called "Q3 budget review" gets something like q3-budget-review-4d7a19e2 followed by a Meta domain. Whenever someone opens a page, their browser looks that address up in DNS, the internet's phone book for turning names into server locations. Services called passive DNS quietly log those lookups and let anyone search them. Claroc searched one, and the chat titles came back readable, like a table of contents.

_Unlisted, it turns out, can still mean listed in a phone book nobody told you about._

The random code was supposed to keep addresses unguessable. But the full address gets logged the first time anyone opens the page, so the code gets published right alongside the title.

Claroc opened a few hundred pages without logging in. Most were harmless, like small-business sites and event calendars. A minority were not:

* A job candidate's prep notes for a confidential call with a frontier AI lab, including the lab's internal contact and meeting time

* A marketing company's internal revenue review marked for its CEO

* A small-business loan application with the amount requested

* A full-year staff vacation calendar listing dozens of employees

_Nothing says "confidential" like a public web page._

Muse is not small, either. Sensor Tower data shows it [passed 10.9M downloads](https://techcrunch.com/2026/10/20/metas-muse-hits-10m-u-s-downloads-in-40-days-a-milestone-reached-by-only-11-other-apps/) in its first 40 days, per TechCrunch. Two caveats: Claroc sells software that spots risky AI sharing, so it has a stake in the story, and its search covered one lookup service, one address pattern, and a short window. It reports no evidence anyone misused the pages, which were public because their owners shared them. Claroc reported the issue to Meta's bug bounty program on October 8.

**Our take:** A share link promises that only people you send it to will open it, and nothing enforces that promise. Muse made it easier to break by printing the chat title in the address, which helps the person sharing and everyone else too. Meta put 39% of its October ad spend behind Muse, per Sensor Tower, so the app is collecting a lot of trust fast. Claroc spotted 27 new share addresses the day it last checked, so what happens to the thousands already out there?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# Meta's Muse agent is already on your site. Can you tell it's there?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6e35b341-ea58-4f4e-9b75-813b2f637722/announcement.png?t=1792435997)
Follow image link: (https://fingerprint.com/blog/how-to-detect-meta-muse-ai-agent/?utm_campaign=Primary102126&utm_source=theneuron&utm_medium=newsletter)
Caption: 

Muse runs a real browser on a cloud virtual machine, signs in to accounts, and completes purchases for real users. It arrives with no verifiable identity, a tampered browser, and suppressed automation flags. Fingerprint labels inferred Muse traffic by name.

* **See it**: Bot Detection returns bot_type: "meta_muse", not just an unknown bot.

* **Understand your traffic: **Device intelligence shows you how much traffic looks like this, and whether it matters.

* **Act on it**: Set Muse policies in our rules engine or your own.

Muse detection is free for existing Bot Detection customers. New teams can start free.

[Read how to detect Muse, step by step](https://fingerprint.com/blog/how-to-detect-meta-muse-ai-agent/?utm_campaign=Primary102126&utm_source=theneuron&utm_medium=newsletter)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Make sense of a spreadsheet someone else left behind

Your colleague quits, and his revenue model lands on your desk. Four tabs, a few cell comments, and finance wants projections by Thursday. That's the scenario in [Anthropic's walkthrough](https://claude.com/resources/use-cases/understand-and-extend-an-inherited-spreadsheet) for using Claude on an inherited spreadsheet, and anyone who has opened a stranger's workbook knows the dread.

The move is to ask for an explanation before any changes. In Anthropic's example, Claude read the legend and comments, decoded the color coding (blue for inputs, green for formulas pulling from other tabs), and explained a seasonality formula. It also flagged what nobody had written down, like a floor that stops the tax line from going negative. Only then did it add the new quarters, keeping all 348 original formulas. _It's a vendor demo, so check the work._

Try it:

1. Copy the file, and work on the copy.

2. Ask for an explanation and an issue log, with no edits.

3. Check each flag yourself or with the owner, then change one assumption and confirm it flows through every tab.

```
I inherited this spreadsheet and need to understand it before changing anything. Don't edit it.

1. Explain how the tabs connect and what each key formula does.
2. List anything undocumented, hidden, hardcoded where neighboring cells are formulas, or linked to outside files.
3. Give me an issue log: cell, what's wrong, which outputs it affects, and High, Medium, or Low risk.
```
**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

# Give your AI agents the whole web with Oxylabs Web API. 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e5302e39-bf50-4edc-a4c0-7c5f2e11c5bf/Web-API-Newsletter-TheNeuron-1.png?t=1791988431)
Follow image link: (https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=2700&url_id=222)
Caption: 

Want absolutely EVERYTHING that happened in AI today? [Read the full digest here](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-wednesday-october-21-2026/).

Reliable access to the whole web - 177M+ IPs across 195 locations and 99.9% uptime – reliable retrieval on the most demanding targets, from JS-heavy pages to complex sites.

[Start for free, get $5 towards your next project](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=2700&url_id=222)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/dd774365-422a-4738-94f5-b9ebb2928a1e/image.png?t=1792566866)
Follow image link: (https://x.com/kimmonismus/status/2112548663327158783)
Caption: Anthropic’s Claude spent 64 hours mostly on its own designing roughly 318,000 tiny proteins meant to stick to scorpion venom toxins. Outside labs tested 211, and 17 stuck to their targets. In the chart, one lost 94% of its grip when a known venom-fighting antibody got there first, a hint it latches onto the same spot. It’s not an antivenom yet.

1. OpenAI [acquired Orchestra Bio](https://openai.com/index/openai-to-acquire-orchestra-bio/), whose agents flag how a delay in one part of a drug program ripples through the rest, and will fold it into its Rosalind life-science tools.

2. Anthropic [confirmed a draft AI safety bill](https://techcrunch.com/2026/10/20/anthropic-pitches-ai-safety-bill-that-may-block-a-model-if-50-people-could-be-killed/) that would let Commerce ask a judge to block a model release posing imminent risk of 50+ deaths or $1B in damage.

3. Spotify [removed 50M+ slop and spam tracks](https://newsroom.spotify.com/2026-10-20/prioritizing-human-artistry/) from recommendations this year and now keeps badge-labeled AI-persona artists out of them by default.

4. Zoom [announced deepfake risk detection](https://news.zoom.com/zoomtopia-2026-security/) that analyzes live video and audio for signs of alteration and shows a confidence indicator, due in December.

5. Otter.ai [secured $320M](https://techcrunch.com/2026/10/20/otter-ai-raises-320-million-from-general-catalysts-growth-fund-for-its-meeting-tool/) from General Catalyst's Customer Value Fund, a financing tied to returns on its marketing spend instead of selling shares.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). ___[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=october-21-wednesday-b)___!_

1. *Put your data to work with AI. Explore strategies for building AI-ready, governed data across hybrid environments. [Learn more.](https://www.eweek.com/hubs/bring-ai-to-your-data/)

2. [ChatGPT Locked Chats](https://help.openai.com/en/articles/20001411-using-locked-chats-in-chatgpt) hides sensitive conversations behind a PIN or Face ID and keeps their memory separate from your regular chats (rolling out now).

3. [Gemini Personal Intelligence](https://blog.google/products-and-platforms/platforms/android/android-auto-cars-with-google-built-in-gemini-personal-intelligence/) now works in Android Auto, so you can ask it to check a flight from your email or navigate to a place from a photo (opt-in, rolling out now).

4. [Jotform App Builder](https://www.producthunt.com/products/jotform) builds and edits lightweight apps right inside ChatGPT and Claude, so a workflow idea becomes something clickable without leaving the chat.

5. ElevenLabs' [Eleven Realtime](https://elevenlabs.io/docs/eleven-agents/customization/realtime-models) models power voice agents that hear and answer in speech directly, with the Max version replying in 0.57 seconds by the company's count.

6. [Mintlify Autopilot](https://www.producthunt.com/products/mintlify) watches your product changes and updates your developer docs automatically, so they stop falling behind the code.

7. [Skillsync](https://skillsync.com/) searches your past Claude Code, Codex, Cursor, and OpenCode sessions on your own machine and feeds relevant old decisions and fixes into each new prompt.

8. [Harness²](https://www.producthunt.com/products/harness-104) is an open-source Google Research framework that lets agents refine their own prompts, tools, and memory over time without answer keys to check against.

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

# 🧠 Midweek Wisdom

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/91f1ad51-e423-4588-88e8-61f9bb287ec5/image.png?t=1792565029)
Follow image link: (https://www.nylas.com/blog/the-state-of-agentic-ai-h2-2026/#:~:text=In%20the%20past%2090%20days%2C%20what%20did%20an%20agent%20do%20wrong%20at%20your%20organization%3F%20Multi%2Dselect%2C%20n%3D1%2C028%3B%204%25%20not%20sure.)
Caption: From Nylas’s agent survey: mistakes rose with the number of agents deployed, and only 53% of respondents could produce a full log of what their agents did. Self-reported data from a tech-heavy sample, so treat it as a signal, not proof.

* Allen Warner of agent-software company Nylas [reports a survey](https://www.nylas.com/blog/the-state-of-agentic-ai-h2-2026/) where 54% of 1,030 respondents saw an AI agent make a mistake in 90 days, rising to 70% at organizations running 21+ agents.

* Melchior Tamisier-Fayard, Theodoros Evgeniou, and Anne-Laure Fayard [describe a hackathon](https://knowledge.insead.edu/technology-innovation/how-use-ai-without-eroding-critical-thinking) where AI that challenged ideas, instead of polishing them, led teams to more varied concepts (INSEAD Knowledge).

* EisnerAmper's Jen Clark [recommends sorting agents](https://www.eisneramper.com/insights/artificial-intelligence-insights/ai-agents-at-work-governance-1026/) by who triggers the work and who chooses the steps, then setting limits on what each can read, say, spend, and change.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5bad3347-cf0a-4c9b-9868-45bcf260caff/TN_Thumbnail_101326_AnastasisGermanidis_Runway_B.png?t=1791882337)
Caption: 

New episodes air **every week** on Wednesdays: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ff533544-6be3-43f7-937d-1a465b29bf0a/A_Cat_s_Commentary_x_2025_-_2026-09-23T133229.922.png?t=1790195911)
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
https://www.theneurondaily.com/p/meta-s-muse-made-shared-chats-searchable
