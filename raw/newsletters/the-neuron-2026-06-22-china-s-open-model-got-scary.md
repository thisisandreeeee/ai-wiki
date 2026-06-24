---
source: gmail
newsletter: "the-neuron"
message_id: "19eef0233c5407e0"
thread_id: "19eef0233c5407e0"
subject: "😺 China's open model got scary"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Mon, 22 Jun 2026 11:05:45 +0000 (UTC)"
ingested: 2026-06-24
sha256: 2543d15c342b2b5a815e8a4382807b480be71260cd28d4a4a5cb6cbdd7be7e50
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/791c8227-b7f0-47df-9db6-6a8dcba8f5dc/Untitled_design__14_.png?t=1782115580)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8279103c-f666-467a-a9bc-81b64d64b260/In_Partnership_with_Google_for_Startups.png?t=1775816894)
Follow image link: (https://cloud.google.com/resources/content/future-of-ai-genmedia?utm_source=gfs&utm_medium=newsletter&utm_campaign=FY26-Q2-GLOBAL-GCP40293-website-dl-StartupGenMedia-168368&utm_content=neuron3)
Caption: 

Welcome, humans. 

So last week, the open-model crowd (people who like AI they can run and modify themselves) got a very loud new toy: [GLM 5.2](https://z.ai/blog/glm-5.2), a new Chinese open-weights model (an AI model where the weights, a.k.a the huge set of numbers that determine how the AI runs, are published so anyone can run the model themselves). People are already running it on their own cloud instances, testing it in coding tasks, and comparing it against frontier APIs (top paid model services).

The fun part is that this is not any old benchmark flex. You can hit it through an API (call it from your own software), download the weights (copy those numbers onto your own machine), quantize it (make those numbers smaller and simpler so the model uses less memory), fine-tune it (retrain the model a bit for a specific job), or run it locally if your desk has enough GPU chips to qualify as a space heater. It's a very big deal… more below!

**Here’s what happened in AI today: **

* 😺 Z.ai released GLM 5.2, an open-weights model with 1M-token context and strong long-horizon coding results.

* 📰 Cursor made it easier to move local coding agents into isolated cloud VMs.

* 🍪 HumanLayer launched an agentic IDE and collaboration platform for engineering teams.

* 🎓️ Record a Task Once, Have Codex Solve it

…and a **[whole lot more that you can read about here](https://www.theneuron.ai/explainer-articles/-everything-that-happened-in-ai-today-friday-june-19-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=deepmind-mapped-ai-agent-controls&_bhlid=212610c34104d9f0b7f36220cea9c32197ed77c9)**.

**Hey: **_Want to reach 700,000+ AI-hungry readers? _[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[ ](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.S: **_Love robots? We’re starting a new robotics newsletter! _[Sign up early here](https://form.jotform.com/260897013570156).

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😺** GLM 5.2 is the open model that made frontier AI feel less closed**

Open models usually get described like thrift-store frontier AI: cheaper, useful, and maybe a little behind. GLM 5.2 is testing that assumption.

[Z.ai](https://Z.ai)['s GLM 5.2](https://z.ai/blog/glm-5.2) is an open-weights model (the weights are downloadable, so builders can run, modify, quantize, or fine-tune it instead of only renting an API). The release has 1M-token context, which means it can take in huge codebases, long research files, or whole project histories in one prompt.

**Here's what happened:**

* Z.ai released GLM 5.2 through its blog, Hugging Face, docs, and OpenRouter access.

* The model is being tested as a long-horizon coding and agent model, especially for tasks that need lots of context.

* Developers have already shown it running locally with MLX on two M3 Ultra Mac Studios.

* Early comparisons put it in the conversation with much pricier closed models on coding, physics-simulation, and reasoning tasks.

* [A LocalLLaMA thread](https://www.reddit.com/r/LocalLLaMA/comments/1u96jof/glms_founder_says_glmfable_before_the_end_of_the/) also circulated a claimed GLM-Fable roadmap tease before year-end, which is worth treating as community chatter unless Z.ai posts it directly.

**How to try it:**

* [API route: try it on OpenRouter](https://openrouter.ai/z-ai/glm-5.2) before touching local setup.

* [Builder route: download the weights on Hugging Face](https://huggingface.co/zai-org/GLM-5.2) if you want to quantize, distill, or fine-tune it.

* [Docs route: read ](https://docs.z.ai/guides/llm/glm-5.2)[Z.ai](https://Z.ai)['s guide](https://docs.z.ai/guides/llm/glm-5.2) for context-window and deployment details.

**Why this matters:**

The real story is optionality. Closed models are convenient, but they can change price, access, policy, or performance without warning. Open weights let teams keep more control over where the model runs, what data touches it, and how deeply they customize it.

GLM 5.2 also changes the cost conversation. Scaling01 highlighted GLM 5.2 at roughly $4.40 per million output tokens, far below many frontier flagship prices. If the quality is close enough, developers start asking a dangerous question: which tasks actually need the expensive model?

That is why the local demos matter. A model you can run, inspect, and route around gives teams leverage. It turns model choice from a vendor dependency into an architecture decision: expensive flagship for the hardest calls, cheaper open model for repeatable work, and local deployment when data cannot leave the building.

**Our take:**

GLM 5.2 probably will not make people cancel every closed-model subscription. It does make the default less obvious. The next AI stack may use frontier models for the hardest work and open models for everything else, especially when privacy, cost, or customization matters.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS **

# **Ready to move beyond single-point tools?**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/10fd5f62-ea9f-49d3-a89f-73d07384996a/GFS_Future_of_AI_LinkedIn_1920x1080__7_.png?t=1781799775)
Follow image link: (https://cloud.google.com/resources/content/future-of-ai-genmedia?utm_source=gfs&utm_medium=newsletter&utm_campaign=FY26-Q2-GLOBAL-GCP40293-website-dl-StartupGenMedia-168368&utm_content=neuron3)
Caption: 

The 2026 ‘Future of AI: Perspectives on generative media for startups’ report launched at [Google Cloud](https://cloud.google.com/resources/content/future-of-ai-genmedia?utm_source=gfs&utm_medium=newsletter&utm_campaign=FY26-Q2-GLOBAL-GCP40293-website-dl-StartupGenMedia-168368&utm_content=neuron3) Next and reveals the strategies startups need to navigate the next era of generative media.

Dive into end-to-end agent workflows, post-keyboard interfaces, and deeply personalized content. Leverage your authentic human taste as the ultimate defensible moat.

[Get the report](https://cloud.google.com/resources/content/future-of-ai-genmedia?utm_source=gfs&utm_medium=newsletter&utm_campaign=FY26-Q2-GLOBAL-GCP40293-website-dl-StartupGenMedia-168368&utm_content=neuron3)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 **AI Skill of the Day: ****Record a Task Once, Have Codex Solve it**

You know that one annoying work task you keep explaining to AI like it has short-term memory loss? OpenAI’s new[ Record & Replay](https://developers.openai.com/codex/record-and-replay) for Codex is built for exactly that.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/043fcd09-839e-4056-8a90-1f7af92296ab/image.png?t=1782110840)
Follow image link: (https://x.com/OpenAIDevs/status/2067681320281723113)
Caption: 

The skill: show Codex a recurring workflow once, then turn that demo into a reusable skill, basically a saved set of instructions Codex can run again later. Think filing an expense report, submitting PTO, creating a correctly configured issue, publishing a video, or downloading the same report every Monday.

Here’s how to use it, if you have access on macOS with Computer Use enabled:

1. Open **Plugins** in the Codex app.

2. Hit the **+** menu and select **Record a skill**.

3. Tell Codex your goal and what inputs may change later.

4. Approve recording, perform the workflow, then stop recording when the task is complete.

5. Ask Codex to refine the skill with your naming rules, defaults, and “please don’t click that cursed dropdown” preferences.

_Favorite detail: the final skill is inspectable and editable, so you get a reusable workflow, not a mystery macro hiding in the walls._

```
I’m about to record a reusable Codex skill.


Goal: [describe the recurring task]
Use this skill when: [when Codex should run it]
Inputs that may change each time: [dates, files, names, links, report ranges, etc.]
Success criteria: [how Codex should know the workflow is complete]
Hidden preferences to preserve: [naming rules, default fields, formatting choices, decision points]

Do not record or reuse: [passwords, secrets, private data, unrelated cleanup steps]
After the recording, draft the skill and ask me what needs to be refined before I reuse it.
```
**Total AI beginner? **[Start here](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/) ([goes with this video](https://www.youtube.com/live/QbFU0UNMVaU?si=skJsgUIDjKjAx3DU)).  

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform) 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🍪 **Treats to Try **

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6df9c346-7360-488b-ace0-d3ddc691d058/AI_Image-Dell-Pro-Max-AI-PC-with-GB10__1_.png?t=1780507718)
Follow image link: (https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro/xcto_fcm1253_usx?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-gemini-got-hijacked-via-whatsapp&_bhlid=12c8b81efdc50f09801aab3f48d885ef8a39d3c3)
Caption: 

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

1. *Your AI roadmap needs a test course. The [Dell Pro Max with GB10](https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro/xcto_fcm1253_usx?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-gemini-got-hijacked-via-whatsapp&_bhlid=12c8b81efdc50f09801aab3f48d885ef8a39d3c3) helps teams experiment before making bigger bets.

2. [HumanLayer](https://www.humanlayer.com/) gives engineering teams task management, versioned artifacts, and human-agent collaboration for implementation work - free for small teams, then $100/user/month Pro.

3. [pool](https://github.com/poolsideai/pool) gives developers a terminal and editor coding agent with ACP editor support, slash commands, MCP tools, and rewind - open source.

4. [ML Intern](https://x.com/_lewtun/status/2067614409678020999) automates the post-training research loop across papers, datasets, GPU sandbox training, evals, and iteration - no pricing details.

5. [Open Design](https://github.com/nexu-io/open-design) gives designers a local-first canvas for BYOK editing, design-system plugins, and code handoffs - open source.

6. [Lore](https://lore.org/) gives binary-heavy teams a content-addressed version-control system with deduplication and sparse workspace hydration - open source.

7. [Retool](https://retool.com/blog/retool-launches-react-ai-app-builder) lets teams build internal apps in Claude Code, Codex, Replit, Lovable, or Retool, then ship them through one governed runtime - free app hosting through July 1.

8. [LM Studio](https://x.com/lmstudio/status/2067301278976180531) previewed private frontier-scale inference streamed from four Mac Studios to a MacBook and iPhone - no pricing details.

9. [xAI Grok TTS](https://x.com/xai/status/2067654108123910495) topped Vapi's blind voice-model humanness leaderboard at 96 out of 100 - no pricing details.

10. [Cua](https://github.com/trycua/cua) runs background Linux computer-use agents that can operate desktop apps through CLI or MCP - open source.

11. [Hyperagent](https://x.com/hyperagentapp/status/2067631028328419492) turns video, dashboards, and daily briefs into generated agentic demos - no pricing details.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# Trending: FOUR popular Neuron podcast eps…

Did you know we have a podcast (_The Neuron: AI Explained)_ where we talk to fascinating people in the industry who teach us how it actually works?  Check it out: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ba00aebe-a1b9-4651-b3fa-78bc48fd4d66/Screenshot_2026-04-27_at_10.18.22_AM.png?t=1777310341)
Follow image link: (https://www.youtube.com/@theneuronai/videos)
Caption: Click to view these episodes on YouTube!

New episodes air **every week** on: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)** **

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn 

* [Cursor](https://x.com/cursor_ai/status/2067366343817805899) made local agents easier to move into the cloud so coding work can continue after a laptop closes.

* _[Sen. Mark Warner](https://www.techtimes.com/articles/318783/20260621/claude-fable-5-resurfaces-android-app-nsa-breach-testimony-reshapes-ban.htm)_ said the NSA’s director told him Anthropic’s Mythos model broke into almost all of the agency’s classified systems in hours during an authorized red-team test, reframing the US export ban around offensive capability rather than a single jailbreak.

* _[Google](https://www.techtimes.com/articles/317919/20260606/google-gemini-35-pro-nears-june-launch-2-million-token-context-deep-think-reasoning.htm)_’s Gemini 3.5 Pro — promised for June with a 2M-token context window and a Deep Think mode — still hadn’t shipped with about 10 days left, keeping prediction markets near 50-55% on a pre-July release.

* _[Amazon](https://variety.com/2026/film/global/luca-guadagnino-sam-altman-movie-artificial-dropped-amazon-1236785830/)_ shelved Luca Guadagnino’s nearly finished Sam Altman biopic “Artificial,” months after its $50 billion OpenAI partnership.

* _[The Reuters Institute](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/dnr-executive-summary)_ reported that weekly use of AI chatbots for news climbed from 7% to 10% globally, even as only about 4% of users clicked through to the original source.

* [Kimmonismus](https://x.com/kimmonismus/status/2067345637201543311) argued that access-cutoff risk is pushing companies and governments toward sovereign open models.

* [Mahi Shafiullah](https://x.com/notmahi/status/2067640872272073089) introduced a robot-learning method that maps chaotic human videos to dexterous robot actions.

* _[L’Oréal](https://www.eweek.com/news/chatgpt-maybelline-try-on-emea-france)_ teamed up with OpenAI to put Maybelline’s virtual makeup try-on tool inside ChatGPT, unveiled at VivaTech 2026.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

**FROM OUR PARTNERS **

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/11898a79-a19b-49b6-8cb2-34281f8e81ff/wethosai-neuron-webinar-image_v02.png?t=1781816414)
Follow image link: (https://us02web.zoom.us/webinar/register/7817816347644/WN_qfpj4V14SxyPxtmTvdBObw)
Caption: 

Generic LLMs displace jobs. The future still belongs to augmented humans. [WethosAI makes you irreplaceable.](https://us02web.zoom.us/webinar/register/7817816347644/WN_qfpj4V14SxyPxtmTvdBObw) Join CEO Stuart McClure this Thursday, June 25, to watch live how System 3 Thinking and Cognitive Twins will upskill your workforce, protect your career, and safeguard your business. All demo. No filler.** **

[Register Free](https://us02web.zoom.us/webinar/register/7817816347644/WN_qfpj4V14SxyPxtmTvdBObw)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 📖 Monday Meme

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4751076e-a924-4ef5-bc55-a2eedd56863b/Screenshot_2026-06-18_at_2.26.26_PM.png?t=1781818337)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6e738d89-2859-420d-a73e-ccf2e8cb196f/Screenshot_2026-06-18_at_2.27.45_PM.png?t=1781818337)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7fc0c7fa-ca2e-4760-901a-beb1d1dde071/Screenshot_2026-06-18_at_2.36.57_PM.png?t=1781818698)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# A Cat’s Commentary 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/21f71f14-b8d4-4756-8a08-b0bdbba90284/A_Cat_s_Commentary_x_2025__46_.png?t=1781818795)
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
https://www.theneurondaily.com/p/glm-5-2-brings-1m-context
