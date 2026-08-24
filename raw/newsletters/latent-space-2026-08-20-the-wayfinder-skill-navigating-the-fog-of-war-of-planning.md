---
source: gmail
newsletter: "latent-space"
message_id: "1a020f9fcacddeb5"
thread_id: "1a020f9fcacddeb5"
subject: "The /wayfinder Skill: Navigating the “Fog of War” of Planning"
from: "\"Latent.Space\" <swyx@substack.com>"
date: "Thu, 20 Aug 2026 20:59:09 +0000"
ingested: 2026-08-24
sha256: 5b970a6d41036f839ea92f4d8d987367af8f2264ed468160871df49d2d8699d0
---
View this post on the web at https://www.latent.space/p/wayfinder-skill

We’re currently developing a new series about skills, with the aim of giving you a regular supply of new skills to use in your projects. We’re kicking things off with an interview — and a super-useful skill — featuring Matt Pocock, whose “AI Skills for Real Engineers [ https://substack.com/redirect/24bbdd4e-732b-4578-905f-b7bf9235a3ad?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]” project has over 220,000 stars on GitHub [ https://substack.com/redirect/e4e3f87b-edc3-425b-a812-420079656ffb?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]. He also talks about these skills to 347,000 subscribers on his YouTube channel [ https://substack.com/redirect/c3856b39-937c-40c6-80b3-9d7981ac3aeb?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ].
Pocock recently released a new skill called /wayfinder [ https://substack.com/redirect/e37c69a2-1f4a-4aec-b06a-2144fc77144e?j=eyJ1IjoiMWxucmoifQ.TOO4JddZ2aOkng20GMCR3ePCcghfMgNuGHoEYV3w1tc ]. Its purpose is to help you and your agent figure out a project where the end state isn’t entirely clear. Or as Pocock put it in our interview, /wayfinder helps you navigate “the fog of war,” where you have a project but “you can’t quite decide everything right at the start.”
The following interview has been slightly condensed for readability, so you can read it, absorb Matt’s insights, and then test out /wayfinder for yourself!
Latent Space: What were the goals of wayfinder?
Pocock: What I noticed is I was doing a lot of work with AFK agents [Away From Keyboard] and trying to schedule in a ton of work so that my agents could run virtually overnight. I would just plan a bunch of stuff, and then I would create a spec and then turn that spec into tickets. And I had a really well-developed set of skills for how to turn work into scheduled stuff that agents could just crack on.
But [...] I was finding the planning stage really onerous, because I would have to be constantly thinking about my session management. Like, how many tokens am I into my context window? How deep am I going here?
I didn’t want to feel constrained in the planning stage anymore. I wanted an orchestrator layer that would basically say, okay, whatever you want to plan, I’m going to handle the planning sessions for you. I’m going to split this out into multiple different threads, do prototyping, do research and pull it all back together, so that you don’t feel constrained in the planning anymore.
And then your specs can be even more detailed, and you can just whack off an AFK agent to go and do tons more work.
Latent Space: What was the design process of coming up with this skill?
Pocock: I had this kernel of an idea of, what if I didn’t have to manage the handoffs? What would that look like? And then, what would it look like to have some kind of centralized document to have all of those pieces together?
Whenever you’re thinking about context management — because that’s really what a skill is, you’re managing the context of the agent you’re working in — you need to think about the information flow. So what I wanted to think about is, what if a grilling session could manage other grilling sessions? What would that look like?
Well, the first step to that is, what does the grilling session that’s being managed need? What does the child need in that situation? So the child probably needs to understand a vague overview of what else is happening, and they need their specific task.
So there, you’ve got two documents. You’ve got a map — which is all of the rest of the stuff, all the decisions that have already been made. And then you’ve got the specific ticket that goes into the actual session. And what you notice there is that those words are very precise.
You’ve got the map, and you’ve got the ticket, and you’ve got the session. And once you’ve got the kernel of an idea, you then need to come up with the words for that idea. Because once you’ve figured out the words, then those entities can be really clearly mapped out by the agent.
Because if you just call everything a ticket, or if you just refer to it in different ways in different places, then it’s going to be really confused and you’re going to get strange behavior. Whereas if you use these very specific, what I call leading words, to lead the agent to understand exactly what each part is, and you’ve understood what the information flow is, then you’ve got your skill.
Latent Space: What kind of use cases do you think wayfinder would be useful for?
Pocock: Well, I’ve been using it for all sorts of stuff. I’ve been using it to actually plan courses as well. In wayfinder, there are different types of tickets.
So you’ve got grilling tickets, which are just a grilling session. Then you’ve got prototype tickets for creating prototypes, research tickets for creating [and doing] research, and then task tickets — which are really broad…basically, just anything the human needs to do that the agent can’t do. And so once you think about that, you realize, OK, I can apply that to anything.
One really key idea in wayfinder is the ‘fog of war’. So this is the concept of, you can’t quite decide everything right at the start.
You can make certain decisions, and those certain decisions sort of lead you there and push further out into the fog of war — kind of like Warcraft III style, exploring the map. And once I had the idea of ‘fog of war’ and ‘map’, I realized those two terms actually work really nicely together, and it really leads the agent into the right idea. So I’ve been using it for engineering, for non-engineering stuff, for course planning, all sorts.
Latent Space: This concept of the fog of war — it’s weird to consider what you don’t know that you don’t know. Maybe LLMs are good at capturing that.
Pocock: I feel like with the grilling stuff that I’m still working on, that captures an idea that you don’t know stuff, but maybe the agent can contribute something and illuminate a part of the room that you don’t quite understand yet.
And wayfinder is just sort of an extra layer on top of that.
Latent Space: Yeah, and there’s all these artifacts. How much time do you spend teaching the model all this terminology?
Pocock: For the last few months, I’ve been pretty obsessed with terminology — and finding the right terms for certain things. I’ve put together, I haven’t actually put it out yet, but it’s an AI coding dictionary — of basically all the terms in AI coding. It’s in this beautiful graph that you can explore and understand exactly what an agent is, exactly what a harness is, exactly what a model is, blah blah blah.
I’ve redone all my courses to use that dictionary and make it really solid. And then all of my skills use a consistent dictionary as well. So they’re all working off the [same] assumptions, the same leading words.
I realized that I needed a ubiquitous language between me and the agent. Between me and the agent, there is a communication barrier. And that’s what I’m trying to do with my skills all the time, is try to find the right words.
And agents are really good at showing you the opportunities for different wording — really good at domain modeling, actually.
Latent Space: When do we directly use the grill-me skill, versus wayfinder?
Pocock: Use ‘grill me’ in cases where you feel like you can plan the whole thing in a single session, and you need to align before you go. So most small features will fit into this. Most stuff where you can see the path ahead of you, but you just want to make sure the agent is on board, ‘grill me’ will work with that.
For stuff where you don’t know the path ahead, for stuff where you can feel the fog of war in front of you, use wayfinder. You’re gonna find your way with wayfinder. So that’s how it works.

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3lOamt3TVRreExDSndiM04wWDJsa0lqb3lNVEUyT1RVNE1qVXNJbWxoZENJNk1UYzROekkxT1RZME55d2laWGh3SWpveE9ERTROemsxTmpRM0xDSnBjM01pT2lKd2RXSXRNVEE0TkRBNE9TSXNJbk4xWWlJNkltUnBjMkZpYkdWZlpXMWhhV3dpZlEuRUpfdDE4NUxkTWhzcjdWMzJFbmJXcGE1ZXRneTdVbFo3eV9fNHlLdzV0SSIsInAiOjIxMTY5NTgyNSwicyI6MTA4NDA4OSwiZiI6ZmFsc2UsInUiOjI2OTAxOTEsImlhdCI6MTc4NzI1OTY0NywiZXhwIjoyMTAyODM1NjQ3LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.sq-z8NzYJORjroQ21GsL7Nvhtutp1_A8NKc4xjidGxU?
