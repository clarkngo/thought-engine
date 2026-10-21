---
title: "Agents Don't Fail. Handoffs Do."
description: "UC Berkeley's MAST study traced about a third of multi-agent failures to the seams between agents, not to the models inside them."
date: 2026-10-21
pillar: "AI Infrastructure & Agentic Systems"
keywords: [multi-agent systems, agent handoffs, MAST, verification, orchestration, LLM failures]
visual: visual.svg
visual_type: image
alt: "Pixel robots labeled Intake, Planner, and Executor pass a context crate holding goal, constraints, and history. At the second handoff two blocks fall out, and the Executor acts on 1 of 3."
source:
  name: "Cemri et al., Why Do Multi-Agent LLM Systems Fail? (UC Berkeley, arXiv 2503.13657)"
  url: "https://arxiv.org/abs/2503.13657"
---

Agents don't fail. Handoffs do.

UC Berkeley researchers annotated more than 1,600 execution traces across seven multi-agent frameworks to build [MAST](https://arxiv.org/abs/2503.13657), a taxonomy of how these systems break.

Roughly a third of the failures sat *between* agents: inter-agent misalignment. Agents derailing from the task. Failing to ask for clarification. Ignoring another agent's input. Saying one thing and doing another.

Another quarter were verification failures: nobody checked, or the checker checked the wrong thing. The largest bucket, about 44%, was system design: vague specs, repeated steps, agents that never learn when to stop.

Notice what's missing from the top of that list: the model not being smart enough.

That's the uncomfortable part. Most teams respond to a flaky pipeline by swapping in a bigger model or rewriting prompts. The researchers tried the prompt-and-workflow route. The best intervention, adding a high-level verification step, improved task success by at most 15.6%. Completion rates stayed low.

You cannot prompt your way out of an architecture problem.

**Design the seams, not just the steps:**

- **Write a handoff contract.** Define what must cross each seam (goal, constraints, history) and in what shape. Reject handoffs that arrive incomplete.
- **Log every handoff, not only every output.** Most traces show what each agent said. Few show what each agent *received*.
- **Verify at the seam, with a separate checker.** Verification was the single biggest lever in the study. Make it independent of the agent being checked.

Where do your agent pipelines actually break: inside the steps, or between them?
