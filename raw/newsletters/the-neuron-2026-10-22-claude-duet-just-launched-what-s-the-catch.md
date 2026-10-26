---
source: gmail
newsletter: "the-neuron"
message_id: "1a1632b6b24e7f1c"
thread_id: "1a1632b6b24e7f1c"
subject: "😺 Claude Duet just launched. What's the catch?"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Thu, 22 Oct 2026 10:32:30 +0000 (UTC)"
ingested: 2026-10-26
sha256: ad467e54752c88d4b76e9da43b5e218e88383b394772aca4ad21a42a0262a4b1
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/41f6c8af-f35e-46b0-8419-3449f28877be/Claude_Works_While_You_Sleep.png?t=1792654559)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/74f646fc-3a0c-4400-8072-2cb011d50f8a/In_partnership_with_lenovo.png?t=1792441517)
Follow image link: (https://www.lenovo.com/us/en/ai/hybrid-ai-advantage/ai-library?cid=all:email:tonk8q)
Caption: 

Welcome, humans.

Okay, so apparently every chatbot has a favorite country, and it's Japan. [Researchers at the University of the Basque Country and Cardiff University](https://arxiv.org/abs/2604.21751) asked LLMs open-ended questions about culture and found a clear tendency toward countries like Japan. Prompting in English gave more varied answers.

The authors say the lean first appears after supervised fine-tuning, the stage where a model is taught to be helpful and polite, not while it's reading the internet. _Somewhere a chatbot is being asked for pizza toppings and recommending a tea ceremony._

The paper came out in April, and [the viral version making the rounds today](https://x.com/thesupermannx/status/2112893797592109088) adds claims the abstract doesn't make, like quantization (model compression) making it worse. Treat those as unconfirmed until someone checks the full paper.

**Here’s what happened in AI today:**

* 😺 Anthropic launched Claude Duet, an agent that works while you're away

* 📰 ChatGPT ads expanded to 89 countries

* 📰 A tampered LiteLLM release stole credentials for two hours

* 🍪 Notion Auto picks cheaper models, stretching agent credits about 10x

* 🎓 Run three coding agents at once with git worktrees

…and a [**whole lot more that you can read about here.**](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-thursday-october-22-2026/)

Advertise to 700K readers of The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

Got a Black Friday or Cyber Monday deal worth shouting about? **700,000 subscribers** might want to hear about it. Put your offer in front of **The Neuron's** AI-curious audience with a sponsored spot in our special Black Friday edition. _Because the best deal in the world doesn't help if nobody sees it. _Planning a holiday promo? [Let's talk!](https://solutions.technologyadvice.com/lp/advertise-in-black-friday-newsletter/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😺 Anthropic's New Claude Duet Works While Your Laptop Is Off, But Has to Ask Before It Spends Your Money

[Claude Duet](https://claude.com/resources/articles/claude-duet) is a new app where Claude acts as a proactive agent. It sends you a morning brief, checks your connected apps every few hours, and messages you only when something actually needs you. It's a research preview for US Pro and Max subscribers (by waitlist), it's built around Claude Opus 5.5, and it uses your plan's existing usage limits.

_Wait, how does it check anything while my phone is in my pocket?_ Because Duet runs on its own virtual machine, which is basically a small cloud computer Claude gets to use, browser included. That's why it keeps working when your phone and laptop are off. It also carries over your Claude memory, skills, and connected apps, and Anthropic lists 6,000+ connectors, including QuickBooks, Stripe, Gusto, Docusign, HubSpot, and Shopify.

An agent that acts while you're not looking raises the obvious question: what stops it from doing something dumb? Anthropic's answer is a stack of brakes.

* Duet shows exactly what it's about to do and waits for your OK before sending a message, making a payment, signing a document, or deleting anything.

* Trading securities and moving money between accounts are off-limits, even with your approval.

* Credentials follow Anthropic's Managed Agents design, so Duet never sees your passwords or tokens. Even a confused Claude has nothing to leak.

* A new classifier blocks sharing the most sensitive info, like credit card numbers and government IDs. Health and finance details go out only when you explicitly say so.

On payments, Duet can use Link (Stripe's wallet, with a virtual card) and Shop Pay. _So yes, an AI can now buy things for you. Read the approval screen._

Anthropic is also upfront about the limits. Duet can misread a thread or miscalibrate urgency, it's weaker at personal errands than work tasks, and it can't yet show you its browser. The one I'd flag is the last: background checks and big tasks count against your usage limits. _The assistant that never sleeps is also spending your quota while you do._

The thing to watch is the ping threshold. Ping too often and Duet becomes the coworker you mute. Ping too rarely and you miss the showing on the wrong day. Anthropic admits urgency is the weak spot, so the number worth asking testers for is how often a ping was actually worth your attention.

If you're a US Pro or Max subscriber, you can [join the waitlist here](https://claude.com/resources/articles/claude-duet).

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# Realize up to 24x faster time to AI value

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8a34bffa-c525-4f1f-b493-98b0e89d3006/AI-Library_Newsletter_Outcome-BusinessValue_640x320_Image_WW-en.jpg?t=1792441498)
Follow image link: (https://www.lenovo.com/us/en/ai/hybrid-ai-advantage/ai-library?cid=all:email:tonk8q)
Caption: 

AI experimentation can prove what’s possible. The bigger challenge is turning that potential into repeatable business value.

The Lenovo AI Library helps you take that step with enterprise-ready AI agents and validated use cases. Signal65 analysis indicates organizations can begin deploying production-ready agents in as little as one week instead of six months, up to 24x faster time to value.

Move from AI experimentation to measurable business impact with Lenovo.

[Explore the Lenovo AI Library](https://www.lenovo.com/us/en/ai/hybrid-ai-advantage/ai-library?cid=all:email:tonk8q)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Run Three Coding Agents at Once Without Them Overwriting Each Other

You asked your coding agent to build a login page, and now you're staring at a spinner for ten minutes. You have a bug and a docs update sitting in the queue. Open a second agent in the same project folder, though, and both will edit the same files on the same branch. That's how half-finished work gets stomped.

The fix is a git worktree. Normally a repo has one working folder with one branch checked out. A worktree is an extra folder from the same repo with its own branch, so each agent gets its own desk while sharing one filing cabinet of history. _Same kitchen, separate cutting boards._ Commits are visible across all of them. Uncommitted edits aren't, which is the point.

1. Give each agent its own worktree. In Claude Code, run `claude --worktree feature-auth` in one terminal and the same command with a different name in a second ([docs](https://code.claude.com/docs/en/common-workflows); the repo needs at least one commit). Codex CLI has no flag for this, so run `git worktree add ../project-bugfix -b bugfix-123`, `cd` in, and start `codex`, per [this walkthrough](https://dev.to/dublecc/parallel-ai-agent-workflows-with-git-worktrees-the-concrete-pattern-59lp).

2. Split the work by files. Tests for module A and docs for module B are safe. Two agents refactoring the same widely used type will collide anyway.

3. Merge one at a time. Once the PRs are open, start a fresh session to pick the order and resolve conflicts. [Intility's Stian Frøystein](https://engineering.intility.com/article/agent-teams-or-how-i-learned-to-stop-worrying-about-merge-conflicts-and-love-git-worktrees) uses that approach and says Claude handles the conflicts well.

```
List the open pull requests in this repo using the gh CLI. For each one, summarize which files it changes. Tell me the safest order to merge them, flag any that will conflict, and resolve conflicts as you merge. Run the tests after each merge and stop if anything fails.
```
The last sentence of that prompt is our addition. Three things still bite: each worktree needs its own install (like `npm ci`), two dev servers on the same port will clash, and a shared database isn't isolated at all. Also, the bottleneck becomes you. Worktrees stop file collisions, not the review queue, so start with two or three agents. When you're done, clean up with `git worktree remove`.

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

### State of Product reveals what AI still hasn’t solved

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/445026fd-cc87-44a5-9688-ed80db4e454e/Screenshot_2026-10-02_at_4.28.33_PM.png?t=1790983719)
Follow image link: (https://www.atlassian.com/software/jira/product-discovery/resources/state-of-product-2027?utm_source=beehiiv_YJ4ZPRQDHV&utm_medium=newsletters&utm_campaign=P%3Ajpd%7CO%3Appm%7CV%3Abeehiiv%7CG%3Aus%7CL%3Aen%7CF%3Aaware%7CT%3Apropecting%7CZ%3Anewsletter%7CI%3Aimc-jpd-ai%7CA%3Aimage%7CD%3Aalld&utm_content=P%3Ajpd%7CO%3Appm%7CV%3Abeehiiv%7CG%3Aus%7CL%3Aen%7CF%3Aaware%7CT%3Apropecting%7CZ%3Anewsletter%7CI%3Aimc-jpd%7CA%3Aimage%7CD%3Aalld%7CU%3Acombined_image-core-brand-default-secondary-1200x600-sop-bento&_bhiiv=opp_6b5c4c63-3c7a-47b0-87af-ba21dd81dd04_24df746c&bhcl_id=7a529676-f84f-4050-a21a-97a13fac5833_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

80% of product professionals say AI helps them ship faster, but customers aren’t seeing value any sooner. [Atlassian’s State of Product 2027](https://www.atlassian.com/software/jira/product-discovery/resources/state-of-product-2027?utm_source=beehiiv_YJ4ZPRQDHV&utm_medium=newsletters&utm_campaign=P%3Ajpd%7CO%3Appm%7CV%3Abeehiiv%7CG%3Aus%7CL%3Aen%7CF%3Aaware%7CT%3Apropecting%7CZ%3Anewsletter%7CI%3Aimc-jpd-ai%7CA%3Aimage%7CD%3Aalld&utm_content=P%3Ajpd%7CO%3Appm%7CV%3Abeehiiv%7CG%3Aus%7CL%3Aen%7CF%3Aaware%7CT%3Apropecting%7CZ%3Anewsletter%7CI%3Aimc-jpd%7CA%3Aimage%7CD%3Aalld%7CU%3Acombined_image-core-brand-default-secondary-1200x600-sop-bento&_bhiiv=opp_6b5c4c63-3c7a-47b0-87af-ba21dd81dd04_24df746c&bhcl_id=7a529676-f84f-4050-a21a-97a13fac5833_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f) explores the gains AI is delivering and the challenges that remain, from decision-making that hasn’t kept pace to gut instinct overriding customer evidence.

_[Read the report](https://www.atlassian.com/software/jira/product-discovery/resources/state-of-product-2027?utm_source=beehiiv_YJ4ZPRQDHV&utm_medium=newsletters&utm_campaign=P%3Ajpd%7CO%3Appm%7CV%3Abeehiiv%7CG%3Aus%7CL%3Aen%7CF%3Aaware%7CT%3Apropecting%7CZ%3Anewsletter%7CI%3Aimc-jpd-ai%7CA%3Aimage%7CD%3Aalld&utm_content=P%3Ajpd%7CO%3Appm%7CV%3Abeehiiv%7CG%3Aus%7CL%3Aen%7CF%3Aaware%7CT%3Apropecting%7CZ%3Anewsletter%7CI%3Aimc-jpd%7CA%3Aimage%7CD%3Aalld%7CU%3Acombined_image-core-brand-default-secondary-1200x600-sop-bento&_bhiiv=opp_6b5c4c63-3c7a-47b0-87af-ba21dd81dd04_24df746c&bhcl_id=7a529676-f84f-4050-a21a-97a13fac5833_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3dda97d8-9517-43e4-9e88-621d16b243bd/image.png?t=1792652179)
Follow image link: (https://x.com/UnitreeRobotics/status/2112819774573179175)
Caption: This is awesome…and scary as well. Just watch the video on X.

* [OpenAI](https://openai.com/index/openai-models-google-cloud/) said its models and Codex are coming to [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers), with GPT-Astra, GPT-6.1 Sol, and GPT-6 Luna in private preview for select enterprise customers.

* OpenAI [expanded ChatGPT ads](https://openai.com/index/chatgpt-ads-expands-26-new-countries/) to 26 more countries, bringing the total to 89, with 100,000+ advertisers; only Free and Go plans show them.

* [OpenAI](https://x.com/OpenAI/status/2112899854569762936), PerturbAI, and Scripps ran 1,946 GPT-Rosalind agents in parallel on [mouse-brain data](https://www.rdworldonline.com/openai-deploys-nearly-2000-gpt-rosalind-agents-to-generate-biological-research-leads-in-32-minutes/) and had ranked drug-target leads in 32 minutes; it's a preprint, and no lab tests yet.

* [LiteLLM](https://docs.litellm.ai/blog/security-incident-oct-21-2026), a popular tool for connecting apps to AI models, confirmed a tampered version was live for two hours on Oct 21; [SafeDep](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/) says it stole credentials.

* [Nvidia](https://nvidianews.nvidia.com/news/openshell-reference-architecture) unveiled OpenShell, a blueprint for walling off AI agents and enforcing rules on what they can touch, with Anthropic, OpenAI, and Microsoft among the first partners.

* [Reuters reported](https://www.investing.com/news/economy-news/openai-president-urges-ai-safeguards-as-group-he-funds-opposes-regulation-4962263) that OpenAI president Greg Brockman and his wife gave $25M to Leading the Future, a group fighting AI rules in 48+ congressional races; OpenAI says it was personal.

Want absolutely EVERYTHING that happened in AI this week? [Click here!](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-thursday-october-22-2026/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

1. _Build an AI-Ready Workplace._ Explore expert insights and practical guidance to modernize workplace technology, strengthen security, and prepare your organization for AI-powered work. [Explore the Hub](https://www.techrepublic.com/hubs/the-ai-ready-workplace-hub/)

2. [Notion Auto](https://www.producthunt.com/products/notion-99) sends each Notion agent task to a cheaper or stronger model as needed, which Notion says stretches your credits about 10x.

3. [UseIt Studio](https://www.producthunt.com/products/useit-studio-from-idea-to-delivery) turns a one-sentence idea into an editable design file for stickers, pins, or gift boxes, complete with bleed and cut-and-fold lines.

4. [Penmentor](https://github.com/AbdullahAlHariri/penmentor) marks up your handwritten calculus like a teacher, circling the first real mistake and giving hints (Linux only, needs Claude Code).

5. [Omnara](https://github.com/omnara-ai/omnara) runs your AI agents on your own machine or a cloud sandbox and saves their progress, so a crash doesn't wipe the job.

6. [Renor](https://github.com/patrickpassosb/renor-engine) lets Claude Code and other coding agents search a folder of your Markdown notes, so they recall past decisions without you re-explaining.

7. [Opposable](https://getopposable.com/blog/computer-use-on-the-phone) lets an AI agent tap and type through your Android apps, with a small on-phone model as backup (weaker on unfamiliar apps, per its makers).

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

## UPCOMING EVENT: The Neuron IRL in San Francisco

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/14f81cf0-9588-4212-b67d-2edfdd8aa8e0/neuron-live_2spnsr_Newsletter_1200x600.png?t=1792516902)
Follow image link: (https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)
Caption: 

The Neuron is **going IRL** on **[November 18 at 4:30 PM PT](https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)**! Join us in San Francisco for **drinks, bites, special guests, and a live recording of The Neuron podcast.** Huge thanks to Slack and Alumni Ventures for making it happen.

**It’s free, but space is limited. Save your spot!**

RSVP for The Neuron IRL (https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 🖼️ Thursday Trivia

You know the drill! One of these is AI, and one is real. Which is which? 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4a6dc60a-848f-4cdf-bca0-25a0207be9a2/image.png?t=1792658272)
Caption: 

**A**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/aa0e4589-0c64-40d7-bd92-9724c2160807/image.png?t=1792658381)
Caption: 

**B**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/833ddfcb-dbb4-4798-925c-3daec62310b9/TN_Thumbnail_102126_AlexKsendzovsky_JonPomeraniec_A.png?t=1792524184)
Follow image link: (https://www.youtube.com/watch?v=8c6KLMT1n7U)
Caption: Click the image to watch the video.

New episodes air **every week** on Wednesdays: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)

_Special shout out to __[Mercor](https://www.mercor.com/apex/?utm_source=theneuron&utm_medium=podcast&utm_campaign=apex&utm_term=gold&utm_content=10_21)__ for sponsoring this episode! _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/edb744f1-04b4-4230-94c8-3a48bf609cd7/A_Cat_s_Commentary_x_2025_-_2026-09-23T133451.309.png?t=1790195910)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

**Trivia Answer: **[A is AI](https://www.reddit.com/r/aivideo/comments/1xc83vp/minimax_h3_music_video_falling_fast/), [B is real](https://www.youtube.com/watch?v=dKoxfDKamZE)

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today!




**Btw: **We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.S. **Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/new-claude-duet-works-while-your-phone-s-off
