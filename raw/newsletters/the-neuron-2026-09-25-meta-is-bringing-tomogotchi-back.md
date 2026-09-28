---
source: gmail
newsletter: "the-neuron"
message_id: "1a0d81ef1389db2f"
thread_id: "1a0d81ef1389db2f"
subject: "😺 Meta is bringing Tomogotchi back"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Fri, 25 Sep 2026 10:31:39 +0000 (UTC)"
ingested: 2026-09-28
sha256: 131bc8c64b16a1274c7c6329ee6323f592ac8515006743ed054e142135a41fd9
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0f2b6ed7-8202-48f1-8fd2-4b658a7e483e/raw?t=1790306485) [The Neuron orange cat mascot holds a tiny Meta-style AI keychain device beside smart glasses, a laptop, and an email envelope.]
Follow image link: (https://theneuron.ai/news/metas-big-ai-bet-now-fits-on-your-keychain/)
Caption: 

Welcome, humans.

So apparently, the new Opus 5.5 is making animated explainer videos that are making it what some call the top video model right now: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4132ff61-73ad-48e0-8839-d64257322079/Screenshot_2026-09-24_at_6.07.06_PM.png?t=1790304561)
Follow image link: (https://www.reddit.com/r/ClaudeAI/comments/1wovwao/jaw_literally_dropped_i_ran_the_prompt_from_the/)
Caption: 

[One Reddit user](https://www.reddit.com/r/ClaudeAI/comments/1wovwao/jaw_literally_dropped_i_ran_the_prompt_from_the/) handed Claude Code a prompt about Friendr, their event-planning app, and a $10 cap for outside model calls. About two hours later, they had a 51-second video with a script, collage art, narration, music, sound effects, and animation synced to the words.

**Here's the part that got me:** Opus didn't generate video frames by itself. It directed other models to make the art and audio, wrote JavaScript to animate everything, asked another model to review drafts, and exported an MP4. The creator reports about $4 in OpenRouter charges; Claude usage was separate. _Apparently, “make me a video” is a full-on project-management gig now._ [Watch the result](https://www.reddit.com/r/ClaudeAI/comments/1wovwao/jaw_literally_dropped_i_ran_the_prompt_from_the/) and see the prompt if you want to try your own version.

**Here's what happened in AI today:**

* 😺 Meta put Muse on glasses and in your pocket.

* 📰 White House reportedly sought first review of frontier models.

* 📰 Akamai signed an $11.6B Anthropic compute commitment.

* 🍪 Gemini 3.8 Live added speech and avatars.

* 🎓 Compound Writing turns edits into reusable AI rules.

…[and a whole lot more that you can read about here](https://theneuron.ai/digest/everything-that-happened-in-ai-today-thursday-september-24-2026/).

Advertise to 700K readers of The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😺 Meta is putting Muse on your glasses and in your pocket

Remember Tamagotchi? That little digital pet you carried around on a keychain growing up? Or maybe your kids had one. Or your parents, depending on how old you are.

Now imagine that little guy was a powerful AI agent. You could talk to it, give it a job, and let it handle things for you.

Well, that's the idea behind [Muse Charm](https://about.fb.com/news/2026/09/the-biggest-news-from-connect-2026/), the pocket-sized device Meta showed off yesterday at [Meta Connect](https://about.fb.com/news/2026/09/the-biggest-news-from-connect-2026/). Meta wants its personal AI agent, Muse, to come along wherever you go, including through your glasses.

So what would you actually ask it to do? Meta's example: look at a school-supply list through your glasses and ask Muse to act on it. The camera supplies the context; your voice supplies the request. Muse uses tools and services you've authorized to do the work.

In [Joanna Stern's interview](https://www.youtube.com/watch?v=2cg56uF4hlc), Zuckerberg talks through the everyday jobs he'd hand Muse, including finding unused subscriptions.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0ae10f34-992b-49aa-b471-164181725043/unnamed.png?t=1790308277) [Mark Zuckerberg discusses Muse in an interview.]
Follow image link: (https://www.youtube.com/watch?v=2cg56uF4hlc&t=1594s)
Caption: 

**Meta also announced a pile of hardware and Muse upgrades:**

* [Muse Realtime Avatar](https://research.meta.ai/blog/bringing-your-muse-to-life) adds expressive characters; work connections include Notion, GitHub, and Box, with glasses access coming in the next few months.

* [Ray-Ban Meta Gen 3](https://www.meta.com/ai-glasses/) is available now; [Ray-Ban Meta Audio](https://about.fb.com/news/2026/09/introducing-ray-ban-meta-audio-glasses-new-styles-plus-muse/) ships October 13 with open-ear listening and assistant access.

* [Meta VR Glasses](https://about.fb.com/news/2026/09/introducing-meta-vr-glasses-3d-movies-immersive-live-sports-100-grams/) are planned for spring 2027, while [Ray-Ban Display](https://about.fb.com/news/2026/09/new-features-for-meta-ray-ban-display-navigation-hologram/) is getting navigation, calendar, spatial audio, and Threads features.

**The appeal is obvious**: notice something, say what you want, and let Muse start the errand. The tradeoff is access. Meta runs Muse in a [dedicated cloud computer](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse), while a separate layer called Sentinel can allow, block, or ask you before actions. Muse cannot override it, and Meta says service credentials enter only approved requests. Plus, a confidential VM planned for testing later this year is meant to block Meta employee access cryptographically.

That still leaves other attack surfaces. Researcher [Patrick Wardle](https://github.com/pwardle/not-a-mused) recently found a Mac debugging setting that local malware could change to redirect dictation and expose Muse's authentication token. Meta [patched it](https://www.unite.ai/meta-hot-fixes-muse-zero-day-that-let-attackers-hijack-the-ai-agent/) by September 22. Meta stressed that code already had to run locally; Wardle noted users can still be tricked into running commands.

Can these devices handle errands reliably, with understandable, controllable permissions? A companion that needs constant supervision? _I already did the Tamagotchi thing. It was fun, but I wanna be the Tamagotchi this time around! _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

# 🎓 AI Skill of the Day: Clean out conflicting AI instructions

You know how we tell you to save useful corrections so AI stops making the same mistake? That advice comes with a housekeeping problem. [Every's Katie Parrott](https://www.youtube.com/watch?v=OQgO26GvAXM&t=1460) had saved old outlines, writing feedback, and several versions of her essay templates so her assistant could remember what worked. Eventually, the drafts started coming back crowded and flat. When she looked through the files, she found that alternative templates had turned into simultaneous requirements for every piece. The assistant was trying to follow all of them.

So Katie ran a review across the instructions, archived the old folders, and rebuilt two current guides: one for the column's structure and one for her voice. She also stopped saving every intermediate version. The idea is to give the assistant a smaller set of instructions that actually agree with each other.

If you have a writing project that has gotten worse after months of tweaking, try the same cleanup. Ask AI to identify conflicting or outdated rules with exact file references, decide what still applies, then archive the rest. Run a familiar assignment afterward and compare the draft. _Sometimes your AI needs a closet cleanout more than another pep talk._

**Copy/paste:**

```
Review the instructions and examples in [project/folder]. Identify duplicated, conflicting, and outdated rules, citing the specific files and short excerpts. Propose what to keep, archive, or rewrite. Do not modify files until I approve.
```


View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

# What did your coding agent do on your laptop last week?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e64b737-8067-4564-8860-eecba5788b10/neuron-secondary-2x1.png?t=1790093052)
Follow image link: (https://www.originhq.com/webinar/next-layer-of-endpoint-security?utm_source=neuron&utm_medium=newsletter&utm_campaign=direct-buys&utm_content=secondary-0923)
Caption: 

SACR's new report names the layer, agent runtime observability, and puts Origin in it. On October 1, the analyst who wrote it walks through the report live with Origin's founder, then goes deep on the trace and what you can do with it. Save your spot.

**[Save your spot](https://www.originhq.com/webinar/next-layer-of-endpoint-security?utm_source=neuron&utm_medium=newsletter&utm_campaign=direct-buys&utm_content=secondary-0923)****.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/fa786649-6820-4a32-8707-d75a8d6afd4b/Screenshot_2026-09-24_at_4.22.47_PM.png?t=1790307709)
Follow image link: (https://www.skild.ai/blogs/physical-self-play)
Caption: [Skild AI](https://www.skild.ai/blogs/physical-self-play) trained a humanoid to play soccer through 140 years of simulated self-play, then transferred the policy to a real robot.

* The White House [reportedly asked OpenAI and Anthropic](https://www.politico.com/news/2026/09/24/white-house-asks-openai-and-anthropic-to-hold-new-models-from-uk-testers-until-u-s-review-01091769) to hold new frontier models from U.K. testers until the U.S. government reviewed them first.

* [Akamai signed a seven-year $11.6B commitment](https://www.globenewswire.com/news-release/2026/09/24/3368729/0/en/akamai-announces-11-6-billion-multi-year-agreement-with-anthropic-to-support-growing-demand.html) to run Anthropic CPU workloads, with an option for another $9B tied to future spend.

* [DeepSeek’s annualized revenue reportedly reached $1B](https://www.reuters.com/world/asia-pacific/chinas-deepseek-annualised-revenue-hits-1-billion-information-reports-2026-09-24/) while the company worked to close roughly $7.5B in financing.

* Google, OpenAI, and Anthropic [reportedly began forming](https://www.theinformation.com/articles/google-openai-anthropic-ai-safety-group-takes-shape?rc=lks9on) a frontier AI standards group around independent testing, incident reporting, and auditor standards.

* [Google said Project Suncatcher](https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/) will fly a TPU prototype on a SpaceX mission with Planet Labs to test whether AI chips can withstand orbit.

* TypeSafe AI (maker of Jev) was reportedly[ discussing a $1B+ round](https://www.theinformation.com/newsletters/dealmaker/jev-fervor-leads-talk-big-valuation-boost) at a valuation above $10B, roughly a week after raising $40M at about $200M.

* [Google Research](https://research.google/blog/coherent-long-form-video-generation/) published a multi-agent approach to longer AI videos, with separate agents checking continuity and production as scenes accumulate.

* [Anthropic's book-trading experiment](https://www.anthropic.com/research/project-swap) sent agents to negotiate for 201 employees; the biggest gap came from agents misunderstanding people's preferences.

Want absolutely EVERYTHING that happened in AI this week? [Click here!](https://theneuron.ai/digest/everything-that-happened-in-ai-today-thursday-september-24-2026/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try.

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6cd824cc-be25-4beb-a0e8-3963f0c3e78e/Brand_Banner_04__2_.png?t=1790282203)
Follow image link: (https://links.outskill.com/NEURSEP4)
Caption: 

1. *Build your own AI Co-Worker that literally works 24/7 even while you’re asleep. [Grab your seat here](https://links.outskill.com/NEURSEP4).

2. [Gemini 3.8 Live](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-with-live-avatar/) adds speech-to-speech in 97 languages plus Live Avatar, with simultaneous vision and audio input.

3. [Agora-2](https://agora.odyssey.systems/) puts up to 20 humans and agents into the same AI-generated world.

4. [Adobe for Claude](https://blog.adobe.com/en/publish/2026/09/24/adobe-comes-to-gemini-expands-what-you-can-do-in-claude) adds Acrobat PDF tools plus hands-on Acrobat and Express editors inside the conversation.

5. [Claude Code cloud sessions](https://claude.com/blog/claude-code-on-the-web) keep coding tasks running on Anthropic’s machines after your laptop closes.

6. [Cursor Rollouts](https://cursor.com/blog/rollouts-and-security-reviewer) follows code through deployment, flags regressions, and can pause a rollout or propose a revert.

7. [Google’s Antigravity SDK](https://developers.googleblog.com/introducing-support-for-local-ai-models-in-the-antigravity-sdk/) runs agents with local models such as Gemma 4 for offline or hybrid workflows.

8. [Gemini phone calls](https://techcrunch.com/2026/09/24/google-tests-letting-gemini-make-phone-calls-initially-for-us-pixel-owners/) are being tested for U.S. Pixel 11 subscribers, letting the agent call businesses, wait on hold, check stock, and make reservations.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 💡 Intelligent Insights

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4cb38d0f-c288-4ab1-8c65-473a6d65fef6/Screenshot_2026-09-24_at_4.27.50_PM.png?t=1790304559)
Follow image link: (https://x.com/kimmonismus/status/2102844654169575547)
Caption: 

* [Ryo Lu](https://x.com/ryolu_/status/2102933485795369213) argues AI’s productivity trap is infinite busywork: thousands of PRs and hundreds of agents can leave humans with less time for taste, intention, and deciding what should exist.

* NVIDIA’s[ Jean-François Puget](https://x.com/JFPuget/status/2103081634140483943) argues AI’s more immediate workplace risk is “brain rot”: forwarding agent reports you never read, then treating “the agent said it” as an excuse instead of owning the output.

* Foundation Capital’s[ Jaya Gupta](https://x.com/JayaGup10/status/2102983087302815941) argues Jev-class decision models could hit frontier-model economics from three directions at once by reducing calls, tokens per call, and dollars spent per decision.

* Y Combinator CEO[ Garry Tan](https://x.com/garrytan/status/2102955139875397806) argues startup distribution now has two loops: make software agents want to use your product, then use agents to make humans want the software.

* Anthropic inference engineer[ Alek Dimitriev](https://x.com/tensor_rotator/status/2103238002860515559) argues clear AI writing is a safety feature: when explanations become hard to understand, people are more likely to hand the decision back to the model.

* [Greg Isenberg](https://x.com/gregisenberg/status/2103198565065523426) argues Meta opening Muse to third-party connectors could create an app-store-like opportunity where businesses compete to become services a personal agent chooses on your behalf.

* [Riley Walz](https://x.com/rtwlz/status/2102793613914816765) argues the set of things one person can accomplish is expanding so quickly that the new bottleneck may simply be whether you’re thinking big enough about what to attempt.

* Here’s the [secret sauce for getting the most out of Opus 5.5](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/), and [a video breaking all the tips down](https://youtu.be/ejjBbaq9RmY?si=Z3m-CNBwcczQzhXC). 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🎙️ New From The Neuron Podcast

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3ef98695-a28f-4f2d-9293-a206a7d30911/ChatGPT_Image_Sep_24__2026__12_24_59_AM.png?t=1790235435)
Follow image link: (https://www.youtube.com/watch?v=RVn6pGLs64w)
Caption: Click the thumbnail to watch on YouTube.

So we tried to benchmark Opus vs GPT-6 Sol an our [interactive black hole](https://aherostrial.github.io/black-hole-opus-test/) and [cat Doom prompts](https://cat-doom.com/), but Opus 5.5 is on a whole ‘nother level. Frankly, _it’s the best model Grant’s ever used. _Watch our livestream w/ the link above or [read the recap here](https://theneuron.ai/explainer-articles/claude-opus-5-5-vs-gpt-6-sol-demos-prompts-timestamps/).

We also got into Meta’s wearable-agent plans and the tradeoff between more safety testing and faster public access. **Click the image above to come watch! **

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/61bc5c8b-43b6-48ed-a6f2-9e76b344fe7d/A_Cat_s_Commentary_x_2025_-_2026-09-23T132712.593.png?t=1790234129)
Caption: Tip of the iceberg, or the foothills of the exponential… ?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today!




**Btw: **We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/meta-unveiled-muse-charm-a-pocket-ai
