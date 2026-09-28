---
source: gmail
newsletter: "latent-space"
message_id: "1a0ce7530ebe1918"
thread_id: "1a0ce7530ebe1918"
subject: "🔬Bio-security is an AI Arms Race - Eric Nguyen (CEO, Radical Numerics)"
from: "\"Latent.Space\" <swyx@substack.com>"
date: "Wed, 23 Sep 2026 13:27:18 +0000"
ingested: 2026-09-28
sha256: 7512abf7d790ffc8f1ba041e8e3bf05f264f4fa0e1fad403e03dd774dc62acb4
---
View this post on the web at https://www.latent.space/p/bio-security-is-an-ai-arms-race-eric

The OpenAI → Hugging Face attack has people asking “what else do we need to worry about?” and Anthropic’s filters flag two things: cyber-security and biology. The natural question is: what about bio-security, then? 
Clem Delangue argues that cyber-warfare defensive capabilities need to be open and to keep pace with frontier models’ attack capabilities
Radical Numerics co-founder Eric Nguyen sat down with us and explained why the same models that increase biological capability can also keep defense from falling behind.
Building a virus from scratch
While he was at Stanford, Eric couldn’t get traction on Genomic Language Models (GLMs) for a long time. Biologists didn’t believe it would work, didn’t think they could verify the output, and didn’t see important applications beyond what they could already do. He kept pushing, eventually helping lead the development of Evo and contributing to Evo 2 at Arc Institute. Those models were later used by a separate Arc/Stanford team to generate entire bacteriophage genomes that were synthesized into functional viruses [ https://substack.com/redirect/c24838ef-b62c-441e-bf3e-134747254524?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]!
Long context unlocks biological intelligence
Early ChatGPT spit out poems and email, and early DNA language models like Evo and Evo-2 could build a genome from scratch. DNA is different, however, from natural language in that it has a very small alphabet (4 characters ACTG) and that its sequences are very long:
60K for an average human gene
long being up to 2.3M
the whole human genome around 3B.
Innovation in long-context models [ https://substack.com/redirect/43c3e48d-7597-47f2-9157-7e67588ba235?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] made this possible about 3 years ago (footnote: striped hyena), long before the frontier labs were building 1M+ context models.
Now Eric and other AI x Bio luminaries have founded Radical Numerics to build and scale GLMs to tack a wide range of biological problems, extending well beyond generating DNA.
Thinking in DNA
Their GLMs already do pretty well with RNA and protein because there are clear markers in the DNA sequence for genes (RNA sequences the perform many functions) and specific genes that encode proteins. This means that the models already generalize to multiple “languages,” before even attempting to train in other modalities, such as 3d protein structure, epigenetics and natural language.
If a model thinks in the DNA language, maybe it understands the imprint that environment left on different genomes as well? Perhaps the model has learned the functional relationship between different sequences, and could extrapolate to new sequences based on that?
And so what we wanted to showcase was that if we show the model progressively better RNAs in a series of steps with its score, right? So you have like low scores first and then you gradually move up the chain. Can the model continue that trajectory on its own? And then in the final step, does it self optimize to a point where it's like the best score it can get? That was the experiment. Can we do that? And so we took a data set, a large data set of aptamers. We held out a portion of the best performing ones and we showed it only the lower ones, but then we ranked it, right? So we showcase lower scores with the RNA aptamers and then progressively got higher, and then ask the model to just like continue with that pattern. And it turns out it was able to recapitulate some of those higher scores that we had not shown it yet.
So, voila: chain-of-thought, thinking in DNA!
The arms race
But much as long-context inference, chain-of-though and multi-modal perception unlocked sophisticated reasoning in natural language LLMs, these capabilities in GLMs are enabling increasingly sophisticated “biological intelligence,” and along with it, greater danger.
According to Eric, defense is currently losing this battle, but Radical Numerics argues to push the frontier harder!
I won’t spoil the details for you. In the episode we talk in detail about:
Biosecurity as an arms race — and how defense can keep up
The genome as the imprint of the environment on DNA
Going truly multi-modal
How chain-of-though works when you “think” in the language of DNA

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3lOamt3TVRreExDSndiM04wWDJsa0lqb3lNVFkzTWpNeU9URXNJbWxoZENJNk1UYzVNREUzTURFNE1Dd2laWGh3SWpveE9ESXhOekEyTVRnd0xDSnBjM01pT2lKd2RXSXRNVEE0TkRBNE9TSXNJbk4xWWlJNkltUnBjMkZpYkdWZlpXMWhhV3dpZlEuM0w1eEhBTDJoekpiclBSeVNIamNTd3prSGdRS2g0SkxQUFpjUXpQYXBSbyIsInAiOjIxNjcyMzI5MSwicyI6MTA4NDA4OSwiZiI6ZmFsc2UsInUiOjI2OTAxOTEsImlhdCI6MTc5MDE3MDE4MCwiZXhwIjoyMTA1NzQ2MTgwLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.p_fFZFgGpHrIipoFeL1j2cRBqshjRGjYRCdBSE4r3pQ?
