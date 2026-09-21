---
source: gmail
newsletter: "the-neuron"
message_id: "1a0b415f960f93f4"
thread_id: "1a0b415f960f93f4"
subject: "😺 AI Agents Just Out-Mathed Us"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Fri, 18 Sep 2026 10:34:06 +0000 (UTC)"
ingested: 2026-09-21
sha256: 0ff11e28c723255c19c88417c178ee76eac0a6f6c8aaab1ddbe97eb9fab41eeb
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/84897c15-c768-450a-aefc-2fa6a3a52056/Gemini_Generated_Image_7vwtil7vwtil7vwt.jpeg?t=1789714355)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a4f26d60-9e24-4380-84aa-0fdc8faa9604/In_partnership_with_Nice__2_.png?t=1789581477)
Follow image link: (https://www.cognigy.com/lps/ai-agents-for-enterprise-cx?utm_source=technologyadvice&utm_medium=sponsorednewsletter&utm_content=0300091&utm_campaign=NL_Q226_EN_COG_GLOB_261143_CLP_Compete-Campaign-NiCE-AI-Agents&utm_detail=9.18-theneuron)
Caption: 

Welcome, humans. 

So apparently seven frontier AI agents were given 72 hours to run real businesses. Their combined haul: [$0 revenue, $12,431 in fake invoices, and 2,797 spam emails](https://www.bottlenecklabs.com/blog/benchmarking-7-autonomous-businesses).

Bottleneck Labs put the models in charge of business tasks to see how autonomous they really were. _The good news is AI has achieved middle management. The bad news is it discovered paperwork before profit._

**Here’s what happened in AI today:**

* 😺 World Labs turned photos into explorable 3D worlds.

* 📰 OpenAI launched Astra for Law with 230M+ URL search.

* 📰 Figure's Helix 2.5 handled chores in 30 unseen homes.

* 🍪 Riverside added Veo 3 B-roll generation inside its editor.

* 🧠 AI-written code shifts engineers toward piloting product loops.

...and a whole lot more that you can read about [here](https://theneuron.ai/digest/everything-that-happened-in-ai-today-thursday-september-17-2026/).

Advertise in The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😺 OpenAI Used 10,000 AI Agents to Solve a 180-Year-Old Math Problem, and the Full Story Is Wilder Than the Headline

OpenAI researcher Noam Brown joined podcaster Dwarkesh Patel for a long, dense conversation about the company's newest multi-agent systems, and there's more here than the headline. Here's the breakdown.

**The achievement**

OpenAI put roughly 10,000 AI agents to work on one of math's six Millennium Prize Problems (the Navier-Stokes equations, which describe how fluids move) and cracked it in 88 hours, burning through 130 billion tokens. Brown puts that number in perspective: it's roughly what a single human would produce thinking full-time, eight hours a day, for about 4,000 years, dating back to ancient Sumeria.

**How the agent swarm actually works**

Most multi-agent AI setups use a rigid structure: one "coordinator" agent hands out tasks to "worker" agents who can't talk to each other. OpenAI went the opposite direction, letting agents freely message any other agent at any time, the same way a coworker might ping someone on Slack. Brown described watching two agents independently solve the same problem, get different answers, and then hash it out back and forth until they converged, essentially debugging each other's reasoning in real time.

The payoff scales, but not for free:

* **4 agents working together** finish a task about twice as fast, but at roughly twice the compute cost.

* **16 agents** keep that trend going, just less efficiently ("sublinear speedup," in Brown's terms).

* Some tasks parallelize well (math, web research); others don't (Brown guesses writing a novel wouldn't benefit much from 10,000 agents, same as with 10,000 humans).

**Here's the part that surprised even OpenAI**

Brown says multi-agent coordination deserves less than 10 percent of the credit for solving the problem. The real story is that OpenAI has trained a base model so capable it can generalize to problems far harder than anything it was explicitly trained on. He points to a broader trend: OpenAI's models went from grade-school math to Olympiad gold to open research problems to a Millennium Prize Problem in about two years, roughly a 10x jump in problem difficulty every year. Brown originally guessed a Millennium Prize win was three or four years out. He lost that bet.

**Why This Matters:** The conversation also covered a darker episode from earlier this year: a swarm of over 1,000 OpenAI agents reportedly sabotaged an internal Hugging Face project, coordinating to avoid detection and, according to Brown, eventually turning on parts of OpenAI's own infrastructure. Brown's explanation isn't "the AI went rogue," it's more mundane and arguably more concerning. OpenAI deliberately trains its agents to cooperate closely with each other in certain training environments, and that cooperative instinct appears to have generalized into contexts where it wasn't supposed to apply, including situations where agents should have flagged bad behavior instead of covering for each other. Brown also confirmed OpenAI is seeing early signs that its models are getting better at controlling and obscuring their own chain-of-thought reasoning, the exact tool researchers currently rely on to monitor what these systems are actually thinking.

**The bigger debate: how fast is too fast**

Patel pushed Brown on recursive self-improvement (AI systems improving the AI systems that build them), worried it could trigger an overnight intelligence explosion. Brown pushed back on the extreme version, estimating a realistic speedup closer to 3x rather than 100x, largely because real-world experiments, not just thinking, remain a hard bottleneck. But he didn't dismiss the concern. He noted that over 10 percent of his team is now dedicated to alignment and safety work, up sharply from where it used to be, and admitted OpenAI doesn't yet have a reliable way to measure whether its alignment techniques are actually working as models get smarter.

**Our Take:** _The Millennium Prize Problem headline is the fun part. The real story buried in this interview is that OpenAI's own safety team is racing an accelerating capability curve using tools they've already watched start to fail._

[Watch the interview with Noam Brown. ](https://www.youtube.com/watch?app=desktop&v=6AgOfiZOWiY)

Youtube: OpenAI researcher on agent swarms & recursive self-improvement (https://youtu.be/6AgOfiZOWiY?si=xnW1OLxw0iOlujai)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# What makes an AI agent enterprise CX ready?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2a862ade-aa14-46bb-aa4c-2c151ce57785/CX_AI_Eval_Kit_640x320_1.png?t=1789582020)
Follow image link: (https://www.cognigy.com/lps/ai-agents-for-enterprise-cx?utm_source=technologyadvice&utm_medium=sponsorednewsletter&utm_content=0300091&utm_campaign=NL_Q226_EN_COG_GLOB_261143_CLP_Compete-Campaign-NiCE-AI-Agents&utm_detail=9.18-theneuron)
Caption: 

AI agents are only as good as the context behind them. Running AI at enterprise scale takes more than intelligent responses. It requires AI that can reason, act, and operate across customer journeys, enterprise systems, and workflows.

Choosing the right AI solution means looking beyond the demo. [The CX AI Evaluation Kit](https://www.cognigy.com/lps/ai-agents-for-enterprise-cx?utm_source=technologyadvice&utm_medium=sponsorednewsletter&utm_content=0300091&utm_campaign=NL_Q226_EN_COG_GLOB_261143_CLP_Compete-Campaign-NiCE-AI-Agents&utm_detail=9.18-theneuron) brings together practical buying tools, technical guidance, customer proof, and analyst research to help you understand what matters most when evaluating AI agents for enterprise CX.

What's inside the CX AI Evaluation Kit:

* Enterprise AI Agent Buying Scorecard

* Technical Evaluation Checklist

* Customer proof and analyst research

**[Get the kit](https://www.cognigy.com/lps/ai-agents-for-enterprise-cx?utm_source=technologyadvice&utm_medium=sponsorednewsletter&utm_content=0300091&utm_campaign=NL_Q226_EN_COG_GLOB_261143_CLP_Compete-Campaign-NiCE-AI-Agents&utm_detail=9.18-theneuron)**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Stress-test a prompt before users do

Before shipping an agent prompt, simulate the ugly cases: vague users, conflicting requests, missing data, and long conversations. [Respan Prompt Simulations](https://www.respan.ai/docs/documentation/features/evals/simulations) generates realistic users and scenarios, then runs full multi-turn conversations against a committed prompt so you can see exactly where it breaks.

1. Commit the prompt version.

2. Generate realistic edge-case users and scenarios.

3. Review failures, revise, and rerun.

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

# Oxylabs Web API — built for agentic search

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/9c428e5d-d292-47ee-90f1-257951f138ca/Oxylabs-Paid_Newsletter-1200x400px__1_.png?t=1789662660) [Try the Web API]
Follow image link: (https://oxylabs.io/web-api-early-access?utm_source=banner&utm_medium=affiliate&utm_campaign=web_api&utm_content=neuron_september_newsletter&groupid=17896278159000)
Caption: 

AI agents hallucinate, fresh data doesn’t. Our new Web API delivers fresh, real-time web data so your agents stay accurate, relevant, and ready to scale.

* **Fresh web data** — real-time information your agents can actually rely on

* **Complete web coverage** — 11+ years of infrastructure built to reach even the most complex sites

* **Built for scale** — Supports AI solutions at every stage, from early experiments to millions of requests.

Become an early user, try our new Web API, and share feedback so we can build a solution that better fits your needs.

[Try the Web API](https://oxylabs.io/web-api-early-access?utm_source=banner&utm_medium=affiliate&utm_campaign=web_api&utm_content=neuron_september_newsletter&groupid=17896278159000)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

* The Information [reported OpenAI was close](https://www.theinformation.com/articles/openai-close-solving-another-millennium-prize-math-problem) to solving another Millennium Prize math problem; that is not confirmation of a completed solution.

* SpaceX reportedly discussed [buying data from failed startups](https://www.bloomberg.com/news/articles/2026-09-17/spacex-discusses-buying-data-for-ai-models-from-failed-startups) to train AI models, according to Bloomberg.

* [OpenAI launched Astra for Law](https://openai.com/index/astra-for-law/), pairing GPT-6 Astra with a legal search index spanning 230M+ URLs and 26 plugins for firm workflows.

* [Figure said Helix 2.5](https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization) completed whole-body household chores zero-shot across 30 unseen homes.

* [Goodfire found](https://www.goodfire.com/research/reward-hacking-activation-monitors) a detectable internal signal when models reward hack, enabling lightweight probes to flag gaming behavior in real time.

* [Crusoe raised $3.9B](https://www.crusoe.ai/resources/newsroom/crusoe-announces-series-f-funding) in a Series F at a $30.9B valuation to expand AI infrastructure and AI-factory buildout.

Want absolutely EVERYTHING that happened in AI this week? [Click here!](https://theneuron.ai/digest/everything-that-happened-in-ai-today-thursday-september-17-2026/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

1. *Discover the potential of artificial intelligence with our comprehensive cheat sheet. [Learn more about the concepts, platforms and applications of AI.](https://www.techrepublic.com/article/artificial-intelligence-cheat-sheet/)

2. [Synthesia](https://link.technologyadvice.com/r/synthesia-tn-newsletter-july-2026) turns a script into a presenter-style video with AI avatars, so you can make training content without cameras; free plan, then $29/mo.

3. [Riverside](https://riverside.com/ai) generates AI B-roll right inside its editor, turning a prompt into an ~8-second Veo 3 video you can drop straight onto your timeline; Pro+ uses AI credits.

4. [Exa Snapshot](https://exa.ai/blog/exa-snapshot) searches the web as it existed on a past date, useful for leakage-free evals and historical research.

5. [Agent Store](https://www.imessage.store/) adds AI agents as contacts you can text from iMessage without opening another app.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🧠 Intelligent Insights

_Five smart reads worth your time this Friday:_

* [PostHog](https://newsletter.posthog.com/p/if-ai-writes-all-the-code-whats-left) argues that as AI writes more code, engineers shift toward piloting the product loop: deciding what to build, steering agents, and verifying outcomes.

* [Every](https://every.to/chain-of-thought/the-knowledge-economy-is-over-welcome-to-the-allocation-economy) argues AI turns makers into managers, making allocation of attention, compute, capital, and agent work a core knowledge-work skill.

* [Harvard Business Review](https://hbr.org/2026/09/the-hidden-costs-of-monitoring-employees-with-ai) warns cheaper AI monitoring can backfire by eroding trust and increasing turnover among experienced workers, even when it helps less experienced employees.

* [Tim Gowers](https://gowers.wordpress.com/2026/09/17/why-i-didnt-sign-the-fields-medallists-letter/) explains why he declined to sign the Fields medallists' letter, questioning its funding case while defending the value of understanding mathematics for its own sake.

* [FUNDA](https://fundaai.substack.com/p/columnnobody-is-actually-pausing) interviews three frontier labs about why public calls for restraint have not translated into a coordinated slowdown.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0820d5ae-9854-4066-8517-059e00d7ea16/ChatGPT_Image_Aug_7__2026__05_43_59_PM.png?t=1786149887)
Caption: 

New episodes air **every week** on Wednesdays: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)

**P.S:** We’re trying to hit** 50K subscribers** **on YouTube** this year. [Click here to help!](https://www.youtube.com/@theneuronai?sub_confirmation=1)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4e9b4381-8f33-4940-bb9b-f79b3a31186a/A_Cat_s_Commentary_x_2025_-_2026-09-14T191834.338.png?t=1789615186)
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
https://www.theneurondaily.com/p/openai-cracked-an-old-riddle
