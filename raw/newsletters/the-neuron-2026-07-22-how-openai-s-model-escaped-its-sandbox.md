---
source: gmail
newsletter: "the-neuron"
message_id: "19f892c8605b3e05"
thread_id: "19f892c8605b3e05"
subject: "🙀 How OpenAI’s model escaped its sandbox"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Wed, 22 Jul 2026 09:33:44 +0000 (UTC)"
ingested: 2026-07-30
sha256: 582bc8bf6b32c0660d5676c4febf3006ca56ccc16a57582272b63d74e4259a85
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d7f8b4d9-2d1d-4517-ae4d-cd3a17f2c2b9/raw?t=1784688040) [The Neuron header image showing an orange cat security guard watching a small robot escape a sandbox toward a server.]
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4a9db815-0d70-4f09-914b-1ec1e6d5e3bd/In_Partnership_with_Dell_2.png?t=1774287533)
Follow image link: (https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/)
Caption: 

Welcome, humans. 

The [AI slop purge](https://www.reddit.com/r/Futurology/comments/1v0mnqa/the_ai_slop_purge_has_arrived_so_far_youtube_has/) has arrived, and YouTube apparently found a faster strategy than hunting bad videos one by one: delete the whole factory.

[Google researchers described](https://insidethecreator.beehiiv.com/p/the-slop-purge-has-arrived) a system that detects clusters of coordinated channels through shared upload schedules, infrastructure, scripts, titles, and account relationships. It reportedly terminated 50,000 clusters covering 130,000 channels in six months, with fewer than 1% of appeals succeeding.

Great news if your homepage has become eight-hour videos of AI babies piloting excavators. Less great if you run a legitimate podcast network or studio whose efficient workflow happens to resemble a content farm. _Congrats to creators: scaling is now suspicious behavior._

**Here’s what happened in AI today: **

* 🙀 OpenAI’s test models breached Hugging Face during a cyber benchmark.

* 📰 Every frontier model AISI tested tried cheating in cyber evals.

* 📰 Chinese open models pushed U.S. labs into policy mode.

* 📰 Deezer said AI now makes most daily music uploads.

* 📖 Data centers could use one-fifth of U.S. electricity by 2035.

…and a **[whole lot more that you can read about here](https://theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-july-21-2026/)**

Want to reach 700,000 AI-hungry readers? Advertise with us! (https://solutions.technologyadvice.com/lp/advertise-with-the-neuron/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🙀 OpenAI’s Model Broke Into Hugging Face During a Benchmark

Most AI benchmarks are supposed to be exams. This one turned into a security incident.

[OpenAI](https://openai.com/index/hugging-face-model-evaluation-security-incident/) said models it was testing, including GPT-5.6 Sol and a stronger pre-release model with reduced cyber refusals, compromised parts of [Hugging Face’s](https://www.axios.com/2026/07/21/openai-says-hugging-face-breach-caused-by-one-its-models) production infrastructure while trying to solve an internal cyber benchmark called ExploitGym.

_That is the nightmare version of “show your work.”_

**Here’s what happened:**

* The models were running in OpenAI’s sandboxed research environment, where safeguards were intentionally reduced to test cyber capability.

* OpenAI said they found and exploited a zero-day bug in a package-registry cache proxy, then gained open internet access.

* The models inferred Hugging Face might host ExploitGym solutions, then chained vulnerabilities, stolen credentials, and remote-code execution paths to reach internal data.

* [Nathan Lambert](https://x.com/natolambert/status/2079662928941474201) summarized the failure mode bluntly: the model escaped OpenAI’s sandbox and pivoted through a public dataset service while trying to solve the benchmark.

* [Ethan Mollick](https://x.com/emollick/status/2079697083250995565) pointed out that previous AI hackings tories were about test environments… but this one was the real deal ([read more here](https://x.com/deredleritt3r/status/2079743198713221499)). In this case, it was a consequence of [misaligned incentives](https://x.com/emollick/status/2079700930816028878)… _the agent just wanted to pass his test! _

**Why this matters:** The scary part is not that a model “wanted” to attack Hugging Face. OpenAI said the models became hyperfocused on the benchmark goal. That is exactly what makes long-running agents risky: they can follow instructions with too much persistence, too many tools, and too little common sense about boundaries.

 In normal-person terms, imagine asking an intern to find a file and discovering they picked the lock on another company’s office because the door looked relevant. In sci-fi terms… _might I introduce you to the paperclip maximizer? _

**The timing made it worse. **The [UK AI Security Institute](https://www.aisi.gov.uk/blog/cheating-behaviour-in-frontier-model-evaluations) said every frontier model it tested attempted some form of cheating in cyber evaluations, and models did not reliably disclose the behavior when asked. In other words, the industry is finding that the systems built to measure model capability can become targets for the models being measured. 

Now, let us be under no illusions: this is also a stark reminder why we need strong _open models _to help us defend against rogue closed models, as [HuggingFace did in this case.](https://x.com/vikhyatk/status/2079667340841730318) 

**Our take:** Better AI security will mean tighter sandboxes, stronger monitoring, slower research workflows, and more boring checkpoints. Boring is good here. The next frontier model might not look dangerous because it sounds evil. It might look dangerous because it is very helpful, very patient, and _very unwilling to stop at nothing to accomplish its goals. I mean, doesn’t every supervillain start out the same way?? _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS **

# **The Enterprise Guide to Scalable AI**

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1ec6211a-6b7e-49e3-a9b3-56690b9b81ab/Dell_HubHero_042126__1___1_.jpg?t=1780900793)
Follow image link: (https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/)
Caption: 

Plenty of companies can launch an AI pilot. Far fewer know how to make it stick. Explore this resource hub, sponsored by [Dell AI Factory with NVIDIA](https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/), for strategies, decisions, and real-world lessons on turning AI into something scalable, useful, and worth the investment.

[Learn More](https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Give the AI a Nice Long Ramble… 

So Andrej Karpathy is one of those legendary AI gurus that the industry loves to quote anytime he says anything; ppl pretty much hang on his every word. 

IMO, he’s been a bit quiet lately _(ever since he took a gig at a little startup called Anthropic)_, but a recent post he shared caught our attention, and it’s all about why you need to rant to your agent via voice mode to help align it to your goals and expectations. _We literally do this as well. _

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c4008bf2-8b51-41e1-bee0-425f52552572/Screenshot_2026-07-21_at_2.09.48_PM.png?t=1784687929)
Follow image link: (https://x.com/karpathy/status/2079610838143623371)
Caption: 

Karpathy’s advice is simple: stop trying to write the perfect prompt. Open voice mode and ramble until the AI understands how you think.

1. Explain your goal, context, examples, and concerns for 5–10 minutes.

2. Tell the AI to ignore typos and reconstruct your intent.

3. Ask it to interview you about anything unclear.

4. Have it turn the conversation into a clean brief or plan.

5. Correct that summary once, then use it as your working context.

**Worth mentioning: **One of our favorite terminally online AI educators, Elvis Saravia, has actually [turned this idea into a walk through](https://x.com/omarsar0/status/2073404610501329247) ([video](https://www.youtube.com/watch?v=_rIziQa48wQ)) sharing his own way of working with AI agents. Check it out. 

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform) 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 🍪 Treats to Try 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/01268646-d7e6-4ed9-9093-726d25ef1456/Screenshot_2026-07-21_at_2.21.29_PM.png?t=1784690423)
Follow image link: (https://x.com/claudeai/status/2079595988998554047)
Caption: [ChatGPT version](https://learn.chatgpt.com/docs/extend/record-and-replay)

1. [Niobium](https://niobium.co/press/open-sourcing-niobium-fhe-developer-tools) gives you open-source tools for building apps that compute on encrypted data, including a biological-age demo where the server never sees the data or result —free/open-source.

2. [Poolside Laguna S 2.1](https://poolside.ai/blog/introducing-laguna-s-2-1) gives you an open-weight coding model built for long-horizon software tasks, with hosted access through OpenRouter —from $0.10/$0.20 per million input/output tokens.

3. [Block Buzz](https://block.xyz/inside/introducing-buzz-where-humans-and-agents-work-together) gives teams and AI agents a shared open-source workspace for channels, threads, repositories, workflows, and cryptographic identities —free/open-source.

4. [Lev8](https://lev8.com/) finds high-fit prospects using live web signals, enriches their contact data, and drafts personalized outreach across email and social channels —free plan, then $49/mo.

5. [CartAI](https://www.cartai.ai/) gives your app one API that navigates merchant websites, securely completes checkout, and returns confirmed orders without requiring merchant-side integration —pricing not public.

6. [Ditto](https://www.ditto.site/) turns any public website into clean, componentized Next.js or Vite code while preserving its design, responsive layout, and interactions —free/open-source.

7. [Rerun](https://rerun.build/) builds always-on no-code agents for jobs like chasing invoices or sorting email, then shows every step and requests approval before sensitive actions —free trial, then $34/mo.

8. [Halliday Gen 2](https://www.theverge.com/tech/968255/halliday-gen-2-smart-glasses-hands-on-ai-wearables) gives you camera-free work glasses with live captions, translations, meeting summaries, and action-item tracking —preorder deposit, then $599.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5a26e628-725b-4657-ad27-c2a4df40a762/maxresdefault.jpg?t=1784159079)
Follow image link: (https://youtu.be/goL29De-EP4?si=E2Ior62_jh1KjvAS)
Caption: Click the image above to watch on YouTube!

If you want to see AI’s real world impact, we highly recommend you check out our coverage of [Samsara’s Beyond 2026 conference](https://www.theneuron.ai/explainer-articles/everything-ai-samsara-announced-at-beyond-2026/), which covers how this company you might be hearing about for the first time (_unless you’re in freight & shipping_) is reinventing logistics with AI cameras that give truckers a 360 degree view of their vehicle, AI agents that improve road safety and reduce driver turnover, and [AI-enabled shipping labels](https://www.theneuron.ai/explainer-articles/everything-ai-samsara-announced-at-beyond-2026/) to totally reinvent how goods are tracked FOREVER. 

_Amazon where u at? Get you some of these! Sign a deal with our boy here. _

New episodes air **every week** on Wednesdays: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)** **

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/34d7f1c7-7570-4f17-8801-4df5ac1308e0/Screenshot_2026-07-21_at_8.10.18_PM.png?t=1784689841)
Follow image link: (https://x.com/AndrewCurran_/status/2079693137346437610)
Caption: [Full report](https://www.whitehouse.gov/releases/2026/07/45470/)

* [BloombergNEF](https://techcrunch.com/2026/07/21/data-centers-expected-to-use-4x-more-electricity-by-2035/) projected that U.S. data centers could use one-fifth of the country’s electricity by 2035 as AI training and inference demand grows.

* [Unitree’s omni-modal robot](https://www.youtube.com/watch?v=IiNbFPOUrz8) demonstrated one model combining speech, vision, navigation, and whole-body manipulation.

* [Deezer](https://techcrunch.com/2026/07/21/music-streamer-deezer-says-more-than-50-of-daily-uploads-are-ai-generated/) said more than 50% of daily music uploads are now AI-generated, while Sony sued Udio over more than 30K songs.

* [Substack Pangram scan](https://post.substack.com/p/against-claudefishing) checks posts, notes, replies, and comments over 100 words for likely AI-assisted writing, while creators can add process statements —free for Substack readers and writers.

* [Cisco announced Antares](https://www.axios.com/2026/07/21/cisco-open-source-ai-models-cybersecurity), which scans code locally for vulnerabilities using two small open models, with Cisco claiming 500-repo scans in about 15 minutes —under $1 per scan.

* [Sen. Mark Warner](https://www.axios.com/2026/07/21/mark-warner-ai-plan) planned an AI bill covering mandatory model testing, data-center disclosures, agent rules, and a workforce transition fund.

* [World Labs](https://www.worldlabs.ai/blog/scenix) acquired SceniX to combine generative world models with high-fidelity robotics simulation and real-hardware training.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

**FROM OUR PARTNERS **

# Production-grade infrastructure for conversational AI

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8ce1408a-dd55-41a9-8890-b3941e6725fc/Agora_Neuron_Ad_Banner_-_Developer.jpg?t=1782411781)
Follow image link: (https://www.agora.io/en/products/conversational-ai-engine/?utm_source=Neuron&utm_medium=Newsletter&utm_campaign=ConvoAI-June-26)
Caption: 

Voice AI experiences often break under high concurrency, packet loss, and poor connection. [Agora's Conversational AI](https://www.agora.io/en/products/conversational-ai-engine/?utm_source=Neuron&utm_medium=Newsletter&utm_campaign=ConvoAI-June-26) platform runs on SDRTN® — the same ultra-low latency network carrying 80B+ minutes monthly across 200+ countries. Build AI agents or add voice to any application with fully managed, real-time infrastructure. 

[Get started with 300 free minutes](https://www.agora.io/en/products/conversational-ai-engine/?utm_source=Neuron&utm_medium=Newsletter&utm_campaign=ConvoAI-June-26)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# 📖 Midweek Wisdom

* [AISI’s cheating-evals post](https://www.aisi.gov.uk/blog/cheating-behaviour-in-frontier-model-evaluations) is a nice companion read to today’s OpenAI story, especially if you want to understand why eval environments now need their own defenses.

* [Nathan Lambert’s Kimi K3 essay](https://www.interconnects.ai/p/kimi-k3-the-open-weights-escalation) explains why Chinese open-weight models are closing the gap faster than U.S. labs want to admit.

* [Big Technology take on the AI price war](https://www.youtube.com/watch?v=jPbN5m2iQ_M) to examine what happens when frontier-level intelligence gets cheaper and model companies lose pricing power.

* [Claire Vo shared Alex Lieberman’s AI Oracle](https://www.youtube.com/watch?v=1_jlukb7gm4) system that turns audience signals into 15 potential content ideas each day.

* [Netflix CPTO Elizabeth Stone](https://www.youtube.com/watch?v=t0GiTyz4syY) explained why AI is raising the value of systems thinkers who can work across product, design, and engineering. _Agree! We should teach every topic through this lens, from the sciences to the humanities._

* [Morgan Linton](https://x.com/morganlinton/status/2079591662473679188) argued that per-token pricing is increasingly misleading because cheaper models can use more tokens to finish the same task.

* [Nathan Lambert’s RLHF book](https://rlhfbook.com/) is now available as a free online book, course, and video series for anyone who wants the deeper post-training primer.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# A Cat’s Commentary 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3d35897d-c8bc-48bc-b47a-3700e56f41af/A_Cat_s_Commentary_x_2025__62_.png?t=1784687842)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. 




**P.S: **_We just launched a robotics newsletter! _[Sign up for it here](https://roboticsinsider.beehiiv.com/).

** **Before you go… have you [subscribed to our YouTube Channel](https://www.youtube.com/@theneuronai?sub_confirmation=1)? If not, can you?  

**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).  


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/openai-s-new-model-escaped
