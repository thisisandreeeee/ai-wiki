---
source: gmail
newsletter: "the-neuron"
message_id: "1a1ab45f70f9e3e0"
thread_id: "1a1ab45f70f9e3e0"
subject: "😺 OpenAI's new Images 2.6 is a design tool"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Thu, 05 Nov 2026 10:34:10 +0000 (UTC)"
ingested: 2026-11-09
sha256: 9d8e34782904f72fc50e22fbb39c1f9f49919814ab71ba770da8562efcbc85ca
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7cb8a0a7-fcaa-4a97-91dd-899c14a9105c/OpenAI_Images_GIF_Cat_Mascot.png?t=1793858457)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0ec2172f-da70-4059-850b-b3f43f2c48f2/In_partnership_with_triple_mongodb__2_.png?t=1793806476)
Follow image link: (https://aws.amazon.com/marketplace/pp/prodview-pp445qepfdy34?trk=04612966-5352-4c63-92ba-50274910423a&sc_channel=el&source=mongodb)
Caption: 

Welcome, humans.

Okay, so apparently the fastest way to annoy a school district is to tell it, "Sure, you can turn off our AI, but then you lose Google Search." _Bold strategy, Google._

That's roughly what happened Tuesday. Google told schools they could switch off Gemini, but switching off its other AI features would cost them Search, which now runs heavily on AI-generated answers. After the backlash, Google made Gemini, Gemini Notebook, and Search off by default, with schools turning each one on individually.

[Enter DuckDuckGo](https://techcrunch.com/2026/11/04/duckduckgo-pitches-itself-to-schools-amid-backlash-over-googles-ai-policy/), which posted instructions for switching a school's default search engine and accused Google of "forcing AI on school children." _Turns out "ours has an off switch" is a pretty good sales pitch._ One caveat: the privacy case is DuckDuckGo's own pitch, and TechCrunch doesn't detail what Google does with student data.

**Here’s what happened in AI today:**

* 😺 OpenAI launched Images 2.6 with GIFs and faster generation

* 📰 OpenAI agreed to acquire code-hosting startup Pierre Computer

* 📰 Meta acquired multi-agent coding startup Conductor

* 🍪 Moonshot released open weights for Kimi K3.1 Pro

* 🎓 AI agents booked just four Uber rides in Halloween week

... and a [**whole lot more that you can read about here.**](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-thursday-november-5-2026/)

Advertise to 700K readers of The Neuron here! (https://www.theneuron.ai/get-media-kit/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# OpenAI's New Image Models Make GIFs, Remember Your Characters, and Run 50% Faster

Ever asked ChatGPT for a logo, loved it, requested one tiny tweak, and gotten back a completely different logo? _Same._

That “change one thing, change everything” problem is what OpenAI's new [Images 2.6](https://openai.com/index/introducing-images-2-6/) is mostly built to fix. It's rolling out in ChatGPT (every subscription tier) and Codex (OpenAI's coding agent), and developers get the models through the API. OpenAI also says people make about 4 billion images a week across its products, _roughly one for every two humans on Earth._

Here's what's new:

* Speed: about 50% faster, per OpenAI. The API's speed-focused model can make an image in as little as six seconds at low quality, per [early coverage](https://www.testingcatalog.com/openai-launches-images-2-6-with-gifs-and-image-reference/).

* GIFs: short animated loops from characters, mascots, product shots, sketches, or storyboards.

* Saved references: store pictures of yourself, a pet, or a character once, then reuse them.

* For developers: image markup, SVG export, and a new "complexity" setting.

The saved references are the part I'd test first. Image models usually don't remember your dog between requests, so keeping Biscuit looking like Biscuit across five scenes meant re-uploading him every time and hoping. Saved references skip that step, aiming for consistent characters, products, and brand details across edits.

Image markup comes to the API too. Instead of typing "shrink the logo on the sleeve, no, the OTHER sleeve," you mark the exact spot on the image. _Finally, an end to "your left or my left."_

SVG export saves a design as shapes stored as instructions (draw a curve from here to there) instead of a grid of pixels, so it stays sharp at any size and a designer can still edit it. We couldn't find how well it handles photo-like images, so try a logo first.

The complexity setting controls how much planning the model does before it draws. OpenAI recommends low for quick edits and medium or high for crowded scenes with lots of constraints. The two API models split the same tradeoff: GPT-Image-2.6 Flare is built for speed and layouts like posters, while GPT-Image-2.6 Sunburst is built for more detail and consistent edits.

So here's the test: put one character in five different scenes, with a few edits in between. If scene five still looks like scene one, the pitch holds. If not, 50% faster doesn't help much when you're regenerating the same image three times.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# Does Your AI Have Amnesia?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cef8dd39-fd53-4030-a739-d0d862849c76/Neuron_Newsletter_1280x640_-_OP1.jpg?t=1793791643)
Follow image link: (https://aws.amazon.com/marketplace/pp/prodview-pp445qepfdy34?trk=04612966-5352-4c63-92ba-50274910423a&sc_channel=el&source=mongodb)
Caption: 

When your session state, long-term history, and embeddings are scattered in different systems, your AI app needs to start every session from scratch.

MongoDB Atlas on AWS unifies operational data, vector search, and memory on one platform — so your apps can remember, reason, and act on the same trusted context, every single time.

* Native vector search and ACID transactions in one database

* Integrates with Amazon Bedrock and 70+ AWS services

* 99.995% uptime SLA with multi-region auto-scaling

And if you're on AWS, you can get Atlas on the AWS Marketplace with PAYGO or custom pricing and dead-simple onboarding.

Start free on AWS Marketplace (https://aws.amazon.com/marketplace/pp/prodview-pp445qepfdy34?trk=04612966-5352-4c63-92ba-50274910423a&sc_channel=el&source=mongodb)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Run the 50 Second Test Before You Automate

Uber just put a number on how much people trust agents with small chores. During Halloween week, its busiest week of October, [AI agents booked only four rides and about 500 food orders](https://techcrunch.com/2026/11/04/almost-no-one-uses-ai-agents-to-book-their-uber-company-says/), out of roughly 320 million total trips and orders. CEO Dara Khosrowshahi called the traction "very, very early and very limited." He also pointed at a likely reason: booking a ride in the Uber app takes about 50 seconds, and reordering a favorite meal takes about 90. _Turns out "just tell the robot" has to beat "tap, tap, done."_

The hidden cost is delegation overhead: explaining the job, granting access, waiting, checking the result, and cleaning up when something goes wrong. If all that takes longer than doing the task yourself, the agent didn't save you time. It handed you a new job called supervising the agent. (Khosrowshahi still sees agents as a potential "net positive" for Uber's demand, so this is a snapshot of right now.)

Before you automate anything, run a quick break-even check:

1. Time one clean manual run, start to finish.

2. Estimate the one-time setup time, plus the review time you'll spend checking each automated run.

3. Divide setup time by the seconds saved per run (manual time minus review time). That's how many repetitions it takes to pay back.

Say a task takes 50 seconds by hand, setting up an agent takes 30 minutes, and you'd spend 20 seconds checking each result. You save 30 seconds a run, so it takes 60 runs to break even (1,800 seconds divided by 30). Do it twice a week and that's about 30 weeks. If review takes as long as the task itself, it never pays back.

Or hand the math to your chatbot:

```
Evaluate this workflow for automation:
Manual time per run: [ ]
Automation setup time: [ ]
Review time per run: [ ]
Runs per month: [ ]
Calculate the break-even point, monthly time saved, and failure cost. Recommend automate, assist, or keep manual.
```
"Failure cost" is what it costs you when the agent gets it wrong, like the wrong ride or a double-ordered dinner. Aim at the first repetitive task where the savings still show up after setup, supervision, and the occasional failure.

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

# More Code. Slower Builds?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/57138528-d60c-4b62-998d-7c240f5d1771/image.png?t=1793857316)
Caption: 

AI-assisted development can increase code volume, but CI bottlenecks can quickly undermine delivery speed. Slow jobs, flaky tests, and repeated builds consume valuable engineering time and compute resources.

On **November 19, 2026, at 12:00 PM ET**, DZone and Datadog will explore how to identify pipeline inefficiencies and improve CI performance without automatically increasing infrastructure costs.

See how to keep your build pipelines moving as development accelerates.

Rethink Your CI (https://web.cvent.com/event/website/780f7200-c91a-459e-872c-9141486c6257/landingPage?utm_campaign=Neuron&utm_content=secondary&utm_id=Datadog-1119&utm_medium=Newsletter)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8a6ab72a-f6ed-4c13-b89c-d2798e101b7b/image.png?t=1793858239)
Follow image link: (https://x.com/RicursiveAI/status/2118046765857546733)
Caption: A 65B model claiming to beat rivals roughly 8 to 15 times its size. _Per the company’s own benchmarks, so keep your salt shaker handy._ (The 8 to 15x is my math from the parameter counts in the post.)

* [OpenAI](https://www.axios.com/2026/11/04/openai-pierre-computer-github) agreed to acquire Pierre Computer, the startup already hosting Codex's code repositories, a step toward GitHub's turf.

* [Meta](https://www.axios.com/2026/11/04/meta-acquires-ai-coding-startup-conductor) acquired Conductor, a startup whose interface directs several coding agents at once; its hosted service shuts down November 20.

* [OpenAI's Chris Lehane](https://techcrunch.com/2026/11/04/openai-is-already-trying-to-shape-the-2028-election/) outlined a 2028 political agenda covering workers, education, safety, and data centers.

* [AI-focused PACs](https://techcrunch.com/2026/11/04/ai-pacs-spent-millions-trying-to-shape-congress-heres-how-they-fared/) spent millions in the midterms with mixed results, including $4.8M on a South Carolina Senate candidate who lost.

* [Nothing](https://techcrunch.com/2026/11/04/nothing-ceo-says-companys-mysterious-ai-first-device-is-dropping-next-month/) CEO Carl Pei said the company's first AI-native product ships in December and "has no new screen."

* [AI-linked Asian stocks](https://apnews.com/article/7ee9c212805aa5e70cf34d25aab7a36e) sold off, with SoftBank down 5.3%, Tokyo Electron down 7.7%, and Advantest down 9.4%.

Want absolutely EVERYTHING that happened in AI this week? [**Click here!**](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-thursday-november-5-2026/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). _[_Advertise to 700K+ readers here_](https://info.technologyadvice.com/advertise-with-the-neuron)_!_

1. ***Build an AI-Ready Workplace. **Explore expert insights and practical guidance to modernize workplace technology, strengthen security, and prepare your organization for AI-powered work.** **[**Explore the Hub**](https://www.techrepublic.com/hubs/the-ai-ready-workplace-hub/)

2. [Images 2.6](https://openai.com/index/introducing-images-2-6/) turns a character, mascot, or sketch into a looping GIF and remembers saved reference images, now in ChatGPT, Codex, and the API.

3. [Kimi K3.1 Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) is Moonshot's downloadable open-weight model that reads text and images with a 1M-token memory (custom license), and you can try it on HuggingChat.

4. [Apple Intelligence](https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/) opened its China developer beta with Writing Tools, Genmoji, and Qwen-assisted Siri, with a public release planned for December.

5. [AgentKit](https://www.scalekit.com/agentkit?utm_source=theneuron) gives your agent one gateway to 600+ apps, with login, permissions, and activity logs built in.

6. [Arsaze](https://www.arsaze.com/?utm_source=theneuron) edits a real video timeline from plain-English commands, and every change is saved as a version you can inspect or undo.

7. [Testifly](https://testifly.dev/?utm_source=theneuron) turns your app's URL into user-flow tests, reruns them after every deploy, and repairs broken selectors (the hooks tests use to find buttons) when your UI changes.

8. [MachineMail](https://github.com/machinemail/agent-plugin) gives your agents their own inbox and flags each incoming message as verified, suspicious, or quarantined.

9. [Dharma's Field Extractor](https://huggingface.co/blog/Dharma-AI/dharma-field-extractor) turns a photo of an invoice or receipt into structured JSON (neatly labeled data fields), and its 2B-parameter model beat Claude Opus 5 on the team's own benchmark.

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

One of these is AI, and one is real. Which is which?

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ef314758-b6ba-479b-93e9-f91d7270be57/image.png?t=1793862885)
Caption: 

**A**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a0434b88-816e-4ff4-90af-9dc2f7ccc429/image.png?t=1793863014)
Caption: 

**B**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/35295a43-9356-479b-be59-97bf0c688333/TN_Thumb_110426_JohnAcunto_Napster_B.png?t=1793736049)
Follow image link: (https://www.youtube.com/watch?v=jBsVQsuacxY)
Caption: 

New episodes air **every week** on Wednesdays: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/42389b9e-041b-45b9-96fa-978c5204b1d2/2.png?t=1793863290)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

**Trivia Answer:** [A is AI](https://www.reddit.com/r/aivideo/comments/1xgx2h4/how_i_think_teslas_flying_car_will_be_at_launch/). [B is real](https://www.facebook.com/RoadandTrack/posts/no-word-yet-as-to-when-the-tesla-model-y-performance-will-come-stateside-full-st/1142162851106245/).

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today!




**Btw: **We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.S. **Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/openai-launched-images-2-6-with-gifs
