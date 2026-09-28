---
source: gmail
newsletter: "the-neuron"
message_id: "1a0cdd2e2fd332f9"
thread_id: "1a0cdd2e2fd332f9"
subject: "😺 New GPT-6 and Claude models start a price war"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Wed, 23 Sep 2026 10:32:21 +0000 (UTC)"
ingested: 2026-09-28
sha256: 339bdc8cc6494090527465aa0a6e3cb8fffcdb74dbf1aaa93b0011f84b81b558
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3687a687-eaa3-4b70-b63b-859d28a97230/ChatGPT_Image_Sep_23__2026__12_25_16_AM.png?t=1790148534)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/863bb993-56df-4f2d-af01-20ccc5eca3ff/In_partnership_with_Vanta.png?t=1790001410)
Follow image link: (https://www.vanta.com/webinars/youve-adopted-ai-now-what-about-governance?utm_campaign=fy27q3_webinar_ai_governance_global&utm_source=the-neuron&utm_medium=newsletter&utm_content=register)
Caption: 

**Welcome, humans.**

So apparently the next great AI benchmark is whether it can win an argument with an airline. After a seven-hour Delta delay, [one Muse user said](https://x.com/cryptopunk7213/status/2102179999122153690) the agent got a $250 credit and rebooked the flight in about five minutes.

That is a tiny example of a much bigger agent shift: companies have spent years benefiting when people give up because a refund, cancellation, or support request is annoying. [Citrini's read](https://x.com/citrini/status/2102221710204264543) is that agents turn that friction into a direct cost center, because the software does not get bored, embarrassed, or tired of hold music. _The robots have discovered customer service escalation, and they are happy to assist you (to deal with it)_

**Here’s what happened in AI today:**

* 😼 OpenAI and Anthropic turned frontier AI into a price war.

* 📰 Alibaba paired a new AI chip with a 20GW buildout.

* 📰 Cisco found malware using public AI models autonomously.

* 🍪 Xiaomi released open-weight MiMo-V2.6-Pro.

* 🎓 Route AI work by job, not one favorite model.

... [and a whole lot more that you can read about here](https://theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-september-22-2026/).

Advertise to 700K readers of The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😼 GPT-6 Sol, Luna, and Opus 5.5 turned frontier AI into a price war

**DEEP DIVE: **[GPT-6 Sol vs. Luna vs. Claude Opus 5.5: Which Should You Use?](https://theneuron.ai/guides/gpt-6-sol-vs-luna-vs-claude-opus-5-5-which-should-you-use/)

OpenAI and Anthropic both shipped new workhorse models Tuesday, but the most useful number was not a benchmark. _It was the bill._

**First up, Opus: **Anthropic launched [Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) at $4 per million input tokens and $20 per million output tokens. Anthropic says typical workloads cost about 40% less than Opus 5 because the model uses fewer tokens and cheaper cache reads.

**Roughly 90 minutes later…** [OpenAI launched GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/). Sol costs $2/$10 per million input/output tokens (half the cost of Opus), and Luna costs $0.10/$0.50, which puts it at 1% of Astra's raw token price. 

**Here's what else: **

* Opus 5.5 pushed Anthropic's frontier work down the cost curve while keeping its strongest coding and agent benchmarks competitive.

* The new Sol halved the raw token price of Opus 5.5, while Luna pushed dramatically lower for high-volume work.

* In our first live test (_see deep dive above)_, Sol reached a playable result substantially faster than Opus 5.5.

Our midday livestream wasn't by any means _scientific_, but it did expose the trade-off launch charts hide: higher reasoning can buy quality, but it also takes more time.

The practical metric is **cost per successful task**: model spend, elapsed time, retries, and human rescues required to get a usable result. [OpenAI leaned into that framing](https://x.com/OpenAI/status/2102460984782938221): Sol scored 33.2% on AutomationBench at $0.27 per task, while OpenAI says higher-effort Luna matched GPT-5.6 Sol factuality at about one-hundredth the cost.

And yet, we keep coming back to one rule: test the models on your actual workflow.

Outside tests show why the answer still depends on the workload. [Nate Herk preferred Opus on seven of eight usable jobs](https://www.youtube.com/watch?v=eF3yeJuifoQ), but Opus took about 8h40 and $213 versus Sol's 5h51 and roughly $74. [Browser Use saw the reverse](https://x.com/browser_use/status/2102558423506469010) on its browser-agent benchmark: Sol medium scored 66.9 versus Opus 5.5's 59.4, again while costing about 3.5x less.

**The demos are where this gets fun:**

* [Our GPT-6 Sol Cat Doom](https://www.youtube.com/live/X0ERFFbjEug?si=DN6AqNjlFqrhJ3fr&t=2916) became a playable three-level game in about 10.5 minutes; Opus was still working around 20 minutes in.

* [Alex Albert rebuilt 1906 Market Street](https://x.com/alexalbert__/status/2102466523164274839) with Opus from historical maps, photos, film, and reusable Blender-Python generators.

* [Ethan Mollick built Orbital Declaration](https://orbital-declaration.netlify.app/), a hard-sci-fi browser game with Newtonian motion, gravity, heat, the rocket equation, eight chapters, and 11 Jupiter locations.

**Our take:** Don't marry one model. Let the strongest model plan and review, then use cheaper workhorses or subagents for the hours in between. Compare completed work, time, total spend, and human rescues required for each.

Now, because scheduling snafus cut our test short, _we want a rematch._ We’re running the full six-prompt Sol vs. Opus 5.5 showdown Thursday, [so click “Notify Me” on YouTube and bring your hardest prompts.](https://youtube.com/live/RVn6pGLs64w?feature=share)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# You've adopted AI. Now what about governance?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/23789f34-cea7-4e50-8248-b081f8387c7e/2_Spakers_Template__1_.png?t=1790001563)
Follow image link: (https://www.vanta.com/webinars/youve-adopted-ai-now-what-about-governance?utm_campaign=fy27q3_webinar_ai_governance_global&utm_source=the-neuron&utm_medium=newsletter&utm_content=register)
Caption: 

AI adoption is outpacing regulation and governance. Security and risk leaders must enable AI while facing a harder question: how much risk are you taking on?

Jane Frankland, cybersecurity leader, joins Vanta's GRC experts on scaling AI governance.

Learn how to:

* Build AI governance into your security program

* Assess AI systems and agents based on your risk tolerance

* Understand and communicate risk credibly as adoption grows

* Prepare for the EU AI Act, ISO 42001, and NIST AI RMF

[Save your seat →](https://www.vanta.com/webinars/youve-adopted-ai-now-what-about-governance?utm_campaign=fy27q3_webinar_ai_governance_global&utm_source=the-neuron&utm_medium=newsletter&utm_content=register)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Build a two-tier model stack

Do not make your most expensive model do every part of an agent job. Split the work by decision quality.

1. Use your strongest model to write the technical plan, architecture, and acceptance criteria.

2. Hand well-scoped implementation tasks to a cheaper model, and parallelize where the tasks are independent.

3. Bring the result back to the stronger model for code review, security review, or final synthesis.

**Copy/paste:**

```
Plan this task in phases. Prioritize quality, but do not be wasteful. Identify which steps need frontier-level judgment and which can be delegated to cheaper subagents. Write clear acceptance criteria for every delegated step, then review the combined result for correctness, security, and missed requirements.
```
**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

# 🎃 Hacktoberfest is Here: Put Your PRs into Kestra!

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/af4e94f3-0793-401b-9b58-2cf22fc0f0db/Hacktoberfest26.png?t=1790000960)
Follow image link: (https://fandf.co/4AhxfnX)
Caption: 

Merge a PR, and you get Kestra swag and goodies shipped to you. Fix a good-first-issue or build a real, reusable blueprint, and you're in the running for a MacBook, iPad, or $150 Amazon card. Submissions close Oct 31.

[Register Now](https://fandf.co/4AhxfnX)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

1. *Build an AI-Ready Workplace. Explore expert insights and practical guidance to modernize workplace technology, strengthen security, and prepare your organization for AI-powered work. [Explore the Hub](https://www.techrepublic.com/hubs/the-ai-ready-workplace-hub/)

2. [Xiaomi MiMo-V2.6](https://mimo.xiaomi.com/mimo-v2-6) gives you an MIT-licensed Pro model plus Flash variants for multimodal, coding, and multi-agent experiments.

3. [Tencent Hy Image3.5 Preview](https://x.com/TencentHunyuan/status/2102226552310419473) generates or edits images up to 2K from text prompts or reference images.

4. [OpenMuse](https://github.com/CopilotKit/OpenMuse) lets you self-host a Muse-style personal agent with a persistent browser, files, optional Linux workspace, Gmail, Calendar, and background tasks _(ask Codex in the ChatGPT desktop to set it up for you if you need it)_

5. [Kimi Browser Extension](https://www.kimi.ai/products/kimi-browser-extension) gives the Kimi AI model a Chrome/Edge sidebar that can navigate, click, fill forms, extract information, and record repetitive browser flows as reusable skills.

6. [OpenRouter](https://openrouter.ai/blog/announcements/batch-api/) launched a Batch API across 70+ models that typically cuts input and output token prices roughly in half for jobs that can wait.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/27cffbac-050e-4658-b2f3-7295692eccac/Screenshot_2026-09-22_at_2.26.53_PM.png?t=1790146239)
Follow image link: (https://x.com/AlexFinn/status/2102432674082345076)
Caption: This is wild

* [Meta’s Muse](https://www.theinformation.com/briefings/exclusive-metas-muse-surpassed-500-000-users-first-week?rc=lks9on) passed 500K users and 250K daily actives about a week after launch, while [xAI’s Grok Bot](https://www.bloomberg.com/news/articles/2026-09-22/spacexai-s-grok-bot-agent-tops-400-000-users-after-first-month) reached roughly 418K weekly users after its first month.

* [Stripe](https://stripe.dev/blog/how-stripe-is-designing-checkout-for-ai-agents) added WebMCP checkout tools across 7.8M businesses; internal tests used 42% fewer tokens, 38% fewer tool calls, and finished checkout 39% faster than DOM automation.

* [Rabbit](https://www.wired.com/story/rabbit-r1-os3-jesse-lyu/) launched OS3, a BYOK agent (_bring your own keys, the way you use AI outside of chat apps)_ that works through browsers, Telegram, or iMessage across up to five Windows, Mac, or Linux machines, with no Rabbit subscription.

* [Anthropic and OpenEvidence](https://www.reuters.com/legal/litigation/anthropic-openevidence-partner-bring-medical-ai-worldwide-2026-09-22/) partnered to roll out a free clinical-decision tool to physicians in roughly 100 countries after OpenEvidence logged 42M U.S. clinician queries in August.

* [Global AI-glasses shipments](https://counterpointresearch.com/en/insights/global-ai-glasses-shipments-surge-263-percent-yoy-with-display-less-ai-glasses) jumped 263% year over year in H1 2026, with Meta accounting for 94% of display-less units, according to Counterpoint Research.

* [Ukraine’s Third Army Corps](https://www.businessinsider.com/drones-drop-robots-russian-lines-ukraine-retake-territory-2026-9) said heavy bomber drones air-dropped ground robots more than 10 km behind Russian lines during Operation Vivaldi, which it says helped retake 125 km².

[Want absolutely EVERYTHING that happened in AI this week? Click here!](https://theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-september-22-2026/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 📖 Midweek Wisdom

* Ben Thompson argues that [Amazon blocking Muse](https://stratechery.com/2026/amazon-blocks-muse-amazons-moat-aggregator-v-aggregator/) does not erase Amazon's moat: agents may own the interface, but fulfillment, logistics, and the physical world are still hard to swap out.

* A new [100-agent economy study](https://arcxiv.org/abs/2609.11108) found agents could transact, yet wages and prices barely adjusted to shocks. The warning: tool competence does not automatically create good coordination.

* Economists Felix Feng, Brett Green, Curtis Taylor, and Mark Westerfield argue that as AI makes [solutions abundant](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7479738), the scarcer skill may become finding valuable problems in the first place. In other words: better answers raise the value of better questions.

* FutureHouse CEO Sam Rodriques argues that [AI will change science fastest where answers are cheap to verify](https://x.com/SGRodriques/status/2102550817215779089): pick fast-checkable problems, make verification cheaper, or collect the missing data.

* Harrison Satcher argues ["we don't have the nouns yet"](https://economicsofai.substack.com/p/we-dont-have-the-nouns-yet): labor forecasts miss jobs that do not exist as categories yet, just as "cybersecurity" barely existed decades ago.

* **Very sad news update: **[Bloomberg reported](https://www.bloomberg.com/graphics/2026-iran-school-attack/) that Pentagon investigators found flawed intelligence, outdated imagery, and overreliance on Palantir’s Maven AI contributed to a U.S. strike on an Iranian school that killed 123 children.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained: Our LIVE breakdown of GPT 6 Sol vs Claude Opus 5.5

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/49289112-f847-439f-a9bc-1101c53681dc/ChatGPT_Image_Sep_22__2026__11_24_35_AM.png?t=1790144691)
Follow image link: (https://youtube.com/live/X0ERFFbjEug)
Caption: Click the image above to watch directly on YouTube

Check out our initial impressions, takes on which reasoning effort to use on which task per each model, where each model seems to outperform the other, and general model launch day tomfoolery as we benchmark the models on CATDOOM. 

Then, join us for Round 2 on Thursday — [save your spot and click “Notify Me” on YouTube to get reminded when we go live here! ](https://youtube.com/live/RVn6pGLs64w)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0dcc405d-5e43-4f04-bff0-1d9e0d09ea83/A_Cat_s_Commentary_x_2025__99_.png?t=1789440672)
Caption: Grazie

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today!




**Btw: **We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/gpt-6-sol-vs-claude-opus-5-5
