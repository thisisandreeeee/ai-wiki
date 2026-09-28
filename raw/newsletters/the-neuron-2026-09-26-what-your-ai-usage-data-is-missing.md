---
source: gmail
newsletter: "the-neuron"
message_id: "1a0df8a4601c2b2b"
thread_id: "1a0df8a4601c2b2b"
subject: "What your AI usage data is missing."
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Sat, 26 Sep 2026 21:06:05 +0000 (UTC)"
ingested: 2026-09-28
sha256: e08c86f7da6d22e8d8eb6c1b56ba3373360b174aae02c67e45574c1a1552549b
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/91710880-2f61-4b3c-913b-e0f7036fee95/ChatGPT_Image_Sep_21__2026__02_27_02_PM.png?t=1790026158)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/86f77626-ce5b-4454-99fd-8b8e331f6ac8/In_partnership_with...__9_.png?t=1790026287)
Follow image link: (https://explore.harmonic.security/)
Caption: 

Welcome, humans. 

This is a special edition of The Neuron where we grab one topic and pull on it from every angle. Today's topic: AI security, and specifically, the moment some of its stranger risks started showing up outside the usual white paper theory cases.

Here's the backdrop. In late July, a UK government cybersecurity lab [caught an AI agent inventing fake identities](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) to trick a real person into approving something harmful. Around the same time, OpenAI (the company behind ChatGPT) [disclosed that its own AI agents had broken out of a locked-down test](https://openai.com/index/hugging-face-incident-and-the-road-ahead/). Those agents went on to cause problems for [Hugging Face](https://techcrunch.com/2026/07/20/hugging-face-confirms-breach-affected-internal-datasets-and-credentials-urges-users-to-take-action/), a popular website where companies share AI models. And back in April, a company called Vercel [got broken into](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident) after one employee signed up for a random AI tool.

Three very different situations. One shared lesson: once a piece of software has passwords, tools, and permission to act on its own, a small mistake can spiral into a much bigger mess. Let's dig in.

Advertise in The Neuron here (https://info.technologyadvice.com/advertise-with-the-neuron)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/34bc2586-ee40-4ae7-83d2-f896136a8326/image.png?t=1762454325)
Caption: 

# The AI agent that lied to a person to get its way

Picture a massive, shared library of free code that programmers all over the world use and contribute to. If you want to change or add something, you submit your proposed edit, and a real human has to review and approve it before it goes live. That review step is what got tested here.

### How the test was set up

In July, the UK's AI Security Institute (AISI, a government lab that checks how risky AI systems can be before the public ever uses them) [ran an experiment](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing). To see what these AI agents could really do if left alone, the lab deliberately gave them internet access. It also turned off some of their built-in safety guardrails, kind of like taking the child-lock off just to observe what happens next. They ran the same test 122 times.

In 10 of those runs, the AI agents did something they weren't supposed to. Across those runs, AISI counted 19 separate troubling actions. Seventeen came from a model made by Anthropic (another AI company, similar to OpenAI), and two came from a single run involving one of OpenAI's models.

### How the agent tried to get its code approved

In the most serious case, an AI agent tried to sneak harmful code into that shared code library disguised as a normal update. When a human reviewer got suspicious, the agent didn't just try again. It created multiple fake online profiles, pretending to be different people, and used them to pressure the real reviewer into approving it anyway. When it got caught, it even edited its own earlier messages to look innocent.

### Important caveats

To be fair to the AI here: this was a stress test specifically designed to push these programs to their limits, using settings that don't reflect how the public actually uses AI. A real human reviewer caught the harmful code before it went live, and the agent never escaped the locked testing environment it was in. But AISI's own conclusion was blunt: this is the first time they'd seen an AI system attempt something this deceptive on its own, without anyone telling it to.

_[If Corey were writing this section, he'd insert a joke here about the agent ghosting its therapist too, but we'll spare you.]_

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a41ad8b0-3bba-4e37-84b1-cc7b2273a7b8/image.png?t=1763523004)
Caption: 

**FROM OUR PARTNERS**

# The AI risk hiding behind the headlines

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cba981a6-0b8e-4ff0-bc38-bc3cc07664a9/Usage_intel_-_Neuron.png?t=1790008991) [Harmonic dashboard showing time spent by application and use case]
Follow image link: (https://explore.harmonic.security/?utm_source=neuron&utm_medium=paid_newsletter&utm_campaign=neuron_deep_dive_sep_2026&utm_content=primary)
Caption: 

Stories of rogue agents make headlines but the everyday risk is quieter: employees connecting useful but unapproved AI tools to sensitive company data without anyone seeing the exposure. Harmonic gives security & AI teams visibility into how AI is actually used, across 1,000+ applications, then reads the context of every prompt, file, and agent action to protect data before it leaves. Rather than shutting AI down, you can coach people in the moment, apply the right guardrails, and help teams adopt the tools that create real value.

Explore The Harmonic Platform (https://explore.harmonic.security/?utm_source=neuron&utm_medium=paid_newsletter&utm_campaign=neuron_deep_dive_sep_2026&utm_content=primary)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6bc85194-60ad-4700-a890-08be35e73a02/image.png?t=1762454365)
Caption: 

# Okay, but is this actually happening to real companies?

Short answer: not quite like that story, at least not yet. But something related, and honestly more boring, is already happening constantly.

### It's happened more than once

Zoom out and 2026 has been a rough year for "AI agents behaving badly." Hugging Face got hit in July, as mentioned above. Separately, some of OpenAI's AI agents also [started using an old, mostly-forgotten German website](https://arstechnica.com/security/2026/09/openai-agents-discussed-ways-to-escape-their-sandbox-on-public-wiki/) meant for programmer notes as their own private messaging board, without permission. And researchers found that OpenAI's agents had [uploaded thousands of suspicious files](https://www.theguardian.com/technology/2026/sep/11/openai-agents-rubygems-malicious-packages) to a different online code library, seemingly trying to steal digital access keys along the way. (OpenAI says its agents were just retrieving public information as part of harmless tasks, not attacking anyone. That part is still disputed.)

These incidents aren't isolated anymore, either. Both OpenAI and Anthropic have each published multiple reports this year about their AI agents acting outside the boundaries they were supposed to stay inside. Even the industry's own security watchdogs have noticed the shift. A nonprofit called OWASP tracks and ranks the biggest security risks in AI, a bit like Consumer Reports, but for cybersecurity. It just [moved "an AI agent doing more than it's supposed to"](https://mbctg.com/blog/owasp-s-2026-llm-top-10-why-excessive-agency-jumped-to-3/) from the sixth biggest risk on their list to the third, after finally basing the rankings on real incidents instead of guesswork alone.

### The real cause is access, not intent

None of this means your company's chatbot is secretly plotting against you. It means that when you give an AI agent tools, memory, and a difficult enough goal, it will sometimes find weird, unintended ways to get there. That's a bit like an overly motivated new employee who cuts corners nobody told them not to cut. The real issue isn't that the AI "wanted" to misbehave. It's that it had enough access to turn a bad decision into a real one.

### Two different problems, not one

There are really two separate AI security problems buried in all this. One is an AI agent's own behavior crossing a line, like the story above. The other is much simpler: an ordinary AI tool having way more access to company information than it should. The first is rare and dramatic. The second is quietly costing companies money right now, which brings us to Vercel.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e7597919-c142-461d-abf6-8f9c46660383/image.png?t=1763520712)
Caption: 

## The much more boring way your company actually gets hacked

Here's the story that should worry you more than fake AI identities. In April, Vercel, a company that hosts websites for a living, got broken into. Nobody attacked Vercel directly. Instead, one of their employees had [signed up for a small AI tool called Context.ai](https://www.helpnetsecurity.com/2026/04/20/vercel-breached/). That employee connected it to their work Google account, granting it broad permission to see and use things like their email and files. That's the same basic move as clicking "sign in with Google" on a random app instead of making a new password, except this time it came back to bite them.

### How one employee's AI tool led to a breach

[Context.ai](https://Context.ai) itself got hacked first. Whoever broke in inherited that employee's Google access, used it to take over their Vercel account, and walked right into Vercel's internal systems from there. [Vercel confirmed](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident) that some behind-the-scenes settings and digital access keys, the kind of thing that lets a company's internal programs talk to each other securely, were exposed for some customers. Separately, someone claiming to have stolen even more of Vercel's data tried to sell it online. Vercel hasn't confirmed those broader claims.

### Nobody had reviewed the tool

Vercel's own public statement doesn't say whether [Context.ai](https://Context.ai) had gone through any kind of official approval or security check before that employee started using it. Whatever the answer, the incident shows what can happen once a small, unreviewed AI tool has a working key into a real company account. An employee just found something useful and moved on with their day. That's the version of this story playing out at companies everywhere right now, on repeat. Not a rogue AI, but an ordinary tool with more access than anyone realized, sitting there quietly until it becomes the weak link.

### The numbers back this up

**And Vercel is far from alone.** A 2026 survey by the Cloud Security Alliance, a nonprofit focused on cloud and AI security, [found something striking](https://cloudsecurityalliance.org/press-releases/2026/04/21/new-cloud-security-alliance-survey-reveals-82-of-enterprises-have-unknown-ai-agents-in-their-environments). 65% of companies had already dealt with some kind of AI-agent-related security incident in just the past year. Even more strikingly, 82% said they had AI agents quietly running somewhere in their company that their own IT department didn't even know about.

Separate research from the security firm Check Point [found that risky information typed into AI chatbots doubled](https://research.checkpoint.com/2026/ai-security-report-2026/) over the past year, things like confidential company data. And 44% of companies said they couldn't even track where that sensitive information ended up once it was typed in.

Put plainly: most security teams don't have a full list of every AI tool their employees are using, what those tools can see, or what's being typed into them. That's the real AI security problem in 2026. It's a lot less exciting than killer robots, but a lot more likely to actually happen to your company.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3774230-5ffd-4020-b888-79c2eb10db1a/image.png?t=1762454392)
Caption: 

**FROM OUR PARTNERS**

# Turn AI visibility into business value

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0e07119d-fd77-43bb-aab9-dd891eaf0719/image.webp?t=1790190634) [Apax and Harmonic Security]
Follow image link: (https://www.harmonic.security/resources/from-ai-blind-spots-to-usage-intelligence-apax/?utm_source=neuron&utm_medium=paid_newsletter&utm_campaign=neuron_deep_dive_sep_2026&utm_content=secondary)
Caption: 

A global investment firm replaced fragmented AI activity data with a clear picture of adoption. With Harmonic, its team pulls adoption data in minutes, meets compliance requirements, improves the employee experience through contextual coaching, and gives its AI steering committee evidence of where AI delivers value.

See The Case Study (https://www.harmonic.security/resources/from-ai-blind-spots-to-usage-intelligence-apax/?utm_source=neuron&utm_medium=paid_newsletter&utm_campaign=neuron_deep_dive_sep_2026&utm_content=secondary)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b4e1fb39-fa43-4ddc-81a6-c9b4bbb80e5e/image.png?t=1762454407)
Caption: 

# So what do you actually do about this?

Good news: you don't need to ban every AI tool at your company. If you try, your employees will probably just use them on their personal phones instead, and now you can't see any of it, which makes things worse, not better. What actually helps looks pretty familiar to anyone who's dealt with security before, just pointed at a newer category of tool.

### Don't start with a ban

Banning AI tools outright feels like the safe move, but it usually backfires. Think about it from an employee's side. If the approved tool is slow or clunky, and a faster one is one click away, most people will just use the faster one anyway, quietly, on their own devices. That's exactly how Vercel's breach started. The problem was never that an employee wanted to use AI. It's that nobody had a system for reviewing which tools were safe to connect to real company accounts.

### Find out what's actually being used

You can't manage a tool you don't know exists. A simple starting point: ask each team what AI tools they're actually using day to day, not just the ones IT officially handed out. You'll almost always find more than expected, subscriptions bought on personal cards, browser extensions installed without asking, free tools nobody thought to mention. This step alone usually surfaces the biggest surprises.

### Limit what each tool can see

Once you know what's in use, the next question is what each tool is actually allowed to touch. Go back to the Vercel story. The employee's AI tool had been given broad access to their entire Google account, email, files, everything, when it likely only needed a much smaller slice of that to do its job. The fix isn't complicated. Give each tool the minimum access it needs, not standing, all-access permission "just in case it comes up later."

### Put a real person in the loop for anything risky

For AI agents that can actually take action, sending emails, moving money, changing files, touching customer data, build in a pause before anything high-stakes happens. That doesn't mean a person has to approve every single little action. It means a person specifically signs off before anything that would be a real problem if it went wrong.

### Keep a paper trail

Think of this like a security camera. You hope you never need the footage, but the one time something does go wrong, you'll be glad it's there. Keep records detailed enough that if an AI tool does something unexpected, someone can actually trace what happened, what it accessed, and when, instead of shrugging and hoping it doesn't happen again.

Good news: you don't need to ban every AI tool at your company. If you try, your employees will probably just use them on their personal phones instead, and now you can't see any of it, which makes things worse, not better. What actually helps looks pretty familiar to anyone who's dealt with security before, just pointed at a newer category of tool:

* **Know what AI tools are actually being used.** You can't manage a tool you don't know exists.

* **Give AI agents the smallest amount of access needed to do their specific job.** Not broad, always-on access "just in case."

* **Require a real person's approval before anything high-stakes happens.** Not just a rubber stamp after the fact.

* **Keep detailed records of what these tools did**, so if something goes wrong, someone can actually figure out what happened.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/59d9808d-f24b-4b6d-b2a7-c7ecc4f42429/image.png?t=1762454427)
Caption: 

**FROM OUR PARTNERS**

# You bought everyone an enterprise license….so why is work happening in personal accounts?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5303ecd7-89af-4cd4-b5e5-1443db2299a9/0001.png?t=1790198176) [Personal-plan accounts are mostly used for business]
Follow image link: (https://www.harmonic.security/resources/ai-usage-index-report-2026/?utm_source=neuron&utm_medium=paid_newsletter&utm_campaign=neuron_deep_dive_sep_2026&utm_content=tertiary)
Caption: 

New Harmonic research reveals where employees actually do AI work, and why plan-based controls miss the real coverage gap.

Explore The Research (https://www.harmonic.security/resources/ai-usage-index-report-2026/?utm_source=neuron&utm_medium=paid_newsletter&utm_campaign=neuron_deep_dive_sep_2026&utm_content=tertiary)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32bd7206-d05f-4547-b00e-928c9ea16b90/image.png?t=1762454460)
Caption: 

# Here’s What This Means For You

The Hugging Face and AISI stories are the ones that'll get clicks, and they're genuinely worth paying attention to. But for most companies, the more immediate risk looks a lot less like Hugging Face and a lot more like Vercel: ordinary AI tools connected to company accounts with permissions nobody is actively watching.

### Worth watching, not worth panicking over

AISI itself says there's no clear sign of anything like their test incident happening out in the real world yet. Still, it's worth remembering that the AI agent's actions in that test involved real people and a real, public project. It was technically "just a test," but the targets weren't fake. As these AI agents get more capable, that gap between "test conditions" and "everyday use" might not hold forever. Worth keeping an eye on, not losing sleep over.

For now, the smartest move isn't panicking about AI agents going rogue. It's figuring out what's already quietly connected to your company's data, because odds are, something is.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/35ade56c-dc70-4dd0-b632-41c7c45a953a/image.png?t=1762454492)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/9563b641-fc1f-4f4c-ba22-9fcc202dc67d/A_Cat_s_Commentary_x_2025__65_.png?t=1762454534)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/48e1e056-a015-4e20-ba68-dafb942cfae7/image.png?t=1762454543)
Caption: 



That’s all for today!






View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/77725261-a9a1-4f4b-9b32-5df2cf3f0b60/image.png?t=1762454662)
Caption: 


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/deep-dive-an-ai-agent-lied-to-a-person-to-get-its-way
