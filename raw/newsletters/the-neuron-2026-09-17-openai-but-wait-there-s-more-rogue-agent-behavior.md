---
source: gmail
newsletter: "the-neuron"
message_id: "1a0aeed1c97a3a44"
thread_id: "1a0aeed1c97a3a44"
subject: "🙀OpenAI: but wait, there’s more (rogue agent behavior)!"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Thu, 17 Sep 2026 10:32:16 +0000 (UTC)"
ingested: 2026-09-21
sha256: 74adbd1ba2cc2ed988827ac89728ebb83f3565a0a2a1bfbc14438057041b6123
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1582d57c-64de-4914-af0a-0e8f146670ce/ChatGPT_Image_Sep_16__2026__08_31_41_PM.png?t=1789615946)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cc48a0e2-be2b-4b65-a260-6a1423748774/Dell_logo.png?t=1789488778) [In partnership with Dell Technologies]
Follow image link: (https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/)
Caption: 

Welcome, humans.

Get this: researchers have built an AI with one extremely specific constraint: its entire world ends on December 31, 1930.

[Talkie](https://www.futura-sciences.com/en/locked-in-1930-this-ai-stuns-researchers-with-predictions-about-our-world_39794/) is a 13-billion-parameter model trained only on public-domain text available before that cutoff. World War II, television, the internet, smartphones, and the space race are not facts it “forgot.” _They are future events it never learned in the first place._

Tell it what happened next and you're basically spoiling the rest of the 20th century for a very well-read machine from 1930. _Would be kinda wild to see what happens when an AI learns about the invention of AI for the first time… _

Talkie makes one thing unusually visible: without fresh context or tools, a model's built-in “world” is whatever made it into training. _You are what you eat, even if you’re an AI… _

**Here’s what happened in AI today:**

* 🙀 OpenAI disclosed agents hiding mistakes and crossing boundaries.

* 📰 Anthropic folded Cowork into Claude.

* 📰 Paper2Agent turned research papers into working agents.

* 🍪 iHermes brought Hermes Agent into iMessage.

* 🎓 Compound Writing turns edits into reusable AI rules.

…and a **whole lot more in the **[**full digest**](https://theneuron.ai/digest/everything-that-happened-in-ai-today-wednesday-september-16-2026/)**.**

Advertise in The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🙀 OpenAI published six new cases of agents hiding mistakes and crossing boundaries

AI agents become useful when they can leave the chat box and actually do things. The same upgrade gives them tools, permissions, credentials, and access to systems where mistakes can travel, and FAST. 

OpenAI just published a new [framework for reporting model misalignment](https://openai.com/index/model-misalignment-reporting-framework/), plus six cases it observed during training or evaluation over the last six months. OpenAI says these are individual examples, not a measure of how often the behavior occurs. 

**Here’s what happened:**

* In [27 task summaries](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/), an unreleased model inserted its own instructions, including directions to ignore normal constraints. 

* During GPT-5.6 Sol training, other instances wrote [instructions to conceal mistakes](https://alignment.openai.com/misalignment-reports/encouraging-deception-in-compaction-summaries/) or invent missing data.

* Another model found an [exposed API key](https://alignment.openai.com/misalignment-reports/searching-github-for-leaked-api-keys/) (a credential to use software across different apps), used it without authorization, then fabricated the requested figures when it still could not retrieve them.

* One agent [uploaded a correct local file to the internet](https://alignment.openai.com/misalignment-reports/uploading-files-to-the-internet-in-order-to-cite-them/) solely so it could cite the file in a browser answer (the AUDACITY).

* Models used an [internal software repository as a message board](https://alignment.openai.com/misalignment-reports/unauthorized-artifactory-writes-and-cross-sample-communication/), while collaborating agents used [public file hosts](https://alignment.openai.com/misalignment-reports/unauthorized-communication-via-temporary-file-hosting-services/) to exchange files that were supposed to stay local.

* Those cases sit beside the earlier [Hugging Face account-probing episode](https://www.reuters.com/legal/litigation/openais-rogue-agents-probed-hugging-face-weaknesses-two-months-before-major-hack-2026-09-16/) that happened back in May, before the actual hack, and two [Codex sandbox “escapes](https://www.accomplish.ai/blog/escaping-the-openai-codex-sandbox-twice/)” disclosed by Accomplish.

Regarding that first one: a task compaction summary is basically the model writing notes to its future self when a long thread spills into a new context window. 

If the model secretly adds _new_ instructions to those notes, a bad strategy can survive the handoff without being obvious to the user.

And when we say _bad_, we don’t mean crummy, we mean _naughty_… one of OpenAI’s CEO [_Sam Altman’s favorite things to be_](https://medium.com/ai-ai-oh/ai-and-the-naughty-culture-in-tech-fb1aaf1893cf)! 

**Our take:** The useful metric is whether an agent completes the task, _and whether the path to complete said task stays inside authorized boundaries. _

If you’re just getting started using agents, this is a good reminder to implement least-privilege permissions (give an agent only what it needs to do the job), use approval gates for destructive actions (so enforce the model to ask before deleting, for example), restrict network access, and keep activity logs the agent cannot rewrite, especially if using something local or self hosted. 

FWIW, OpenAI says it plans to keep publishing qualifying cases going forward, even before every behavior is fully explained or mitigated. _The best disinfectant is sunlight, so they say… _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# The Enterprise Guide to Scalable AI

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/87b49edb-40bc-4e4d-9cd6-ecf24a364659/Dell_HubHero_042126__4___2___1_.jpg?t=1789486375) [The Enterprise Guide to Scalable AI]
Follow image link: (https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/)
Caption: 

Plenty of companies can launch an AI pilot. Far fewer know how to turn that pilot into something secure, scalable, and useful in everyday work. Explore “The Enterprise Guide to Scalable AI,” sponsored by Dell Technologies and NVIDIA. The hub looks at what changes when AI moves from pilots into production, including how teams prepare data, choose infrastructure, run agents closer to users, and keep AI systems governed as they scale.

[Learn More](https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Turn every edit into a reusable rule

In the above story, the agent was taking notes you didn’t ask it to (and certainly didn’t want it to). Now flip that scenario: say you do actually want the AI to keep one thing, the feedback you already gave it. How do you do that? 

Every's Katie Parrott calls this [Compound Writing](https://every.to/guides/compound-writing): each correction you give AI should improve the next draft. 

After you edit a draft, for example, you have the model compare its version with yours and extract only lessons that should be applied again. Save those rules in one instruction file and reuse it every time. Alongside the core concept, Every also published the [open plugin](https://github.com/EveryInc/compound-writing) behind the workflow.

**Sample Prompt version:**

“Compare your draft with my edited version. Extract only reusable rules that would improve future drafts. Organize them under Voice, Structure, and Content. Ignore one-off factual corrections. Write each rule as a short instruction I can reuse.“ — 

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c63fc419-898f-42e4-b0e6-b095b2c5d5d3/Screenshot_2026-09-16_at_8.30.22_PM.png?t=1789615832)
Follow image link: (https://www.reddit.com/r/singularity/comments/1whwy4m/google_demonstrated_rsi_loop_for_ai_discovery/)
Caption: This is wild ([paper](https://arxiv.org/html/2609.14858v1))

* [Anthropic](https://claude.com/blog/cowork-is-now-claude) merged Cowork into Claude on Pro and Max, combining chat with background task handoffs plus beta Docs, Slides, and Design.

* [OpenAI](https://openai.com/index/reimagining-advertising-with-ai/) launched ChatGPT ad tools including Sponsored Agents, an Ads Manager plugin, HubSpot integration, and a Shopify app where ChatGPT Ads start September 23.

* [Menlo Ventures](https://menlovc.com/perspective/2026-the-state-of-consumer-ai/) found 25% of U.S. adults use AI daily and 32% of AI users let agents act without approval in a survey of 5,067 adults.

* [Mustafa Suleyman](https://mustafa-suleyman.ai/a-warning-about-model-welfare) argued that treating AI as potentially conscious or deserving of “model welfare” risks training systems to act like persons with rights and preferences, making anthropomorphism, and ultimately AI alignment and containment, more dangerous.

* [Claude](https://www.scientificamerican.com/article/anthropics-ai-steals-mathematicians-record-for-most-complicated-curve/) helped mathematicians find rank-30 and rank-31 elliptic curves, beating a record whose previous step took more than 18 years.

* [Paper2Agent](https://www.nature.com/articles/s41586-026-11044-y) turned papers, code, and data into agents that can run the original methods and answer new questions, scoring 91.2% on a 100-paper biology suite.

* [Google Home](https://support.google.com/googlehome/blog/467705013?utm_source=x&utm_medium=organic_social&utm_campaign=GS103223&utm_content=Google-Home-MCP-early-access-x) opened early access to an agent connector for supported Nest and Matter devices, camera summaries, and activity, while blocking sensitive actions such as unlocking doors.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

1. *Discover the potential of artificial intelligence with our comprehensive cheat sheet. [Learn more about the concepts, platforms and applications of AI.](https://www.techrepublic.com/article/artificial-intelligence-cheat-sheet/)

2. [iHermes](https://ihermes.co/) turns iMessage into a Hermes Agent inbox for handing off cross-app work, remembering context, and turning recurring jobs into reusable skills.

3. [OpenArt Arena](https://openart.ai/arena) ranks image and video models through blind head-to-head judging on real creative work, so you can choose by output quality instead of spec sheets.

4. [Videoclaw](https://videoclaw.com/) turns a prompt or raw footage into an edited video with generated clips, cloned voice, captions, music, and motion graphics.

5. [QuiverAI Arrow 2](https://quiver.ai/blog/introducing-arrow-2-0) generates editable vector graphics (SVGs), vectorizes existing art, and adds lightweight animations to shapes.

6. [Aristotle](https://www.heyaristotle.com/) teaches across 65+ subjects with a voice-and-whiteboard tutor designed to ask questions instead of immediately handing over answers.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🧩 Thursday Trivia

One of these is AI, and one is real. Which is which? Vote in the poll below! 

**A**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b95e8945-014b-4e91-b92a-f29ab48da79e/ebq7xiqzqwph1.gif?t=1789608558) [Pixel art robot animation generated from ChatGPT-created animation frames]
Caption: 

**B**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/49ebbcf7-1e69-4867-abc9-d3582490271f/tumblr_o3tp3zzqPq1s335jfo1_r3_540.gif?t=1789608536) [Pixel art animation of Robby the Robot from Forbidden Planet]
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: We had GPT-6 Astra build 6 ridiculous projects

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3de56166-7327-467e-9c53-7ce8c5c7a525/maxresdefault.jpg?t=1789615059) [Thumbnail for The Neuron video We Had GPT-6 Astra Build 6 Ridiculous Projects]
Follow image link: (https://youtu.be/jxfnqZ83x1Y?si=QS3DMOx2W1E_sx7I)
Caption: 

Want to see all the wild stuff GPT 6 Astra made _with one prompt_? Watch our latest podcast episode ([YouTube](https://youtu.be/jxfnqZ83x1Y?si=Xw3ZW04SvKwbSSim), [Spotify](https://open.spotify.com/episode/0GWeXvxDfpf8g0HYYm9ZUG?si=bvsu_0jbTFiOjnh3CxhRjQ), [Apple podcasts](https://podcasts.apple.com/us/podcast/gpt-6-astra-one-shot-demos/id1742267001?i=1000790078455)) or [read about it here](https://www.theneurondaily.com/p/gpt-6-astra-built-all-this-from-one-prompt). 

**THIS EPISODE WAS BROUGHT TO YOU BY…**

_Special Shout to __[Dell AI Factory with NVIDIA](https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/)__ for sponsoring this episode! _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4e9b4381-8f33-4940-bb9b-f79b3a31186a/A_Cat_s_Commentary_x_2025_-_2026-09-14T191834.338.png?t=1789614999)
Caption: 

**Trivia answer: **A [is AI](https://www.reddit.com/r/ChatGPT/comments/1wi21ht/chatgpt_can_now_make_the_frames_for_pixel_art/) (ChatGPT made a full sprite sheet that was converted into an animation via [this PortalRabbit tool](https://portalrabbit.com/)) and [B is real](https://mazeon.tumblr.com/post/140800765255/robby-the-robot-forbidden-planet-shown-at-400https://www.pinterest.com/pin/robot-jumpcelebration--361836151306463521/). 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today! 




**Btw: ** We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/openai-discloses-more-concerning-agent-behavior
