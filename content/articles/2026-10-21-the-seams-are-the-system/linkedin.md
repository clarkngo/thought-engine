# LinkedIn copy: The Seams Are the System

## Post

Last week I wrote about two failures that look unrelated.

One is a reliability problem: UC Berkeley's MAST study of 1,600+ multi-agent traces.

One is a security incident: the agent swarm that broke into Hugging Face in July.

They're the same failure.

In both, the components mostly worked. The boundaries between them didn't.

Agent to agent: roughly a third of MAST failures were agents failing each other. Derailing, ignoring input, not asking.

Data to code: the intrusion started with a dataset config that got rendered, and ran.

Privilege to privilege: one shared credential turned a foothold into admin on two clusters in about a second.

And in neither case would a smarter model have closed the gap.

I call these boundaries seams. I've written a longer, citable piece on why agentic infrastructure fails at its seams, with four design rules:

• Contract every crossing.
• Treat inputs as executable.
• Scope authority to the seam.
• Verify at the seam, and make verification loud.

It also maps the seams onto higher ed: advising handoffs, AI that reads student submissions, and the API keys between our LMS and SIS.

Where is the most dangerous seam in your organization's AI stack right now?

[🔗 Full article in the first comment]

#AIAgents #MultiAgentSystems #AIEngineering #HigherEd

## First comment

🔗 Full article: The Seams Are the System (with references and a "cite this" block): https://clarkngo.github.io/thought-engine/articles/2026-10-21-the-seams-are-the-system/

Sources: Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (arXiv:2503.13657) and Hugging Face's technical timeline of the July 2026 intrusion.

## Visual

Upload `visual.gif` (or `visual.mp4`) from this folder. Re-render with:
npm run render -- content/articles/2026-10-21-the-seams-are-the-system/visual.svg
