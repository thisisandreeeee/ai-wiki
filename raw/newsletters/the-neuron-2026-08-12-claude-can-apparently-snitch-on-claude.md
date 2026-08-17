---
source: gmail
newsletter: "the-neuron"
message_id: "19ff587313afe367"
thread_id: "19ff587313afe367"
subject: "😺 Claude can apparently snitch on ...Claude"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Wed, 12 Aug 2026 10:31:42 +0000 (UTC)"
ingested: 2026-08-17
sha256: 939f96772b235aebcc76ffee44655f675d18a14d69e2f79d090b0effd9ed5681
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/449720c2-ced8-4476-b3e5-76314efd250d/ChatGPT_Image_Aug_11__2026__05_45_19_PM.png?t=1786495618)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/9c05b666-99e3-40cf-a6e1-ca5ca46843bd/In_Partnership_with_Beyond_Trust.png?t=1785930492)
Follow image link: (https://www.beyondtrust.com/products/ai-agent-security?campid=701Vw00000jOLKkIAO)
Caption: 

Welcome, humans.

So, yesterday we covered how [Anthropic is adding invisible provenance markers to Claude-generated text](https://www.the-independent.com/tech/claude-anthropic-update-watermark-new-b3031096.html), and people are, technically speaking, _pissed_. 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f14a54a5-b872-4c4d-9124-9de8b37f2eb7/Screenshot_2026-08-11_at_4.52.19_PM.png?t=1786493368)
Follow image link: (https://www.reddit.com/r/claude/comments/1vl8tjs/our_data_anthropics_mark/)
Caption: 

The complaint is basically: after years of arguments over whose writing and code contributed to training AI, Claude can now leave Anthropic’s invisible stamp behind to say, basically, “_Well IDK about all THAT, but me the AI definitely wrote THIS_.” 

Let’s think about what this means, though. The [U.S. Copyright Office says](https://www.copyright.gov/newsnet/2025/1060.html) purely AI-generated material needs sufficient human authorship to qualify for copyright. So can a chunk of text you may not be able to copyright still be watermarked? _Welcome to intellectual property law, where vibes rule everything around me. _

Meanwhile, in _other things you don’t like suddenly trying to make you like them, _someone came up with a solution to the whole “[we all hate data centers](https://www.theneurondaily.com/p/the-ai-data-center-backlash-is-going-bipartisan)” thing and built [OPEN LIVING](https://www.reddit.com/r/OpenAI/comments/1vlcjzz/open_living_a_data_center_you_can_live_in/), a satirical data center you can apparently live in.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b7b14ea6-c499-47ef-9244-26f0fe18dde5/Screenshot_2026-08-11_at_3.46.52_PM.png?t=1786493530)
Caption: America doesn’t build enough housing? but they build too many datacenters? Brother, I GOT YOU.

_At least you know they’ve got central AC covered, what with all that recycled water they’ve got flowing through there to cool down the servers. So long as no one _[_summons the banana demon_](https://www.reddit.com/r/aivideo/comments/1vlnf91/i_hit_extend_video_10_times_using_the_prompt_a/)_ (very scary video; you’ve been warned) while I’m trying to sleep, I think I could swing it. _

**Here’s what happened in AI today:**

* 🙀 Researchers extracted hidden reasoning from frontier AI models.

* 📰 NVIDIA lined up $500B+ for AI infrastructure financing.

* 📰 Anthropic reportedly signed Riot’s $9.1B compute deal.

* 📰 Qwen’s 27B open model is landing this week.

* 🎓 A plugin translates Claude’s “Claudish” into English.

Advertise in The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🙀 Researchers Cracked Open AI’s Hidden Reasoning

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6ed40bd1-25bc-4ba1-933a-df0e133718c8/Screenshot_2026-08-11_at_5.19.34_PM.png?t=1786493985)
Follow image link: (https://www.reddit.com/r/singularity/comments/1vlhteb/researchers_find_way_to_extract_hidden_reasoning/)
Caption: 

AI labs have spent years hiding models’ private reasoning so competitors, attackers, and curious users can’t simply read the machinery underneath. Well, researchers just found a surprisingly simple way around that wall.

Claude, ChatGPT, and Gemini can do private step-by-step reasoning before showing you an answer.

**Here’s what happened:**

* A new [research paper](https://arxiv.org/abs/2608.09867) found encrypted reasoning blocks from OpenAI, Anthropic, and Google could actually be replayed into weaker sibling models from the same provider.

* Researchers found those encrypted blocks were too portable. A trace from a powerful model could be replayed into a cheaper, weaker model from the same company.

* With a jailbreak prompt, those weaker models sometimes turned the encrypted blocks back into readable reasoning, **without researchers ever stealing the encryption key.**

* Across 315,320 public reasoning blocks, they recovered 367 pieces of personal information and 182 credentials, including API keys and passwords.

* They also found evidence consistent with model distillation: Kimi K3 sometimes produced reasoning strikingly similar to hidden traces from frontier models, though similarity alone does not prove how it was trained.

Think of Claude Opus sealing its private notes inside an envelope. Your app can hold the envelope but can’t open it. Researchers discovered they could sometimes hand that envelope to Claude Haiku and convince Haiku to read the notes aloud.

The weird part is **how that envelope became available to attack at all.** Labs weren’t sending the model’s reasoning around as readable text. They encrypted it, sent the encrypted block through their APIs to the app, then let the app hand it back later so the model could resume where it left off.

That created a new **attack surface** (basically, another place an attacker can try to break the system): the encrypted block itself was now moving between models, apps, sessions, and users. The app couldn’t read it, but another model from the same provider sometimes could.

**Why this matters:** Those hidden notes could expose user secrets, information intentionally withheld from the final answer, or valuable training data. Competitors could potentially use them for **distillation** (training a smaller model on a stronger model’s examples) to copy some of its capabilities.

Hidden reasoning was supposed to protect users and the labs’ intellectual property. This research shows secrecy can create a new security boundary that needs defending, especially when encrypted traces travel between models, sessions, and users.

OpenAI, Anthropic, and Google were notified before publication and changed their systems (_nice try, sneaky distillers!_). Although…

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# Least Privilege for the Age of AI Agents

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/19a5e8dd-bd1a-4513-9155-cd055bd7f283/Beyond_Trust_The_Neuron_Podcast-Ad_placement-July2026.png?t=1785930516)
Follow image link: (https://www.beyondtrust.com/products/ai-agent-security?campid=701Vw00000jOLKkIAO)
Caption: 

AI agents are growing 40% year-over-year inside enterprises. 7% of orgs already had an agent-related security incident this year.

The problem: AI agents don't create new permissions — they weaponize the ones already there. Same cloud keys, same tokens. No scoping. No expiration. No one watching.

[BeyondTrust](https://www.beyondtrust.com/products/ai-agent-security?campid=701Vw00000jOLKkIAO) AI Agent Security:

* Sees every agent — including shadow AI

* Attributes every action to human or agent

* Blocks risky commands, enforces approval before agents act

* Works across Claude Code, Copilot, Cursor, more — one policy, any vendor

[→ Learn More](https://www.beyondtrust.com/products/ai-agent-security?campid=701Vw00000jOLKkIAO)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Translate Claudish to English

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/fbe95298-1fd7-49b1-84b0-3869f6eac8f1/Screenshot_2026-08-11_at_3.45.07_PM.png?t=1786494228)
Follow image link: (https://www.reddit.com/r/ClaudeAI/comments/1vl0n1t/claude_code_plugin_for_translating_from_claudish/)
Caption: 

Claude Code can be excellent at explaining a codebase, right up until it starts speaking fluent _Claudish_: if you’ve coded much with AI, you’ve seen these terms: “load-bearing,” “well-defined seam,” “rough edges worth knowing.”

So, naturally, a developer built [Claudish to English](https://www.reddit.com/r/ClaudeAI/comments/1vl0n1t/claude_code_plugin_for_translating_from_claudish/) to fix exactly that issue. The plugin listens for Claude Code’s displayed messages, sends the output to a local model through [Ollama](https://ollama.com/), then shows a simpler rewrite in your terminal. Claude itself still sees the original, so the translation only changes what _you_ read.

You can also use this to translate selected Markdown files, and if you run the rewrite model locally, your text stays on your machine. [Plus, plugin is free and open source](https://github.com/gvzdv/claudish-to-english)!

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🍪 Treats to Try

1. [Grok Bot](https://x.ai/news/introducing-grok-bot) gives you always-on agents with persistent cloud computers that work across apps and coordinate with other bots —pricing not public.

2. [LTX-2.5](https://ltx.io/model/ltx-2-5) generates consistent multi-shot video with native audio and 4K HDR, and lets you run or fine-tune the open weights on your own hardware —free for organizations under $10M ARR; API from $0.09/sec.

3. [Unsloth Desktop](https://unslothai.substack.com/p/introducing-unsloth-desktop) lets you download, run, and fine-tune 500+ text, vision, audio, and embedding models locally on Windows, macOS, and Linux —free/open-source.

4. [Ploy](https://ploy.ai/) builds, tests, and automatically improves your marketing website, from new landing pages and SEO fixes to visitor identification and outreach (raised $27M) —free plan, then $50/mo.

5. [Mirage](https://mirage.app/) generates and edits layered videos, including expressive avatar performances from an image and audio, and just used the tech for a [Reuters-licensed live news broadcast on X](https://x.com/i/broadcasts/1nJOLQEqZZrxR) —from $0.175/sec via API.

6. [Oumi](http://oumi.ai/) turns your company into a compounding AI factory, where you can build, deploy, and continuously improve specialized models on your own production data while owning the weights, data, and recipes.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/9391b961-6d0a-41b8-9486-0ea97c658865/Screenshot_2026-08-11_at_3.46.31_PM.png?t=1786492400)
Follow image link: (https://www.reddit.com/r/StableDiffusion/comments/1vl3e16/i_used_minimax_to_make_lord_of_the_rings_about_9/)
Caption: I just love dumb stuff like this 

* [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital) partnered with major Wall Street firms on platforms designed to mobilize more than $500B for AI compute infrastructure.

* [Anthropic](https://www.barrons.com/articles/riot-platforms-stock-anthropic-compute-deal-f59f7a15) reportedly signed a $9.1B deal with Riot Platforms for 191 MW of computing capacity from the former Bitcoin miner.

* [Meta](https://www.theguardian.com/technology/2026/aug/11/meta-glasses-banned-from-courts-in-england-and-wales) smart glasses were banned from courts in England and Wales over concerns about covert recording and privacy.

* [Qwen](https://www.reddit.com/r/LocalLLaMA/comments/1vl8bpt/qwen_3827b_coming_this_week/) teased a 27B-parameter Qwen 3.8 open-weight model arriving this week.

* [Modular](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here) released Mojo 1.0, giving its high-performance language for CPUs, GPUs, and AI workloads a stable production release.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

**FROM OUR PARTNERS**

### Free email without sacrificing your privacy

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e681ff8c-20dd-4e60-9c89-1c2af388efa1/05_4__1_.png?t=1776610303)
Follow image link: (https://go.getproton.me/aff_ad?campaign_id=2576&aff_id=12271&aff_type=ho&aff_sub2=Concept5_Static4&aff_sub3=YJ4ZPRQDHV&aff_sub4=Secondary&utm_campaign=us-en-2c-mail-gro_dis-g_acq-mofu_free_beehiiv_test&utm_source=beehiiv.com&utm_medium=dis_ad&utm_term=&utm_ads=Concept5_Static4&_bhiiv=opp_f4d7e10c-31f6-42f2-bee3-40d58a9c2fd1_598ab766&bhcl_id=8003fae5-a160-4daf-9c39-d92cee2931ab_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

Gmail tracks you. [Proton](https://go.getproton.me/aff_ad?campaign_id=2576&aff_id=12271&aff_type=ho&aff_sub2=Concept5_Static4&aff_sub3=YJ4ZPRQDHV&aff_sub4=Secondary&utm_campaign=us-en-2c-mail-gro_dis-g_acq-mofu_free_beehiiv_test&utm_source=beehiiv.com&utm_medium=dis_ad&utm_term=&utm_ads=Concept5_Static4&_bhiiv=opp_f4d7e10c-31f6-42f2-bee3-40d58a9c2fd1_598ab766&bhcl_id=8003fae5-a160-4daf-9c39-d92cee2931ab_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f) doesn’t. Get private email that puts your data — and your privacy — first.

[Ditch the Gmail data grab](https://go.getproton.me/aff_ad?campaign_id=2576&aff_id=12271&aff_type=ho&aff_sub2=Concept5_Static4&aff_sub3=YJ4ZPRQDHV&aff_sub4=Secondary&utm_campaign=us-en-2c-mail-gro_dis-g_acq-mofu_free_beehiiv_test&utm_source=beehiiv.com&utm_medium=dis_ad&utm_term=&utm_ads=Concept5_Static4&_bhiiv=opp_f4d7e10c-31f6-42f2-bee3-40d58a9c2fd1_598ab766&bhcl_id=8003fae5-a160-4daf-9c39-d92cee2931ab_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 📖 Midweek Wisdom

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b4ba87e9-c0b2-4a63-b9ab-714a510fb7c7/Screenshot_2026-08-11_at_4.56.28_PM.png?t=1786492599)
Follow image link: (https://www.dwarkesh.com/p/era-of-continual-learning)
Caption: 

[Dwarkesh Patel is one of AI’s biggest podcasters](https://www.dwarkesh.com/p/era-of-continual-learning), and he’s long argued that **continual learning** (an AI updating its own internal settings from experience, so work today makes it better tomorrow) is a missing ingredient in today’s AI. In his latest video, he asks: **what changes when AI keeps learning after release?**

**Quick LLM 101: **today’s models are mostly **“frozen-weight” models.** _Weights_ are billions of internal settings that tell the model which patterns matter and what words or ideas are likely to come next. Training adjusts them, and after release, they mostly stop changing. So actual continual learning would mean those weights keep updating from experience over time, like an employee learning on the job.

**Here are Dwarkesh's 8 Predictions on how this change will impact the industry:**

* [(0:58)](https://youtu.be/iewm45atodE?si=q6kDBMpG3XnigfQN&t=58) **Safety regulation will need to become continuous.** If the model changes after launch, one pre-release test won’t cut it. Dwarkesh suggests monthly or quarterly checks.

* [(2:02)](https://youtu.be/iewm45atodE?si=q6kDBMpG3XnigfQN&t=122) **Alignment gets harder.** Alignment means keeping AI behavior consistent with human goals. So labs must stop continual evolving models from learning dangerous behavior, jailbreaks, or malicious backdoors.

* [(3:04)](https://youtu.be/iewm45atodE?si=q6kDBMpG3XnigfQN&t=184) **AI minds will diversify.** Different real-world experience could make even identical starting models diverge, _kinda like us humans_. _So no more AI group-think (which would really help my LinkedIn Feed TBH)! _

* [(3:53)](https://youtu.be/iewm45atodE?si=q6kDBMpG3XnigfQN&t=233) **Leaders will pull away faster.** A better evolving model → more users → more experience → better model. _Small leads could compound._

* [(4:12)](https://youtu.be/iewm45atodE?si=q6kDBMpG3XnigfQN&t=252) **Labs will ship sooner**. If usage itself improves the model, keeping your best model private gives competitors more learning time.

* [(4:38)](https://youtu.be/iewm45atodE?si=q6kDBMpG3XnigfQN&t=278) **Switching models gets painful.** Leaving an AI that spent 18 months learning your company could feel like replacing a veteran employee with a brand-new intern. _There’s gotta be a simple solution to this IMO. _

* [(5:56)](https://youtu.be/iewm45atodE?si=q6kDBMpG3XnigfQN&t=356) **Labs may subsidize training access**. Labs could offer cheaper AI for training access, while reserving better models for customers who opt in.

* [(6:52)](https://youtu.be/iewm45atodE?si=q6kDBMpG3XnigfQN&t=412) **Personalized AI favors big organizations**. AI runs more efficiently when many requests are processed together, called _batching_. Big companies can do that; individuals cannot. Dwarkesh says the efficiency gap could exceed **100X**.** **_So what if Neoclouds or Apple offer private batching on private servers? Open weight evolving AI could still thrive. _

**The big idea here**: if (or when) this happens, continual learning will transform AI models from software you buy into something closer to **an employee you develop**. That changes safety, competition, privacy, pricing, and lock-in.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron:

[NVIDIA’s Nemotron 3.5 Lightning](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4) and [NeMo Switchyard](https://github.com/NVIDIA-NeMo/Switchyard) are two new open AI tools that make the case for running routine agent work locally, then routing tougher tasks to stronger models when needed. [Read our full review here.](https://www.theneuron.ai/news/nvidia-nemotron-lightning-switchyard-review-local-first-ai-agents/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f3f8aba7-d930-4b04-8d71-a53727ac59ff/A_Cat_s_Commentary_x_2025__75_.png?t=1785898027)
Caption: This was a packed to the point review! 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today! 




**Btw: **We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**[Subscribe to our YouTube Channel](https://www.youtube.com/@theneuronai?sub_confirmation=1)** for free live tutorials and AI industry interviews. 

**P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/openai-claude-and-gemini-s-reasoning-got-cracked
