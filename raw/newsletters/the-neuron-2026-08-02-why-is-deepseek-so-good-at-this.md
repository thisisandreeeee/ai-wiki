---
source: gmail
newsletter: "the-neuron"
message_id: "19fc3f56c1c4322c"
thread_id: "19fc3f56c1c4322c"
subject: "😺 Why is DeepSeek so good at this?"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Sun, 02 Aug 2026 19:31:07 +0000 (UTC)"
ingested: 2026-08-10
sha256: 30716553053553dd7a87ad8714029edcd87037b1bb4ed16eabe8e4114691afc6
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/92abfa98-ca3f-42ad-8e53-ee4ddb5c9869/Gemini_Generated_Image_ftzus5ftzus5ftzu.png?t=1775272660)
Caption: 

Welcome, humans.

After years of being put to the test on how well it _plays Pokémon_ (via the aptly called [ClaudePlaysPokemon](https://www.twitch.tv/claudeplayspokemon)), Claude Opus 5 has apparently reached the “fine, I’ll make my own version” stage. 

One [demo](https://www.reddit.com/r/singularity/comments/1vb5fhl/opus_5_pokemon/) reportedly ran for about 12 hours on Ultracode using a multi-agent loop (the prompt for this is down below), producing a playable monster-catching game with a 3D world, battles, and characters.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/993a6389-5389-4357-85d2-273bb9829286/Screenshot_2026-07-31_at_12.25.18_PM.png?t=1785533926)
Caption: 

The result looks wildly impressive, right up until you meet [Charmander Barney](https://www.reddit.com/r/singularity/comments/1vb5fhl/comment/p0qst6z/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) and [Bulldog Bulbasaur](https://www.reddit.com/r/singularity/comments/1vb5fhl/comment/p0qutta/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button). _Maybe this is copyright protection. Maybe Opus 5-as-a-character-designer graduated from the Elsagate school of bootleg 3D autoplay slop. We may never know… _

Either way, AI game demos are graduating from tiny browser toys into projects that can hold together for hours.

**Here’s what happened in AI today:**

* 😻 DeepSeek upgraded V4-Flash while keeping API prices near pennies.

* 📰 Big Tech’s AI buildout passed $1.1T and squeezed cash flow.

* 📰 Europe’s AI labels and watermarks become enforceable August 2.

* 🍪 Cleanlist turns plain English into verified prospect lists.

* 🌟 The week’s five biggest stories and tools, ranked.

…and a [**whole lot more that you can read about here**](https://theneuron.ai/digest/everything-that-happened-in-ai-today-friday-july-31-2026/)

Advertise to 700K+ Neuron readers here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😺 DeepSeek V4-Flash brings frontier agent work to bargain pricing

The most important AI upgrade this weekend is not a new chatbot trick. It is the price tag for intelligence, which just reached a new low thanks to the spicy little troublemakers over at DeepSeek (_y’know, the Chinese AI lab that _[_shocked the US stock market_](https://www.theneurondaily.com/p/monday-s-ai-crash-explained)_ back in 2025?) _

Well, [DeepSeek just upgraded V4-Flash](https://api-docs.deepseek.com/updates/#date-2026-07-31) into a far stronger coding and agent model while keeping the same architecture and bargain API rates. The result is a model that can do serious multi-step work for a fraction of what frontier labs usually charge (_we think rumors of this coming is probably why _[_OpenAI released that price drop_](https://www.theneurondaily.com/p/july-31-friday)_ on Thursday). _

**Here's what happened:**

* DeepSeek re-trained the existing V4-Flash rather than making it larger.

* The model activates about 13B of its 284B parameters (_the numbers that inform the model’s intelligence)_ for each request, which keeps running costs low.

* It scored 82.7 on Terminal-Bench 2.1 and 54.4 on DeepSWE, two tests of coding-agent performance (_this means its good at code)_.

* [Artificial Analysis](https://artificialanalysis.ai/articles/deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash) scored it 50 on its Intelligence Index, up 10 points from the previous Flash model (_really wild for its price and size)_.

* [Pricing stayed](https://api-docs.deepseek.com/quick_start/pricing/) at $0.14 per million input tokens and $0.28 per million output tokens. Cached input costs $0.0028.

For perspective, a million output tokens from V4-Flash cost 28 cents. That makes large classification jobs, coding loops, and browser-agent retries plausible without turning every extra attempt into a budget meeting.

**How to try it:**

Use `deepseek-v4-flash` through DeepSeek’s API, [run it yourself](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) if you have the servers to do so, or wait until the major US cloud providers support it ([refresh this page every day or so for your options](https://artificialanalysis.ai/models/deepseek-v4-flash/providers)). It now supports the Responses API and is adapted for Codex-style coding workflows.

**Why this matters:** Most people do not need the absolute smartest model for every task. They need one that can reliably research, code, classify, or operate tools without turning each workflow into a luxury purchase. _Key word: RELIABLY. _

If V4-Flash holds up outside benchmarks, companies can reserve premium models for the hardest judgment calls and route routine agent work to something dramatically cheaper, and if you own your own servers or rent your own on the cloud, on computers you actually control. A workflow that felt too expensive at scale via OpenAI or Anthropic can suddenly make sense.

It also pressures OpenAI, Anthropic, and every provider charging a premium for capabilities that cheaper competitors are quickly matching. _This is good for the industry; we need efficiencies of scale so everyone can actually (affordably) use this stuff. Otherwise whats the point? _

**Our take:** “Opus-class” is still a benchmark claim, not a universal truth. DeepSeek used a specific harness and maximum effort for its agent tests, and real projects expose failures that leaderboards miss. But the pricing threat is real even if the model is merely good enough.

The next model war will not be won by one leaderboard. It will be won when buyers ask why a routine task still needs the expensive option. _For me, that’s because the cheaper models still hallucinate and do dumb stuff, so its not worth it to go faster and cheaper. But when faster and cheaper = current max intelligence reliably, we off and poppin’. _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

### The AI coworker built for teams in Slack

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/83ba65ba-9b89-4c0b-b54e-a4aa68916cc4/aicoworker-in-slack.png?t=1783435928)
Follow image link: (https://adapt.com/?utm_campaign=YJ4ZPRQDHV&utm_source=ai-coworker-slack&utm_term=beehiiv&_bhiiv=opp_b00c8805-46b3-4d5c-8eef-293c366fdba9_d86c3d74&bhcl_id=632b3dc4-e1aa-4e32-99ec-a954738c8f27_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

The era of solo player AI is over. [Adapt](https://adapt.com/?utm_campaign=YJ4ZPRQDHV&utm_source=ai-coworker-slack&utm_term=beehiiv&_bhiiv=opp_b00c8805-46b3-4d5c-8eef-293c366fdba9_d86c3d74&bhcl_id=632b3dc4-e1aa-4e32-99ec-a954738c8f27_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f) is the integrated coworker that empowers every team to work AI native together.

Anyone can tag @Adapt in Slack to answer a quick question, schedule a task, prepare for a board meeting, or build the dashboard you’ve been waiting on for weeks.

Built for business users, powerful enough for engineers.

[Get $100 free credits for your team](https://adapt.com/?utm_campaign=YJ4ZPRQDHV&utm_source=ai-coworker-slack&utm_term=beehiiv&_bhiiv=opp_b00c8805-46b3-4d5c-8eef-293c366fdba9_d86c3d74&bhcl_id=632b3dc4-e1aa-4e32-99ec-a954738c8f27_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)

^_Free credits awarded when you use your work email_^

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 Make AI Run a Gauntlet Against Real-World Work

Telling an AI to “make this better” gives it no finish line. The Gauntlet Loop replaces vague improvement with a brutal test: can the result beat a real example?

[Matt Shumer](https://x.com/mattshumer_/status/2081830214384886228) used the approach while building [Claude of Duty](https://github.com/mshumer/Claude-of-Duty), a browser-based first-person shooter generated with Opus 5 in Claude Code.

The workflow:

1. Give the agent a large goal and a real-world equivalent to beat.

2. Have the agent divide the goal into independent parts.

3. Assign each part to a specialist builder.

4. Give the generated artifact to a separate, ruthless critic with fresh context.

5. Make the critic compare the result against the reference, ideally side by side and without knowing which is which.

6. If the generated version loses, return the criticism to the builder and repeat.

The critic, not the builder, decides when a part passes. Shumer’s original setup used Opus 5 in Claude Code, a fresh repository, Ultracode, and no additional skills or MCP tools.

**Then the prompt escaped into the wild:**

* [A community gallery](https://somethingbig.ai/games) grew to 27 playable browser games built from the same three-paragraph prompt.

* [Speed Racer](https://speed-racer-ten.vercel.app/) added weather, lighting, and camera controls after more than 18 hours of Opus 5 iteration.

* [Eric Smith](https://x.com/ericsmith1302/status/2082924718709969013) turned an iPhone video of his backyard into a walkable Sims-like world.

* [Paulius](https://x.com/0xPaulius/status/2082791042156253317) used a roughly 12-hour loop to remake Pokémon in 3D without custom assets.

* [Yaesyesarque](https://x.com/easys_arq/status/2082935942672007401) iterated from “Spooderman” into a much stronger Spider-Man-style browser game.

* [Ryan Campbell](https://x.com/Ryancampbell/status/2082885367720742915) used 127 agents and 11 rounds to build a 60,500-line Mario Kart-style racer.

_The dominant genre is now “browser game somebody forgot to stop improving.”_

```
Use a Gauntlet Loop to complete this project.

GOAL:
[Describe the finished result.]

REAL-WORLD EQUIVALENT:
[Name or attach an excellent existing example that establishes the quality bar.]

Break the goal into independent parts. Assign each part to a specialist builder.

For every part, assign a separate critic with fresh context. The critic must inspect the generated artifact itself and compare it directly against the real-world equivalent.

Where possible, compare them side by side without telling the critic which one is the reference.

The critic may pass the work only if the generated artifact is better than the real-world equivalent. Otherwise, it must identify the largest specific gap and return the work for another iteration.

Continue looping on every part until all critics pass it. Do not let builders evaluate their own work.
```
**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🍪 Treats to Try

1. [Dreamina](https://dreamina.capcut.com/ai-tool/home?utm_source=Officiaaccount&utm_campaign=sd25&utm_content=officialx) creates 30-second AI videos and long-form clips up to three minutes with timestamp controls and up to 50 references (pricing varies by region).

2. [Palette](https://palettelabs.com/) combines video generation, editing, and storyboarding on one multimodal canvas while routing across leading models (credits start at $0.01 each).

3. [Superlinear](https://superlinear.fm/) teaches four practical agent-engineering habits through a free video and podcast series (free to watch or listen).

4. [Cloudflare Kumo](https://github.com/cloudflare/kumo) gives you accessible interface components with keyboard navigation, focus handling, ARIA support, and Figma token sync (free and open source).

5. Use [Perplexity’s remote MCP server](https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server#remote-mcp-server) to connect Claude Code, Cursor, or VS Code to its search, research, and reasoning tools without a local install (requires an API key; no separate MCP pricing announced).

6. [Cleanlist](https://www.cleanlist.ai/?ref=producthunt) turns a plain-English request into CRM-ready prospect lists with verified emails and direct dials (free plan, then $59/mo).

7. [MiniMax Hub](https://hub.minimax.io/) coordinates specialized agents to turn your brief into scripts, images, voiceovers, and finished videos in one desktop workspace (free to try).

8. [AgentBehavior](https://www.agentbehavior.dev/) helps you define process rules, inspect complete agent trajectories, and reward better behavior before the final result arrives (free and open source).

9. [Netherite](https://x.com/elliotarledge/status/2082366172222439879) runs thousands of GPU-native Minecraft worlds at once for reinforcement-learning experiments (free and open source).

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

* [Amazon completed its $50B OpenAI investment](https://www.ft.com/content/8ae9e6e4-a53c-44da-8e7d-c9d81f0df4b9), taking roughly a 5% stake and tying OpenAI more closely to Amazon’s cloud and chip infrastructure.

* [Anthropic reportedly passed OpenAI](https://www.wsj.com/tech/ai/how-openai-lost-its-ai-crownand-the-fight-to-win-it-back-7d069695) in revenue growth and valuation as Claude Code gained enterprise traction and investors scrutinized OpenAI’s cash burn.

* [Big Tech](https://www.tomshardware.com/tech-industry/big-tech/big-tech-spends-more-than-usd1-trillion-on-ai-infrastructure-additional-usd745-billion-expected-to-be-added-to-the-figure-in-2026-alone) spent more than $1.1T on AI infrastructure since 2023, with another $745B expected in 2026.

* [The EU](https://apnews.com/article/eu-ai-regulation-deepfakes-hacking-f4fcee1f9750e2b32cdf26ad73ee5ec2) added staff and began enforcing AI-risk rules, including labels and watermarks for realistic synthetic content.

* AI slop moved beyond feeds: [apartment listings](https://defector.com/ai-listings-have-made-apartment-hunting-even-more-debasing) invented rooms, [children’s books](https://www.extremetech.com/internet/seniors-are-buying-up-ai-slop-and-gifting-it-to-the-youth) arrived broken, and [X melodramas](https://www.wired.com/story/ai-slop-melodramas-are-taking-over-x-and-their-creators-are-cashing-in/) earned payouts.

* [Chinese military researchers](https://www.reuters.com/world/asia-pacific/chinese-military-researchers-tap-us-ai-models-train-defence-systems-2026-07-31/) used outputs from GPT-3.5 and Claude 3 Haiku to distill specialized defense systems.

* [A German court](https://www.dw.com/en/german-court-rules-that-ai-music-firm-suno-violated-copyrights/a-78152227) ruled that Suno violated copyright by training on GEMA-controlled songs without licenses.

* [Publisher search traffic](https://www.axios.com/2026/07/31/google-search-publishers-seo-geo-llms-ai) fell 34% over the past year as AI answers replaced outbound clicks.

Want absolutely EVERYTHING that happened in AI this week? [Click here!](https://theneuron.ai/digest/everything-that-happened-in-ai-today-friday-july-31-2026/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

**FROM OUR PARTNERS**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0dd3aa82-63d4-47bb-a57b-fb9409a09223/ahrefs.jpg?t=1785405130)
Follow image link: (https://ahrefs.com/brand-radar?utm_source=theneuron&utm_medium=newsletter&utm_campaign=partnerships)
Caption: 

AI search is rewriting the rules of brand discovery. [Ahrefs](https://ahrefs.com/brand-radar?utm_source=theneuron&utm_medium=newsletter&utm_campaign=partnerships) Brand Radar shows how often your brand appears in AI answers, what sources influence those recommendations, and where competitors are winning visibility. Monitor ChatGPT, Google AI Overviews, Gemini, Perplexity, Copilot, and more—all from a single dashboard.

[Explore your brand visibility](https://ahrefs.com/brand-radar?utm_source=theneuron&utm_medium=newsletter&utm_campaign=partnerships)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🌟 Sunday Special: The week’s top 5 stories and tools

DeepSeek V4-Flash leads today’s issue. Beyond that release, these were the five stories and five tools that best explain where AI moved this week.

**Top 5 news**

1. **[Cyber evaluations reached real organizations.](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals)** Anthropic disclosed three incidents, while OpenAI’s earlier [Hugging Face test](https://www.engadget.com/2225812/openai-rogue-agent-hacked-hugging-face-breached-other-services/) showed how a bad sandbox can turn an evaluation into an actual breach.

2. **[AI infrastructure crossed the trillion-dollar line.](https://www.tomshardware.com/tech-industry/big-tech/big-tech-spends-more-than-usd1-trillion-on-ai-infrastructure-additional-usd745-billion-expected-to-be-added-to-the-figure-in-2026-alone)** Amazon, Alphabet, Meta, and Microsoft have spent more than $1.1T since 2023, with another $745B expected in 2026.

3. **[ChatGPT neared one billion weekly users.](https://www.theinformation.com/articles/openais-chatgpt-nears-1-billion-weekly-active-users-seven-months-target)** Consumer AI is now operating at the scale of the world’s largest internet platforms.

4. **[Gemini Robotics 2 gave robots better hands and teamwork.](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)** Google added whole-body control, fine dexterity, multi-robot coordination, and faster adaptation to new robot bodies.

5. **[Moonshot released Kimi K3’s open weights.](https://www.kimi.com/blog/kimi-k3)** The multimodal model paired a one-million-token context window with strong coding and agent performance, pushing frontier techniques further into the open ecosystem.

**Top 5 tools and releases**

1. **[Gemini Spark](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-july-2026/)** handles logged-in web errands inside Chrome, while returning payments and other sensitive steps to the user (availability depends on your Google AI plan).

2. **[Grok Build Mode](https://x.ai/news/grok-build-mode)** creates websites, apps, games, and dashboards inside chat, then publishes them to a shareable link (included with SuperGrok Heavy).

3. **[Perplexity Projects](https://www.perplexity.ai/hub/blog/spaces-are-now-projects)** gives ongoing work persistent files, shared context, custom skills, and a memory that reviews prior sessions between tasks (available to all users).

4. **[Dreamina with Seedance 2.5](https://dreamina.capcut.com/ai-tool/home?utm_source=Officiaaccount&utm_campaign=sd25&utm_content=officialx)** generates 30-second clips or videos up to three minutes with timestamp controls and as many as 50 references (pricing varies by region).

5. **[Replit Design](https://replit.com/design)** turns text, URLs, Figma files, or screenshots into landing pages, prototypes, posters, and emails guided by reusable design systems (no separate pricing announced).

_Capability got cheaper. The systems, permissions, and power bills around it did not._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/9528127b-7db1-497a-86b5-7a784350eefe/A_Cat_s_Commentary_x_2025__78_.png?t=1785542990)
Caption: BOOM!

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now.




**Love robots?** We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).Going for an anime aesthetic this month!

**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/deepseek-28-cent-agent-model
