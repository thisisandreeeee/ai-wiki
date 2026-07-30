---
source: gmail
newsletter: "latent-space"
message_id: "19fb2c039462addf"
thread_id: "19fb2c039462addf"
subject: "Ontologies Are So Back: Why AI Agents Are Reviving the Semantic Web"
from: "\"Latent.Space\" <swyx@substack.com>"
date: "Thu, 30 Jul 2026 11:17:55 +0000"
ingested: 2026-07-30
sha256: 0fd398889a3a283bc14ce78fc2317b767fdcb7a309da1dd6e12c5e2f48f1ebd9
---
View this post on the web at https://www.latent.space/p/ontologies-agentic-systems

One of the most watched videos from the recent AI Engineer World’s Fair is a 20-minute talk by  [ https://substack.com/redirect/ee542172-397a-489b-be30-3ea642dd7b6a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]Frank Coyle [ https://substack.com/redirect/ee542172-397a-489b-be30-3ea642dd7b6a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], a professor of computer science who currently teaches generative AI and LLMs at UC Berkeley. Drawing on his decades of experience, Coyle re-introduced the concept and practice of ontologies to today’s AI engineers.
Coyle argued that while LLMs are very effective at providing probabilistic reasoning, for agentic systems to be truly effective they need “logical guardrails” — by which he means ontologies.
In computer science, an ontology is “a description of data structure – of classes, properties, and relationships in a domain of knowledge” (as nicely defined by Oxford Semantic Technologies [ https://substack.com/redirect/c305d876-1209-4f8c-9d75-08cc554d991b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]). Coyle himself defined an ontology as simply “data as graphs.” He added that ontologies as a concept go right back to Aristotle, and have been used throughout the history of Artificial Intelligence.
The company Neo4j, known for its graph database systems, is also using ontologies in its agentic products.
In a keynote session at AIEWF [ https://substack.com/redirect/cdf6c93e-e173-4d89-babf-1c7c1adebfae?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], Neo4j CEO Emil Eifrem talked about three different types of ontologies to enable a “smarter shared substrate” to run agents at scale. The first is a business-facing ontology, describing the key concepts in an organization; next is a technical ontology, which Eifrem described as “all the metadata of all the data sources and data assets in your enterprise ecosystem”; and finally execution traces, which are “the runtime signals out of your agent.”
What’s Old is New Again: the Semantic Web
Frank Coyle thinks web ontologies are especially useful in building agentic systems. He mentioned Schema.org, FOAF, Dublin Core and other ontologies familiar to web developers — or at least, those of a certain vintage. He also mentioned “augmenting technologies” like RDFS (Resource Description Framework Schema) and OWL (Web Ontology Language).
One benefit of using these established ontologies is that they’re already in the training data of LLMs, so developers can just prompt for them — much better than reinventing ontologies from first principles.
“This stuff has been out there underlying a lot of what we already do,” Coyle said. “So take advantage of these things that already exist.”
As an example, he showed a Claude agent loop which used an ontology to help validate the LLM’s reasoning after the tool had run.
Coyle calls the convergence of probabilistic agents with ontologies “neurosymbolic AI.”
“Sounds pretty fancy,” he said, “but it’s really neural networks tied into symbolic AI — rule-based systems come under that category, as do the knowledge graphs that we’re assembling.”
He reiterated that neurosymbolic AI represents “a way to keep the LLM on its guardrails.”
The Pros and Cons of Ontologies
Someone who has been steeped in ontologies for many years and is now combining that with AI engineering is Kingsley Idehen, who runs a company called OpenLink Software [ https://substack.com/redirect/46ac0076-f459-4ff8-a7c8-ce88252cad84?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]. He’s been building an “agent engineering stack” that uses Semantic Web technologies — including [ https://substack.com/redirect/f8aa9956-02a0-4d50-ade1-1450e4a4b5fa?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] an “agent with RDF memory.” 
I asked Idehen to explain to me the benefits of ontologies.
“The beauty of LLMs is that they are powerful processors of language,” he replied. “The beauty of an ontology is that it defines the types of entities and relationships through which language acquires computable context. Together, they bring the expressive power of language to computing’s UI/UX stack.”
That makes a lot of sense, but if you’ve been a web developer for a while you’ll know the challenges of ontologies: maintenance and keeping them up-to-date. It’s why the 1990s and 2000s vision for a “Semantic Web” — which was based on ontologies — never took off.
Current AI developer Prasenjit Sarkar offered a potential solution for the maintenance problem on X, arguing that [ https://substack.com/redirect/81b2f05d-17d4-4e59-9b99-b0c19207ddf0?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] “when an agent maintains the ontology as part of its own operation, updating definitions when it encounters edge cases, the maintenance problem changes character.” It’s still a hard problem though, he added.
Despite these issues, the structured nature of ontologies does appear to be a good match with the occasionally wayward tendencies of probabilistic LLMs. You get the power of LLMs, but ontologies will keep them in check.
Plus, as Neo4j’s Eifrem explained, ontologies allow us to move from “a world of thick agents with manually wired data sources” to a new world of “thin agents on a smarter shared ontology-based semantic layer.”
Loops and Guardrails
Back to Coyle’s presentation. He also had a great point about loop engineering, which he noted “has been around forever” in computer science. The problem, of course, is that loops can break or otherwise “go off the rails.”
Again, this is where an ontology system can act as a guardrail to a probabilistic LLM. One of Coyle’s slides referred to it as “a bounded set of rules around an unbounded loop.”
Near the end of his presentation, Coyle demonstrated how to use OWL as a check on agents. One slide showed that while language can be slippery, “an OWL axiom is a rule a machine enforces.”
He also showed how “you can have a reasoner built on ontology, to check [and] keep the LLM on track — have guardrails to keep it honest.”
Semantic Vibes
Perhaps ontologies are starting to resonate with AI engineers because a central concern at this time is quality control for loop engineering. We saw this debate play out at AIEWF [ https://substack.com/redirect/219871bc-e381-48a1-b772-146fd4f06870?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], with many conference speakers not willing to go all-in on fully automated “software factories [ https://substack.com/redirect/233012c8-fee3-43c1-9c70-912225194434?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]” just yet. One of the key learnings from the event [ https://substack.com/redirect/66ac9d53-f445-4a28-9321-a1666e2dcf5b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] was that there need to be guardrails and humans in the loop.
Also it’s fascinating to see traditional web technologies make a resurgence in the field of AI engineering, especially after the 2025 trend of “vibe coding” made it seem like anyone could create software. Of course, since then the penny has dropped: we need to maintain that software and make sure it doesn’t break! So in 2026, we’re seeing a return to software engineering discipline — including now a revival of web ontologies as a way to keep probabilistic LLMs honest.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3lOamt3TVRreExDSndiM04wWDJsa0lqb3lNRGc0TkRZeE1EQXNJbWxoZENJNk1UYzROVFF4TURNMk9Dd2laWGh3SWpveE9ERTJPVFEyTXpZNExDSnBjM01pT2lKd2RXSXRNVEE0TkRBNE9TSXNJbk4xWWlJNkltUnBjMkZpYkdWZlpXMWhhV3dpZlEuSURBUExiZEEyUlRmcHMyYUtxVDdZeUdmdGptQUd4ZmljV3FzUTk1TzBKbyIsInAiOjIwODg0NjEwMCwicyI6MTA4NDA4OSwiZiI6ZmFsc2UsInUiOjI2OTAxOTEsImlhdCI6MTc4NTQxMDM2OCwiZXhwIjoyMTAwOTg2MzY4LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.40PeT8ULkxFvXSlJfEasXoHfFvnLoq0Wk8DvhTnFqq0?
