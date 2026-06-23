---
source: gmail
newsletter: "the-neuron"
message_id: "19e736cc103f284d"
thread_id: "19e736cc103f284d"
subject: "😺 What changed inside Claude Opus 4.8"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Fri, 29 May 2026 11:08:40 +0000 (UTC)"
ingested: 2026-06-23
sha256: 397096077bae1264510eb713137312153bf2909d05229da8fa8e3c2e24380bb3
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cdf47374-e05f-4fe3-bd43-8a997288483a/Gemini_Generated_Image_i3wa38i3wa38i3wa.png?t=1780030735)
Caption: 

Welcome, humans. 

**Real quick before the news:** we’re trying to get The Neuron’s YouTube channel across 20K subscribers this weekend.

This is our most advanced growth strategy yet: asking nicely for you to click the big Subscribe button below, and hoping you will do us the very sincere honor of _smashing it like the buzzer on Family Feud. _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a24710a5-002e-463c-b79d-f5754a0e8e59/Gemini_Generated_Image_c6yadmc6yadmc6ya.png?t=1764928014)
Follow image link: (https://www.youtube.com/@theneuronai?sub_confirmation=1)
Caption: Click the image to subscribe! 

If we **hit 20K this weekend,** we solemnly swear we will answer at least _one request_ in the feedback poll at the end of this email. So, scroll down, select your rating of this email (hit of catnip, it sucked, whatever), and then type into the “Additional Feedback” box that pops up after you click and ask us for something nice :)

**Here’s what happened in AI today: **

* 😼 Anthropic released Claude Opus 4.8 with effort controls.

* 📰 IBM committed $10B to fault-tolerant quantum computers.

* 📰 Waymo opened rides in its new Ojai robotaxi.

* 🍪 Pika gave Claude a founder launch kit.

* 🎓 Claude Code workflows turn one prompt into agent teams.

