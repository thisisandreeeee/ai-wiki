---
source: gmail
newsletter: "the-neuron"
message_id: "1a0300db6c0c1191"
thread_id: "1a0300db6c0c1191"
subject: "😺 Sam Altman: \"dear peasants\" isn't a good AI pitch"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Sun, 23 Aug 2026 19:16:22 +0000 (UTC)"
ingested: 2026-08-24
sha256: 88549fd5e08bcaca7c3ac4c8fb1a440286474427f120ee26dae063141b4b0dc8
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/92abfa98-ca3f-42ad-8e53-ee4ddb5c9869/Gemini_Generated_Image_ftzus5ftzus5ftzu.png?t=1775272660)
Caption: 

Welcome, humans.

So the datacenter backlash discourse has taken a turn for the worse, with knives coming out on all sides trying to explain away why people hate them so much. 

Sam Altman went on [David Senra’s podcast](https://www.youtube.com/watch?v=kG8AoExkX40) and addressed some of the industry’s messaging directly: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/41f608c4-408d-447d-a091-56a8bea219b9/Screenshot_2026-08-23_at_10.49.47_AM.png?t=1787507431)
Follow image link: (https://www.youtube.com/watch?v=kG8AoExkX40)
Caption: 

He said a lot of AI builders _(subtext for really, mainly Dario)_ have spent years talking about extinction risk and disappearing jobs, then “have not as a field done a very good job” explaining the benefits or how the downsides could be mitigated. His preferred pitch is much more human: AI should give people “more power and personal freedom,” and he thinks it could create “the greatest boom in people starting smaller businesses that we have ever seen.”

The internet immediately stress-tested that argument. [Andrew Curran](https://x.com/AndrewCurran_/status/2091546008165736722) highlighted Altman’s admission, while [Nikola Jurkovic](https://x.com/nikolaj2030/status/2091550683447373868) argued the problem isn’t messaging so much as people rejecting the underlying risk-and-trust bargain. 

Altman’s own parody of the industry’s current pitch [started with:](https://youtu.be/kG8AoExkX40?si=lbUUePp9ppJuuONK&t=2553) “dear peasants, we will bequeath upon you these gifts…” before joking that AI builders would make the decisions. _Okay yeah, maybe workshop that one._

IMO, this is not a messaging issue: this is a “people are afraid of losing their freedom” issue, and that has to be addressed at both the policy level (_what we doing ‘bout this, government?) _and the product level (_how do you make your AI products help people, not replace them?) _so that everyone is _actually_ _more empowered_ by this technology’s upside and protect from its downsides. 

The industry needs to Solve _THAT. _Not _“messaging.” The actual PROBLEM. _

**Here’s what happened in AI this weekend:**

* 😺 Instinct kept email records after users disconnected Google.

* 📰 DeepSeek added vision to its bargain Flash model.

* 📰 Open models led Aikido’s fresh cyber bug test.

* 📰 NVIDIA’s AVO cleared ARC-AGI-3’s public set.

* 🎓 Turn your notes to your AI into actual reusable skills. 

…and a **[whole lot more in the latest full Around the Horn digest](https://theneuron.ai/digest/everything-that-happened-in-ai-today-friday-august-21-2026/)**.

Advertise in The Neuron here! (https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😿 Silicon Valley loves Instinct. Its delete button just caught up.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/54a020e0-26aa-46d6-b6bb-aac0b95f4264/Screenshot_2026-08-23_at_10.10.32_AM.png?t=1787505911)
Follow image link: (https://x.com/clairevo/status/2090929592853037078)
Caption: 

The next generation of AI agents are getting really useful… by knowing a slightly terrifying amount about you.

The new agent [Instinct](https://instinct.co/) may be the clearest early example: Alex Heath’s [Sources.news](https://sources.news/p/two-new-ai-assistants-have-silicon) says the invite-only personal agent has Silicon Valley buzzing, while [Digg](https://digg.com/tech/9ban0heh) highlighted investors calling it a standout personal assistant.

Investor [Sheel Mohnot](https://x.com/pitdesi/status/2090579987778937159) described Instinct as “OpenClaw for normal people” after using it for doctors, bills, travel, tolls, and other life admin. That magic comes from access: Instinct can connect to email, messages, your screen, audio, location, and other apps so it can act proactively.

_And then Claire Vo started poking around behind the scenes…_

**Here's what happened:**

* [Claire Vo](https://x.com/clairevo/status/2090970541557698755) found that disconnecting Google stopped future access but did not erase full email copies Instinct had already synced into its own records.

* After her post, [Vo said](https://x.com/clairevo/status/2091191049041715403) the Instinct team called this a gap they would close ASAP and pushed a new deletion tool overnight.

* The new tool deletes synced data collected to date while preserving conversation history and generated memory, which Vo said makes sense for how the assistant works.

* Her earlier testing also showed Instinct could package retained records and send them elsewhere when prompted, illustrating how powerful persistent agent memory can become.

**FYI: **Instinct’s [privacy notice](https://instinct.co/privacy-policy) says the assistant can access screen contents, private communications, credentials, payment data, and health information when enabled, and says Google Workspace data is not used to train its models. Its separate [terms](https://instinct.co/terms) grant a broad license to user-provided materials, subject to those Google-data restrictions.

**Our take:** This is a data-management lesson for ANY AI tool you use. “Disconnect access,” “delete synced data,” “delete generated memory,” and “delete my account” are different controls, and you should pay attention to the difference.

And before connecting an agent to ANY sensitive data source, know what it can read, what it keeps, how deletion works, and what rights you grant in the terms. Pro tip: _you can point your existing Claude / ChatGPT / Gemini at a connector / plugin / new tool’s website and ask it to check these things for you before you connect! Just ask it to give you the actual words / source link of what it found so you can fact check it yourself. _

**Uh oh**: did you already connect a bunch of stuff and now you’re sorta regretting it? Here’s how to do a quick audit: [Peter Yang’s advice](https://x.com/petergyang/status/2091331251211059468) is to open [your Google account](https://myaccount.google.com/) in Chrome, give Codex or Claude Code the open tab, ask it to list third-party apps with access, then choose which connections you want it to revoke.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

# 🎓 AI Skill of the Day: Turn Your Judgment Into a Reusable Skill

Most AI feedback disappears when the chat ends. [Omar Saravia](https://x.com/omarsar0/status/2090471258966159670) argues the strongest agent workflows do the opposite: humans verify the hard outputs, then encode that judgment into reusable skills or verifiers, so expertise compounds instead of getting replaced.

1. Give the agent a real task, then review the difficult output yourself.

2. Explain exactly why you accepted or rejected it, focusing on the decision rule instead of this one example.

3. Save that rule as a checklist, skill, or verifier and reuse it on the next run.

**Copy this:**

```
After I review this output, turn my corrections into a reusable checklist or verifier skill for future runs. Preserve the decision criteria, not merely this example.
```
The trick is not removing the expert. It’s making the expert’s judgment compound, so you can focus on net new problems that arise.

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

1. *_[ClickUp Brain](https://link.technologyadvice.com/r/clickup-tn-newsletter-july-2026)__ answers questions across your workspace and gives you AI teammates you can assign real tasks to; from $9/user/mo billed annually._

2. [Slack Code](https://www.salesforce.com/introducing-slack-code/?bc=HL) gives humans and coding agents one channel to write code, review diffs and previews, and ship with the surrounding conversation intact.

3. [Meta Pocket](https://techcrunch.com/2026/08/20/meta-brings-pocket-an-app-that-lets-you-vibe-code-and-share-games-to-us-users/) turns prompts into small phone games that can react to touch, tilt, sound, photos, or the live camera.

4. [Spline V2](https://blog.spline.design/spline-v2) lets you build 3D scenes in a faster browser editor, then create and edit them through AI Agent Mode or direct AI-tool connections.

5. [Foundation by Chroma](https://www.trychroma.com/foundation) learns from agent sessions and automatically maintains a versioned, provenance-tracked team wiki.

6. [ChatGPT read-only sharing](https://x.com/ChatGPT/status/2090517084262551917) lets you share a Work or Codex conversation without letting the viewer continue or alter the original chat.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/381e4539-21a7-4ef4-86f3-19a446063198/Screenshot_2026-08-23_at_9.45.42_AM.png?t=1787503562)
Follow image link: (https://munderdiffl.in/)
Caption: This app called [Munder Difflin](https://munderdiffl.in/) literally turns your AI agents into characters from The Office ([read more](https://news.ycombinator.com/item?id=49398152)) 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c169196e-512b-4dc1-923d-dd37c55640ac/Screenshot_2026-08-23_at_9.47.18_AM.png?t=1787503647)
Follow image link: (https://x.com/YounisJoseph/status/2091297990845874468)
Caption: This controversial study on using language model AIs for medical diagnosis went viral on X this morning. Here’s the [main criticism](https://x.com/iScienceLuvr/status/2091388678958723479): the models used are old (GPT 4o). Here’s [Joseph’s response to that criticism](https://x.com/YounisJoseph/status/2091393487967232471)

* [DeepSeek added vision to V4 Flash](https://x.com/deepseek_ai/status/2090730032574631962), keeping its low-cost Flash tier while adding multimodal input and visual-agent capabilities.

* [NVIDIA’s AVO agent system](https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/) completed all 183 public ARC-AGI-3 levels, showing how much the harness around a model can matter on long-running tasks.

* [Aikido’s 11.7-billion-token cyber test](https://www.aikido.dev/blog/ai-model-benchmarks-aug-21-2026) found DeepSeek V4 Pro recovered 28 of 32 fresh vulnerabilities, while three cheap open-model runs beat one Opus 5 or Grok pass on coverage.

* [OpenAI](https://x.com/OpenAI/status/2090885187634905500) cut GPT-5.6 Sol API and credit pricing by more than 20% for the next three months.

* [Cerebras unveiled CS-4](https://x.com/andrewdfeldman/status/2090918209113469078), a rack-scale inference system it says delivers up to 30× the speed of the nearest GPU competitor and 10× CS-3 throughput.

* [China put nearly 50 humanoid traffic robots](https://krro.com/2026/08/20/china-puts-robocops-on-traffic-duty-minus-the-arrest-powers/) across about eight cities, where they can flag helmet and traffic violations but have no arrest powers.

* [Apple Music](https://www.billboard.com/pro/apple-music-to-label-ai-generated-music/) said it will label tracks materially generated with AI, including disclosures for audio, artwork, composition, and music videos.

* [Women accounted for only 26% of new U.S. AI hires](https://www.axios.com/2026/08/18/ai-women-jobs-hiring) in 2025, versus roughly half of hires in non-AI roles.

* [Spirit flight attendants challenged Google’s $10M data bid](https://www.wsj.com/pro/bankruptcy/spirit-flight-attendants-fight-googles-data-bid-for-ai-e939e049), and a bankruptcy judge delayed approval of the sale.

* [Amazon](https://www.aboutamazon.com/news/transportation/amazon-prime-air-drone-delivery-expansion) said Prime Air drone delivery will expand to nearly 500 U.S. cities and towns by the end of 2026.

* [Pew Research Center](https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/) found significant AI-writing signals on 10% of a random July webpage sample and more than one-third of pages published after ChatGPT launched.

Want the rest? **[Read the full Around the Horn digest here.](https://theneuron.ai/digest/everything-that-happened-in-ai-today-friday-august-21-2026/)**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 😸 Sunday Special

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1efaae24-0729-4547-94cc-6909fbd4c9c3/Screenshot_2026-08-23_at_9.51.37_AM.png?t=1787503932)
Follow image link: (https://x.com/iScienceLuvr/status/2091388678958723479)
Caption: For the hardware geeks (and tech teams considering on-prem server buildouts) out there; also [Alex Z has the best youtube channel](https://www.youtube.com/@AZisk) for these kinda questions.

## Top 5 Stories of the Week

1. [NVIDIA put a $105B safety net under OpenAI](https://nvidianews.nvidia.com/news/nvidia-guarantees-sb-energy-s-ports-pike-technology-campus-in-ohio-to-exclusively-host-nvidia-ai-compute).

2. [Moderna’s personalized mRNA cancer therapy met Phase 3 goals](https://www.merck.com/news/merck-and-moderna-announce-phase-3-interpath-001-trial-of-intismeran-autogene-plus-keytruda-met-endpoints-of-recurrence-free-survival-rfs-and-distant-metastasis-free-survival-dmfs-in-patient/).

3. [Google won Spirit’s $10M data auction, pending approval](https://www.cnn.com/2026/08/18/business/google-spirit-airlines-data).

4. [Generalist taught a robot from one 3-second demo](https://generalistai.com/blog/gen-1.5).

5. [Anthropic passed OpenAI in quarterly revenue](https://www.cnbc.com/2026/08/19/stock-winners-and-losers-as-anthropic-passes-openai-as-hottest-ai-upstart.html).

## Top 5 Tools of the Week

1. [ChatGPT Sites](https://learn.chatgpt.com/docs/sites?surface=app) builds and hosts websites from chat.

2. [Cursor Origin](https://cursor.com/changelog/origin-code-hosting) gives agents a GitHub-style code host.

3. [GPT-Image-2](https://developers.openai.com/cookbook/examples/multimodal/transparent-image-assets-for-campaigns-and-presentations) generates transparent-background assets directly.

4. [FLUX Video Upscale](https://bfl.ai/video-upscaler) regenerates short clips up to 4K.

5. [Notion Skills](https://x.com/NotionHQ/status/2090500028393726026) turns team workflows into reusable agent playbooks.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# Building AI agents? Steal Samsara’s playbook

Samsara is deploying agents across thousands of real-world workers, and its lessons apply far beyond trucking: **start with low-stakes tasks, give agents the right context, encode your best people’s expertise, and test everything with real users.**

[Read the biggest agent-building lessons from our interview →](https://www.theneuron.ai/news/how-samsara-is-bringing-ai-agents-into-the-physical-world/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a870e4b1-f01e-4d3f-9a7c-2d7fb2b01682/A_Cat_s_Commentary_x_2025__80_.png?t=1785898026)
Caption: IYKYK

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today! 




**Btw: ** We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/why-sam-altman-thinks-people-hate-ai
