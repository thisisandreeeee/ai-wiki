---
source: gmail
newsletter: "the-neuron"
message_id: "1a1bfa567015bf07"
thread_id: "1a1bfa567015bf07"
subject: "😺 Would you trust AI math?"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Mon, 09 Nov 2026 09:30:48 +0000 (UTC)"
ingested: 2026-11-16
sha256: 1ca13fe5c0fd8df71eaee477346fb185a4eee240eaab2057f4d0c71462a3e312
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4befa56d-a6ae-497b-9765-01f9f359b5c6/AI_Solves_the_Quantum_Puzzle.png?t=1794203135)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5be0839c-e38c-47bb-9aab-707b2cf69aff/In_partnership_with_terrakata__1_.png?t=1793225898)
Follow image link: (https://terrakata.io/contact)
Caption: 

Welcome, humans.

So apparently Anthropic went shopping for electricity and came home with someone else's backorder. The Financial Times reported on Sunday, [per CNBC](https://www.cnbc.com/2026/11/08/anthropic-generator-deal-ai-data-centers.html), that Anthropic agreed to pay about $3.4B for 1.7 gigawatts of gas-fired generators. A gigawatt powers roughly 800,000 homes, so that's around 1.4M homes' worth of electricity.

The twist is that the supplier, OnePWR, had ordered the generators from Caterpillar two years ago and needed cash to finish paying for them. Big generators now come with multi-year waits, so Anthropic took over the orders to skip the line. _It's like dodging a two-year restaurant waitlist by buying out someone else's reservation, except the restaurant is Caterpillar and the entrée is 1.7 gigawatts._

One caveat. This comes from a single unnamed person, Reuters couldn't verify it, and neither company has commented.

Corey's going [LIVE TODAY at 11am CT/9am PT](https://youtube.com/live/TBcS30iNSQw?feature=share) to sort through the latest AI news and rumors, from potential new OpenAI and Anthropic models to the Anthropic IPO valuation roller coaster and what the midterms mean for AI. **Join The Neuron LIVE** for a look at what's real, what's speculation, and what could happen next!

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1ce63765-c079-463d-928c-84dd4d3372fe/The_Neuron_AI_Week_Ahead_1920x1080.jpg?t=1793983354)
Follow image link: (https://youtube.com/live/TBcS30iNSQw?feature=share)
Caption: 

**Here’s what happened in AI today:**

* 😺 A startup says an Anthropic model proved a quantum conjecture.

* 📰 Nvidia's board opened an investigation into CEO Jensen Huang.

* 📰 The U.S. AI safety center began informally reporting to the White House.

* 🍪 Perplexity launched Teammates agents for Max subscribers.

* 🎓 Make your AI try to break its own work.

... and a [**whole lot more that you can read about here.**](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-monday-november-9-2026/)

Advertise to 700K readers of The Neuron here! (https://www.theneuron.ai/get-media-kit/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😺 A Startup Says an Unreleased Anthropic Model Cracked an 18-Year-Old Quantum Computing Puzzle

Okay, so a startup called [Physical Superintelligence (PSI)](https://psi.inc/research/aaronson-ambainis/) says its AI just solved a math puzzle that experts have been stuck on since 2008. The AI is an unreleased Anthropic model that the public can't use yet. PSI says it had a full proof by day three of its run.

The puzzle has a scary name (the Aaronson-Ambainis conjecture), but the question underneath is simple. Quantum computers are supposed to be wildly faster than regular ones. Faster at _what_, exactly? Nobody has fully nailed that down.

Here's the idea. Picture a giant wall of hidden light switches, and a machine that has to answer a question about the pattern. It can't see the whole wall. It can peek at one switch at a time, and every peek costs something. The rule everyone suspected was true says that if the answer really depends on the switches, then at least one switch matters a lot. Not a thousand switches that each matter a tiny bit.

Why does that help a regular computer? Because it can hunt down that one big switch first, like playing 20 Questions and always asking the question that rules out the most possibilities. Do that a few times and you've copied what the quantum computer would have said.

So the proof says that on messy, patternless problems, a regular computer can keep up with a quantum one without a crazy amount of extra peeking. The extra work grows like squaring a number, not like doubling it over and over. _Quantum computers are not secretly better at everything, which is awkward for the sales deck._

How it was found is the other half of the story. PSI built a research system that runs copies of the Anthropic model. A human, David Turturean, set up the system, picked the problem, ran it, and prompted the model to write up the paper. He's also the one responsible if it's wrong. After the day-three proof, the system improved the result twice.

So how do you trust a proof from a machine? AI math claims have gotten messy lately. After OpenAI released more than 300 math results, [mathematicians including Terence Tao pushed back](https://officechai.com/ai/us-startup-physical-superintelligence-proves-aaronson-ambainis-conjecture-a-key-open-problem-in-quantum-computing/) on who deserves credit and how new the results really were.

PSI's answer is a tool called Lean. Think of it as spellcheck for logic. You write the proof in a strict format, and Lean either confirms every step follows or rejects it. It doesn't care whether a human or an AI wrote the proof. _Which means a confident-sounding AI can't charm its way past it._ Lean has been having a moment, too. On Friday we flagged [Axiom's giant Lean version](https://axiommath.ai/research/the-stacks-project-formalized/) of a 7,500-page math reference built mostly by AI agents.

One catch is that Lean only checks that the proof matches the statement someone typed in. So PSI also wrote the puzzle itself in Lean and published the code, so people can check the wording.

Experts are weighing in. Four Stanford researchers who solved a smaller version in August read the full proof, sent comments, and called it a major result. But the paper thanks them, so that's feedback from inside the circle, not a verdict from the whole field. We couldn't find comments from Scott Aaronson or Andris Ambainis, the two namesakes.

Here's what [The Quantum Insider](https://thequantuminsider.com/2026/11/06/ai-assisted-proof-settles-longstanding-question-about-quantum-speedups/) says the result does _not_ show:

* It counts peeks at the data, not total computing time, so a regular computer could still take ages.

* It works for most inputs, not every single one.

* "A bit more work" can still be a huge number, so this isn't a practical shortcut.

* It doesn't prove regular computers can copy all of quantum computing.

**Why this matters.** Two things. First, it's a reality check on quantum hype. If you work in finance, security, or anywhere people pitch you quantum timelines, this sharpens the question to ask. Does the problem have hidden structure to exploit, or is it just messy data? Nothing here changes how Shor's algorithm (the one that threatens today's encryption) works, because that one relies on structure. Second, it's an early example of AI producing a new, checkable result in real math, with Lean as the receipt. Expect more of these, and expect the same fights over credit.

Next up, watch the shorter Stanford write-up, where specialists will stress-test the proof, and whether PSI's system can pull this off again on a problem nobody pointed it at. One proof is a result. A second, on something unrelated, starts to look like a pattern.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# **Bring us the bottleneck.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2cb532b0-f796-4d3a-8be6-4d3f89a766dc/terrakata-abstract-workflow-ad-v4-slate-blue.png?t=1793225645)
Follow image link: (https://terrakata.io/contact)
Caption: 

Still moving data between spreadsheets, emails, and business systems? TerraKata builds custom AI tools around your workflow, connecting data, automating repetitive work, and deploying on your infrastructure. Tell us what’s slowing your team down.

Let’s build the fix (https://terrakata.io/contact)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Make your AI try to fail its own work before you see it

A new research benchmark called [Co-Design Bench](https://arxiv.org/abs/2610.35138) tested coding agents on 273 real app-editing tasks, and the scores show something every AI user has felt. Experts wrote 2,331 hidden acceptance criteria for those tasks, which the models never saw. The best of ten models met 69.9% of the criteria on an average task. But it fully completed only 26.4% of tasks.

That gap is the whole lesson. A task only counts as done when every criterion passes, so one quietly missed requirement sinks an otherwise polished result. _"Mostly done" is a polite way of saying "not done."_

Notice how the researchers graded, too. A judge checked each criterion against evidence, then a separate verifier challenged every pass. That's the part you can copy. The paper measured the gap and used that grading style, but it didn't test whether checklists close the gap, so the workflow below is our adaptation. Our hunch is that an AI is much tougher on a draft when its only job is to break it.

1. Get the checklist first. Paste this, then edit the list yourself, because it can't check a requirement nobody stated.

```
Before doing this task, turn my request into a numbered checklist of acceptance criteria. Each item must be something I could mark pass or fail, with no vague words like "good" or "engaging." Show me the checklist and wait for my OK.

Task: [paste your request]
```
2. Say "go," let it do the work, then open a fresh chat and make that chat the skeptic.

```
Below are a task, its acceptance checklist, and the finished work. Your job is to prove the work wrong. For each checklist item, look for evidence that it fails and point to the exact part of the work that shows it. Mark each item FAIL, PASS, or UNCERTAIN. Only mark PASS if you tried to break it and couldn't.

[paste task, checklist, and work]
```
3. Send only the FAIL and UNCERTAIN items back to the first chat to fix, then run the skeptic again on the new version.

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

### Steal Attio’s GTM setup.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b20994ca-d546-4833-b420-e1420364e575/steal-gtm-setup-nov-1200x600.png?t=1793810575)
Follow image link: (https://attio.com/blog/the-system-that-runs-our-gtm?utm_source=beehiiv&utm_medium=newsletter-sponsorship&utm_campaign=beehiiv-Y26&utm_content=YJ4ZPRQDHV&_bhiiv=opp_d6571391-7f5f-4916-8c7d-d4fea7800255_2d7a5811&bhcl_id=8e0291ca-945d-46bf-93e7-c89af05cc6e5_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

For the first time, see the system that runs GTM at [Attio](https://attio.com/blog/the-system-that-runs-our-gtm?utm_source=beehiiv&utm_medium=newsletter-sponsorship&utm_campaign=beehiiv-Y26&utm_content=YJ4ZPRQDHV&_bhiiv=opp_d6571391-7f5f-4916-8c7d-d4fea7800255_2d7a5811&bhcl_id=8e0291ca-945d-46bf-93e7-c89af05cc6e5_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f), the #1 fastest-growing CRM on Brex and Ramp.

Attio’s Rev Ops and Solutions leads have written up all of it, including how it spots at-risk accounts early and surfaces upsell opportunities while they’re still warm.

[Read the playbook.](https://attio.com/blog/the-system-that-runs-our-gtm?utm_source=beehiiv&utm_medium=newsletter-sponsorship&utm_campaign=beehiiv-Y26&utm_content=YJ4ZPRQDHV&_bhiiv=opp_d6571391-7f5f-4916-8c7d-d4fea7800255_2d7a5811&bhcl_id=8e0291ca-945d-46bf-93e7-c89af05cc6e5_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6a71c7aa-33df-4e15-98e8-368d9fcb131f/image.png?t=1794204261)
Follow image link: (https://x.com/dummerspast39/status/2119483953354842554)
Caption: A rumor account says OpenAI’s GPT-6.2 Sol launches next Thursday, and an Artificial Analysis screenshot shows it tying Gemini 4 Carbon for first at 60, one point ahead of Opus 5.5, at $1.19 per task versus $10.04. OpenAI hasn’t confirmed any of it, so treat it as just a rumor.

* [Adobe said](https://www.theneuron.ai/news/adobe-says-the-next-ai-skill-isnt-better-prompting-its-creative-direction/) creative direction, not better prompting, will be the key AI skill as agents take on more production work, ahead of its Adobe MAX conference starting Tuesday.

* [Nvidia's board](https://www.axios.com/2026/11/08/nvidia-ceo-jensen-huang-admits-affair-board-to-launch-investigation) opened an independent investigation after CEO Jensen Huang admitted a relationship with a suspected Chinese spy, saying it has no reason to believe company secrets were compromised.

* The U.S. government's AI safety testing center began informally reporting to a White House office, [AP reported](https://apnews.com/article/ai-safety-trump-white-house-d3318eb2cf011df53e9ddb3e03d25f13), and it still has no permanent leader.

* [SemiAnalysis reported](https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner) that the first 120MW phase of China's planned 800MW Galaxy AI campus in Inner Mongolia was delivered in August at about a fifth of comparable U.S. cost.

* U.S. employers [added 70,000 professional and business services jobs](https://www.marketplace.org/story/2026/11/06/latest-jobs-report-shows-a-whitecollar-hiring-turnaround) in October, a surprise gain that some economists said suggests AI isn't wiping out white-collar work.

* AI super PACs spent about $79M across 68 races this cycle, and OpenAI-linked Leading the Future ended with just over $20M of its roughly $100M, [TheNextWeb reported](https://thenextweb.com/news/ai-super-pacs-midterms-results-leading-the-future).

Want absolutely EVERYTHING that happened in AI this week? [**Click here!**](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-monday-november-9-2026/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). _[_Advertise to 700K+ readers here_](https://info.technologyadvice.com/advertise-with-the-neuron)_!_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c217f8a7-ffc9-4564-b633-02e7d57a8394/chatgpt-ads-banner-1920x960.png?t=1793631987)
Follow image link: (https://www.triplewhale.com/reports-guides/chatgpt-ads?utm_source=neuron&utm_medium=paid-media&utm_campaign=mkt-chatgptadsguide-paidmedia-1126&utm_content=newsletter_tertiary-11092026)
Caption: 

1. *Struggling to get your ChatGPT Ads campaigns off the ground? Get early data and setup tips from this free guide. [Get the free guide](https://www.triplewhale.com/reports-guides/chatgpt-ads?utm_source=neuron&utm_medium=paid-media&utm_campaign=mkt-chatgptadsguide-paidmedia-1126&utm_content=newsletter_tertiary-11092026)

2. [Perplexity Teammates](https://www.theverge.com/ai-artificial-intelligence/1028302/perplexity-teammates-ai-agents-work) gives Max subscribers on the web agents that own an ongoing job like research or bug triage and ping you in Slack when they need a call.

3. [Inkling 2 Small](https://the-decoder.com/thinking-machines-inkling-2-small-claims-top-spot-among-western-open-weight-models/) is Thinking Machines' new text-and-image model with an adjustable reasoning dial, on its Tinker platform now, with open Apache 2.0 weights promised after safety testing.

4. [seam](https://www.producthunt.com/products/seam-2) turns your MacBook's notch into a control strip for on-device voice dictation, music, a focus timer, and alerts when Claude Code finishes.

5. [Quest](https://www.new.quest/) builds an editable memory of your goals and preferences, then talks you through decisions instead of just finishing tasks.

6. [Tobira Site Agent](https://tobira.ai/agentic-site/) puts an agent on your website that answers visitors, qualifies leads, and lets visitors' own AI agents request demos, trials, or orders.

7. [Arete-27B](https://nousresearch.com/arete) is Nous Research's retuned version of Alibaba's Qwen3.8-27B that cut answers with Chinese state framing from 22% to 1% on Nous's own test, with the weights, data, and test published.

8. [HyperFlow H3 Flash](https://github.com/Video-Rebirth/hyperflow-h3-flash) shrinks Video Rebirth's video-and-audio generator from 31B to 13.7B parameters, so it makes clips with sound in just four to eight generation steps.

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

# 😹 Monday Meme

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/52ddf39e-c283-4eaf-8308-6d8f3d40d8c0/image.png?t=1794209519)
Follow image link: (https://x.com/sesanaallen/status/2114547134016241905)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0820d5ae-9854-4066-8517-059e00d7ea16/ChatGPT_Image_Aug_7__2026__05_43_59_PM.png?t=1786149887)
Caption: 

New episodes air **every week** on Wednesdays: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/394af99d-dd05-4601-b42e-5b00580cdeee/1.png?t=1794209603)
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
https://www.theneurondaily.com/p/anthropic-s-ai-cracks-a-puzzle
