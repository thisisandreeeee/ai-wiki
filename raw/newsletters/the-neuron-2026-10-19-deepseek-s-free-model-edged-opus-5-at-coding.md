---
source: gmail
newsletter: "the-neuron"
message_id: "1a153d60446c843b"
thread_id: "1a153d60446c843b"
subject: "😺 DeepSeek's free model edged Opus 5 at coding"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Mon, 19 Oct 2026 11:04:51 +0000 (UTC)"
ingested: 2026-10-26
sha256: a2984a8113ba67479e67fea39835212728e6eb616fea35c021426dd60d0efff0
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/dc54129e-bb06-44b9-b8e5-8f53265eb3d2/DeepSeek_s_Cheaper_Search_Revolution.png?t=1792397190)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f3918243-ceb5-4d2b-8795-b8f7f8dcb7b5/In_partnership_with...__10_.png?t=1791472664)
Follow image link: (https://go.granola.ai/theneuron-q4)
Caption: 

Welcome, humans.

So apparently Disney is shopping for AI talent in the Character.AI bankruptcy bargain bin.

Character.AI is the chatbot startup that filed for bankruptcy last week. According to a [legal filing](https://techcrunch.com/2026/10/18/disney-agrees-to-hire-the-majority-of-character-ais-workforce/), Disney agreed to offer jobs to at least 60 of its employees, the majority of the company, at an estimated $60M a year in pay. That works out to roughly $1M a head, and the vast majority reportedly said yes.

Disney had already agreed to buy some of its assets for $20M, and Character.AI's former CEO, Karandeep Anand, recently became Disney's first CTO.

_So the startup Disney once __[accused of copying its characters](https://techcrunch.com/2026/09/18/disneys-first-cto-led-an-ai-startup-it-once-accused-of-copying-its-characters/)__ is now basically Disney's AI department. Hollywood endings!_ One catch: this is a "stalking horse" bid, meaning an opening offer in a bankruptcy auction that another bidder can still beat.

**Here’s what happened in AI today:**

* 😺 DeepSeek's open coding model and bargain web search

* 📰 47+ big US data center projects stalled or blocked

* 📰 Anthropic pledged 5% of its shares to public benefit

* 🍪 Krea 3 edits images in under 8 seconds

* 🎓 A fix for agents drowning in tool output

…and a [**whole lot more that you can read about here**](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-monday-october-19-2026/)**.**

Advertise to 700K readers of The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# DeepSeek's Downloadable Model Edged Out Opus 5 on a Coding Test, and Its Web Search Undercuts Rivals by 85%

On Saturday, DeepSeek [released](https://api-docs.deepseek.com/news/news261017/) two things at once: a model update called V4.1-Flash-1017, and public access to its own web Search and Fetch tools for AI agents. Think of it as a new brain plus a pair of eyes, both priced like a clearance sale.

The brain first. This is a [minor update](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) to DeepSeek's cheaper "Flash" tier, and the weights are free to download under an MIT license, so anyone can run it or build a paid service on it. On DeepSWE v1.1, a coding-agent test, DeepSeek reports 77.0, versus 74.0 for Claude Opus 5 and 73.0 for GPT-5.6 Sol.

The fine print: DeepSeek ran those tests itself, and Opus 5 still wins on Humanity's Last Exam (56.3 to 42.6) and Terminal-Bench 4.0 (51.8 to 42.3). Read it as a great-value coder, not a new smartest model.

The value part is real, though. DeepSeek charges $0.15 per million input tokens (word-sized chunks of text) and $0.60 per million output tokens off-peak. In August, [Artificial Analysis found](https://thenextweb.com/news/deepseek-v4-flash-cheapest-ai-model-to-run) the earlier Flash model cost about 3 cents to run its whole test suite, versus $1.86 for GPT-5.6 Sol and $3.15 for Claude Fable 5. _Three cents. A single sticky note costs more._

Now the eyes. An AI model can't browse the web by itself, so it needs tools. DeepSeek's [Search and Fetch](https://api-docs.deepseek.com/guides/search/) are two: Search returns ranked results for a query, and Fetch opens one page and returns its text as Markdown (plain text with light formatting). The pricing:

* Each costs $0.75 per 1,000 successful requests. Failed and empty calls are free.

* One [pricing roundup](https://finance.yahoo.com/technology/ai/articles/deepseek-monetizes-agent-retrieval-layer-185236272.html) lists rivals at $5 per 1,000 and up, including Brave, Tavily, and Perplexity. That's the 85% gap in the headline.

* Calls made through DeepSeek Harness, Claude Code, or Codex are free until billing starts November 1, Beijing time.

_Pages come back as full text, which is exactly the big-tool-output problem in today's AI Skill below._

So what does this do to everyone else? Our read: open weights cap prices, since any cloud can host the model and OpenRouter already lists about a dozen. Analysts cited by [IBTimes](https://www.ibtimes.com.au/deepseek-ai-challenge-us-rivals-price-coding-1876728) see that as a structural challenge to closed labs' premium pricing. The top models look safe on the hardest reasoning, so the squeeze lands on bulk work like routine coding and agent loops. No rival has cut prices yet, so that's a forecast.

Then there's the geopolitics, because DeepSeek never launches in a vacuum:

* Copying accusations: On September 8, the NSA, FBI, and CISA [issued a joint advisory](https://www.theregister.com/ai-and-ml/2026/09/09/us-claims-chinese-ai-companies-core-ai-strategy-is-distilling-american-models/5295171) saying DeepSeek and Alibaba used distillation at industrial scale. That means training a model on another model's answers, like copying a straight-A student's homework. Beijing has pushed back and hinted at retaliation.

* The chip fight: IDC says Nvidia's share of China's AI chip market fell to 34% in early 2026, while Huawei's rose to 28%.

* Beijing's own brakes: On Friday, China [proposed export controls](https://thenextweb.com/news/china-ai-export-controls-draft) on 23 AI items, including weights for models with 2 trillion or more parameters or a top-10 world ranking. The draft names no models, but Bloomberg and the AP say Kimi K3 and Qwen3.8-Max exceed the size line. API and app access would continue.

_Notice what DeepSeek shipped on the safe side of that line: open weights for a mid-size model, and a pay-per-call API for the rest. Strategy or coincidence? We can't tell._

What this means for you: Search and Fetch run on DeepSeek's servers, and several governments restrict DeepSeek on official devices over data security. Public-web research is a reasonable use. Keep confidential material out, and check your IT policy first.

Two dates to watch: November 1, when the free window ends and real bills begin, and whether anyone independent can reproduce that 77.0.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# Stop screenshotting slides mid-call

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/24cfa84b-4abd-4e22-bc16-f3d8a5bfc264/Granola_Conceptual_R_Everything_01_1920x1080.png?t=1791477662)
Follow image link: (https://go.granola.ai/theneuron-q4)
Caption: 

Granola, the AI notepad for people with back-to-back meetings, now captures what's shared on screen too. With Snapshots, the decks, designs, charts and docs from your calls go straight into your notes, next to what you jotted down. Later, ask Granola about last week's roadmap review and the slides come back with the answer.

Download Granola and try it in your next meeting.
3 months on us with the code **THENEURON**.

**[Try Granola](https://go.granola.ai/theneuron-q4)**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Stop Your AI Agent From Drowning in Its Own Tool Output

Picture an agent that watches your app's logs. Every check, the tool dumps another big batch of log text into the conversation, and the agent re-reads all of it on every turn. AWS developer advocate Elizabeth Fuentes Leone [walked through this](https://www.youtube.com/watch?v=DrfyORO8RqA) in a talk posted October 7. Agents break when tools return big outputs, and a bigger context window (how much text a model can hold in view at once) doesn't fix it.

In her session abstract, one tool returned 214KB of logs, the answers got worse, and nothing threw an error.

How bad does it get? Chew Loong Nian [re-ran her fixes](https://pub.towardsai.net/how-to-fix-aws-strands-agents-context-bloat-one-plugin-cut-252k-tokens-to-9k-f47b357496bd) in AWS's open-source Strands agent framework with a scripted model.

Eight log fetches left a default agent holding about 252,000 tokens of history (tokens are the word-sized chunks a model counts). One built-in plugin cut that to about 9,000. The obvious shortcut, a smaller sliding window, cut it to about a quarter of that, but it throws away whole turns, including whatever the agent learned from them.

The plugin uses a **memory pointer**: the big output goes into storage, and the agent's context gets a short ID it can use to fetch the data later.

Her second fix is a cap on repeat calls. In her abstract, an agent that retried the same call fourteen times dropped to two once it had a clear "done" signal and repeat calls were blocked. _Fourteen to two. Somebody's API bill just exhaled._ One caveat: Chew's test measures how much text stays in context, not whether the answers improved.

You probably aren't writing Strands code, but her abstract says the fixes work with any agent framework. If you build or buy agents, ask for three things:

1. Store big tool outputs outside the conversation and hand the agent a short ID.

2. Cap how many times an agent can call the same tool per task.

3. Give the agent a clear "done" signal.

```
Review my agent for tools that can return large outputs (logs, search results, files). For each one: (1) save the full output to a file and return only a short summary plus a file ID, (2) set a maximum number of calls per tool per task, and (3) add a clear "done" condition so the agent stops once it has an answer.
```
**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

### When your support agent gets it wrong, who's accountable?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1f7e89d2-d4ae-450e-bc8f-5fb34e64c635/Paid_Social_Warm_1200x627__2_.png?t=1790786122)
Follow image link: (https://front.registration.goldcast.io/series/f7a5a6e2-a125-4eff-90cc-ea68f93122c3?utm_source=beehiiv&utm_medium=cpm&utm_campaign=ongoing_YJ4ZPRQDHV_consideration_norpac&utm_content=running-agents-in-customer-work-series_V1&_bhiiv=opp_1bbbdbe1-8a5b-4144-8198-7d7a26fa6e6f_2e4a08a6&bhcl_id=4ded08c3-5929-4792-b117-a399c7eea5ae_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

Every agent handling refunds, account changes, or tickets needs three answers: what it can pick up, what it's allowed to do, and when it hands back. [Running Agents in Customer Work](https://front.registration.goldcast.io/series/f7a5a6e2-a125-4eff-90cc-ea68f93122c3?utm_source=beehiiv&utm_medium=cpm&utm_campaign=ongoing_YJ4ZPRQDHV_consideration_norpac&utm_content=running-agents-in-customer-work-series_V1&_bhiiv=opp_1bbbdbe1-8a5b-4144-8198-7d7a26fa6e6f_2e4a08a6&bhcl_id=4ded08c3-5929-4792-b117-a399c7eea5ae_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f) is four conversations on agentic AI in customer ops. [Register now](https://front.registration.goldcast.io/series/f7a5a6e2-a125-4eff-90cc-ea68f93122c3?utm_source=beehiiv&utm_medium=cpm&utm_campaign=ongoing_YJ4ZPRQDHV_consideration_norpac&utm_content=running-agents-in-customer-work-series_V1&_bhiiv=opp_1bbbdbe1-8a5b-4144-8198-7d7a26fa6e6f_2e4a08a6&bhcl_id=4ded08c3-5929-4792-b117-a399c7eea5ae_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f), four Tuesdays, 10 a.m. PT.

[Register now](https://front.registration.goldcast.io/series/f7a5a6e2-a125-4eff-90cc-ea68f93122c3?utm_source=beehiiv&utm_medium=cpm&utm_campaign=ongoing_YJ4ZPRQDHV_consideration_norpac&utm_content=running-agents-in-customer-work-series_V1&_bhiiv=opp_1bbbdbe1-8a5b-4144-8198-7d7a26fa6e6f_2e4a08a6&bhcl_id=4ded08c3-5929-4792-b117-a399c7eea5ae_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/9bf7b370-d3d3-470d-9b0b-57ac1f5dbd1c/Outskill_-_10_19.png?t=1791820063)
Follow image link: (https://links.outskill.com/NEUROCT4)
Caption: 

1. *Master Astra and 15+ powerful AI tools in Outskill’s free live workshop. Build custom AI agents, automate workflows, and boost productivity. [Save your seat today!](https://links.outskill.com/NEUROCT4)

2. [Krea 3](https://www.krea.ai/krea-3) edits images in under 8 seconds at 2K, so you can swap a product's background or lighting using up to 6 reference images to keep it consistent.

3. [CallSitter](https://github.com/szerintedmi/callsitter) answers your phone so scammers waste their time on a bot, sales calls get a polite no, and real callers leave a message—open-source code.

4. [Sphinx](https://sphinx-six-theta.vercel.app/) quizzes you on what your agent's code actually does before Git lets you push it—free/open-source.

5. [WhatsApp MCP](https://github.com/finereli/whatsapp-mcp) lets your AI agent search and read your own WhatsApp chats (read-only, but it's unofficial and against WhatsApp's terms).

6. [llmspeed](https://llmspeed.dev/) lets you feel how fast a local model runs on a specific GPU, Mac, or laptop before you spend money on it.

7. [Rubi](https://github.com/YURIBEDRAN/rubi) maps your codebase into a knowledge graph so Claude Code, Codex, Cursor, and others stop rereading the whole repo every session.

8. [pi-cowboy](https://github.com/electric-dragon-80000v/pi-cowboy) runs Codex, Claude Code, and OpenCode agents side by side on one task, each in its own lightweight copy of your repo.

9. [DocuMemory](https://www.documemory.dev/) turns your AI chats into compact, searchable decision notes that Claude Code, Cursor, and other MCP tools can reuse next session.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5dcddb1f-97e4-4a8b-95ce-ae10ca3c6fe9/image.png?t=1792395477)
Follow image link: (https://x.com/chetaslua/status/2111661115117900177)
Caption: Three unannounced OpenAI models, aurora red, green, and blue alpha, briefly appeared in its API Saturday, then vanished. Blind image tests followed, suggesting a new image model (unconfirmed). So why care? Per Arena’s leaderboard, OpenAI already holds the top three text-to-image spots, while Google’s new Nano Banana 2.1 sits sixth.

* Anthropic [pledged 5% of its shares](https://www.anthropic.com/news/public-benefit-fund) to a new Public Benefit Fund, pending stockholder approval, with more possible as its value grows.

* The Financial Times counted at least 47 large US data center projects [delayed, withdrawn, or blocked](https://www.ft.com/content/9ea5a37d-15c9-4d5b-94d6-719048c9cd3c) in 2026, while Bernstein rated only about 35% of the planned pipeline credible.

* Microsoft [pulled out of](https://siliconangle.com/2026/10/18/neocloud-operator-nscales-ipo-plans-could-be-at-risk-after-microsoft-pulls-the-plug-on-u-k-data-center-project/) Nscale's planned Essex data center, the Telegraph reported, as grid officials told Nscale power wouldn't arrive until the 2030s.

* Samsung [teamed up with rival TSMC](https://en.sedaily.com/finance/2026/10/18/samsung-to-tap-tsmc-3-nanometer-lines-for-nvidia-custom-hbm) to build the base layer of Nvidia's custom memory chips, which Seoul Economic Daily says boost memory bandwidth by up to 30%.

* Axios found that 42% of 102 top US publishers [blocked AI training crawlers](https://www.axios.com/media-trends-membership/2026/10/17/publishers-block-ai-training-search-crawlers), versus 25% that blocked AI search bots.

* DoubleVerify data showed AI "slop" sites [grew more than fivefold](https://www.axios.com/media-trends-membership/2026/10/17/ai-slop-geo-content-farm-recommendations) in Q2 from a year earlier, with traffic to them quadrupling, Axios reported.

Want absolutely EVERYTHING that happened in AI this week? [Click here!](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-monday-october-19-2026/)

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

## 😹 Monday Meme

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ff6d07ad-b61f-43d1-9b61-8b1e0474047d/image.png?t=1792397883)
Follow image link: (https://x.com/horrormuseum/status/2111931108178940414)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5bad3347-cf0a-4c9b-9868-45bcf260caff/TN_Thumbnail_101326_AnastasisGermanidis_Runway_B.png?t=1791882337)
Caption: 

New episodes air **every week** on Wednesdays: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/92c6a486-1c07-4877-9175-3d880e28860f/A_Cat_s_Commentary_x_2025_-_2026-09-28T163108.460.png?t=1790640265)
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
https://www.theneurondaily.com/p/deepseek-s-free-model-edged-opus-5-at-coding
