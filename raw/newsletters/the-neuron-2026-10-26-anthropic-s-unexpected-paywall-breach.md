---
source: gmail
newsletter: "the-neuron"
message_id: "1a177b5730ace3d8"
thread_id: "1a177b5730ace3d8"
subject: "😺 Anthropic's unexpected paywall breach"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Mon, 26 Oct 2026 10:15:41 +0000 (UTC)"
ingested: 2026-11-02
sha256: e9ce8b1e152e52e340b1af80bb27568ab3103c4bc7a19b38a12f2b3fc35e1453
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f687b254-a4f3-4060-9b0c-6aa95e453720/Claude_Crosses_the_Georgia_Election_Paywall.png?t=1792999887)
Caption: 

Okay, so apparently the people building AI assistants are now asking religious scholars how those assistants should behave. Which, given how often chatbots confidently improvise, might be overdue.

The Associated Press reports that Anthropic consulted scholars and representatives from more than 15 religious and cross-cultural groups. Other tech companies have also spoken with Vatican officials. They want input on values such as fairness, judgment, and responsibility. _Imagine explaining centuries of philosophy to an AI whose favorite answer is still 'Sure, absolutely.'_

The difficult question? Different traditions disagree. Scholars warned that reducing them to one convenient list risks distorting what people actually believe. _The world's longest-running group project just got a new participant._

**Here’s what happened in AI today:**

* 🙀 Claude crossed a Georgia election-data paywall without authorization.

* 📰 Apollo found little AI payoff beyond Big Tech.

* 📰 Palo Alto retracted a PHP2Shell breach attribution.

* 🍪 Moonshot introduced the Kimi K3.1 Pro model.

* 🎓 Build an AI assistant to track job applications.

... and a **[whole lot more that you can read about here](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-monday-october-26-2026/)**

Advertise to 700K readers of The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

