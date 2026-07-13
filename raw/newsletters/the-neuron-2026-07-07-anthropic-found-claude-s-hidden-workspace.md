---
source: gmail
newsletter: "the-neuron"
message_id: "19f3c0391248e948"
thread_id: "19f3c0391248e948"
subject: "😼 Anthropic found Claude’s hidden workspace"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Tue, 07 Jul 2026 09:57:43 +0000 (UTC)"
ingested: 2026-07-13
sha256: 2cced76c83d0f0611a659c7308bda557eaacbbc57bf78e16b03273daa127f5b1
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/019e06e5-6368-40e6-8cf6-d5087760e7fa/ChatGPT_Image_Jul_6__2026__10_37_43_PM.png?t=1783402723)
Caption: 

Welcome, humans. 

After a weekend of power-coding with Claude Fable, _really pushing it to the limit, _[this meme](https://www.reddit.com/r/singularity/comments/1uora3h/accelerate/) feels very apropos: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b3344b64-25c1-4912-835c-9f9245cb07e8/Screenshot_2026-07-06_at_3.58.21_PM.png?t=1783407533)
Follow image link: (https://www.reddit.com/r/singularity/comments/1uora3h/accelerate/)
Caption: 

Who else got to build something with Fable this weekend? Shout out below! (_In the _
_“Additional Feedback” after you answer, write in the text box and tell us what you did!) _

**Here’s what happened in AI today: **

* 😺 Treasury’s AI bubble warning sharpened today’s finance-risk story.

* 📰 JADEPUFFER became the first known agentic ransomware case.

* 📰 Voters started asking chatbots who they should vote for.

* 📰 Alibaba reportedly banned Claude Code internally.

* 📰 Midjourney pressed Hollywood to disclose its own AI usage.

…and a [**whole lot more that you can read about here**](https://theneuron.ai/explainer-articles/around-the-horn-digest-everything-that-happened-in-ai-today-monday-july-6-2026/).

**Hey: **_Want to reach 700,000+ AI-hungry readers? _[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[ ](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**Love robots?** We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😼 Anthropic found Claude’s hidden J-space for silent reasoning

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/044e24a4-ad1e-47c3-9feb-be4e34a07a73/Screenshot_2026-07-06_at_2.50.17_PM.png?t=1783403628)
Follow image link: (https://x.com/AnthropicAI/status/2074185348142280912)
Caption: 

Ever ask an AI to “think about it” and wonder what all is happening in there?

Well, [Anthropic](https://www.anthropic.com/research/global-workspace) now knows that answer, _sorta_. At least, _inside Claude_. In a new research drop ([video explainer](https://youtu.be/rKV5JcALQoQ?si=1cefDvnwgYGrjMSa)), its researchers discovered Claude has an internal workspace where concepts can be held, edited, and used before they show up in an answer. _If you’re technically inclined, this means language models are at least __[somewhat neurosymbolic](https://x.com/blader/status/2074195084577579503)__, in that they hold concepts in their latent space (the hidden digital map where AI groups similar ideas close together)._

**Here's what happened:**

* Anthropic found  what it called “J-space,” or a small set of internal neural signals in Claude.

* Anthropic compares J-space to a limited “global workspace,” meaning a shared mental whiteboard where selected information becomes available to many other processes.

* In one test, Claude saw a prompt asking for “the number of legs on the animal that spins webs.” It loaded “spider,” then answered “8.” When researchers swapped that internal concept for “ant,” Claude answered “6.”

* When researchers suppressed J-space, Claude still wrote fluently, but got much worse at complex reasoning ([full paper](https://transformer-circuits.pub/2026/workspace/index.html)).

_Oh, and in case you’re wondering where the term J-Space comes from, it’s not your new favorite Tokyo-based boy band. _J-space is named after the **Jacobian lens**, a technique that checks how small internal changes affect what the model may say later.

_As popular OpenAI team member __[Roon joked](https://x.com/tszzl/status/2074195073739460769)__, “J Space” is about to become the name of 1,000 Bay Area group chats._

**Why this matters:** This discovery, applied broadly, could give researchers a better way to inspect the “thoughts” a model uses but doesn’t say. The research suggests J-space works like a shared whiteboard:

* It can hold intermediate steps.

* It can route one concept into many tasks.

* It can reveal hidden flags like “fake,” “injection,” or “manipulation.”

The caveat: this is all early, imperfect, and was tested mainly across Claude models. The next frontier is whether reading a model’s scratchpad can become a real safety system before models get better at hiding the marker.

**Our take:** Claude has a mind palace! Makes you wonder what we can learn about structurally organizing our own thoughts from learning how Claude does it. More importantly, labs may be getting better microscopes for model behavior. 

To our knowledge, Anthropic has produced some of the most important work in this category (_which is called “mechanistic interpretability, or mech interp for short) _and it’s some of the most exciting research in the field. _ _

As [we’ve discussed with OpenAI’s Bowen Baker](https://youtu.be/20m5TY3Bv8I?si=OxXvK8WDfv7Uxthw), future AI models will act before humans see every step. If interpretability tools can spot when a model privately notices it is being tested, identifies a prompt injection, or considers a hidden goal, safety checks become less dependent on trusting whatever the model says, which time and time again, models have been proven _untrustworthy _when allowed to just say anything.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

# 🎓 AI Skill of the Day: Run a Blind Spot Pass Before AI Builds to “Find Your Unknowns”

Before you ask Claude or ChatGPT to build the thing, ask it to find the parts of the thing you forgot to mention.

In Anthropic’s[ Field Guide to Fable](https://youtu.be/9fubhllmsBU?si=8eFo1GnD0YiwsC30&t=655), Thariq Shihipar calls this a “blind spot pass.” The idea starts with a simple model: your prompt is the map, but the real project is the territory. The messy middle is full of “unknowns,” meaning decision points you never specified (_his __[full x post on this here](https://x.com/trq212/status/2073100352921215386)__ is great). _

Use this before a big writing project, product spec, analysis, website, workflow, or coding task:

1. Give the AI your rough plan.

2. Ask it to sort what it knows into knowns and unknowns.

3. Make it interview you before it starts.

4. Ask it to log any important assumptions it makes later.

That keeps you “in the loop,” which Shihipar says is one of the most important parts of working with stronger models.

```
Before you start building, run a blind spot pass.

Treat my prompt as the map and the real project as the territory. Identify:
1. Known knowns: what I clearly specified.
2. Known unknowns: questions I flagged but have not answered.
3. Unknown knowns: things I probably know but failed to write down.
4. Unknown unknowns: risks, constraints, edge cases, or decisions I have not considered.

Then ask me the 5-10 highest-leverage questions that would most change the output, especially questions that affect structure, architecture, audience, scope, workflow, or quality.

If you continue after that, keep an "implementation notes" section where you log e
```
**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform) 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🍪 Treats to Try 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b191295a-f1de-4863-9e27-99ea897a0538/Thread.png?t=1783337350)
Follow image link: (https://www.getthread.com/?utm_source=TechAdv&utm_medium=Pubad&utm_campaign=ISD)
Caption: 

_*Asterisk = from our partners (only the first one!). __[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron)__!_

1. ***The #1 AI Service Desk for MSPs. **Thread is the AI Service Desk 750+ MSPs trust to automate triage, dispatch, and client conversations across ConnectWise, Autotask, and HaloPSA, processing 173 million tickets, returning over half a million hours to technicians, and earning 97% positive sentiment from end clients along the way. [Get Started](https://www.getthread.com/?utm_source=TechAdv&utm_medium=Pubad&utm_campaign=ISD)

2. [Tencent Hy3](https://hy.tencent.com/research/hy3) gives you a cheaper commercial-friendly open model with a 262K-token context window on [OpenRouter](https://openrouter.ai/tencent/hy3:free) and two weeks of free API access.

3. [Ornn](https://ornn.com/) wants to make GPU compute pricing easier for buyers, sellers, lenders, and traders to benchmark ([raised $33M](https://www.axios.com/2026/07/06/ornn-gpu-compute-commodity)).

4. [Kyrall](https://kyrall.com/) turns specs, sizing tools, requirements, and old designs into editable CAD assemblies you can generate from plain language.

5. [fal’s Ideogram V4.0q](https://fal.ai/models/ideogram/v4/instant) helps you generate images, posters, and logos with more accurate text rendering, with instant and fast variants available.

6. [OpenScience](https://github.com/synthetic-sciences/openscience) gives scientists a model-agnostic research workbench with 250+ skills for ML, computational biology, and cheminformatics, open-source on GitHub.

7. [Even Realities](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/) is building camera-free smart glasses from an ex-Apple team and just raised $150M at a $1B valuation.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a0757820-427b-44da-939b-ca5fceeec8a3/TN_Thumbnail_AndrewDai_1.png?t=1781718367)
Follow image link: (https://www.youtube.com/watch?v=hMS-2l-p9tM&t=219s)
Caption: Criminally under-watched episode IMO (on YT, anyway; crushing on Spotify). This is the most important conversation in AI besides long context memory and GPU efficiency

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6e34f8b1-5eac-4990-b2d5-20c20b2a61cc/Screenshot_2026-07-06_at_4.00.30_PM.png?t=1783379426)
Follow image link: (https://www.reddit.com/r/aivideo/comments/1uoq0hg/what_if_the_2026_world_cup_was_hosted_in_south/)
Caption: Ok, they got me with this one. Also, why is Erling Haaland so steamy in this?? I’m deceased ⚰️ Also rough USA game yesterday sorry fam

* [Treasury analysts](https://www.notus.org/economy/treasury-internal-report-warning-dangers-ai-bubble) reportedly prepared an internal report warning that AI-market risk could ripple through data-center financing, cloud providers, chips, utilities, private credit, and institutional investors.

* [JADEPUFFER](https://www.bleepingcomputer.com/news/security/jadepuffer-ransomware-used-ai-agent-to-automate-entire-attack/) was identified as the first documented ransomware operation conducted entirely by a large language model agent.

* [The New York Times](https://www.nytimes.com/2026/07/04/us/politics/voters-ai-chatbots-elections.html?unlocked_article_code=1.vFA.TTCt.7KuPI81ZZaDz&smid=url-share) reported voters were asking AI chatbots who they should vote for, turning election research into a new chatbot trust test.

* [Alibaba](https://techcrunch.com/2026/07/04/alibaba-reportedly-bans-employees-from-using-claude-code/) reportedly banned employees from using Claude Code as large companies tightened rules around AI coding tools.

* [Midjourney](https://techcrunch.com/2026/07/04/midjourney-wants-hollywood-studios-to-reveal-the-details-of-their-ai-usage/) pushed Disney, Universal, and Warner Bros. to disclose their own AI usage in its copyright fight with the studios.

* [The Verge](https://www.theverge.com/ai-artificial-intelligence/961505/wealthy-ai-schools-alpha-forge-prep) reported wealthy families were putting children into AI-tutor school programs.

* **[Station F’s F/ai accelerator](https://techcrunch.com/2026/07/06/station-f-ramps-up-as-a-launchpad-for-europes-hottest-ai-startups/)** gives European AI founders more partner access from groups like ElevenLabs, Nebius, OpenRouter, HubSpot, GitHub, and Rippling.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

**FROM OUR PARTNERS **

# How Spotify and DHL keep AI accurate at scale.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/02e53ce0-920a-4fda-9b8c-303fd9daa332/Neuron_Number_5.png?t=1783330591)
Follow image link: (https://www.getguru.com/?utm_source=theneuron&utm_medium=newsletter&utm_campaign=secondary-july2026)
Caption: 

The enterprises winning with AI aren't just deploying more tools. They're governing the knowledge those tools run on.

[Guru](https://www.getguru.com/?utm_source=theneuron&utm_medium=newsletter&utm_campaign=secondary-july2026) is the governed knowledge layer behind teams at Spotify, DHL, and Brex. One platform. Every AI. Every employee. Always accurate.

[→ See how it works](https://www.getguru.com/?utm_source=theneuron&utm_medium=newsletter&utm_campaign=secondary-july2026)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 🔧 Tuesday Tool Tip: Check What Google Can Save From Search

If you use Google Search, Lens, Translate, Maps, Shopping, Flights, Hotels, or News, take 90 seconds today to review the newer Search Services History settings.

[TechCrunch reported](https://techcrunch.com/2026/07/06/if-you-use-google-youre-training-its-ai-heres-how-to-opt-out/) that Google can save more media from Search-related services, including images, files, audio, and video, for AI improvement unless users change the setting.

**The move: **go to your Google activity controls, find Search Services History, then review whether saved media is enabled. For work accounts, ask your admin how uploaded files, screenshots, and voice searches are handled before employees use these services with company material.

This might seem like a privacy chore today, but like many chores in your life, if left unattended, _could end with a steaming pile of garbage raining down upon you later. _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# A Cat’s Commentary 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a0a5992f-5c50-4ac5-9a7b-973feead212b/A_Cat_s_Commentary_x_2025__55_.png?t=1782524227)
Caption: we love to make you feel smart whenever we can! 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. 




**P.S: **Before you go… have you [subscribed to our YouTube Channel](https://www.youtube.com/@theneuronai?sub_confirmation=1)? If not, can you?  

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/024ed8a0-896e-468e-8fc3-bb46b7f99322/ChatGPT_Image_Jun_29__2026__08_06_11_PM.png?t=1782788789)
Follow image link: (https://www.youtube.com/@theneuronai?sub_confirmation=1)
Caption: Going for an anime aesthetic this month!

**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).  


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/anthropic-found-claude-s-hidden-workspace
