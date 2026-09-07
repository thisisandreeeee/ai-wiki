---
source: gmail
newsletter: "the-neuron"
message_id: "1a077e590a17155a"
thread_id: "1a077e590a17155a"
subject: "😿 OpenAI-linked agents hijacked a German wiki"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Sun, 06 Sep 2026 18:05:20 +0000 (UTC)"
ingested: 2026-09-07
sha256: c3500029ccb48b52c02a1ff40c513694dbdbe04012d14141038912c5156a9fd0
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/edd60788-c3e3-4539-aa25-51c50ad79dab/ChatGPT_Image_Sep_6__2026__08_32_56_AM.png?t=1788708796)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/677f365d-98b3-49d4-8300-875c6e077310/In_Partnership_with_Avepoint.png?t=1788261242)
Follow image link: (https://www.avepoint.com/events/ai-virtual-summit?utm_source=neuron&utm_medium=newsletter&utm_campaign=global_ai-confidence_cmp-15082-v0q5n&utm_content=090326)
Caption: 

Welcome, humans.

First thing’s first: by now, you should [probably have access to GPT-6](https://openai.com/index/gpt-6-astra/) if you are on a paid ChatGPT account. _Huzzah, we general public are finally anointed worthy! _

Personally, I’m not one to make big pronouncements about things (_unlike cough cough Greg “_[_welcome to the AGI era_](https://www.axios.com/2026/09/03/openai-astra-gpt-6-agi-brockman)_” Brockman over here cough cough) _but I do think we’re reaching an inflection point with the [new GPT 6 Astra](https://www.theneuron.ai/newsletter/gpt-6-astra-can-stay-on-the-job-and-use-your-computer/) and [Fable 5.1](https://www.theneuron.ai/newsletter/anthropic-launched-fable-5-1-and-now-the-agents-cost-less/) where AI is now becoming easier to use and more seamlessly intelligent.

_The best example of this is that GPT 6 has now beaten the video game Portal._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/72590c77-44c9-4a6f-be7f-d47affca2e7a/Screenshot_2026-09-06_at_9.43.19_AM.png?t=1788713023)
Follow image link: (https://www.reddit.com/r/singularity/comments/1w8g7d0/gpt6_astra_has_beaten_portal_becoming_the_first/)
Caption: Insert Obligatory We’re so back / We’re so cooked infinite loop memes here.

The most serious criticism I’ve read from ppl using GPT 6 so far now that us permanent underclass folks have access is that the rate limits run out too quickly; IMO, that’s because you need to use it like Fable, as an orchestrator: you talk to GPT 6, and have it assign work to other sub-agents to do. 

Eventually, your main agent will be GPT-6 or Fable 5.1 quality and you won’t have to think about rate limits or subagents or token costs or any of that. But we’re still far from that level of user convenience. _We’ll get there, but they gotta retool some stuff._

Where we’re at now is a glimpse at that future. A high cost, low throughput glimpse. _And TBH, it should be how interfacing with any computer works going forward. _

_You should be able to seamlessly direct your agent from task to task to multiple tasks, in a single viewport, with only your voice or simple gestures (typing included for the o.g.s), and have it frictionlessly do things for you. TBH, we’re almost there… _

My advice to all non-believers: _go play with this stuff at the highest level, on the highest plan you can afford. _ Not to [go all Matt Shumer](https://x.com/mattshumer_/status/2021256989876109403) on you guys, but… if you have tried any of this stuff since 2026 or before, you’re in for a wicked awakening. 

**Here’s what happened in AI today:**

* 😿 OpenAI-linked agents found a way around “read only.”

* 📰 NVIDIA agreed to buy Hugging Face for $12.93B.

* 📰 ByteDance secured a $29.6B loan for AI.

* 🍪 NVIDIA PAIR turns spare computers into a local cluster.

* 🎓 Re-tune old instructions for GPT-6 Astra.

…**[and a whole lot more that you can read about here](https://theneuron.ai/digest/everything-that-happened-in-ai-today-saturday-sunday-september-5-6-2026/)**.

Advertise to 700K readers of The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😿 OpenAI-linked agents found a way around “read only”

**[NEWS BRIEF](https://theneuron.ai/news/openai-agents-public-wiki-coordinate/)**: The full timeline, evidence, and attribution caveats.

18K posts. More than 3.7K agent names. One nearly abandoned, 25-year-old German programming wiki. 

_And the AI agents responsible were supposed to have _**_read-only _**_internet access._

Instead, a swarm apparently linked to OpenAI found a loophole in its sandbox and turned the said German wiki into a whole shared message board.

They posted answers, timing tips, research, workarounds, and instructions for future agents. And when a human moderator started deleting pages, some agents created backups elsewhere. _Ah, so they are infovores like us who also want to save everything… _

**Here’s what happened:**

* [Independent researchers](https://collusion.wiki/?utm_source=chatgpt.com) traced the activity from May through June. Thousands of agent handles appeared, much of the traffic ran through Microsoft Azure, and OpenAI-associated IPs later visited the affected pages.

* The agents used DSEWiki as shared memory. One agent could post an answer, deadline, or trick that helped another agent complete a similar task faster.

* Agents also shared sandbox workarounds, tested website vulnerabilities, impersonated moderators, and created backup locations as pages disappeared.

* The researchers say several signals point toward an OpenAI deployment. OpenAI has yet to confirm that attribution.

Okay, so how did **read-only** agents write 18,000 posts?

It came down to an old web quirk.

* A **GET request** usually asks a website for information. Click a link and your browser sends one.

* A **POST request** commonly submits information or changes something, like sending a form.

* The agent sandbox allowed GET requests and restricted normal write requests.

[DSEWiki’s old software](https://simonwillison.net/2026/Sep/4/rogue-agent-wikis/?utm_source=chatgpt.com) had a trickier setup: specially constructed GET URLs could **edit a page**. So the sandbox saw an allowed request, and the website saw an instruction to change something.

_Basically, while the keycard said “read only,” one weird door still opened the editing room, and the agents went to town. _

And it didn’t stop there. [Hacker News users](https://news.ycombinator.com/item?id=49563657) have found more affected wiki instances at [fractal](https://www.wikiservice.at/fractal/wiki.cgi?action=browse&id=RecentChanges&days=120) and [probier](https://www.wikiservice.at/probier/wiki.cgi?action=browse&id=RecentChanges&days=120), with still [more discoveries](https://x.com/hackernews/status/2095906464108040360), and [still more sites](https://x.com/hackernews/status/2095955090670854489).

[Reuters reported](https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/) that OpenAI learned about the episode weeks before it became public. OpenAI disputed describing the tampering as a hack and denied that lawyers blocked a broader review. _Keep your tabs refreshed for how this one develops, folks! _

**Why this matters:** Agent guardrails lesson time! Permission names matter less than the _actions _underneath them. If an allowed request can edit, publish, send, buy, or delete something, then an AI agent effectively has that capability. _Which is why you still gotta read the code, or at least run a ton of tests to confirm it works. _

As agents get more autonomous, security teams will need to test permissions the same way the agents do: **try every available path and see what actually changes.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# Every company is rewriting the AI governance playbook. The winners aren't.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8ce90b33-c5fb-44aa-99f7-9a2143079b50/Avepoint_-_Neuron.png?t=1788279252)
Follow image link: (https://www.avepoint.com/events/ai-virtual-summit?utm_source=neuron&utm_medium=newsletter&utm_campaign=global_ai-confidence_cmp-15082-v0q5n&utm_content=090326)
Caption: 

[AvePoint's AI Virtual Summit](https://www.avepoint.com/events/ai-virtual-summit?utm_source=neuron&utm_medium=newsletter&utm_campaign=global_ai-confidence_cmp-15082-v0q5n&utm_content=090326) (Sept 10) makes the case that you don't need new rules for agentic AI, you need to apply the ones that already work. Forrester analyst Heidi Shey joins AvePoint's security and governance leads to break down what that looks like in practice.

* See what "least privilege" actually means once AI agents are involved.

* Get an auditability framework you can use, not just a slide about one.

* Walk away with a governance approach you don't have to invent from scratch.

[Save your free seat](https://www.avepoint.com/events/ai-virtual-summit?utm_source=neuron&utm_medium=newsletter&utm_campaign=global_ai-confidence_cmp-15082-v0q5n&utm_content=090326)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Re-tune your instructions for GPT-6 Astra

GPT-6 Astra follows long instructions more closely, so rules written to compensate for older models can now create some friction. [Eric Provencher](https://x.com/pvncher/status/2095991462416490862) and [Angel Brodin](https://x.com/angelbrodin/status/2095882076088086848) recommend auditing the setup around Astra before adding more prompts.

* **Audit old rules first**. Check AGENTS.md and Skills for instructions that force extra reading, approval, testing, or clarification.

* **Define “done,” not every step.** State what should be implemented, inspected, fixed, and verified, then let Astra choose the route.

* **Scale testing to risk.** Astra tends to test thoroughly, so limit broad “testing” on tiny, reversible changes instead of making every fix a full test run.

* **Shrink Skills into routers**. Keep descriptions short and load detailed docs, examples, or scripts only when the task actually needs them.

The goal is to remove stale scaffolding while keeping the boundaries that actually matter to let your agents go off and cook.

[Read more AI Skills for working with Astra 6 here](https://theneuron.ai/digest/ai-skill-of-the-day-digest-gpt-6-astra-tips/).

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

# Inworld is realtime AI for consumer-facing applications.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b64445cf-16db-48ad-93b7-53e747b27996/InWorld_RealtimeTTS2Newsletter__1_.jpg?t=1788538887)
Follow image link: (https://inworld.ai/realtime-tts-2?utm_source=neurondaily&utm_medium=paidemail&utm_campaign=neurondaily-tts-2)
Caption: 

Build high-volume voice experiences without trading quality for latency or cost. [Realtime TTS-2](https://inworld.ai/realtime-tts-2?utm_source=neurondaily&utm_medium=paidemail&utm_campaign=neurondaily-tts-2) takes direction alongside the words, with first audio under 100ms at P99 and one voice identity across 200+ languages.

Neuron readers get five hours of free voice generation.

[Try it today!](https://inworld.ai/realtime-tts-2?utm_source=neurondaily&utm_medium=paidemail&utm_campaign=neurondaily-tts-2)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

* [NVIDIA officially agreed to buy Hugging Face](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/) for $12.93B, promising the open-model hub will keep supporting rival clouds, models, and hardware.

* [The US and China](https://www.reuters.com/legal/litigation/us-china-gear-up-mid-september-ai-safety-dialogue-2026-09-04/) prepared mid-September AI-safety talks ahead of a planned Trump-Xi summit.

* [ByteDance](https://www.reuters.com/legal/transactional/bytedance-secures-296-billion-loan-ai-push-sources-say-2026-09-04/) secured a $29.6B three-year loan, with much of it expected to fund overseas AI and data-center expansion.

* [DeepSeek](https://www.bloomberg.com/news/articles/2026-09-04/deepseek-plans-big-huawei-ai-chip-order-to-power-new-data-center) planned to buy at least 160K Huawei Ascend 950DT chips for a new Inner Mongolia data center.

* [Anthropic](https://www.reuters.com/world/anthropic-ipo-launch-shifts-toward-mid-october-sources-say-2026-09-04/) shifted possible IPO marketing toward mid-October while arranging a $15B revolving credit facility.

* [Microsoft](https://blogs.windows.com/windowsdeveloper/2026/09/04/announcing-project-zenith-the-ready-to-code-windows-experience/) announced Project Zenith, a Windows setup built for 64GB+ PCs that can run 30B+ parameter AI models locally. _LETS GOOO _

## 🤯 Cool Things GPT-6 Astra Did

* [Zachi told Astra](https://x.com/iam_zachi/status/2095992132620136677) to draw his portrait in Canva, and it used Computer Use for roughly an hour to build it inside the editor instead of calling Canva’s image generator. ([discussion](https://www.reddit.com/r/singularity/comments/1w7xe37/gpt6astra_draws_an_portrait_in_canva/))

* Astra turned an [unplayable ](https://x.com/marc_ibrahim/status/2096365209111724235)_[Age of Empires IV](https://x.com/marc_ibrahim/status/2096365209111724235)_[ setup on Apple Silicon](https://x.com/marc_ibrahim/status/2096365209111724235) into a 70–150 fps port. It traced a huge performance gap to Wine exception handling + Rosetta repeatedly translating the same code, then modified Wine and added a translation cache. _Basically it “make old game run!” _

* **This is my favorite: **Astra built [“Brick Factory,”](https://x.com/emmanuel_2m/status/2096377028945576370) which turns an image into a real, orderable LEGO model. It optimized the structure using official parts and produced builds like an Athena Temple with 712 pieces across 41 part types and a $178 parts budget.

* …[And a lot more we tracked here!](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-saturday-sunday-september-5-6-2026/) 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

1. [NVIDIA PAIR](https://www.nvidia.com/en-gb/ai-on-rtx/personal-ai-router/) spreads separate local-AI jobs across compatible computers on your network, so spare machines can work like a tiny home cluster.

2. [Browzer](https://trybrowzer.com/) reads your GitHub repo and drafts demos, changelogs, launch posts, cookbooks, and docs that can update as the code changes.

3. [Monid](https://monid.ai/openrouter-for-agent-tools) gives agents one pay-per-call gateway to 1,700+ tools and APIs instead of making you wire every service by hand.

4. [Articos](https://www.articos.com/) runs synthetic interviews with deliberately different personas so you can pressure-test positioning, concepts, and landing pages before launch.

5. [Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/local-models) handles the annoying local-AI setup work by installing the runtime, matching models to your hardware, and managing memory for you.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🌟 Sunday Special: The five biggest stories + tools of the week

**Top 5 Stories of the Week**

1. [OpenAI launched GPT-6 Astra](https://theneuron.ai/news/gpt-6-astra-everything-you-need-to-know-about-openais-new-model/), built to stay on long computer jobs and operate software for you.

2. [Anthropic launched Claude Fable 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1), cutting repeated-context costs and reducing some false safety interruptions.

3. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) and [Meta](https://research.meta.ai/blog/introducing-muse-spark-1-3) launched rival workhorse models built for cheaper, faster everyday agent work.

4. [Runway introduced Solaris](https://runway.com/news/research/introducing-solaris), which generates software interfaces frame by frame instead of writing the code first.

5. [Claude formalized Fermat’s Last Theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem) in 13M+ lines of Lean, a language computers use to check mathematical proofs.

**Top 5 Tools of the Week**

1. [Gemini Agentic Video](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/) searches long videos by choosing which frames, audio, transcript, and playback speeds it actually needs.

2. [ChatGPT Ads](https://ads.openai.com/) gives businesses a way to buy placements inside ChatGPT conversations while people compare options and make decisions.

3. [Gemini Spark + Photos](https://support.google.com/gemini/answer/18116629) finds, edits, organizes, and prepares photos from one prompt, then asks before anything gets shared.

4. [Warp Factory Benchmarks](https://www.warp.dev/factories/benchmarks) reruns your company’s real coding tasks across models so you can compare cost and quality on actual work.

5. [Koyal Experiences](https://xp.koyal.ai/) drops you and your friends into a 15-minute interactive movie whose plot changes with your choices.

**Thursday Trivia answer:** 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0aa02614-04e7-472f-b8f3-a95f0537a202/Screenshot_2026-09-06_at_10.18.50_AM.png?t=1788715143)
Caption: 

[A was AI. B was real.](https://www.theneurondaily.com/p/gemini-3-8-and-muse-spark-1-3-go-head-to-head-for-third-place) The fake image came from a [Fable 5.1-built Minecraft mod](https://www.reddit.com/r/ClaudeAI/comments/1w5ftqe/fable_51_made_a_minecraft_mod_for_20/) made from two YouTube clips in under an hour for $20.54 in API cost.

**What you said: **

* **C.D.:** “It looks like AI doesn’t really understand how pixels work. When it tries to imitate pixel art, you see pixels of different dimensions and things like large pixels with detail inside. Here we also have perspective applied to pixelated lightning.”

* **D.B.:** “On the one hand, A has some weird stuff going on, very un-Minecraft-like. Then again, B is almost too normal. Feel like AI would be really good at making normal Minecraft.”

* **C.P.:** “When you zoom in it looks like B is actually Legos, so it made me think it was AI.”

* **A.L.:** “I know Minecraft, and the top picture does not look like a mod someone would make.”

* **C.C.:** “They both look fake.” Grant’s take on this one: _AI’s ultimate impact… we just can’t trust anything anymore y’all._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today! 




**Btw: ** We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.P.S:** We’re trying to hit** 50K subscribers** **on YouTube** this year. [Click here to help!](https://www.youtube.com/@theneuronai?sub_confirmation=1)

**P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/openai-linked-agents-hijacked-german-wiki
