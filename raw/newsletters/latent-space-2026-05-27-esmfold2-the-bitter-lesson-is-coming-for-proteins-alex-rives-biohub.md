---
source: gmail
newsletter: "latent-space"
message_id: "19e6a8cea3575f41"
thread_id: "19e6a8cea3575f41"
subject: "🔬ESMFold2: The Bitter Lesson is Coming for Proteins - Alex Rives, BioHub"
from: "\"Latent.Space\" <swyx@substack.com>"
date: "Wed, 27 May 2026 17:46:16 +0000"
ingested: 2026-06-23
sha256: fa715f22038e0db3636f20f4a2c104aaca62a363eed55f8127ae87956b8b1a08
---
View this post on the web at https://www.latent.space/p/esmfold2

Editor’s note: In our first BioHub pod with Priscilla and Mark [ https://substack.com/redirect/c2831316-8ae9-4579-9b51-31a7d73909bf?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] they discussed their acquisition of EvoScale [ https://substack.com/redirect/88ad37c8-f8c0-49f6-aadb-ab23cd87b691?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], led by Alex Rives [ https://substack.com/redirect/3c1f9ea8-1d15-4bf5-8a7e-8cd51a21ae34?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], who is now Head of Science at BioHub. With ESM-1 they trained language models on millions of protein sequences drawn from across life, with a simple “next token” objective: predict the amino acids that have been randomly masked out, based on the context of the rest of the sequence. But they soon found that these models also learned biological structure and function, including properties the model had never been explicitly shown AND that this ability scales predictably with compute, leading to ESM2 and ESM3 [ https://substack.com/redirect/3e454270-c7c7-4bc1-9971-f9dfb106afb8?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Today, Alex announced [ https://substack.com/redirect/12f46b3b-768e-441a-9ff1-db42e4d0c6a0?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] ESMFold 2, an open scientific engine to power prediction, design, and discovery across protein biology.
Building on Cryo-EM data (discussed in the CZI pod), ESMFold2 reports state of the art performance on protein interactions, especially antibodies, a critical modality for therapeutics, and evidence that inference time scaling is also working across five targets in cancer and immunology.
In a nod to that other famous AI x protein folding project, they are also releasing an atlas of 6.8 billion proteins, and 1.1 billion predicted structures, which you can play around with on their website [ https://substack.com/redirect/63b13e51-e3dd-4432-ab54-9b5e5d663ba8?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]. We are honored to work with them for this huge release!
One of the refrains we’ve heard on the Science pod has been that protein folding, materials design, cellular biology, etc. are very different problems from Language Modeling. They definitely are. Yet Alex Rives and the ESM team at BioHub just released a preprint and model [ https://substack.com/redirect/0d17e5aa-f9a0-4309-8141-b2928e8f208a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], demonstrating that vanilla BERT-like transformer models trained on sufficiently large and diverse data sets can beat specialized models like AlphaFold3 on some of the hardest protein-related problems. 
Andrew White had a great segment [ https://substack.com/redirect/aeaeebd6-3ae7-40cb-9bc8-724599bb1542?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] in our first LS-Science episode that explained how mind blowing AlphaFold2 was when it was released in 2020: it suddenly solved problems on a GPU on your desktop that DESRes [ https://substack.com/redirect/98a92dd0-9c27-4a39-b7bd-192c297dfbff?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] had built custom-ASIC supercomputer clusters to solve. John Jumper and Demmis Hassabis received the Nobel Prize [ https://substack.com/redirect/2f3cfed9-878a-455a-8a12-63a5dc3aad71?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] in Chemistry for this work.
AlphaFold2 took advantage of an very clever observation: if multiple species co-evolve pairs of mutations, this implies that the mutations correspond to parts of the protein that are close in 3d space. This is usually shorthanded as MSAs (multi-sequence alignments), and is the key insight which makes AlphaFold2 so effective.
Like other inductive biases, however, it hurts generalization.
Scale-pilled before it was cool
If you take a look at the timeline for scaling laws for LLMs and release of structure prediction models, the ESM team notably doubled down on their MSAs-be-damned approach after AlphaFold2 released. This obviously requires a great deal of belief in the scale hypothesis.
Why the conviction?
ESM developed at a time when many of the scaling laws and the “Bitter Lesson” were proving increasingly correct. AlphaFold2’s wild success must have been both exciting and bitterly disappointing.  But using MSAs mean that the model is is dependent on training data that contains MSAs in order to be accurate in a given domain.  For things like antibodies that don’t have MSAs to train on, AlphaFold tends to do poorly.
ESM takes a different approach: learn the relationship between different proteins by unsupervised training on as much diversity as you can find (sound familiar?) and then correlate that back to structures know from the Protein Data Bank (PDB) and other sources. 
In other words, a World Model.
World Model for proteins
“World Model” is a hype term that I define like this:
Use unsupervised training to learn abstract patterns from the data:
The abstraction should be semantic - novel constructions represent things that obey the rules of the real world
The abstraction should be compositional - recombining different patterns leads to novel and often valid constructions
The abstraction should support generalization - it predicts things in the real world it wasn’t trained on 
Once you have a world model, you can attach “heads” to it for downstream tasks: predict properties of a protein, decompose its functional features, or search the representation for proteins that meet design criteria. The two big models BioHub just released under MIT license map directly onto this:
World model → ESMC (a model trained on 2.8 billion sequences)
Structure-prediction head → ESMFold2
One of the interesting ways the world model can “predict things” is to generate proteins sequences and then measure the predicted properties, such as binding affinity, in the lab.  Alex talks in the episode about validating some of the harder molecules they predicted in the wet-lab. Very cool!
Another way is to use mech-interp techniques such as Sparse Auto Encoders [ https://substack.com/redirect/afa6d871-5beb-41a8-9fe5-6945339d1035?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] (SAEs) to extract semantic features from your model, and then find novel features that predict unknown biology.  I won’t spoil this part for you: it was one of the highlights of the episode for me!
A cell is a computer
We have all heard that genes are like computer programs, but usually the analogy fizzles after that. Of course genes are transcribed into RNA and RNA is translated into proteins, so genes are programs for building proteins, but that carries the analogy only to “binary digits are programs.”  
Here’s a better analogy: you can think of the cell nucleus as a storage device / storage controller, the ribosome as a JIT-compiler and runtime, and the semantic features that we learn from our world model via SAEs as functions, proteins as processes that interact together in workflows (signalling pathways) to produce behaviors and outputs (phenotypes). 
Like functions, the SAE features have a hierarchical composition from local, secondary and tertiary structures (mimicing protein structure), but also motifs that are conceptual, such as membrane integrations, disordered regions and disulfide bonds. As we learn to compose these features we into novel protein designs, we move further towards programmable biology. 
Alex goes into much more detail about this in the episode, as well as:
Principles for new data collection
BioHub’s vision
Modeling the cell
Enjoy!
Full Video podcast
please like and subscribe!
X: https://x.com/alexrives [ https://substack.com/redirect/8d536778-84e5-4a23-9ffd-3f253893a3b8?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]
LinkedIn:

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3lOamt3TVRreExDSndiM04wWDJsa0lqb3hPVGswT0RjNE16WXNJbWxoZENJNk1UYzNPVGt3TkRBM09Dd2laWGh3SWpveE9ERXhORFF3TURjNExDSnBjM01pT2lKd2RXSXRNVEE0TkRBNE9TSXNJbk4xWWlJNkltUnBjMkZpYkdWZlpXMWhhV3dpZlEuRlFDLURpYnNyVjFuV1E5NjM5by1WTk5BZWRaWGx5MjZNOHZNdFZ3X3FwNCIsInAiOjE5OTQ4NzgzNiwicyI6MTA4NDA4OSwiZiI6ZmFsc2UsInUiOjI2OTAxOTEsImlhdCI6MTc3OTkwNDA3OCwiZXhwIjoyMDk1NDgwMDc4LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.VqOczLnVcDEyCwN-VeNXh106dHIORYJa6AtFvgP8vm8?
