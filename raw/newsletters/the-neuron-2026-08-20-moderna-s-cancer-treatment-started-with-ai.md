---
source: gmail
newsletter: "the-neuron"
message_id: "1a01e82688ffebe0"
thread_id: "1a01e82688ffebe0"
subject: "😺 Moderna’s cancer treatment started with AI"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Thu, 20 Aug 2026 09:30:57 +0000 (UTC)"
ingested: 2026-08-24
sha256: fc96331e5240aa1800d98bbca1b32fb4acb064ae2f5a78a63561953057c2039f
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ae317ca0-8b6a-4195-990e-546c3cf76515/ChatGPT_Image_Aug_19__2026__06_14_27_PM.png?t=1787191514)
Caption: 

Welcome, humans.

So guess what: AI has now, OFFICIALLY, helped design a cancer treatment that just cleared Phase 3. 

[Merck and Moderna reported the first positive Phase 3 result for an individualized mRNA cancer therapy](https://www.merck.com/news/merck-and-moderna-announce-phase-3-interpath-001-trial-of-intismeran-autogene-plus-keytruda-met-endpoints-of-recurrence-free-survival-rfs-and-distant-metastasis-free-survival-dmfs-in-patient/), and the wild part is how each dose gets made. _Makes ya feel a LITTLE differently about all those datacenters now, doesn’t it? _

Here’s what’s up: [Moderna says its AI algorithms](https://www.modernatx.com/en-US/media-center/all-media/blogs/advancing-fight-against-cancer) take sequencing data from a patient’s tumor and blood, review the cancer’s mutations, and predict up to 34 “neoantigens” most likely to trigger an immune response. 

Those AI-selected targets are encoded into a custom mRNA therapy made for that patient, then paired with KEYTRUDA. In the melanoma trial, the combo significantly improved recurrence-free and distant-metastasis-free survival versus KEYTRUDA alone; overall-survival follow-up is still ongoing.

_This matters a lot to me personally, because my cousin died from Melanoma. So ya, I’m gonna take the win. _

Meanwhile, [OpenAI is reportedly closing the door on new custom GPT creation for personal ChatGPT accounts](https://sqmagazine.co.uk/openai-blocks-personal-accounts-new-gpts/), which got us wondering: how many people still build their AI workflows around custom GPTs versus the newer wave of skills, workspace agents, coding agents, and Openclaws and the like?

_Translation: are custom GPTs still part of your daily stack, or have they become the AI equivalent of an old Chrome extension you swear you still use?_

**Here’s what happened in AI today:**

* 😺 Generalist learned a task from one 3-second demo.

* 📰 Anthropic passed OpenAI in quarterly revenue.

* 🎓 Cursor can auto-fix new PR feedback.

* 🍪 Google gave students a free year of Gemini.

* 📰 Flock built AI to search police surveillance data.

…and a **[whole lot more in today's full Around the Horn digest](https://theneuron.ai/digest/everything-that-happened-in-ai-today-wednesday-august-19-2026/)**.

**Hey!** We've only got **a few ad slots left in Q3 **and they are going FAST! 

If you want to get your ad in front of 700K+ daily readers who are LOCKED in on AI and what really matters, make sure you reach out ASAP w/ the button below. 

I want to book my ad now (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

**P.S: **want to get ahead of the crowd?** Email **[**Garrett**](mailto:garrett.willis@technologyadvice.com)** **directly and he'll get you set up. 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😺 A robot learned a new task from one 3-second example

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0bf222b6-3db3-4daf-ac58-a14a4a97965d/Screenshot_2026-08-19_at_3.09.54_PM.png?t=1787192052)
Follow image link: (https://x.com/GeneralistAI/status/2090161945307664621)
Caption: 

So y’know how you and I can pretty much watch somebody do something once, and at least attempt it, even if we kinda suck at it? Well, now robots can do that too!

Yesterday, [Rich Sutton argued](https://www.youtube.com/watch?v=xH7U7w9Qzlo) that AI’s next leap won’t come from stuffing models with more human-made data. It’ll come from agents that keep learning from the world they’re actually operating in. Less than 24 hours later, [Generalist dropped GEN-1.5](https://generalistai.com/blog/gen-1.5), a robot model that makes that idea feel a lot less theoretical.

**Here's what happened:** GEN-1.5 can watch a single 3–12-second physical demonstration and immediately attempt the new task. Generalist calls it “physical prompting”: the demo sits in the robot’s 30-second context window, with zero gradient updates.

* Across 10 simple tasks, one demo produced 59% average success; 10 weight updates on five minutes of data raised that to 83%.

* It can copy some human-hand demonstrations, use simulated demonstrations on a real robot, combine two physical prompts, and improvise with unseen tools.

* Previous robot adaptation can take tens of thousands of gradient steps. Generalist says 10 steps changed GEN-1.5’s weights by less than 0.15%.

**Our take:** This matters for two reasons. First, the interface changes from programming a robot to showing it. Second, it starts to make Sutton’s “Big World” thesis concrete: the world is far bigger than any static training set, so useful intelligence has to keep learning from whatever it encounters now.

There’s an important distinction Sutton would care about: GEN-1.5’s one-shot trick is in-context learning, not persistent learning. Its weights do not change. The few-shot mode, where GEN-1.5 updates its weights in 1–10 steps, is actually closer to Sutton’s continual-learning vision.

The milestone isn’t 59%. It’s that eight months of broad physical pretraining made a few seconds of new experience useful. Generalist describes adaptation now as closer to reminding the model of something it nearly knows. If robots can make those new skills persist and compound without forgetting old ones, Sutton’s “learn from the current world” future starts looking a lot less abstract.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

# 🎓 AI Skill of the Day: Make Cursor auto-fix new PR feedback

[Cursor’s new Subscriptions](https://cursor.com/changelog/08-19-26) let cloud agents monitor a pull request (a proposed code change) after they create it, wake back up when CI checks fail or a bot leaves feedback, and keep working without a fresh prompt.

**Try this on your next PR:**

1. Ask a Cursor cloud agent to make the change and open a pull request.

2. Then set one finish line and walk away. Cursor automatically subscribes to PRs its agents create.

“/goal keep this PR merge-ready: fix failing CI checks and bot review comments until everything passes.“ — 

**Non-coder trick:** steal the same “new feedback → unresolved work” loop. Keep one chat for a launch or project. Each time feedback arrives, paste it in and ask: “Compare this with the last round. Show only what is still unresolved and the next action.”

_The useful bit isn’t “use an agent*.” It’s letting one job wake back up when the thing it is responsible for changes. _

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

_*well, if you’re comfortable, you really should be using agents lol. For that, _[_click this_](https://www.youtube.com/live/jbnpPt4AEbM?si=QXgoMWJlV-gyonh7)_._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

1. *[Beautiful.ai](https://link.technologyadvice.com/r/beautiful.ai-tn-newsletter-august-2026) turns your content into polished slides that automatically reformat as you edit. 14-day free trial, then $12/mo billed annually.

2. [Berd](https://venturebeat.com/orchestration/blocks-new-apache-2-0-agent-workspace-berd-works-across-models-and-harnesses-stores-conversation-history-locally) keeps projects, skills, credentials, and history in one desktop home so you can reuse them across Goose, Claude Code, Codex, and other agent apps. Free on macOS, Windows, and Linux.

3. [Ornith-1.5](https://ornith.ai/ornith_1_5.html) ships MIT-licensed 9B, 35B, and 397B self-improving open models, while [Soniox](https://soniox.com/text-to-speech) clones voices and generates expressive speech in 60+ languages.

4. [Taku](https://taku.ai/?ref=producthunt) turns reusable AI workflows into one-click desktop mini-apps you can run, remix, and share without config files. Free to start.

5. [Google](https://blog.google/innovation-and-ai/products/gemini-app/student-offer-google-ai/) gives eligible college students one year of a paid AI plan plus study notebooks, visualizations, and Deep Research. Free for 12 months for eligible students.

6. [Google Search’s generative UI](https://blog.google/products-and-platforms/products/search/search-io-2026/) can turn a complex question into custom interactive visuals, tables, graphs, or simulations in AI Mode. Rolling out free in Search.

7. [Alexa+](https://echo.amazon.com/about) lets you plan, draft, create images, and carry conversations between your browser, Echo, and Fire TV. Free to try in your browser; free with Prime.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/04f70dc9-a5a1-4cd3-a61e-23893c4df273/Screenshot_2026-08-19_at_7.35.34_PM.png?t=1787193347)
Follow image link: (https://www.reddit.com/r/Futurology/comments/1vsrg0s/corporate_america_is_backing_sal_khans_plan_for_a/)
Caption: Very big deal. In the future with AI’s impact on work, degrees should only cost $10K. I argue we should make single year or single semester degrees that you can stack and combine for multi-skilling.

* [Anthropic passed OpenAI](https://www.cnbc.com/2026/08/19/stock-winners-and-losers-as-anthropic-passes-openai-as-hottest-ai-upstart.html) on quarterly revenue, while OpenAI put a date on going public:

↳ Anthropic reported $11.6B in Q2 revenue versus OpenAI's $6.7B, and posted a small operating profit.

↳ [OpenAI CFO Sarah Friar](https://www.cnbc.com/2026/08/19/open-ai-ipo-timing-2027-friar.html) told employees the company expects to go public in 2027, or sooner if growth keeps accelerating.

* [Flock Safety](https://www.wired.com/story/flock-safety-os-investigate/) built a police AI that searches movements, associates, arrest records, dispatch logs, and commercial identity data with natural language.

* [The FTC](https://www.ftc.gov/system/files/ftc_gov/pdf/p034101-ftc-enforcement-policy-statement-re-personalized-pricing-proposed-for-public-comment.pdf) proposed treating secret personalized prices based on private consumer data as potentially deceptive.

* [AI companies are buying rare books](https://www.cbsnews.com/video/ai-companies-buying-books-scan-destroy-404-media-investigation-finds/), scanning them for training data, then shredding the originals; an AirTag traced one to an Amazon-owned facility.

* [Unitree](https://www.cnbc.com/2026/08/19/china-backflipping-robot-maker-unitree-jumps-shanghai-ipo.html) jumped 542% in its Shanghai debut after an IPO that raised roughly $905M.

* [Chinese AI firms](https://www.cnbc.com/2026/08/19/china-ai-nvidia-chips-us-export-controls.html) accessed advanced Nvidia compute through overseas clouds, exposing a remote-access loophole in U.S. chip controls.

* [Meta AI for Mac](https://www.theverge.com/tech/982270/meta-ai-mac-app) adds screen sharing, cross-app dictation, ad analysis, and Google Workspace workflows to Meta’s desktop assistant.

**Want the rest? **[Read the full Around the Horn digest here.](https://theneuron.ai/digest/everything-that-happened-in-ai-today-wednesday-august-19-2026/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

**FROM OUR PARTNERS**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f36729b2-4542-4d9c-93cb-e6ba3fc14d1a/Guru_Neuron_Secondary_8.20.26__1_.jpg?t=1787070501)
Caption: 

Nobody has time to fact-check everything your AI pulls from. That's why AI treats all your company knowledge as accurate, even though only 8-12% of it is ever reviewed. [Guru's](http://Gettheebook(andaccurateAIanswers)today) new ebook shows how leading teams fix this, so every AI answer is one you can trust.

[Get the ebook (and accurate AI answers) today](http://Gettheebook(andaccurateAIanswers)today)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🧩 Thursday Trivia

You know the drill: One is AI, and one is real. Which is which? Vote below, then tell us what tipped you off.

**A.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c55d0cf6-4107-4c2e-be3c-ce07db59cee5/trivia_answer_a_8.20.2026.png?t=1787070462) [Thursday Trivia option A]
Caption: 

**B.**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f4c24ff6-08e0-4e8d-93cc-cbdd13a3bd7a/trivia_answer_b_8.20.2026.png?t=1787070462) [Thursday Trivia option B]
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# Join us LIVE later today to talk all things new AI tool launches (but y’kow, for normies)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/926d350b-1093-4fac-9e22-60ee9ac4c1e2/LIVE_Thumbnails__YT___LI___9_.png?t=1787167959)
Follow image link: (https://www.youtube.com/live/Zo-ApzdU0RQ?si=rfg5wJU638x31D4w)
Caption: Click here to open the tab; it’ll start instantly when we begin!

Click the image above to join us later today at **10am PT | 1pm ET** for a round-up of all the new stuff that came out this week and what you should really care about. 

Plus, there’s a rumor OpenAI’s new Astra model is coming out today… _we highly doubt that, but we’ll be ready just in case._ 

**P.S:** We’re trying to hit** 50K subscribers** **on YouTube** this year. [Click here to help!](https://www.youtube.com/@theneuronai?sub_confirmation=1)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6e1b65ec-719e-4f86-9376-353bf2782704/A_Cat_s_Commentary_x_2025__84_.png?t=1786761785)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today! 




**Btw: ** We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/ai-helped-moderna-fight-cancer-today
