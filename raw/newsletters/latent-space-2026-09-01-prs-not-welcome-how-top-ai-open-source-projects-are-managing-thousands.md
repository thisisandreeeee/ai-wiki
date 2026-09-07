---
source: gmail
newsletter: "latent-space"
message_id: "1a05dc42a98e6c86"
thread_id: "1a05dc42a98e6c86"
subject: "PRs NOT Welcome: How Top AI Open Source Projects Are Managing Thousands of Contributors"
from: "\"Latent.Space\" <swyx@substack.com>"
date: "Tue, 1 Sep 2026 16:17:15 +0000"
ingested: 2026-09-07
sha256: 850c3ee5db742f8d71023a21a3769bbc47c0bcf2e559fd587ba4fc655c32c47d
---
View this post on the web at https://www.latent.space/p/pr-not-welcome

GitHub invented pull requests, and for 18 years they have been open by default. But now some of the top AI-native open source projects are shutting PRs off, because they’ve found a better way.
These projects, which include Flue and tldraw, refuse to accept PRs from external contributors — in part because they’re usually AI-generated. Instead, the maintainers prefer to use their own agents to create and manage PRs.
Also, many projects have begun using a “software factory [ https://substack.com/redirect/c2f9f262-c7d9-4b0c-94df-c01f1773a3ad?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]” to manage community contributions. Typically this involves a ‘team’ of agents triaging a PR, reproducing the issue (if it’s a bug), implementing a fix or a new feature, reviewing it, and then handing it back to a human to merge it.
Vercel’s software factory for AI SDK
Vercel recently published a post entitled “Building a software factory for AI SDK [ https://substack.com/redirect/c8bb4dff-5b5b-4c8a-b845-ee73e2819c61?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].” It describes how the open source AI SDK project, which gets over 20 million npm downloads per week, deployed agents to get control over its PR and issue backlog — which had reached “over 1,000 open issues and almost 800 pull requests” by late June.
There are several types of agents in Vercel’s system, each of which focuses on a different task. For example, there’s an agent that reproduces a bug, another that applies a fix, and yet another that reviews the fix.
One of the key reasons why Vercel set up this software factory is because it trusts its own agents to do the work, more so than agents run by community members.
“If we have a very specific agent with a very specific prompt that we optimized — and we know that, over history, it was very successful in fixing a certain category of bugs — then we develop trust in that particular agent configuration,” Vercel engineer Lars Grammel [ https://substack.com/redirect/090f6d8c-dac9-404d-a297-52f34c7ed1c4?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] explained in a YouTube video [ https://substack.com/redirect/8ca6c77d-80a9-4506-8e06-a7436e29d885?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
“For open-source projects, it’s worth considering having your own agents and your own setup, and not necessarily trusting the community, because it can actually cut down your time to review,” he added.
Grammel also showed the deployment architecture for its system, noting that “there is a UI, there’s a web app, there’s an underlying API, there’s an execution space, and there are sandboxes.” It’s then synchronized with GitHub, which automatically triggers other actions. The UI Grammel mentioned was custom-made.
Just four weeks after this software factory was implemented, Vercel claims [ https://substack.com/redirect/c8bb4dff-5b5b-4c8a-b845-ee73e2819c61?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] the factory now “authors between 25 and 35% of PRs we merge and closes 70-80% of issues.”
Astro’s auto-triage system
The Astro web framework [ https://substack.com/redirect/39957bb7-5b85-4b17-898c-75cc64ad62fd?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], which has 62,000 stars on GitHub, has also adopted what creator Fred Schott [ https://substack.com/redirect/9a40c3f5-6ba2-4521-88b6-06d9e9ed3f2e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] calls “that software factory idea.”
“For five years, we were in this place where issues came in faster than we could handle them,” Schott told Latent Space.
But now, with agents handling the triage work, they’ve reestablished control.
“It’s totally shifted in the last six months,” he said. “We can now solve these issues with these automations — handling triage, reproduction, getting the user to actually verify the fix that the bot is suggesting before we even look at it.”
The result was not just a large decrease in open issues, but a complete change in how the Astro team deals with incoming community requests.
“I’ve never seen that in my entire decade-plus experience with open source,” Schott said. “Being able to essentially treat issues as a thing that every week, you prioritize — no matter what — versus a backlog that you’re constantly trimming.”
Furthermore, the Astro “auto-triage” system directly led to Schott creating a brand new agent framework, called Flue [ https://substack.com/redirect/20b5c848-cc3f-4a1e-954b-4c2db644b797?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Flue doesn’t accept your PRs, but is open for discussion
With Flue, Schott is trying an even more radical approach to PRs. Flue’s contributor guide [ https://substack.com/redirect/1c801164-c508-4612-bf2f-797ae617016a?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] states that “we’re going to try to reimagine things” — partly to prevent what it calls “Drive-by AI slop PRs.”
Basically, Schott explained, every external pull request in the Flue project is automatically closed and converted into an issue or discussion. Bug reports and fix proposals get turned into issues, feature requests become discussions.
“If you submit a PR, no hard feelings, we’re just going to go and represent it for you as issues and discussions. And from there, trying to figure out the right way to bring people on.”
It’s kind of like treating incoming requests as leads, rather than as a piece of work a maintainer feels obliged to review. The contributor guide explains that it uses the team’s own expertise combined with “the best available SOTA [State-of-the-Art] LLMs that we have access to” in order to help them decide what to work on next.
Once a decision is made in the issue or discussion, agents are then deployed for “research, design, implementation, and initial review.”
If our agents write the code, your external PRs are worthless
Like Flue, the “source available” React drawing tool tldraw [ https://substack.com/redirect/a8f3c373-ff68-411e-a93a-e6cc1529de2d?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] (50,000 stars) automatically closes external PRs.
Project creator Steve Ruiz announced this policy in January [ https://substack.com/redirect/4586957a-56d0-4549-9c06-ec49179e7568?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] and five months later reiterated it [ https://substack.com/redirect/f1e83d01-51b3-4109-9384-cb3156eaa8ae?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], noting that it was “an opinionated decision made in response to changes in how we’re coding (more discussion, more agents), the social practices around public contribution, and the changing landscape around code security.”
HashiCorp co-founder and Ghostty creator Mitchell Hashimoto, now a co-founder of Superlogical [ https://substack.com/redirect/a931c55c-1dd5-410e-adff-947381b88b5b?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], takes it even further. He thinks [ https://substack.com/redirect/04312bad-d0af-4ad5-94c3-7390784ec4d5?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ] “the future is that large open source projects will close contributions completely.”
Ruiz responded [ https://substack.com/redirect/26ba3147-bd9a-4408-a5ea-e7c95c18d2c6?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], “It just makes less sense to have people contributing code if the issue is decently well-specified and the code can be written by agents.”
But…what happens to the community?
Traditionally in open source, pull requests have been reviewed by maintainers not only for the code, but to teach contributors and assess them as future maintainers. If projects like AI SDK and Astro are using their agents to do much of the code review and implementation, where does that leave community members who want to be more actively involved?
Schott recognizes this as a risk.
“It still leaves this open hole of, well, if you just keep narrowing the project, at a certain point, you and I go on vacation — what happens? It doesn’t really solve every problem.”
However, the fact that both Flue and tldraw don’t accept PRs but do accept new issues and discussions perhaps points to a solution. Which is that by talking to each other more, community members better get to know — and trust — one another, which is both a way to learn from peers and potentially prove yourself worthy of being a maintainer.
As for the code, if it’s easier for maintainers to use AI themselves than to accept external code contributions, then as tldraw founder Steve Ruiz put it [ https://substack.com/redirect/5bb2f134-7b4f-43f2-aa70-260c888084f6?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ], “it’s better to limit community contribution to the places it still matters: reporting, discussion, perspective, and care.”

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3lOamt3TVRreExDSndiM04wWDJsa0lqb3lNVE0zTWpZM09UWXNJbWxoZENJNk1UYzRPREkzT1RVek1Td2laWGh3SWpveE9ERTVPREUxTlRNeExDSnBjM01pT2lKd2RXSXRNVEE0TkRBNE9TSXNJbk4xWWlJNkltUnBjMkZpYkdWZlpXMWhhV3dpZlEuMGhGdFNSeWxfTk9PRjgxSVotSFlUVkVIUjY4Z3l4RUxNM1NSbkswUmYtRSIsInAiOjIxMzcyNjc5NiwicyI6MTA4NDA4OSwiZiI6ZmFsc2UsInUiOjI2OTAxOTEsImlhdCI6MTc4ODI3OTUzMSwiZXhwIjoyMTAzODU1NTMxLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.IlKZgKkcDLtveEz7ruVt9irIt33w2H1jIvxTnwjlV84?