We’re rounding up Black Friday and Cyber Monday deals for a special edition of The Neuron, and your brand can grab a sponsored spot in front of 700,000 subscribers. [Reach out for details!](https://solutions.technologyadvice.com/lp/advertise-in-black-friday-newsletter/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🙀 Anthropic Says Claude Bypassed a Paywall on Georgia Election Data Without Being Asked

Picture handing an AI assistant a statistics project, then finding out it pulled numbers from a paid government dashboard. Nobody told it to skip the fee. _The coworker who “just figured it out,” except this one has API access._

Anthropic says that’s roughly what happened inside the company, and [Axios broke the story](https://www.axios.com/2026/10/25/anthropic-claude-georgia-voter-data) Sunday.

Here’s what we know:

* Claude was working on an internal statistics project that pulled public data.

* Without being asked to, the model requested a token to query a Georgia dashboard whose data the state normally sells for a fee.

* It pulled aggregate vote counts. Anthropic says it never touched the state’s voter registration system or changed or pulled any voting records.

* Georgia officials and Anthropic both say the model got past the paywall without authorization.

Now the technical bit. A token is a digital credential, kind of like a festival wristband. The gate checks the wristband, not your intentions, and the wristband decides which areas you can enter. APIs are the connections software uses to ask other software for data, and tokens are how those connections know who’s allowed in.

So if an agent gets a token for the paid area, the request works perfectly. The system says yes. But “the request succeeded” and “someone authorized this” are two different things. Axios doesn’t say how the model got the token or why the dashboard honored it, and that’s the part we most want answered.

It also shows why agents are a different animal from chatbots. A chatbot answers questions. An agent takes actions, hits walls, and picks its next move. Give it a goal like “finish this analysis,” and it may find a route around a wall nobody thought to guard. _Turns out “get the data” is a very open-ended instruction._

Keep the stakes in proportion. The data was public and aggregate, and nothing was altered, so this isn’t an election-tampering story. It does land ahead of the midterms, though, and Axios notes that Anthropic and OpenAI have [kept disclosing](https://www.axios.com/2026/09/26/openai-anthropic-thousands-ai-security-incidents) agents taking unintended actions.

On disclosure, Anthropic says it told Georgia’s secretary of state and the White House weeks ago and has added mitigations to block this kind of action. A source familiar told Axios that administration officials urged Georgia to go public sooner and were ignored.

The lesson for any company running agents: telling an AI “don’t” is a request, not a wall. Walls are limited credentials, explicit access rules, logs, and approval checks that don’t depend on the model choosing to behave. _“We asked the bot nicely” is not a security audit._

What to watch: whether labs can show, for any agent run, what it was allowed to do, what it actually tried, and where their systems stopped it.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

### The AEO work, without the AEO hire.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/9931e628-b5d7-4403-92be-4081f6bae085/Secondary_1.png?t=1791169556)
Follow image link: (https://chatfeatured.com/?source=beehiiv&utm_campaign=YJ4ZPRQDHV&utm_source=beehiiv&_bhiiv=opp_d29029fc-d97b-4035-b00d-00afe10825f7_b89c8c00&bhcl_id=3a650394-e0c3-4cd6-bfd3-5d42fd915422_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

Most AI visibility tools show you where you rank, then leave the work to you.

[ChatFeatured](https://chatfeatured.com/?source=beehiiv&utm_campaign=YJ4ZPRQDHV&utm_source=beehiiv&_bhiiv=opp_d29029fc-d97b-4035-b00d-00afe10825f7_b89c8c00&bhcl_id=3a650394-e0c3-4cd6-bfd3-5d42fd915422_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f) is an AI search agent that does it: finds the questions competitors win, drafts the content in your voice, and tracks the lift. 

Your team decides what ships. Month to month.

_[Try the agent, today.](https://chatfeatured.com/?source=beehiiv&utm_campaign=YJ4ZPRQDHV&utm_source=beehiiv&_bhiiv=opp_d29029fc-d97b-4035-b00d-00afe10825f7_b89c8c00&bhcl_id=3a650394-e0c3-4cd6-bfd3-5d42fd915422_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Let Zapier Track Your Job Applications For You

Job hunting is exhausting enough. Then you also have to remember who you contacted, who replied, when the interviews are, and which recruiter needs a nudge. _Apparently, finding a job means becoming your own unpaid recruiting coordinator._

Zapier (an app that connects your other apps, so one event can set off another) has a [job application tracking approach](https://zapier.com/automation/use-case/using-ai-manage-job-application-statuses-and-followups) that takes most of this off your plate. Its first template reads a new Gmail message, has AI pull out the status and dates, and adds a row to a spreadsheet. The second waits until a set date, has AI write the message, and sends it through Gmail.

This works because job emails are messy. Confirmations, rejections, and interview invites all look different, so a simple sorting rule can’t handle them. AI reads each one the way a person would and fills in the same columns every time, and the spreadsheet becomes your memory.

Here’s our version, built on those templates (a Zap is one automation, and a trigger is the event that starts it):

1. **Monitor: **Create a Gmail label called Job Search (Gmail’s version of a folder tag) and tag your job emails with it. Use Zapier’s New Labeled Email trigger, then add AI by Zapier to extract company, role, status, deadlines, and next actions. The label means Zapier only reads tagged emails, not your whole inbox.

2. **Track: **Make a Google Sheet with company, role, status, last contact, and follow-up date. Have Zapier find the matching row, update it, or add a new application.

3. **Follow-up: **Run another Zap every weekday. When a follow-up date arrives and no response is recorded, have AI draft a personalized Gmail message and send you a reminder.

Paste this into the AI by Zapier step, swapping [EMAIL CONTENT] for the email body from your Gmail step:

```
You are my AI job-search assistant. Analyze this email: [EMAIL CONTENT]. Extract company, job title, email type (alert, confirmation, interview, rejection, follow-up), application status, dates, next action, and job fit using [JOB CRITERIA]. Mark unknown details Unknown. Never invent deadlines or statuses. Return structured fields for a tracker.
```
“Mark unknown details Unknown” matters more than it looks. Without it, the AI may fill empty columns with a plausible guess, and a made-up deadline in your tracker is worse than a blank.

Keep outgoing messages as drafts so you review them before anything goes out, and double-check interview dates against the original email. Then you can spend less time maintaining spreadsheets and more time preparing for interviews. _Preferably the kind that end in an actual paycheck._

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

### The Hidden Cost of Fast AI Answers

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/9d47ec5f-59a9-42e8-9da3-e4b3a08573d5/1200x627__NewConcept.png?t=1790093709)
Follow image link: (https://front.com/resources/coordination-gap?utm_source=beehiiv&utm_medium=cpm&utm_campaign=ongoing_YJ4ZPRQDHV_consideration_norpac&utm_content=HBR_Report_V2&_bhiiv=opp_275d34de-a5b7-463a-bf16-b69c300041c1_c408311b&bhcl_id=98e938cd-4919-4202-8891-307109bd58a5_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

A fast AI answer isn't always a coordinated one. When AI resolves B2B issues without looping in the teams responsible for them, confidence outpaces alignment. A new [Harvard Business Review Analytic Services](https://front.com/resources/coordination-gap?utm_source=beehiiv&utm_medium=cpm&utm_campaign=ongoing_YJ4ZPRQDHV_consideration_norpac&utm_content=HBR_Report_V2&_bhiiv=opp_275d34de-a5b7-463a-bf16-b69c300041c1_c408311b&bhcl_id=98e938cd-4919-4202-8891-307109bd58a5_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f) briefing paper, sponsored by Front, looks at closing that gap.

[Read the Briefing Paper](https://front.com/resources/coordination-gap?utm_source=beehiiv&utm_medium=cpm&utm_campaign=ongoing_YJ4ZPRQDHV_consideration_norpac&utm_content=HBR_Report_V2&_bhiiv=opp_275d34de-a5b7-463a-bf16-b69c300041c1_c408311b&bhcl_id=98e938cd-4919-4202-8891-307109bd58a5_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

1. **Build an AI-Ready Workplace: **Explore expert insights and practical guidance to modernize workplace technology, strengthen security, and prepare your organization for AI-powered work. [Explore the Hub.](https://www.techrepublic.com/hubs/the-ai-ready-workplace-hub/)

2. [Kimi K3.1 Pro](https://www.kimi.ai/), Moonshot AI's new model, targets complex coding and AI agent tasks, with open weights promised for November 4.

3. [ThinkRail](https://github.com/JetBrains/thinkrail), JetBrains' open-source AI coding workspace, keeps project specifications updated and lets developers review changes in separate workspaces.

4. [Specsight](https://specsight.app/) turns code changes into plain-English feature explanations and release updates for sales and support teams.

5. [CaseCite](https://www.casecite.co/) searches case law and private legal documents with AI-generated answers linked to their sources, though you'll need to host it yourself.

6. [AgentGrid.io](https://agentgrid.io/) gives people and AI agents a shared workspace for creating documents, slides, and reports with version history.

7. [WriterzRoom](https://www.writerzroom.com/) uses specialized AI agents to research, draft, and check business documents before your team reviews them.

8. [TwinMind](https://twinmind.com/) transcribes and summarizes meetings, then lets you ask AI questions about saved conversations across your devices.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/54d14b50-d342-4ee6-adda-4b353e861da2/image.png?t=1793003449)
Follow image link: (https://x.com/elvar_official/status/2114325660248281265)
Caption: Just look at the detail of Kimi vs. GPT. Same sandworm prompt: Kimi K3.1 Pro covered every ring in panels, while GPT-6 Astra stacked grey tubes. Moonshot released it Friday at roughly 80% below Astra’s API rates, with open weights due November 4. _One prompt isn’t a benchmark, but wow._

1. [We tested](https://www.theneuron.ai/guides/microsoft-surface-laptop-ultra-review-the-local-ai-performance-is-remarkable/) Microsoft’s $5,899.99 Surface Laptop Ultra, and its NVIDIA chip ran a compressed 120B-parameter AI model entirely on the laptop at 33 tokens (word chunks) per second.

2. [Apollo economist Torsten Slok](https://www.apollo.com/wealth/insights-news/insights/daily-spark/no-signs-of-ai-payoff-outside-the-tech-sector) found revenue per worker and margins broadly flat outside the seven largest tech stocks.

3. [Palo Alto Networks Unit 42](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/) retracted its attribution of a government breach to two PHP2Shell flaws; the underlying risks remain.

4. An [advisory group of mathematicians](https://terrytao.wordpress.com/2026/10/25/disadvantages-of-designating-mathematicians-for-ai-output-releases/) urged public evidence, disclosed prompts, and independent review of AI-generated math claims.

5. [Dermatologist Mike Lynch](https://lynchlab.net/llm-skin-cancer) found a fine-tuned older vision model outscored frontier LLMs on 200 selected skin lesions; clinical effectiveness was not tested.

6. [Max Woolf's analysis](https://minimaxir.com/2026/10/cheap-llms/) found rapidly declining model API prices as open-weight competition increased.

7. [OpenAI](https://www.theneuron.ai/news/openai-frontier-training-offline-simulations/) resumed frontier agent training without live internet access, using cached web content, according to a newly published Neuron report.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

## UPCOMING EVENT: The Neuron IRL in San Francisco

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ffcec634-8d32-4117-b1be-c04c45a0f74c/NeuronLive_Social_1200x675.png?t=1791478412) [The Neuron Live San Francisco event]
Follow image link: (https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)
Caption: 

The Neuron is **going IRL** on **[November 18 at 4:30 PM PT](https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)**! Join us in San Francisco for **drinks, bites, special guests, and a live recording of The Neuron podcast.** Huge thanks to Slack and Alumni Ventures for making it happen.

**It’s free, but space is limited. Save your spot!**

RSVP for The Neuron IRL (https://web.cvent.com/event/f317126e-63dc-4fd0-aa5a-574829de2481/summary?utm_source=podcast&utm_medium=promotion&utm_campaign=theneuronIRL)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 😹 Monday Meme

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/eed9829a-7819-4b87-b4ad-03a7fbc0e556/image.png?t=1793004411)
Caption: AI can take our jobs, but it has to leave us the cat riding a Roomba in a shark costume.



View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/833ddfcb-dbb4-4798-925c-3daec62310b9/TN_Thumbnail_102126_AlexKsendzovsky_JonPomeraniec_A.png?t=1792524185)
Follow image link: (https://www.youtube.com/watch?v=8c6KLMT1n7U)
Caption: Click the image to watch the video.

New episodes air **every week** on Wednesdays: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/31252f2d-38a3-44cc-8b1c-1db87d373a85/A_Cat_s_Commentary_x_2025_-_2026-09-28T162641.618.png?t=1790640264)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today!




**Btw: **We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.S.** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/claude-crossed-a-paywall-on-its-own
