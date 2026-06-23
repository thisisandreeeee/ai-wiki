---
source: gmail
newsletter: "latent-space"
message_id: "19e8ef72bb2b0680"
thread_id: "19e8ef72bb2b0680"
subject: "🔬Scaling Past Informal AI - Carina Hong, Axiom Math"
from: "\"Latent.Space\" <swyx@substack.com>"
date: "Wed, 3 Jun 2026 19:27:49 +0000"
ingested: 2026-06-23
sha256: 2549e663d52c52b3f3a775ed4689cc5c8208f390d3e19fbb89e84fdd7bbc324c
---
View this post on the web at https://www.latent.space/p/axiom

In 2025, seven-month-old startup Axiom solved all 12 of the problems Putnam exam [ https://substack.com/redirect/69dc8833-a5c4-4f35-ae31-23cbdacb7a12?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] (scoring 8/12 in the time limit) a prestigious undergraduate math exam. The 12/12 score is better than the top undergraduates (110/120) and the closest AI system that reported a result (DeepSeek 103/120), although it is unclear what the people and other systems would have scored with more time. Nonetheless, the Putnam exam is legendary for its difficulty, with the median score typically being 0 or 1 points. Taken by itself, this seems like a minor feather in the cap of AI; one of a long series of accomplishments by AI systems in elite competitions with humans, starting with Deep Blue beating Kasparov.
Fast forward to mid-2026, and Claude Code and Codex are setting the world on fire. In 2024 Anthropic’s bet on code and enterprise looked like a more pragmatic niche play vs. OpenAI’s better models and massive consume scale. Today, Amodei’s all in bet on acceleration via code (images and video be damned) seems prescient.
Despite Anthropic’s growing momentum, however, Axiom CEO Carina Hong sees coding ability as a necessary but not sufficient milestone on the path to AGI. Code arguably pushes the jagged frontier to the point of super intelligence in some domains outside of coding [ https://substack.com/redirect/138a4f76-4843-4b98-b6a5-c393881c52e7?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], but there are surprising gaps (link) that Carina believes will bottleneck AI progress. (Stats on math benchmarks).
The informal bottleneck
“Verified AI” sounds like eating broccoli and paying taxes, but to Axiom it means something very different. “Verification to me is about scaling brilliance, compounding brilliance,” Carina told us.
It actually took a while for me to understand what she means by this (sounded like marketing-speak until it clicked). Carina brings up the legendary mathematician Srinivasa Ramanujan (“The Man who knew Infinity” [ https://substack.com/redirect/6a65e44f-3033-4344-b0af-fe52f65d4e33?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]) to illustrate this point. When G.H. Hardy finally persuaded Ramanujan to formally prove theorems instead of relying on his (formidable) intuition, it reportedly improved his own capabilities. This is presumably because formally proving things forced Ramanujan to articulate the details in a way that open up new lines of thinking, etc. This is how you “compound” in math — building on solid rather than shaky foundations… also known as Axioms.
But formally proving things also allowed others to benefit from his intuition: the proofs are way of communicating an intuition and persuading others that the intuition is correct. This is scaling (more people use the result) and compounding (people can learn from and build on his work).
This is the core insight that lets us understand the approach Axiom is taking.
Verified Generation
There are two ways that Verified AI shows up: in training and in inference.
But a quick detour: to a first approximation, “Formal Verification” means using type checkers [ https://substack.com/redirect/cc270ba6-6e21-4eee-ad54-51442af19ca9?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] (like for TypeScript, C++ or Rust, but more capable) to verify mathematical proofs that are meticulously specified using a language like Lean. It takes a lot of work to translate an “informal” proof (albeit one that most people would not remotely call “informal”) in to a Lean proof. Axiom themselves have open sourced groundbreaking work with AXLE [ https://substack.com/redirect/97bde5c5-b481-4e6f-a20c-739ef6e60b67?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] - their toolkit of interactive Lean applications for exploring, validating, and manipulating mathematical proofs.
You can imagine how this would be (very) useful during Reinforcement Learning: instead of relying on best guesses based on statistics (GRPO, RLHF, etc.), you can just verify the proof is correct using a Lean verifier. This is obviously a much stronger reward signal, akin to compiling code and testing it (which is what is typically done with RL on coding).
The catch: LLM are not (currently) very good at proving things with Lean.
Enter Axiom: While they have not officially reported benchmark numbers besides the 12/12 Putnam result, Carina reports that they have achieved a very impressive 99% (187/189) ProofGen on the Verina codegen benchmark [ https://arxiv.org/html/2505.23135v1 ]. This benchmark is to generate code and proof of correctness for a series of problems. For context, OpenAI o3 (the last known OpenAI run) achieved 4.9% on this benchmark.
Based on the sparse benchmarking, it’s hard to say how the frontier labs are currently doing outside the annual IMO milestones [ https://www.latent.space/p/captaining-imo-gold-deep-think-on ], but Carina suggests that they still are not training to generate Lean proofs directly, rather relying on informal proofs.
Time will tell if the frontier labs’ current approaches will close this gap.
Scaling and compounding
Carina’s Ramanujan analogy is pretty direct. Better proofs → better Lean generation → better RL. A stronger signal means higher sample efficiency and higher maximum performance. Great!
Scaling is pretty clear too: once I have proved something in Lean, the quality of the output is basically as high as if it came from a human, so my high quality training set has grown in a way that an informal rollout corpus cannot. I can trust my Lean proofs.
Compounding is also clear: now all of future inference and training can build upon those proofs.
On the other hand, a model trained only using statistical signals like GRPO during RL lacks the sample efficiency, maximum performance and compounding corpus that a system that uses formal verification benefits from.
All roads lead to verification
Broccoli and taxes notwithstanding, verification has shown up in a lot of our conversations. In the domain of physical systems, recall Applied Intuition [ https://www.latent.space/p/appliedintuition ]:
“I think [verifiability] is probably the hardest problem right now, because the as the models get better, it can be harder and harder to find the faults on the system. And so the problem of doing proper eval to find those faults, that problem also keeps getting harder as the models get better.” 
In theoretical physics, we recall Alex Lupsasca:
“…now that we’re in this regime where you can just get ChatGPT to tackle thousands of questions at the same time, it will return proofs for a significant fraction of them. Now actually the onus is back on the humans to verify all the outputs. And so, yeah, as that becomes a bottleneck, I think formalizing math and automating verification will become more valuable.”
Verification is, in fact, the key differences between AI for science and AI for computation: in science you to have to actually test (verify) your hypothesis by performing physical experiments. Lab in the loop systems like Radical AI [ https://www.radical-ai.com/ ] and Lila [ https://www.lila.ai/ ] build around exactly this premise (we have recorded episodes with both of these teams and will release them soon!)
And yes, formally verifying critical systems such as flight control, nuclear power plants and pacemakers is a growing focus as the software and hardware that run them becomes more complex.
Carina believes so strongly that AGI requires verified generation that she makes the unqualified claim that “We do not believe there is any other possible future.”
Expensive to produce, cheap to verify
Lean proofs are hard generate, but they can be easily shown to be correct or incorrect. But how do you know that the proof you created maps correctly to the problem you care about? As Carina puts it: “Anything that can be specified can be proven. Humans are bad at specifying everything we want.”
Are we now in the specification business? Check out the episode to hear Carina’s take, as well as:
Why hardware verification is a killer app
Details on the AXLE open API and recently released Discovery toolkit
The Erdos debacle
The OpenAI GPT-f diaspora
Full Video Podcast
Timestamps:
0:00 Intro: The $200M Series A and the Math Startup Thesis
4:52 Verified AI: Scaling Brilliance, Not Fixing Lousiness
13:42 Axiom’s System: Lean Data, RL, and the Putnam Perfect Score
22:12 Mathematical Discovery — Before the Conjecture
25:12 Rice’s Theorem, Incompleteness, and Practical Limits
30:42 Code With Proof — The Verina Benchmark
37:57 Proof Trees, Context Windows, and Scaling Limits
43:57 Markets, Moat, and the Business Case ($1.6B valuation)
55:27 Personal Origin Story: Oxford, UCL Gatsby, Stanford Law
1:00:57 The Erdos Controversy and the Difficulty of Search
1:06:02 AlphaZero for Math, Self-Improvement
1:08:47 Startup Advantage and the OpenAI GPTF Thread
1:13:17 Axle API — Open Infrastructure for Lean at Scale
1:20:47 Collaboration, Polymath, and Human Attention as the Bottleneck
1:22:21 Founding Story — Obsession, Law School, and Julie Zhuo
1:26:17 The Bigger Vision — AGI, Science, and Transfer Learning
1:35:02 Bottlenecks, Fragmentation, and the Field’s Future

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3lOamt3TVRreExDSndiM04wWDJsa0lqb3hPVGs1T1RRNE9EWXNJbWxoZENJNk1UYzRNRFV4TlRBeU1Td2laWGh3SWpveE9ERXlNRFV4TURJeExDSnBjM01pT2lKd2RXSXRNVEE0TkRBNE9TSXNJbk4xWWlJNkltUnBjMkZpYkdWZlpXMWhhV3dpZlEuXzl6eWFqSURkQWQ1eXV1QkstU3lBSGVSQ1pUM3BCX1lLQUJaN0JhWTZBNCIsInAiOjE5OTk5NDg4NiwicyI6MTA4NDA4OSwiZiI6ZmFsc2UsInUiOjI2OTAxOTEsImlhdCI6MTc4MDUxNTAyMSwiZXhwIjoyMDk2MDkxMDIxLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.uKes1z9wK5kDv1zmSLHwBrDa-reNlv3GlXMBXr5fgu8?
