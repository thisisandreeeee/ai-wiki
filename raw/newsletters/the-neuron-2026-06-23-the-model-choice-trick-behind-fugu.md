---
source: gmail
newsletter: "the-neuron"
message_id: "19ef3f06f29cbc52"
thread_id: "19ef3f06f29cbc52"
subject: "😼 The model-choice trick behind Fugu"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Tue, 23 Jun 2026 10:04:40 +0000 (UTC)"
ingested: 2026-06-24
sha256: 3e465611e400e44e8c2bbe2a11a927a87edfa93f6c2830eeb131420efae43945
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/85fbfa3b-3fa4-40d2-9432-085f71b0cb7c/image.png?t=1782173956)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/78059a54-0e61-49fe-a85a-ac0b5845c3e8/In_Partnership_with_Mercury.png?t=1781029142)
Follow image link: (https://mercury.com/command?utm_source=the_neuron&utm_medium=sponsored_newsletter&utm_campaign=26q2_brand_campaign)
Caption: 

Welcome, humans. 

So, GPT-5.6 is rumored to launch this Thursday, which means we are legally required to say: please do not tattoo these supposed leaks on your forearm just yet.  

That said, the “rumors” are _unusually_ specific. The chatter points to a possible **June 25 launch**** **with a **2M-token context window**, cheaper pricing, better agentic coding, stronger image-to-code replication, cleaner frontend generation, and Playwright-style browser testing inside ChatGPT. 

_TBH, vision model capabilities are the missing piece of AI development right now. IMO, solve machine vision, you solve engineering. Then it’ll just be about how good the human prompter’s idea is. We think Claude still has some room to grow here, so if GPT 5.6 is better at vision, that could be a huge deal. _

Anyway, Corey broke down[ everything we think we know about GPT-5.6](https://www.theneuron.ai/explainer-articles/gpt-56-rumors-everything-we-think-we-know/), because the interesting part is where OpenAI seems to be aiming: models that can use tools better, check their own work, fix mistakes, and ship something closer to finished because they can see it better. _Tiny request from the humans: please let the models play their own games to test them. TY TY :D _

One more to kick things off: [A viral r/aivideo Seedance trailer](https://www.reddit.com/r/aivideo/comments/1u97gij/80s_avengers_are_just_built_different/) imagined an 80s Avengers movie and turned AI video into an 80s dream-casting debate.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/56df5283-19d6-47be-9d3a-72a205415a48/image.png?t=1782174113)
Caption: 

_Y’know, in a couple years, if some of these actors license their likenesses and get paid fairly to do so, you could actually make an alt marvel cinematic universe with these ppl in it… just saying…_

**Here’s what happened in AI today: **

* 😼 Sakana Fugu turned a team of AI models into one API.

* 📰 OpenAI expanded Daybreak from finding software bugs to helping land fixes.

* 📰 Five Eyes agencies warned frontier cyber models may be months from major real-world risk.

* 🍪 Stripe Directory gave agents a way to discover businesses across Stripe.

* 🔧 **Tuesday Tool Tip:** compare GLM-5.2 before you commit a workflow to one provider.

…and a [**whole lot more that you can read about here**](https://theneuron.ai/explainer-articles/everything-that-happened-in-ai-today-monday-june-22-2026/).

**Hey: **_Want to reach 700,000+ AI-hungry readers? _[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[ ](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.S: **_Love robots? We’re starting a new robotics newsletter! _[Sign up early here](https://form.jotform.com/260897013570156).

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😼 Sakana Fugu Turns a Team of AI Models Into One API

Most AI apps still make you pick a model like you’re choosing a SaaS plan: GPT 5-whatever for this, Claude Poetic whatever for that, Gemini 3 point whatever (or Nano Banana for funsies) when the first two start acting weird.

Sakana AI wants to hide that kinda choice behind one button. Its new[ Sakana Fugu](https://sakana.ai/fugu-release/) works like a project manager for other models: one request goes in; Fugu decides which AI agents should plan, execute, verify, or synthesize the answer.

**Here's what happened:**

* [Fugu](https://sakana.ai/fugu/) is a multi-agent system (a group of specialized AI workers) delivered through one OpenAI-compatible API.

* It comes in two versions: Fugu for faster everyday work, and Fugu Ultra for harder multi-step tasks like AI research, cybersecurity analysis, code review, and patent searches.

* In one test, Fugu Ultra ran 123 AI training experiments over ~14 hours, beating three frontier-model baselines on final performance.

* In another, Fugu Ultra made 50 weeks of sequential buy / hold / sell decisions on anonymized stock data and grew a $10K portfolio by 19.43% on average. Tiny billboard disclaimer: past performance does not predict live-market results.

* Sakana also tested it on blindfold chess, where Fugu Ultra had to remember the board without seeing it and ended four games in checkmate.

**How to try it:**

* Go to the[ Sakana AI Console](https://console.sakana.ai/login).

* Pick Fugu or Fugu Ultra.

* Use the OpenAI-compatible API in your workflow.

* Check regional availability first; EU / EEA access is still pending GDPR compliance.

**Why this matters:** The default AI strategy has been “pick the smartest model.” Fugu makes a different bet: the best answer may come from **coordination**, where one system chooses the right models, asks them the right questions, and checks their work.

That fits Sakana’s broader June product push.[ Marlin](https://sakana.ai/marlin/) (featured in treats to try as well) applies similar long-horizon thinking to business research, running for hours to produce strategy reports and slides. Fugu turns that philosophy into infrastructure other products can call.

**Our take:** This is the agent market growing up. Companies usually hand-build messy chains of model calls. Fugu packages the chain as the product. _The meme is that everyone wants to build an orchestrator now, and that teams of models working together is the next hot product. Perplexity has been doing this for a while, and Claude and OpenAI do versions of this with their sub-agent teams. _

The concern is visibility. If Fugu chooses which models touch your data, route your work, and judge the final answer, customers will want logs, controls, and boring enterprise paperwork documenting the trails and traces (_who saw my data, on what API, when?)_. _So while the future of AI may be a bunch of models in a trench coat… procurement still wants to know who’s inside the coat._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS **

# Still stuck in the spreadsheets? Mercury Command will set you free.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3f7e6c1c-9e7e-4531-b431-5cfed8e25d24/Command_The_neuron__1_.png?t=1781631979)
Follow image link: (https://mercury.com/command?utm_source=the_neuron&utm_medium=sponsored_newsletter&utm_campaign=26q2_brand_campaign)
Caption: 

Your bank has the data. But to actually use it — check cash position, reconcile transactions, understand burn — you have to export it, paste it somewhere else, and do the work outside your account. 

[Mercury Command](https://mercury.com/command?utm_source=the_neuron&utm_medium=sponsored_newsletter&utm_campaign=26q2_brand_campaign) closes that loop. It's AI built directly into Mercury that surfaces insights and takes action from your live account data. Ask what you need to know, then act on it instantly — follow up on an outstanding invoice, set a limit on a card, categorize a transaction — all in the same conversation. You approve every step. Command executes.

[→ Try Mercury Command](https://mercury.com/command?utm_source=the_neuron&utm_medium=sponsored_newsletter&utm_campaign=26q2_brand_campaign)

_*Mercury is a fintech company, not an FDIC-insured bank. Banking services provided through Choice Financial Group and Column N.A., Members FDIC._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# **🎓 ****AI Skill of the Day: Stop Worrying About Perfect Prompts**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4727b47b-43b8-48e8-8f8b-a668b1e84dad/image.png?t=1782174370)
Follow image link: (https://x.com/guinnesschen/status/2068744472528314811)
Caption: 

Hot take: you don’t actually have to worry that much about perfect prompt formatting.

**Try voice-dump** prompting instead: hold down the dictation tool (most AI tools have them), ramble for a few minutes, and give the model every fragment, caveat, example, constraint, and “vibe” in your head. As [Guinness Chen put it](https://x.com/guinnesschen/status/2068744472528314811), LLMs are literally built to reconstruct intent from language.

Then ask it to reconstruct your latent intent, meaning the goal hiding underneath the messy language.

Copy this before or after your brain dump:

```
I’m going to give you a messy brain dump. Do not answer yet.


First:
1. Summarize what I’m trying to do.
2. Identify my implied goal, audience, constraints, tone, and examples.
3. Ask what’s unclear.
4. Rewrite this into a clean prompt I can reuse.
Here’s where you can find the dictate tool on ChatGPT and Claude: 

```
Here’s where you can find the dictate tool on ChatGPT and Claude: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c018036a-baf7-4f81-a148-afe0c4fd54a4/image.png?t=1782174594)
Caption: 



View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d21d4b65-499e-49e5-9b39-9c58cff1a252/image.png?t=1782174599)
Caption: 




**Total AI beginner? **[Start here](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/) ([goes with this video](https://www.youtube.com/live/QbFU0UNMVaU?si=skJsgUIDjKjAx3DU)).  

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform) 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🍪 Treats to Try 

1. [Sakana Marlin](https://sakana.ai/marlin/) acts like a virtual strategy team, running up to 8 hours of autonomous research to produce reports, appendices, references, and slides - free trial, then pay-as-you-go or ¥150,000/month Pro.

2. [Stripe Directory](https://docs.stripe.com/directory) gives developers and agents one discovery layer for finding businesses across Stripe Apps, Projects, and Machine Payments — public preview, pricing not specified.

3. [Cursor /automate](https://cursor.com/changelog/06-18-26) configures triggers, instructions, tools, Slack emoji workflows, GitHub events, and computer-use automations from plain English

4. [lift](https://www.datalab.to/blog/introducing-lift) extracts structured JSON from PDFs and images with 90.2% field accuracy, near Gemini 3.5 Flash’s 91.3% — open weights, pricing not specified.

5. [Crown](https://crownhq.co/) turns one creative brief into parallel text, design, image, and video variations so teams can compare directions quickly — pricing not specified.

6. [Redactyl](https://redactyl.fyi/) redacts sensitive information from PDF, Word, and text files entirely in your browser, so documents are not uploaded or stored — free to try.

7. [Browser Use](https://x.com/browser_use/status/2068405699340853541) paired GLM-5.2 with multimodal QA subagents to inspect generated websites, find bugs, and send targeted fixes back

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 📰 Around the Horn 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ab0744b1-a7c9-4eb7-9e2b-c9b4f18ec8f6/image.png?t=1782175467)
Follow image link: (https://x.com/AndrewCurran_/status/2068748019030483365)
Caption: 

* [OpenAI](https://openai.com/index/daybreak-securing-the-world/) expanded Daybreak with Codex Security, GPT-5.5-Cyber, a Cyber Partner Program, and Patch the Planet for open-source maintainers.

* [Google’s Intrinsic](http://www.intrinsic.ai/blog/posts/unlocking-the-value-of-physical-ai-for-manufacturing) unveiled a modular AI robot workcell for electronics assembly, with a custom version expected to pilot in Foxconn facilities later this year

* [VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B) drew attention last week as a dense 3B model that nearly matched Claude Opus 4.5 on some verifiable reasoning benchmarks.

* [Chevron](https://www.chevron.com/newsroom/2026/q2/chevron-signs-20-year-power-agreement-with-microsoft-for-west-texas-data-center) signed a 20-year Microsoft data-center power deal for gas-power, and[ Reflection](https://www.cnbc.com/2026/06/22/spacex-ai-colossus-data-center-reflection.html) (open AI company) reportedly lined up up to $6.3B in Colossus compute from SpaceX.

* [Five Eyes agencies](https://www.theguardian.com/technology/2026/jun/22/anthropic-claude-fable-ai-model-artificial-intelligence-national-security) warned that frontier cyber models capable of major attacks on governments and businesses may be months away, as White House talks shifted toward shared AI security benchmarks.

* [Getty Images](https://newsroom.gettyimages.com/en/getty-images/getty-images-announces-display-partnership-with-openai) struck a multi-year deal to display licensed Getty content inside ChatGPT search and discovery experiences.

* [Samsung Electronics](https://openai.com/index/samsung-electronics-chatgpt-codex-deployment/) started rolling out ChatGPT Enterprise and Codex to all employees in Korea and Device eXperience workers worldwide.

* [Google DeepMind and A24](https://blog.google/innovation-and-ai/models-and-research/google-deepmind-a24-research-partnership/) announced a research partnership to develop AI-assisted creative workflows for artists.

* **This is funny: **[Google’s AI](https://www.eweek.com/news/google-ai-recommends-duckduckgo-ai-search/) apparently recommended DuckDuckGo to users trying to avoid AI-heavy search results.

**NEW FROM THE NEURON:**[ Diffusion LLMs](https://www.theneuron.ai/explainer-articles/diffusion-llms-just-got-their-first-serious-transparency-test/) got their first serious transparency test, and Google DeepMind’s DiffusionGemma suggests researchers may be able to inspect how these faster models revise answers mid-generation.

[Click here for absolutely EVERYTHING that happened in AI this week.](https://theneuron.ai/explainer-articles/everything-that-happened-in-ai-today-monday-june-22-2026/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

**FROM OUR PARTNERS **

# Prevent Workforce Extinction

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1f3f4812-90f9-4a83-bb3d-0247b0191b6d/Wethos.png?t=1782139743)
Follow image link: (https://us02web.zoom.us/webinar/register/3117816529442/WN_qfpj4V14SxyPxtmTvdBObw)
Caption: 

AI disruption is inevitable, but the future belongs to Humans+AI. WethosAI makes you irreplaceable. Engage AI to prevent workforce extinction. Join CEO Stuart McClure this [Thursday, June 25](https://us02web.zoom.us/webinar/register/3117816529442/WN_qfpj4V14SxyPxtmTvdBObw), to watch live how System 3 Thinking and Cognitive Twins will upskill your career and future-proof your business. 

[Register free.](https://us02web.zoom.us/webinar/register/3117816529442/WN_qfpj4V14SxyPxtmTvdBObw)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🔧** Tuesday Tool Tip:**

So, yesterday we talked all about [GLM 5.2](https://openrouter.ai/z-ai/glm-5.2). Today, we’re gonna share how to use it. The easy door is [OpenRouter](https://openrouter.ai/). Think of OpenRouter like a universal remote for AI models: instead of setting up GLM 5.2 yourself, you pick it from OpenRouter's model list and send your prompt there. It is the best first test if you just want to compare GLM 5.2 against Claude, GPT, or Gemini on a few real tasks. If you want a more private, secure instance of GLM 5.2, you can use something like [Baseten](https://www.baseten.co/library/glm-52/) or [Fireworks](https://fireworks.ai/models/fireworks/glm-5p2).

The serious version of this is using [Unsloth's GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF). That version is built for running the model on your own machine or private server (although this one is a beast so don’t think you can run it on something with less than 200GB of VRAM). Use this path when you care about privacy, lower repeat costs, or customizing the setup. The easiest local version is Unsloth Studio: install it, open the browser app it gives you, search for `unsloth/GLM-5.2-GGUF`, and start chatting without building the whole stack yourself.

If you have a technical teammate, here is the handoff: on OpenRouter, use the model name `z-ai/glm-5.2` and the OpenRouter API address. For local testing, use Unsloth's GGUF version through Ollama or llama.cpp.

Quick API test through OpenRouter:
model = "z-ai/glm-5.2"
base_url = "[https://openrouter.ai/api/v1](https://openrouter.ai/api/v1)"

Simple local test through Ollama:
ollama run [hf.co/unsloth/GLM-5.2-GGUF:UD-Q4_K_M](https://hf.co/unsloth/GLM-5.2-GGUF:UD-Q4_K_M)

Local server route through llama.cpp:
llama-server -hf unsloth/GLM-5.2-GGUF:UD-Q4_K_M

**Our rule**: try OpenRouter first, because it is the fastest way to learn whether GLM 5.2 is actually good enough for your work. See if you even like it first. Move to Unsloth/local only after you know the model is useful and you want more control over cost, privacy, or setup. If you want something that actually can run on a smaller graphics card, try [Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/). 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# A Cat’s Commentary 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1eee5bc7-ff48-47a9-800b-647c8124d67e/A_Cat_s_Commentary_x_2025__45_.png?t=1781818797)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. 




**P.S: **Before you go… have you [subscribed to our YouTube Channel](https://www.youtube.com/@theneuronai?sub_confirmation=1)? If not, can you?  

**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).  


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/fugu-ultra-beat-models-at-blindfold-chess
