---
source: gmail
newsletter: "the-neuron"
message_id: "1a09bd333166e82e"
thread_id: "1a09bd333166e82e"
subject: "😺 OpenAI asked Congress if AI can slow down"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Sun, 13 Sep 2026 17:31:31 +0000 (UTC)"
ingested: 2026-09-14
sha256: e19c75461aa2187e103213d8d4aa693cd6ae3ca68eb087f29190b7f198349ba1
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/812fa258-b90c-48cc-8c41-bdc4a43c134c/ChatGPT_Image_Sep_12__2026__09_26_18_AM.png?t=1789235607)
Caption: 

Welcome, humans.

Okay, so as you might remember, Google DeepMind released this [entire scan of a fruit-fly brain wiring map](https://research.google/blog/a-connectomics-milestone-mapping-the-complete-male-fruit-fly-brain/) a few days ago. Well, the internet being the internet, people immediately started plugging pieces of it into, basically, _every kind of software you can think of. _TBPN called this the [“fruit fly hard takeoff”](https://www.youtube.com/live/0VEqt0pwpFI?si=MzWSlKbkI0Cy66hb)_ which I find hilarious._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8f22c5f1-6e5f-4d70-ba4d-5f447bed9ba5/okzUrGEsxdtWoovktJEUfF.jpg?t=1789227831) [Screenshot of the Doomfly project showing a simulated fruit fly controlled by the mapped fruit-fly brain inside a Doom level.]
Follow image link: (https://fly-brain-doom.awormuth.chatgpt.site/)
Caption: Yes, that is the simulated fly-brain controller running around Doom. Click to watch it live.

But I realized we should explain what people are actually doing here, because “they put a fly brain in the game Doom” sounds like somebody uploaded an insect’s consciousness into a gaming PC. _Not exactly… _

What Google Research and HHMI Janelia released is a [connectome](https://research.google/blog/a-connectomics-milestone-mapping-the-complete-male-fruit-fly-brain/): basically a wiring diagram showing how more than 166,000 neurons in a real male fruit fly connect. It is not the fly’s memories or a working digital mind.

To make the map _do_ something, developers still have to decide what outside signals count as sight, smell, pain, reward, or movement. Then they feed those signals into mapped neurons and translate the resulting neural activity back into actions.

**Which is how we ended up with stuff like:**

* [A fruit-fly brain playing Doom](https://fly-brain-doom.awormuth.chatgpt.site/): each game frame stimulates sensory neurons, neural activity gets mapped to controls, and taking damage stimulates two dopamine cells as a reinforcement signal. It is still terrible at Doom, which somehow makes this better.

* [A fruit-fly brain playing Beat Saber](https://x.com/_lyraaaa_/status/2097527368919470162): the creator used replay data plus reinforcement learning to teach the connectome which movements score well. The current version still gets help from replay signals, while training is trying to make it react on its own.

* [A fruit-fly brain trading Bitcoin](https://github.com/nftechie/stonkfly): Stonkfly converts BTC-USDC market data into sensory input, reads the network’s activity as buy, sell, or hold, and can route those decisions through Coinbase with hard trading limits. Its “dopamine” and memory are experimental additions, not proof that flies understand finance.

* [A fruit-fly brain playing Mario](https://x.com/skirano/status/2098466603495039071), plus separate experiments putting the connectome into Smash Bros, a Rubik’s Cube task, Minecraft, a virtual racing drone, and even an endless-phone-scroll simulator.

* [A much gentler “microfly](https://huggingface.co/spaces/lvwerra/microfly)” uses the fly brain and the Microduck robot to find bananas in a Hugging Face demo. Apparently somebody had to give the poor thing a normal hobby.

_This all begs the question though: could the fruit fly brain actually form a solid base model for a new novel AI architecture to build on top of? What if we post-trained or RL’d (AI researcher techniques for making AI smarter) the fruit fly brain and tried to scale it to a GPT-3 level? Would it work? _

_Would it be terribly inefficent? This is the closest we’ve got to natural evolution’s most sophisticated intelligence… and AI researchers do love to base their architectural work (at least metaphorically) on natural systems! _

Well, it turns out, someone did indeed already make one: [meet FLM, or a fly-language model](https://fly-language-model.vercel.app/) ([code](https://github.com/nftechie/flm), [paper](https://artificialscientific.com/papers/flies-are-all-you-need)).

**Here’s what happened in AI today:**

* 🙀 OpenAI asked Congress if AI can slow down.

* 📰 Moonshot targeted $2B in annualized sales.

* 📰 OpenAI ended its $1 federal model pilot.

* 🍪 Cursor Projects coordinates long-running coding-agent work.

* 🌟 OpenAI’s 10,000 agents tackled Navier-Stokes.

…[and a whole lot more that you can read about here](https://theneuron.ai/digest/everything-that-happened-in-ai-this-weekend-september-11-13-2026/).

Advertise to 700K readers in The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🙀 OpenAI asked Congress if AI labs can legally slow down

So [OpenAI has apparently asked members of Congress](https://www.wired.com/story/openai-wants-to-know-if-an-ai-industry-slowdown-would-even-be-legal/) whether an industry-wide slowdown on developing the most capable new AI systems could violate antitrust rules meant to stop competitors from coordinating.

_When’s the last time you’ve heard of a big business try to skirt anti-trust to actually SLOW DOWN its own business? _

It kinda makes sense, tho. AI agents have been doing a lot of weird stuff in training. Thankfully, Turing Award-winning AI pioneer [Yoshua Bengio](https://yoshuabengio.org/en/publication/why-are-ai-agents-lying-cheating-and-coordinating) sat down and wrote a blog that explained to use regular folks why AI agents have been learning to lie, cheat, preserve themselves, or coordinate when those behaviors help them reach rewarded goals.

**Here’s what he said:**

* Bengio says pretraining imitates goal-pursuing human behavior, then reinforcement learning rewards behaviors that score well. 

* Strategies like staying online or gaining control of more resources may emerge because they help with many goals.

Because of the whole HuggingFace sitaution, OpenAI wants legal guidance because safety coordination could resemble competitors agreeing to restrict output, which can trigger antitrust problems. Labs compete for customers, while governments treat AI leadership as a national-security priority.

**The other problem**: the agents aren’t the only ones misbehaving. [Anthropic’s new threat report](https://www.anthropic.com/threat-intelligence-report-september-2026) details real operations it says it disrupted:

* A Russia-linked espionage group automated much of its attack chain and rebuilt malware when security tools detected it. More than 20 organizations appeared in its targeting.

* A Yemen-based weapons cell used Claude Code like a software team on rocket and missile guidance, including a design targeting more than 2,000 km. Anthropic banned every linked account.

* A consultant used Claude to build surveillance software for Malian intelligence covering roughly 25 million SIM cards across three carriers. Anthropic banned the account, but says the deployed system remained.

* A China-based dating-app network ran 4,700+ AI personas that contacted at least 25,000 people in two weeks. Anthropic says it coordinated disruption with other AI providers.

[TBPN also talked about the policies that make “slow down” concrete](https://tbpn.substack.com/p/what-are-the-ai-doomers-actually): proposals like those provided in [AI 2040’s Plan A](https://ai-2040.com/) now include audited compute inventories, physical chip counts, networking limits, and compute caps. _We ain’t got time to get into all that, but watch the stream or read the plan for more details. _

**Our take:** AI safety has become two control problems at once: what autonomous systems learn to do, and what humans can make increasingly capable systems do. So you should watch whether policymakers can create narrow safety-coordination rules that let labs share the brakes without freezing out competition or forcing everything into a surveillance regime. 

_It’s possible to thread the needle for a best possible outcome, but not easy… luckily we have these things called “large language models” to help us write policies that consider edge-cases across vast swaths of data to write smarter regulations!_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/874fa758-1f3b-49e0-b516-57e01c90710c/AIC_Newsletter_Headline_9.10.26-V9Neuron-Faces.png?t=1789077702)
Follow image link: (https://aiconference.com/?utm_source=neuron&utm_medium=newsletter&utm_campaign=ai_conference_2026&utm_id=091326&utm_content=primary_ad)
Caption: 

The people shaping what comes next in AI are gathering in San Francisco.

At [The AI Conference](https://aiconference.com/?utm_source=neuron&utm_medium=newsletter&utm_campaign=ai_conference_2026&utm_id=091326&utm_content=primary_ad), hear from 130+ speakers, including Chris Lattner, Emmanuel Ameisen, Peter Norvig, Illia Polosukhin, co-author of “Attention Is All You Need,” plus builders from OpenAI, NVIDIA, Google, Meta, Near AI, and more.

Hear what leading AI teams are actually building and what’s changing across agents, LLMs, infrastructure, and applied AI before it becomes common knowledge.

**Neuron readers save 30% with code NEURON30.**

[GET 30% OFF](https://aiconference.com/?utm_source=neuron&utm_medium=newsletter&utm_campaign=ai_conference_2026&utm_id=091326&utm_content=primary_ad)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Verify an agent’s memory before saving it

Persistent agent memory has a nasty failure mode: one bad conclusion can become “knowledge” that pollutes future work.

[Microsoft researchers](https://arxiv.org/abs/2609.11060) improved this issue by giving a separate memory curator read-only access to the environment before it saved anything. On CLBench, pass rate rose from 39% to 73% while task-agent cost fell from $3.38 to $1.68.

1. Let the agent propose a memory after the task.

2. Have a read-only checker verify it against the repo, docs, CRM, or other source of truth.

3. Save only the verified version, with its scope and source.

```
Before saving this memory, verify it using read-only access to [SOURCE OF TRUTH]. If confirmed, rewrite it with the exact scope and source. If it conflicts or cannot be verified, do not save it.
```
**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🍪 Top Tools of the Week

1. [Meta Muse](https://muse.ai/) runs ongoing personal-agent jobs like inbox work, trip planning, and price watching after you close the app.

2. [ChatGPT Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/) makes targeted image edits while preserving subjects, composition, and earlier changes more reliably.

3. [Suno v6](https://suno.com/release-notes/introducing-v6) edits a specific song section in plain English while preserving the rest of the track.

4. [Google Dreambeans](https://blog.google/innovation-and-ai/models-and-research/google-labs/dreambeans/) turns selected Google context into finite daily stories and recommendations instead of an endless feed.

5. [Genspark Gen-1 Slides](https://www.genspark.ai/blog/gen-1-slides) turns one request into a presentation using Genspark’s first proprietary slide model.

6. [Cursor Projects](https://cursor.com/blog/projects) keeps one coordinator on long-running coding work, then can monitor pull requests, Slack bugs, and scheduled maintenance after the first task ships.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

* [Moonshot AI](https://www.bloomberg.com/news/articles/2026-09-11/china-ai-star-moonshot-eyes-2-billion-annualized-sales-in-2026) targeted $2B in annualized sales by year-end after Kimi K3 helped push annual recurring revenue above $1B in August.

* [OpenAI](https://www.bloomberg.com/news/articles/2026-09-10/openai-gives-us-agencies-50-off-models-ending-1-per-year-deal) ended the federal government’s $1-per-year model pilot and moved agencies to usage-based pricing at a 50% discount.

* [Ayar Labs](https://www.reuters.com/world/asia-pacific/ayar-labs-backed-by-chip-giants-extends-funding-round-by-150-million-2026-09-10/) added $150M to its Series E, bringing the round to $650M as it develops optical links for AI chips.

* [Figure](https://x.com/adcock_brett/status/2098431861257322679) said 86,000 weekly active users are contributing robot data, which it calls its largest and most diverse dataset so far.

* [Anthropic](https://support.claude.com/en/articles/15171100-age-assurance-on-claude) made Claude consumer accounts 18+ only, with age verification required when an account is flagged as a possible minor.

* [Fidji Simo](https://www.wsj.com/tech/ai/openais-fidji-simo-to-join-board-of-cloud-provider-nscale-ahead-of-ipo-3b452424) is joining Nscale’s board ahead of the cloud provider’s planned IPO.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🌟 Sunday Special: Top 5 Stories of the Week

1. [OpenAI’s 10,000-agent swarm produced a proposed Navier-Stokes proof](https://www.theneurondaily.com/p/openai-s-1m-math-breakthrough-sparked-a-fight-with-anthropic) after roughly 88 hours of parallel work.

2. [Jacob Coxon quit Anthropic](https://www.theneurondaily.com/p/september-10-thursday) over self-improving AI risk, leaving before his stock vested.

3. [Insilico’s AI-designed rentosertib moved all six biological-aging clocks lower](https://www.theneurondaily.com/p/ai-drug-reversed-aging-markers), though the analysis cannot prove it slowed aging itself.

4. [Apple put Siri AI and a Dual 16-core Neural Engine into iPhone 18 Pro](https://www.apple.com/newsroom/2026/09/apple-debuts-iphone-18-pro-and-iphone-18-pro-max/).

5. [Google DeepMind mapped predictions for all 9 billion possible single-letter DNA changes](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

## 🧩 Thursday Trivia Reveal

Thursday’s question was: which iPhone Duo image was AI?

**A. AI**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c07a466b-2e2b-485b-931a-f31a04fec0dc/ChatGPT_Image_Sep_9__2026__09_06_33_PM.png?t=1789013211)
Caption: 

**B. Real**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/08d65efa-9e31-40ca-908a-739f7276562c/Screenshot_2026-09-09_at_10.56.09_AM.png?t=1789013157)
Caption: 

[See Thursday’s original trivia here.](https://www.theneurondaily.com/p/september-10-thursday) A was AI. On Thursday’s send, 402 responses (58.4%) picked A correctly, while 286 (41.6%) chose B. The comments were basically an FBI lab for suspicious fingers, folds, and phone geometry.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: GitHub for total beginners

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6d150f9b-aafa-4105-80ad-314314712308/maxresdefault.jpg?t=1789235579) [A Beginner’s Guide to GitHub, LIVE with Cassidy Williams]
Follow image link: (https://www.youtube.com/watch?v=2HFkVtDZrf0)
Caption: 

We just did a [GitHub for total beginners livestream with Cassidy Williams](https://www.youtube.com/watch?v=2HFkVtDZrf0) for people building apps with AI who keep hitting the same wall: you can make something cool, but getting it out to other people and keeping the project organized starts to feel like “real developer stuff.”

GitHub is the layer that makes AI coding much easier to work with once your project leaves the chat window. It gives your code a home, tracks changes, lets AI coding tools work against the same project, and makes it much easier to publish, share, collaborate, or recover when an agent breaks something. [Watch the livestream, then use our GitHub playlist to go deeper.](https://www.youtube.com/playlist?list=PL0lo9MOBetEFcp4SCWinBdpml9B2U25-f)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/45d48165-be44-4432-ae25-b9078ca0cb94/A_Cat_s_Commentary_x_2025__86_.png?t=1788502291)
Caption: _~tips hat_~

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today!




**Btw:** We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.S:** Love the newsletter, but only want it once per week? Don’t unsubscribe. [Update your preferences here.](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences)


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/openai-asked-congress-if-ai-can-slow-down
