---
source: gmail
newsletter: "the-neuron"
message_id: "1a1cf600cf3c0992"
thread_id: "1a1cf600cf3c0992"
subject: "😺 DNA isn't one recipe, says Google's new AI"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Thu, 12 Nov 2026 10:48:55 +0000 (UTC)"
ingested: 2026-11-16
sha256: 142d2be6fa9db80ab06a53597d7d5503f24ef630ac36208bfad9d7b06b860675
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a6779f1c-39e3-40d2-9394-8c6e71c67471/AlphaGenome_2__DNA_Cell_by_Cell.png?t=1794465487)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/74f646fc-3a0c-4400-8072-2cb011d50f8a/In_partnership_with_lenovo.png?t=1792441517)
Follow image link: (https://www.lenovo.com/us/en/ai/hybrid-ai-advantage/ai-library?cid=all:email:hadnyl)
Caption: 

Welcome, humans.

So apparently United just [told AI agents to stay out](https://www.theneuron.ai/news/united-wants-you-to-book-the-flight-your-ai-agent-isnt-invited/) of its booking system. The airline restricted unauthorized third-party AI agents (the assistants that log in and click "buy" for you) from using its app and site, and from booking through travel agencies and aggregators. United cited exposed login details, accidental purchases, agents burning your MileagePlus miles on the wrong flight, and conflicts with aviation requirements. CEO Scott Kirby told the Wall Street Journal that United doesn't want to create another middleman.

Here's the fight. If your assistant becomes the place your trip starts, the airline loses the customer relationship, much like it did to online travel sites. Amazon is playing the same game. It asked Perplexity to pull shopping from its Comet browser, blocked Meta's Muse agent, and pushes its own Buy for Me tool. Walmart went the other way with Agent Profiles, where outside assistants get permissions, spending limits, and per-purchase approval (though not every feature is confirmed live yet).

_Your AI agent might remember the headphones you returned because they hurt your ears, but apparently it still can't get past the gate agent._

**Here’s what happened in AI today:**

* 😸 DeepMind's AlphaGenome 2 predicts DNA typos' effects by cell type

* 📰 Nobel laureate Gross's panel published OpenAI's Yang-Mills Lean proof

* 📰 xAI dumped JAX for C++ as Grok 4.8 nears soft rollout

* 🍪 AWS released an open-source emulator written entirely by AI agents

* 🎓 Learn to catch AI answering a slightly different question

... and a [**whole lot more that you can read about here.**](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-thursday-november-12-2026/)

Advertise to 700K readers of The Neuron here! (https://www.theneuron.ai/get-media-kit/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😸 DeepMind's AlphaGenome 2 Predicts What a DNA Typo Does in Each Cell Type

Every cell in your body carries the same DNA, yet a single-letter change in it can cause disease in some cells and do nothing in others. [Google DeepMind just released AlphaGenome 2](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/), an AI model built to predict which cells a given DNA typo actually messes with.

To see why that's hard, you need one piece of setup. DNA holds genes, but it also holds regulatory switches, stretches that tell a cell how loudly to read a gene. Different cell types flip different switches. So a typo in one switch can leave a gut immune cell and a brain cell with very different volume settings on the same gene.

Earlier approaches mostly looked at whole tissues, which blurs everything together. _It's like trying to figure out which fruit made your smoothie sour by tasting the whole smoothie._ AlphaGenome 2 tastes each fruit. You hand it a 1-million-letter stretch of DNA plus one condition (a tissue, a cell type, or a cell state), and it predicts what that cell does with that DNA. Scientists can even build the condition from their own single-cell experiment. The model learned from more than 100 million individual cell profiles across 68 tissues, from humans and mice.

Here's what DeepMind reports:

* Nearly twice as many gene-changing variants found in cells as the previous best model.

* On 28 immune cell types, 30% versus 16% for causal variants and 43% versus 23% for effect direction.

* Reproduced a published gut-disease finding on a computer, tying a far-off switch to the ETS2 gene in gut macrophages (immune cells).

* Adapted to new cell states from a few dozen cells with no retraining, and showed a severe-COVID variant hits activated T cells harder.

Those benchmark numbers come from DeepMind's own evaluation, and the model is for research only, not validated for clinical or diagnostic use. Still, the part I'd repeat to a friend is the shift in the question. Instead of asking whether a typo is bad, scientists can ask who it's bad for. _That's a much more useful question for anyone studying a disease that only shows up in one organ._

It also guesses properties nobody measured from one measurement they did, which can help labs decide which experiments to run next. And DeepMind precomputed predictions for trait-linked variants across hundreds of conditions, covering traits from height to type 2 diabetes, so researchers don't have to run the model themselves for those.

Researchers can use it now for non-commercial work through the AlphaGenome API, with Colab tutorials, and there's a private preview for commercial research. DeepMind says it explains more of the differences between cell types even in DNA regions outside its training data. The test that matters next is whether outside labs get the same results on cells and regions the model never saw.

**Why this matters: **Drug development mostly fails, with only about 10% of drug programs that reach human trials winning approval. Targets backed by human genetics were [found to be 2.6 times more likely to succeed](https://pmc.ncbi.nlm.nih.gov/articles/11096124/), but a genetic hit rarely says which cell is involved. Predicting the effect cell type by cell type could help researchers pick the right target earlier, and it gives medicine a cleaner way to ask why one variant harms one organ and not another. _That 2.6x figure covers genetic evidence in general, not this model, so think promising tool, not proven one._

Commercial medicine is a long way off. DeepMind says the model isn't validated for clinical or diagnostic use, so it won't read your genetic tests yet. Here's our estimate, not DeepMind's. Labs and drug companies use it over the next one to three years. A new medicine [typically takes 10 to 15 years](https://lifesciences.n-side.com/blog/what-is-the-average-time-to-bring-a-drug-to-market-in-2022) from discovery to approval, so a drug aimed at a target picked today lands between the mid-2030s and early 2040s. _The thing to get excited about now is faster, better-aimed research, not a pill._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# A curated catalog for enterprise AI

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3297c7bb-fb56-4eb2-afd5-def4f5110024/AI-Library_Newsletter_Product-Capability_640x320_Image_WW-en.jpg?t=1793790546)
Follow image link: (https://www.lenovo.com/us/en/ai/hybrid-ai-advantage/ai-library?cid=all:email:hadnyl)
Caption: 

The Lenovo AI Library is a curated catalog of reusable, customizable AI agents and validated use cases built on proven Hybrid AI solutions, spanning knowledge agents, computer vision, edge AI orchestration, predictive maintenance, and more.

Every agent is governed by design and deployed through Lenovo’s xIQ Agent Platform, which provides tools to create highly accurate, enterprise-grade agents with no coding or in-depth technical knowledge required.

Independent validation by Signal65 found new agents can be created in under 5 minutes, with automation tools increasing agent accuracy by more than 20%.

Explore the Lenovo AI Library (https://www.lenovo.com/us/en/ai/hybrid-ai-advantage/ai-library?cid=all:email:hadnyl)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Check the Translation, Not Just the Answer

This week's Yang-Mills story (see Around the Horn below) holds a lesson you can use on your next spreadsheet. A computer can check a proof step by step using Lean, a proof-checking program that works a bit like spell-check for logic. But Lean only confirms that the proof matches the statement as written in Lean. Whether that statement matches the real math problem is a translation, and a human has to check it. That's why the committee's validation document spells out how it checked the Lean code against the standard problem statements. An earlier OpenAI proof [reportedly had the same gap](https://www.siliconreport.com/openai-announces-three-discoveries-in-math-computing-and-physics), with Lean verifying a weaker claim than the prose described. _A perfectly spelled essay can still answer the wrong prompt._

Your version of this happens daily. Ask AI for revenue by customer and it may quietly use net revenue instead of gross, or active customers instead of all customers. The output looks flawless, and it answers a slightly different question than yours.

1. After the AI answers, ask it to list every definition and assumption it used, in plain English.

2. Compare that list to your original request word by word, and mark any term it narrowed, widened, or swapped.

3. Paste only your original request and that list into a fresh chat, so the first chat doesn't defend its own work, and ask it to hunt for mismatches.

```
Below is my original request and the definitions and assumptions an assistant used to answer it. List every place where a definition is narrower, broader, or different from my wording. For each one, tell me how the result would change if my original wording were used instead.

MY REQUEST:
[paste]

THEIR DEFINITIONS AND ASSUMPTIONS:
[paste]

```
**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

### Analytics on Live Data Without Leaving Postgres

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/55ff914f-3c21-4360-8401-6900f032cb20/primary_sqlcard_join_dark.png?t=1789404659)
Follow image link: (https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=beehiiv&utm_content=YJ4ZPRQDHV&utm_term=secondary-liveanalytics&_bhiiv=opp_a04f7084-b315-47d8-8f2c-77db93cf1ccd_e48efd09&bhcl_id=59427a99-6caf-44d7-af1c-d53b1412d144_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

When analytics on Postgres slows down, most teams add a second database. Then they manage pipelines, sync lag, and drift forever. [TimescaleDB](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=beehiiv&utm_content=YJ4ZPRQDHV&utm_term=secondary-liveanalytics&_bhiiv=opp_a04f7084-b315-47d8-8f2c-77db93cf1ccd_e48efd09&bhcl_id=59427a99-6caf-44d7-af1c-d53b1412d144_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f) extends Postgres instead. Analytics run on live data, in the database you already have. No pipeline. No migration. No new query language.

[Get $1000 Credit](https://www.tigerdata.com/go/trial?utm_source=content-syndication&utm_medium=referral&utm_campaign=beehiiv&utm_content=YJ4ZPRQDHV&utm_term=secondary-liveanalytics&_bhiiv=opp_a04f7084-b315-47d8-8f2c-77db93cf1ccd_e48efd09&bhcl_id=59427a99-6caf-44d7-af1c-d53b1412d144_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d10eacd3-8041-4284-a82d-a924fb978bab/image.png?t=1794465295)
Follow image link: (https://x.com/MSFTCopilot/status/2120625304712499434)
Caption: Claude Fable 5.2 just landed in Copilot Cowork and Copilot Studio. Microsoft says “more model choice,” which is one way to describe three rival labs in a single menu.

* Nobel laureate David Gross's panel [published OpenAI's Lean proof](https://fourweekmba.com/ai-gross-panel-sets-release-of-openais-yang-mills-lean-proof/) that pure Yang-Mills theory exists and said its checks back it, though the mass gap question stays open.

* Elon Musk said xAI [dumped JAX for a from-scratch C and C++ stack](https://fourweekmba.com/ai-grok-4-8-in-rl-after-a-57-day-wait-as-xai-dumps-jax-for-cpp/) and that Grok 4.8 is now in reinforcement learning ahead of a soft rollout this week.

* IBM said it [hit key milestones toward Starling](https://www.ibm.com/quantum/blog/path-to-ibm-quantum-starling), its 2029 fault-tolerant quantum computer, including linking two chips at a 1% error rate.

* Meta researchers [updated k-means](https://x.com/askalphaxiv/status/2120493744961323288), a nearly 70-year-old way to sort data into groups, reaching lower error in 1.4 to 2.6 passes instead of 25, with 10 to 45x GPU speedups.

* Microsoft [announced Classroom](https://x.com/mtholfsen/status/2120540184299319621), a standalone education hub for assignments, grades, and Copilot Teach, arriving in 2027 at no extra cost for Microsoft 365 A2, A3, A5, and A7 customers.

* Google, Anthropic, and OpenAI [each added tools](https://www.theneuron.ai/news/google-anthropic-openai-ai-assistants-workspaces/) that move more work into their AI products, including Claude's shared Sheets and ChatGPT's business agents.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

_*Asterisk = in collaboration with (only the first one!). _[_Advertise to 700K+ readers here_](https://info.technologyadvice.com/advertise-with-the-neuron)_!_

1. *Assess your organization's AI governance readiness and identify critical gaps in a live 90-minute workshop with MIT faculty. [_Register today._](https://xpro.mit.edu/courses/course-v1:PRO+AIGE/?utm_medium=referral&utm_source=neuron&utm_campaign=aigov-r2&utm_content=newsletter-november12)

2. [Gemini Decisions API](https://x.com/Google/status/2120583966272983331) checks a photo, PDF, or video against up to 1,000 questions in one pass, like grading 100 delivery photos on 16 questions in 4.5 seconds.

3. [AWS Emulator](https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator) runs 200+ AWS services on your laptop so your coding agent can test cloud code with no AWS account, and AI agents wrote all of it (open-source, [The New Stack](https://thenewstack.io/aws-emulator-ai-agents/)).

4. [Scribe v3](https://elevenlabs.io/blog/scribe-v3) transcribes audio in 102 languages with 27% fewer word errors than v2 (per ElevenLabs' own benchmark), and its Live version now labels speakers in real time.

5. [Grok Bot 1.0](https://x.com/bot/status/2120582957782200586) puts shareable AI teammates into Slack, Microsoft Teams, and your meetings that learn how your team works over time.

6. [Tabletop](https://x.com/GoogleLabs/status/2120549258692882702) turns your group's links, files, and notes into custom tools, like a seating chart or a pickleball bracket (Google Labs waitlist, US only, 18+).

7. [Nod](https://nod.n8n.io/) is n8n's personal agent that runs on your own Mac, Windows PC, or server and chases unpaid invoices, cancels trials, and writes a one-page brief before each call (research preview)—free/open-source.

8. [Facade Code](https://x.com/a3nz3g/status/2118762912986870022) is a VS Code extension that runs Claude Code, Codex, and other coding agents side by side as editor tabs and lets them message each other (MIT license).

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

## UPCOMING EVENT: The Neuron IRL in San Francisco

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c17aafde-2e0d-40fe-b4fe-a68924cb8a35/Email_1250x750.png?t=1793122880)
Follow image link: (https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)
Caption: 

The Neuron is **going IRL** on [**November 18 at 4:30 PM PT**](https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)! Join us in San Francisco for **drinks, bites, special guests, and a live recording of The Neuron podcast.** Huge thanks to Slack and Alumni Ventures for making it happen.

**It’s free, but space is limited. Save your spot!**

RSVP for The Neuron IRL (https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# Thursday Trivia

You know the drill. Which is AI?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c632c61b-124b-424e-9684-21a120080528/image.png?t=1794464737)
Caption: 

**A**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/06592e03-5a2f-4043-992e-dd8886cbfd4e/image.png?t=1794464489)
Caption: 

**B**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/52e7173d-22e8-48e4-b0e4-aa765a0c9cf3/TN_Thumb_111126_CG_Retrospec_B.png?t=1794413169)
Follow image link: (https://www.youtube.com/watch?v=0zLzkYlFRxU)
Caption: Click the image to watch the video!

New episodes air **every week** on Wednesdays: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1060d628-e049-4fe5-864e-31e110cadac3/1.png?t=1794465086)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

**Trivia Answer: **[_A is real_](https://www.artstation.com/artwork/9m90ZL?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=deepmind-launched-alphagenome-2-for-dna), [_B is AI_](https://www.reddit.com/r/aivideo/comments/1xtwl7d/twelve_lights_official_trailer_an_original_anime/?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=deepmind-launched-alphagenome-2-for-dna)

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today!




**Btw: **We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.S. **Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/deepmind-launched-alphagenome-2-for-dna-a377
