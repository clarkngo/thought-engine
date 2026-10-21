# LinkedIn copy: Agents Don't Fail. Handoffs Do.

## Post

Agents don't fail. Handoffs do.

UC Berkeley researchers annotated 1,600+ execution traces across 7 multi-agent frameworks to map how these systems break (the MAST study).

Roughly a third of failures happened BETWEEN agents.

Agents derailing from the task. Not asking for clarification. Ignoring each other's input. Saying one thing, doing another.

Another quarter were verification failures. Nobody checked, or the checker checked the wrong thing.

The biggest bucket, about 44%, was system design: vague specs, repeated steps, agents that never know when to stop.

Notice what's missing from the top of the list: the model not being smart enough.

Most teams answer a flaky pipeline with a bigger model or a prompt rewrite. The researchers tried better prompts and workflows. The best fix, an added verification step, lifted task success by at most 15.6%. Completion rates stayed low.

You cannot prompt your way out of an architecture problem.

Design the seams, not just the steps:

• Write a handoff contract. Define what must cross each seam: goal, constraints, history. Reject incomplete handoffs.
• Log every handoff, not only every output. Most traces show what an agent said. Few show what it received.
• Verify at the seam, with a separate checker. Verification was the biggest lever in the study.

Where do your agent pipelines actually break: inside the steps, or between them?

[🔗 Link to research in the first comment]

## First comment

🔗 Link to research: "Why Do Multi-Agent LLM Systems Fail?" (Cemri et al., UC Berkeley) https://arxiv.org/abs/2503.13657

Category shares are the sums of the paper's per-failure-mode percentages (v3).

## Visual

Upload `visual.gif` (or `visual.mp4`) from this folder. Render it with:
npm run render -- content/posts/2026-10-21-agents-dont-fail-handoffs-do/visual.svg