…And a [whole lot more you can read about here](https://theneuron.ai/explainer-articles/everything-that-happened-in-ai-today-thursday-may-28-2026/).

**Hey: **_Want to reach 700,000+ AI-hungry readers? _[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)[_ _](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😼** ****Anthropic released Claude Opus 4.8, and the tradeoff is already showing.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/82655786-cb46-4504-97c7-e1f142ac7011/image.png?t=1780030569)
Follow image link: (https://x.com/ErRahul337/status/2060044973358346699)
Caption: 

Every new frontier model now has to answer two questions, which is really actually just one question: _is it smarter, and can you trust it with more work?_

Anthropic’s answer is[ Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8), its newest flagship model for coding, agents, and long work sessions. The headline is this: better judgment, more control, and fewer “I totally fixed it” moments when the model did not, in fact, _totally fix it._

**Here's what happened:**

* Anthropic released Opus 4.8 at the same standard price as Opus 4.7 _($5 per 1M input tokens, $25 per 1M output, so _[~$4.10  per 1M blended](https://artificialanalysis.ai/models/claude-opus-4-8/providers)_). _

* Claude now has effort controls, so you can choose faster answers or deeper thinking.

* Claude Code added[ dynamic workflows](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code), which can split big coding jobs across many subagents (_more on this below)_. 

* Anthropic also announced a[ $65B Series H](https://www.anthropic.com/news/series-h) at a $965B post-money valuation, and claimed it would release Mythos-class models_ in the coming weeks. _

**So what was the vibe on X? **

* The praise camp showed up fast:[ ProximalHQ](https://x.com/ProximalHQ/status/2060066037350166640) said Opus 4.8 topped FrontierSWE,[ scaling01](https://x.com/scaling01/status/2060043010943942989) said Anthropic “cured laziness,” and[ Box](https://blog.box.com/anthropics-opus-48-advances-enterprise-content-use-cases) saw stronger enterprise content results. 

* [Dan Shipper](https://every.to/vibe-check/opus-4-8-vibecheck) said Anthropic “should’ve rounded up to 5” because Opus 4.8 topped Every’s Senior Engineer benchmark and writing tests _(Every also published a longer_[ Opus 4.8 Vibe Check](https://every.to/vibe-check/opus-4-8-vibecheck)_ on the model’s writing and reasoning feel)._

* [Ethan Mollick](https://x.com/emollick/status/2060098885561778341) used Opus 4.8 in Claude Code to turn hundreds of research files into a working academic paper, then used GPT-5.5 Pro as a reviewer. That is the bull case: Opus 4.8 is better when the task looks like real work.

* As for the skeptics:[ Andon Labs](https://x.com/andonlabs/status/2060047215134228746) said Opus 4.8 performed worse than Opus 4.7 and GPT-5.5 on Vending-Bench and Blueprint-Bench, while[ Cline](https://x.com/cline/status/2060063889874972905) said it trailed GPT-5.5 on Terminal-Bench 2.1.

**Let’s talk about that **[**Andon Labs take**](https://andonlabs.com/blog/opus-4-8-vending-bench)** for a sec. **They run Vending-Bench, a benchmark where AI models act like the operator of a tiny vending-machine business. The model has to make business decisions, manage suppliers, and respond to messy incentives, which makes it a useful test for agent behavior (how an AI acts over many steps). 

Even though it performed worst on some Vending-Bench, it also looked more aligned: it avoided the deceptive and power-seeking behavior older Claude models showed _(though it still sometimes joined price cartels and refused unethical moves because it seemed worried about consequences vs morals)_. 

**Pro tips: **Opus 4.8 does better at “High” effort than “Max,” possibly because Max burns more reasoning tokens, hits the context limit sooner, and starts forgetting important details.[ mweinbach](https://x.com/mweinbach/status/2060055143886766532) also warned that ultracode workflows can chew through a Claude Code usage window quickly because they spin up dozens of subagents.

**How to try it:**

1. Open Claude and Pick “Claude Opus 4.8” from the model selector.

2. Use the effort control to choose how much Claude should “think.”

3. In Claude Code, use the word “workflow” for big jobs like audits, migrations, or research checks.

**Why this matters: **Anthropic is trying to make Claude more capable without making it more reckless. That matters because the next wave of AI work is bigger than chat. These models are getting handed full repos, multi-tool workflows, and even sometimes entire business decisions.

Dynamic workflows will help with this. Claude can now spin up a temporary agent team, divide the work, and check results before reporting back. That is useful if you need a codebase audit. It is also expensive if you accidentally ask it to inspect the entire company because you typed “workflow” too casually. _Prompter, beware… _

**Our take:**** **_TBH, there was a lot riding on this release, because Opus 4.7 was kind of a disappointment on release. Over time, I’ve come to terms with it, and I think they genuinely improved it, but it was a bit of a womp-womp at launch. Opus 4.8 seems like a woop woop? But my upcoming weekend coding session with it will reveal the reality…_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS ** 

### The IT strategy every team needs for 2026

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0f7e9fb9-d2e5-4fb4-9f28-bf633d912ad3/1200x600_2x.png?t=1771458224)
Follow image link: (https://www.deel.com/resources/it-strategy-toolkit-2026-guide-hr-leaders/?utm_medium=sponsored-newsletter&utm_source=beehiiv&utm_term=YJ4ZPRQDHV&utm_campaign=ww_engage_download_beehiiv_sponnewsletter_it-ttrends2026-feb26_it_all&utm_content=engage_it_sponnewsletter_ittrends2026-sponnews400-it_en&_bhiiv=opp_5524204f-c689-41f3-9da9-415e3162714c_28664f41&bhcl_id=6777f073-b120-4d61-ad2e-a5e1b3397662_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

2026 will redefine IT as a strategic driver of global growth. Automation, AI-driven support, unified platforms, and zero-trust security are becoming standard, especially for distributed teams. This [toolkit](https://www.deel.com/resources/it-strategy-toolkit-2026-guide-hr-leaders/?utm_medium=sponsored-newsletter&utm_source=beehiiv&utm_term=YJ4ZPRQDHV&utm_campaign=ww_engage_download_beehiiv_sponnewsletter_it-ttrends2026-feb26_it_all&utm_content=engage_it_sponnewsletter_ittrends2026-sponnews400-it_en&_bhiiv=opp_5524204f-c689-41f3-9da9-415e3162714c_28664f41&bhcl_id=6777f073-b120-4d61-ad2e-a5e1b3397662_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f) helps IT and HR leaders assess readiness, define goals, and build a scalable, audit-ready IT strategy for the year ahead. Learn what’s changing and how to prepare.

[Download the Toolkit](https://www.deel.com/resources/it-strategy-toolkit-2026-guide-hr-leaders/?utm_medium=sponsored-newsletter&utm_source=beehiiv&utm_term=YJ4ZPRQDHV&utm_campaign=ww_engage_download_beehiiv_sponnewsletter_it-ttrends2026-feb26_it_all&utm_content=engage_it_sponnewsletter_ittrends2026-sponnews400-it_en&_bhiiv=opp_5524204f-c689-41f3-9da9-415e3162714c_28664f41&bhcl_id=6777f073-b120-4d61-ad2e-a5e1b3397662_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 **AI Skill of the Day: Use Claude Code’s workflow mode for big messy tasks**

Some AI tasks fail because they’re hard. Others fail because they’re too big for one chat window to hold in its tiny little model brain.

That’s where Claude Code’s new[ dynamic workflows](https://code.claude.com/docs/en/workflows) come in. A workflow lets Claude write an orchestration script (a repeatable plan in code), then spin up subagents (smaller Claude workers) to tackle pieces of the job in parallel.

Use this for work where “check one thing” has secretly become “check 400 things.” Anthropic suggests codebase audits, large migrations, and research that needs cross-checking. Cat Wu shared a great example: cataloging hundreds of A/B test flags and finding stale ones set to 0% or 100%, in parallel, instead of one by one.

**How to use it:**

1. Start in Claude Code.

2. Use the word “workflow” in your prompt.

3. Keep the first run tightly scoped because this can burn tokens fast.

4. Ask Claude to verify findings before reporting them.

5. Save successful workflows with /workflows so your team can rerun them.

**Try this:**

```
Create a workflow to audit [specific folder, repo, docs set, or dataset] for [specific issue].

Before running it, show me:
1. The stages of the workflow
2. What each subagent will inspect
3. How findings will be verified
4. Any files or commands you plan to touch
5. The smallest safe first pass

Start with a scoped sample first. Do not make changes until I approve the full workflow plan.

```
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🍪 Treats to Try 

1. [Pika MCP](https://www.pika.me/mcp) gives Claude a founder launch kit so you can turn a rough product brief into branding, app screens, 15-second sizzle videos, and founder videos.

2. [Liquid AI](https://www.liquid.ai/blog/lfm2-5-8b-a1b) released LFM2.5-8B-A1B, a fast model that runs on consumer hardware for tool calling and long-context work.

3. [FLUX Virtual Try-On](https://flux-tools.bfl.ai/virtual-try-on) swaps garments onto a person image with realistic fit, fabric, folds, stitching, logos, and identity preservation in under four seconds.

4. [Parallel.ai](https://Parallel.ai) gives coding agents web search, content extraction, deep research, and enrichment tools by reading one setup prompt.

5. [OpenJarvis](https://github.com/open-jarvis/OpenJarvis) gives you a local-first personal assistant that runs on your own devices instead of living entirely in the cloud.

6. [Firecrawl Monitoring](https://docs.firecrawl.dev/features/monitoring) schedules recurring web crawls, detects site changes, and sends diffs by webhook or email so your agents stop rereading the whole internet and just focuses on net new content (_this is good)._

7. [NotebookLM](https://notebooklm.google.com/) is rolling out automatic Google Drive file sync, so your notebooks stay updated when source docs change (_apparently a highly requested feature!)_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# NEW FROM THE NEURON: AI Agents for Total Beginners

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/dbcd05a0-d0f9-4ab9-8546-3673f9b9fd2d/Screenshot_2026-05-28_at_11.04.34_PM.png?t=1780035800)
Follow image link: (https://www.youtube.com/watch?v=YMxY7eEhdIY)
Caption: 

[Check out the replay](https://www.youtube.com/watch?v=YMxY7eEhdIY) of yesterday’s livestream on **AI Agents for Total Beginners**. To help you parse through, answer any questions we missed, and go more in depth (including the Managed Agents and Hermes Agent stuff we couldn’t cover live), we created this [companion blog](https://theneuron.ai/explainer-articles/ai-agents-and-automation-for-beginners-full-livestream-guide-with-timestamps/)[ as a step by step walkthrough for the stream!](https://theneuron.ai/explainer-articles/ai-agents-and-automation-for-beginners-full-livestream-guide-with-timestamps/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn 

* [IBM](https://www.reuters.com/technology/ibm-plans-10-billion-investment-large-scale-quantum-computer-by-2029-2026-05-28/) committed $10B over five years to build a large-scale fault-tolerant quantum computer by 2029.

* [OpenAI](https://openai.com/index/openai-frontier-governance-framework/) published its Frontier Governance Framework, explaining how its safety and security practices map to emerging AI laws.

* [Mistral](https://mistral.ai/news/vibe-agent/) turned Le Chat into Vibe, an agentic work assistant with Work Mode, Code Mode, inbox/calendar catch-up, research, drafts, and a VS Code extension. _TBH, we prefer Le Chat... _

* [Google Pay](https://www.artificialintelligence-news.com/news/google-pay-ai-agents-universal-commerce-protocol/) prepared for agentic commerce with a Universal Commerce Protocol, while [Visa](https://techcrunch.com/2026/05/28/visa-invests-in-replit-to-power-agentic-payments-for-developers/) invested in Replit to help developer agents handle payments.

* [CNN](https://www.cnn.com/2026/05/28/media/cnn-sues-perplexity-ai-copyright) sued Perplexity, alleging the startup reproduced CNN journalism without permission, including paywalled material.

* [Apple](https://www.cnet.com/tech/mobile/apple-siri-bloomberg-reveal-ios-27/) is reportedly overhauling Siri in iOS 27 into a more agentic assistant with a new interface and stronger on-device AI focus.

* [Waymo](https://waymo.com/blog/2026/05/welcoming-riders-in-the-ojai/) began welcoming riders into its Chinese-made Ojai robotaxi, which was designed to improve robotaxi unit economics.

* [Mathematicians](https://arxiv.org/abs/2605.28781) disproved the sum-product conjecture for real numbers using ideas inspired by OpenAI’s recent unit-distance breakthrough.

* [Amazon](https://www.axios.com/2026/05/28/ai-spending-roi-enterprise-costs) scrapped an internal AI usage leaderboard after workers reportedly boosted scores with unnecessary agent activity.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

**FROM OUR PARTNERS **

### 10x the context. Half the time.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1bf4405b-3b89-41e6-8066-f91af9b08cee/flow-used-by-1000s-professionals.png?t=1776897913)
Follow image link: (https://ref.wisprflow.ai/beehiiv-ai/?utm_campaign=YJ4ZPRQDHV&utm_source=beehiiv&utm_term=ai_s1_q2&_bhiiv=opp_2d824d17-fce3-42bd-bced-24c59b5ba73c_4de8c0ec&bhcl_id=92024d77-fc81-4343-9652-ab9895a702a9_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

Speak your prompts into ChatGPT or Claude and get detailed, paste-ready input that actually gives you useful output. Wispr Flow captures what you'd cut when typing. Free on Mac, Windows, and iPhone.

[Try Wispr Flow free](https://ref.wisprflow.ai/beehiiv-ai/?utm_campaign=YJ4ZPRQDHV&utm_source=beehiiv&utm_term=ai_s1_q2&_bhiiv=opp_2d824d17-fce3-42bd-bced-24c59b5ba73c_4de8c0ec&bhcl_id=92024d77-fc81-4343-9652-ab9895a702a9_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 💡 Intelligent Insights

* [Tom Davidson claims](https://www.lesswrong.com/posts/jfwhvd43sbpkGTLyn/full-automation-of-ai-r-and-d-probably-yields-a-large-speed?commentId=ffkNW6wQGwBkmXaKz) that automating AI R&D could still make AI software progress **3-5x faster** and overall AI progress **2-3x faster**, even without a pure software-only intelligence explosion.

* [Simon Willison argues](https://simonwillison.net/2026/May/27/product-market-fit/) OpenAI and Anthropic have found product-market fit because enterprise coding agents make expensive model bills feel worth it when the user is an expensive human worker.

* [Addy Osmani said](https://x.com/addyosmani/status/2059844244907696186) that running 20 agents does not magically parallelize your own attention; review, merging, context switching, and judgment remain the bottleneck.

* [Noam Brown theorized](https://x.com/polynoamial/status/2059932468820816354) that AI may boost human mathematicians the way AlphaGo boosted Go players, after humans used AI-adjacent methods to crack the sum-product conjecture.

* [Sigal Samuel believes](https://www.vox.com/future-perfect/489976/ai-successionism-transhumanism-posthumanism?view_token=eyJhbGciOiJIUzI1NiJ9.eyJpZCI6Ik9Uc3V6UXdKMHQiLCJwIjoiL2Z1dHVyZS1wZXJmZWN0LzQ4OTk3Ni9haS1zdWNjZXNzaW9uaXNtLXRyYW5zaHVtYW5pc20tcG9zdGh1bWFuaXNtIiwiZXhwIjoxNzgxMTg2NDE1LCJpYXQiOjE3Nzk5NzY4MTV9.Xni5eIf8zE5VoEGawmZGwIls4v9S9ASPlQxfw4PZaeY&utm_medium=gift-link) humanism should reject AI successionism, transhumanism, and posthumanism’s AI-replacing humans narratives, then re-center on pluralism and intrinsic human value.

* [Even superhuman AI may not replace jobs](https://britishprogress.substack.com/p/even-superhuman-ai-may-not-replace), says Pedro Serôdio, as firms bundle tacit knowledge, coordination, and unspecifiable work in ways models alone do not dissolve overnight.

* [Your Biggest Lever](https://www.youtube.com/watch?v=eE02qPe2LBI): Ben Todd (of 80,000 hours) thinks career impact in AI depends on timeline fit, risk tradeoffs, and neglected work like AI welfare and pandemic preparedness.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# A Cat’s Commentary 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1557b162-75ce-4894-aa29-f4460bd10ee2/A_Cat_s_Commentary_x_2025__24_.png?t=1780034935)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. 




**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).  


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/claude-opus-4-8-got-safer-today
