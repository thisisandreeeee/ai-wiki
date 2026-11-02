---
source: gmail
newsletter: "the-neuron"
message_id: "1a18c6587f7d0731"
thread_id: "1a18c6587f7d0731"
subject: "😸 You can now download Mistral Large 4"
from: "The Neuron <theneuron@newsletter.theneurondaily.com>"
date: "Fri, 30 Oct 2026 10:39:58 +0000 (UTC)"
ingested: 2026-11-02
sha256: ce3b754ac828e334810e0b2fc562defbb0107cb481c2f7aa3683d17e5dc7c3ac
---
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/70782624-7dc8-45c6-a1e0-47a25f70d75f/Mistral_s_Open_Weights_Vault.png?t=1793343268)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2fc7e13d-f65f-434d-9e36-6d1834e224bf/In_partnership_with_triple_whale__1_.png?t=1793290841)
Follow image link: (https://www.triplewhale.com/bfcm-command-center?utm_source=neuron&utm_medium=paid-media&utm_campaign=mkt-bfcmcommandcenter-paidmedia-1026&utm_content=newsletter_primary-10302026)
Caption: 

Welcome, humans.

So apparently Amazon just posted its fastest AWS growth in almost five years, with [sales up 39% to $46.0B](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx) and usage of Bedrock (its service for building apps on AI models) growing nearly 17x.

Then you scroll down to the cash line. Amazon's free cash flow over the last 12 months swung from a $14.8B inflow to a $42.4B outflow, a $57B swing, mostly because of AI spending.

And the spending keeps going: Amazon is holding its roughly $220B capex plan for 2026, mostly for AWS, and told investors 2027 will be even bigger. _Free cash flow has never felt less free._

**Here’s what happened in AI today:**

* 😸 Mistral releases open weights for trillion-parameter Large 4

* 📰 Reddit tests mostly logged-in browsing as search traffic drops

* 📰 Deepgram agrees to buy voice-agent maker Daily

* 📰 Wabi raises $55M at a $1.25B valuation

* 🍪 Meta quietly launches Style Sketch closet app in Southeast Asia

…and a **whole lot more that you can read about here(hyperlink bold text w/ link)**.

Advertise to 700K readers of The Neuron here! (https://www.theneuron.ai/get-media-kit/)

Your Black Friday deal. **700,000 subscribers.** Get your offer in front of **The Neuron’s **audience with a sponsored spot in our special Black Friday edition. Have a Black Friday or Cyber Monday promo planned? [_Let’s talk!_](https://solutions.technologyadvice.com/lp/advertise-in-black-friday-newsletter/)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777310197)
Caption: 

# 😸 Mistral Releases Open Weights for Its Trillion-Parameter Large 4 Model

[Mistral](https://mistral.ai/news/mistral-large-4-oss/) just released the downloadable weights for Mistral Large 4, a 1-trillion-parameter model nicknamed Le Chonk, on Hugging Face and through its API, three weeks after an October 6 preview. _Le Chonk. We respect the commitment._

Weights are the numbers a model learned in training, basically its brain. With them, a company can run the model on its own servers and keep its data in-house instead of sending it to someone else's API. Large 4 is also a mixture-of-experts model, so only about 49B of its trillion parameters work at a time, like calling the right specialists instead of the whole hospital.

Here's what happened:

* Mistral spent three more weeks on reinforcement learning (training by reward) after the preview, and says the model ties GLM-5.3 on a coding-agent index while using 47% fewer tokens per task.

* It handles text and images, offers three reasoning settings, supports a 1M-token context window, and runs on Microsoft Foundry.

* Artificial Analysis called the preview the strongest model it had seen from outside the U.S. and China. Mistral's newer numbers are its own and haven't been independently replicated.

**Here's the part worth slowing down on:** Mistral says its testing suggested Large 4 could increase attackers' real-world abilities, even though the model refused 96.6% of malicious cyber requests on selected benchmarks. That figure covers a defined test set, not every attack. With public weights, nobody has shown how much protection survives modification, and Mistral hasn't said how big the boost could be.

So Mistral split the release. The general model is downloadable, but a stronger cyber variant goes only to vetted partners like Orange Cyberdefense. That variant is for penetration testing and red-teaming, and contracts limit testing to systems the testers own or are authorized to probe. Google limited Gemini 4 Carbon to selected defenders on October 28, and Anthropic expanded its Cyber Verification Program on October 6. Nothing shows these moves are connected.

One attribution needs care. Mistral's announcement carries a statement attributed to an ENISA spokesperson (ENISA is the EU's cybersecurity agency) about testing Large 4. ENISA confirmed testing Mistral's cyber models earlier in October, but Agence Europe corrected a report on October 16 to say Large 4 wasn't named. ENISA's own confirmation wasn't located.

**Running it:** Downloading is cheap, and running it is not. Mistral's recommended setup splits the model across eight GPUs. The modified MIT license allows internal self-hosting, but anyone selling the model as a service needs a separate commercial license, which is tighter than Large 3's Apache 2.0.

**Why this matters:** Banks, governments, and security teams that can't send sensitive code to an outside API now have a frontier-scale model they can host themselves. Cisco, Cloudflare, CrowdStrike, ABN AMRO, and others offered supportive statements, ranging from testing to plans, so they don't all prove finished deployments. Mistral also pitches a European option (a €3B round led by Samsung, training on 3,800 Nvidia GPUs in European data centers), but Microsoft committed billions in July to use part of that capacity. Control here means choosing where the model runs, not cutting ties with U.S. companies.

**Our take:** _Mistral is betting that control sells, and the partner list suggests some buyers agree. But the pitch rests on Mistral's own benchmarks and a safety call Mistral made itself. The company hasn't said how much easier attacks could get, so the full technical report is the document to watch._

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1774505086)
Caption: 

**FROM OUR PARTNERS**

# Run this holiday shopping season from the free BFCM Command Center.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/59e8e3b0-97f9-4c11-a539-d7ae638da47e/BFCMProductExperience_2x1_newsletter_EBlast__2_.png?t=1793290276)
Follow image link: (https://www.triplewhale.com/bfcm-command-center?utm_source=neuron&utm_medium=paid-media&utm_campaign=mkt-bfcmcommandcenter-paidmedia-1026&utm_content=newsletter_primary-10302026)
Caption: 

Black Friday and Cyber Monday compress decisions into minutes. Moby, the AI teammate for commerce, helps you keep up.

Moby lives inside Triple Whale's free BFCM Command Center, and understands your business and past performance. Before the rush, set one plan for your revenue goal, budget, and channel mix. Once your sale starts, Moby surfaces what needs attention, tells you what changed, and recommends what to do next.

You review, approve, and act while there's still time to change the outcome. You stay in control.

Your BFCM Command Center is waiting.

Get started for free (https://www.triplewhale.com/bfcm-command-center?utm_source=neuron&utm_medium=paid-media&utm_campaign=mkt-bfcmcommandcenter-paidmedia-1026&utm_content=newsletter_primary-10302026)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# 🎓 AI Skill of the Day: Make your website discoverable by AI with Claude

A reader told us Claude flagged their business website as invisible to AI search. But how do you know what's actually broken, and what should you fix first?

[Semrush just published a walkthrough](https://www.semrush.com/blog/semrush-seo-audit-with-claude/) that connects its website auditing tool directly to Claude. Semrush scans your site for broken links, indexing problems, and technical issues. Claude then analyzes that evidence and helps prioritize repairs. _Finally, a website diagnosis based on data instead of AI vibes._

Here's the workflow:

1. **Audit your website.** Create a project in Semrush Site Audit and run a crawl. Check broken internal links, 404 errors (missing pages), and the AI Search Health report, including whether search crawlers can access important pages.

2. **Connect the audit to Claude.** In Claude, open Settings → Connectors, find Semrush, and authorize it. Ask Claude to retrieve your completed audit and build a repair plan ranked by business impact. Focus on your important service or product pages first.

3. **Fix, rescan, and measure.** Repair incorrect links in your website editor, redirect genuinely moved pages, and resolve accidental crawler restrictions. Rerun the audit to confirm the fixes. Then use Semrush's [Prompt Tracking](https://www.semrush.com/kb/1503-prompt-tracking) to monitor whether your business appears or gets cited when people ask AI tools questions about your services.

You can also give Claude this supporting instruction:

```
Using my latest Semrush Site Audit, identify the 10 highest-impact problems. Show affected URLs, evidence, recommended fixes, who should implement them, and how to verify each repair. Prioritize pages that generate business.
```
One important distinction: fixing technical problems makes your website easier to discover, but doesn't guarantee AI recommendations. The next thing to track is whether your important pages actually start appearing in relevant AI answers.

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

**FROM OUR PARTNERS**

### Most AI Tools Weren't Built for This

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d034705b-2aa8-46d3-857c-59a57efebfd7/1200x627__Concept_A.png?t=1790093678)
Follow image link: (https://front.com/resources/coordination-gap?utm_source=beehiiv&utm_medium=cpm&utm_campaign=ongoing_YJ4ZPRQDHV_consideration_norpac&utm_content=HBR_Report_V1&_bhiiv=opp_ed381483-be4f-4f87-91ef-c16cc2568d1f_c408311b&bhcl_id=202efb82-d95e-4369-ad58-e372f6e93cba_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)
Caption: 

B2B customer issues move across teams and systems, not through a single chat window. A new [Harvard Business Review Analytic Services](https://front.com/resources/coordination-gap?utm_source=beehiiv&utm_medium=cpm&utm_campaign=ongoing_YJ4ZPRQDHV_consideration_norpac&utm_content=HBR_Report_V1&_bhiiv=opp_ed381483-be4f-4f87-91ef-c16cc2568d1f_c408311b&bhcl_id=202efb82-d95e-4369-ad58-e372f6e93cba_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f) briefing paper, sponsored by Front, breaks down where AI tools fall short in B2B service and what to ask before you invest.

[Get the Free Report](https://front.com/resources/coordination-gap?utm_source=beehiiv&utm_medium=cpm&utm_campaign=ongoing_YJ4ZPRQDHV_consideration_norpac&utm_content=HBR_Report_V1&_bhiiv=opp_ed381483-be4f-4f87-91ef-c16cc2568d1f_c408311b&bhcl_id=202efb82-d95e-4369-ad58-e372f6e93cba_442a72a3-e456-4c93-a138-def08506a93e_7495e2a4-ed2a-4100-a8a9-196611122b0f)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3e18b5e5-17be-4d32-84f0-d3be471494d2/image.png?t=1772983496)
Caption: 

# 📰 Around the Horn

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7d2a9e01-38ab-4c34-81c1-c7eea688340c/image.png?t=1793345553)
Follow image link: (https://x.com/Gemini_Notebook/status/2115887660489462091)
Caption: **Plot twist for finals week:** the free textbook is right there, and your procrastination has no one left to blame.

* Reddit said it [will test logged-in browsing](https://techcrunch.com/2026/10/29/as-search-traffic-dries-up-reddit-announces-its-shifting-to-a-logged-in-experience/) in select non-U.S. markets as search referrals fell by 1M+ per week.

* Deepgram [agreed to buy Daily](https://techcrunch.com/2026/10/29/deepgram-acquires-pipecat-maker-daily-to-bolster-its-voice-ai-infrastructure/), the team behind open-source voice-agent framework Pipecat, and promised to keep Pipecat free.

* Wabi [raised $55M](https://techcrunch.com/2026/10/29/wabi-the-ai-agent-that-builds-mini-apps-now-valued-at-1-25b-after-latest-round/) at a $1.25B valuation for a shared personal agent from Replika creator Eugenia Kuyda.

* Rivian [said it will license](https://techcrunch.com/2026/10/29/rivian-expands-joint-venture-with-vw-to-include-ai-assistant/) parts of its AI voice assistant to Volkswagen through their $5.8B joint venture.

* Dream [emerged from stealth](https://techcrunch.com/2026/10/29/ex-palantir-execs-launch-dream-with-17m-from-a16z-to-build-ai-world-models-for-construction/) with $17M from a16z to generate full building layouts, plumbing and HVAC included.

* SuperMe [raised $20M](https://techcrunch.com/2026/10/29/superme-raises-20m-for-its-network-of-ai-expert-profiles/) to build AI profiles of human experts, led by Forerunner with Greylock joining.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1777315670)
Caption: 

# 🍪 Treats to Try

_*Asterisk = from our partners (only the first one!). _[_Advertise to 700K+ readers here_](https://info.technologyadvice.com/advertise-with-the-neuron)_!_

1. *Found a task you’d happily hand to an AI agent? **The Neuron Academy** has step-by-step courses on building workflows, agents, and apps. _The task will still be there after the lesson. Sorry. _[Learn how to build yours →](https://theneuronacademy.com)

2. [Mistral Large 4](https://mistral.ai/news/mistral-large-4-oss/) gives you a trillion-parameter model you can download and run on your own servers or call through Mistral's API.

3. [Floot](https://floot.build/) builds full apps with a database, logins, hosting, and a live link from a chat inside ChatGPT.

4. [Empacer](https://www.empacer.com/) turns your spoken requests into draft customer replies, social posts, and invoices, then waits for your approval before anything goes out.

5. [Style Sketch](https://techcrunch.com/2026/10/29/meta-quietly-launches-an-ai-fashion-app-called-style-sketch/) is Meta's new app that builds a virtual closet from your Instagram photos and suggests outfits, try-ons, and packing plans (Indonesia, Singapore, and Thailand only for now).

6. [Viggle JST-2](https://viggle.ai/jst2) turns text, images, or video into 3D scenes and full-body character motion that follows real physics.

7. [Mintive](https://www.mintive.com/blog/mintive-launch) gives each of your agents its own revocable identity and logs every action from user to agent to tool call (raised $11M).

8. [phpClaw](https://github.com/phpclaw-php/phpclaw-monorepo) gives PHP developers an MIT-licensed agent runtime with tools, memory, and adapters for Laravel, Symfony, WordPress, Drupal, and Magento.

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

# 💡 Intelligent Insights

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/39004987-9828-4ab7-a713-8f9367ae68c6/Personality_Indexes__30_Oct__26_.png?t=1793345869)
Follow image link: (https://artificialanalysis.ai/articles/aa-personalitybench#personality-indexes-chart)
Caption: 

* Artificial Analysis [launched AA-PersonalityBench](https://artificialanalysis.ai/articles/aa-personalitybench), which ranks 38 models on 30 traits like humor and sycophancy, and scored Claude Fable 5.1 funnier than Claude Opus 5.5.

* Chip War author Chris Miller [argued](https://www.washingtonpost.com/opinions/2026/10/29/ai-build-out-has-given-america-dutch-disease/) that data centers are soaking up memory chips, workers, and resources, raising costs for industries that get no AI upside.

* FT reporters Clara Murray and John Burn-Murdoch [found](https://www.ft.com/content/1cc2516d-b718-4e2c-a3b2-1f8bd8acce01) that agents speed up research and coding, but checking their results adds stress, mistakes, and work (subscription required).

* Zocdoc CEO Oliver Kharraz [argued](https://fortune.com/2026/10/28/zocdoc-ceo-will-ai-agents-make-your-business-more-valuable-or-more-vulnerable/) that as AI assistants bypass websites, companies with verified information and real transactions could gain influence.

* The Atlantic's Ross Andersen [explored](https://www.theatlantic.com/technology/2026/10/ai-hedge-financial-tips/689187/) how AI scenarios, from widespread prosperity to severe job disruption, could upend conventional retirement planning.

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8fcaf1c4-3238-439a-bc66-57f7c4a27e05/image.png?t=1777315698)
Caption: 

# New from The Neuron: AI Explained

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a377e108-d280-4f8c-8ac7-fe757c6f3335/TN_Thumbnail_102826_EvanBeard_StandardBots_B.png?t=1793142809)
Follow image link: (https://www.youtube.com/watch?v=BCfQwnUyuPM)
Caption: Click the image to watch the video!

New episodes air **every week** on Wednesdays: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001) | [YouTube](https://www.youtube.com/@theneuronai)

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e3fc4846-242b-4300-a968-fefe66ec4628/image.png?t=1774646505)
Caption: 

# A Cat’s Commentary

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d233304e-9482-42de-bf58-da0595f9adab/Cat_s_Commentary_2026-10-28_at_7.33.11_PM_3.png?t=1793345746)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/cb85188d-9e8c-4d8f-9a61-4106067d3400/image.png?t=1777315630)
Caption: 

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a91e1dde-2674-4f02-9770-8dc0e804d697/image.png?t=1764643057)
Caption: 

That’s all for now. If you want to get featured above, fill out the poll below and tell us how we did today!




**Btw: **We just launched a robotics newsletter! [Sign up for it here](https://roboticsinsider.beehiiv.com/).

**P.S. **Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences).


———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://www.theneurondaily.com/p/mistral-released-a-1t-parameter-open-model
