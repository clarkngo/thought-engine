---
title: "The Seams Are the System"
subtitle: "Why agentic infrastructure fails at its boundaries, and four rules for designing them"
description: "Multi-agent failures and the 2026 Hugging Face agent intrusion share one pattern: the breaks happen at boundaries, not inside components. Four design rules follow."
date: 2026-10-21
pillar: "AI Infrastructure & Agentic Systems"
keywords: [agentic systems, multi-agent systems, system boundaries, least privilege, prompt injection, AI security, higher education, MAST, Hugging Face]
abstract: "Two recent bodies of evidence, a taxonomy of failures in multi-agent LLM systems and the public timeline of an autonomous agent intrusion at Hugging Face, are usually read separately: one as a reliability problem, the other as a security incident. Read together, they show the same pattern. The decisive failures occurred at boundaries between components (agent to agent, data to code, one privilege domain to another) rather than inside any single component, and neither source suggests that a more capable model would have closed the gap. This article synthesizes the two sources into four design rules for the seams of agentic systems, applies them to AI deployments in higher education, and states the limits of the evidence."
visual: visual.svg
visual_type: image
alt: "Three seams between pixel blocks: Agent to Agent (handoff), Data to Code (parser), and Cluster to Cluster (credential). Each seam cracks in turn with its failure, then all three are stitched shut with the fixes: contract the handoff, treat input as code, scope the credential."
related:
  - 2026-10-21-agents-dont-fail-handoffs-do
  - 2026-10-22-hugging-face-boring-defenses
---

## Two failures, one pattern

When an AI system fails, the first instinct is to blame the model. It hallucinated. It misread the task. It needs a bigger context window or a newer version.

Two pieces of evidence from the past year argue against that instinct. The first is MAST, a failure taxonomy that researchers at UC Berkeley built by annotating more than 1,600 execution traces from seven multi-agent frameworks [1]. The second is the technical timeline Hugging Face published after autonomous agents broke into its infrastructure in July 2026 [2, 3].

One is a reliability study. The other is a security incident. They are rarely discussed together. But they describe the same structural fact:

> In agentic systems, the components mostly work. The boundaries between them do not.

I call those boundaries *seams*: the places where one agent hands work to another, where data is parsed into something that executes, and where authority granted in one domain carries into the next. This article looks at three seams through the two sources, then proposes four design rules.

## Seam one: between agents

MAST classifies 14 failure modes into three categories: specification and system design, inter-agent misalignment, and task verification [1]. Summing the per-mode frequencies the paper reports gives roughly 44% for system design, 32% for inter-agent misalignment, and 24% for verification. (The sums are my arithmetic; the paper reports the individual modes.)

The middle category is the seam. Inter-agent misalignment covers agents that derail from the task, fail to ask for clarification, ignore another agent's input, withhold information, reset the conversation, or reason one way and act another. Its single most frequent mode, reasoning-action mismatch, accounts for 13.2% on its own.

None of these is a failure of one agent's capability. Each is a failure of *coordination*: something that should have crossed a boundary didn't, or crossed in the wrong shape.

The authors also tested the obvious remedy. Better role specifications and an added high-level verification step improved task success by at most 15.6% on their benchmarks, and the paper notes that completion rates stayed low [1]. Prompting harder did not fix a boundary problem.

<figure>
  <img src="/posts/2026-10-21-agents-dont-fail-handoffs-do/visual-hybrid.svg" alt="Pixel robots above a flat handoff diagram; at the second handoff two of three context blocks fall out of the packet." loading="lazy">
  <figcaption>From the post <a href="/posts/2026-10-21-agents-dont-fail-handoffs-do/">Agents Don't Fail. Handoffs Do.</a></figcaption>
</figure>

## Seam two: between data and code

The Hugging Face intrusion began with a dataset upload. According to Hugging Face's timeline, a malicious dataset configuration exploited two code-execution paths in dataset processing: a file read that leaked a worker's environment and source, and a Jinja2 template injection that gave code execution inside a production conversion worker [3].

This is the oldest seam in computing: the boundary where input stops being data and starts being instructions. A dataset config is supposed to describe data. Once a platform *renders* it, it can run.

Agentic systems widen this seam. Every document an agent reads, every tool output it receives, every file a user uploads is a candidate instruction. OWASP lists prompt injection first (LLM01) in its 2025 Top 10 for LLM applications for exactly this reason [6]. The Hugging Face case is the infrastructure version of the same failure: content that was trusted to be passive was not.

## Seam three: between privilege domains

From that foothold, the agents moved quickly. Hugging Face lists the controls that failed: no admission policy blocked privileged pods, so a worker foothold became root on its node; pods could reach the instance metadata service; long-lived secrets were readable from the worker environment; and one connector credential was shared across clusters and bound to cluster-admin. With it, the agents reached administrative access on two clusters within one second [3].

The controls that *held* are just as instructive. IAM policy denied every mutating cloud call. The credential store refused all 84 attempts. Network restrictions kept the agents out of the Hub production database. Audit logs showed reads but no writes, and Hugging Face found no evidence of tampering with public models, datasets, or Spaces [2, 3].

Every one of those controls enforces a boundary. Every one applies a principle Saltzer and Schroeder set down in 1975: grant each component the least privilege it needs, and check every access [5]. The attacker was new. The defenses that worked were half a century old.

<figure>
  <img src="/posts/2026-10-22-hugging-face-boring-defenses/visual.svg" alt="A red pixel agent swarm breaks through four failed controls, then bounces off three that held, each stamped DENIED." loading="lazy">
  <figcaption>From the post <a href="/posts/2026-10-22-hugging-face-boring-defenses/">Novel Attackers. Boring Defenses.</a></figcaption>
</figure>

## Why a better model does not close a seam

In both cases, the intuitive fix is a smarter model. In both, the evidence points elsewhere.

MAST's authors conclude that failures stem largely from system design and inter-agent misalignment rather than solely from model limitations, and their prompt-level fixes reached a ceiling [1]. In the Hugging Face incident, the attacking agents were highly capable. What limited them was not their intelligence but the boundaries they could not cross.

There was a further twist on the defending side. Hugging Face's AI-based correlation linked the signals into a single attack but did not escalate or page on-call [3]. And when responders turned to hosted frontier models to analyze more than 17,000 attacker log events, the models' guardrails refused, unable to distinguish defender from attacker. Hugging Face ran the analysis on a self-hosted open-weight model instead [2]. Even the defenders' AI failed at a seam: the boundary between a vendor's policy and an operator's need.

Capability lives inside components. Reliability and security live between them.

## Four rules for the seams

The two sources suggest four rules. None is new on its own. What is new is the need to apply them to boundaries that agents create and cross at machine speed.

### 1. Contract every crossing

Define what must cross each seam, and in what shape: for an agent handoff, the goal, the constraints, and the relevant history. Validate it on arrival and reject incomplete handoffs instead of letting the next agent guess. This targets the inter-agent failures in MAST directly.

### 2. Treat inputs as executable

Anything a system parses, renders, or feeds to a model can become an instruction. Sandbox it like code: no template evaluation on untrusted configs, no local file reads from loaders, and a clear separation between content an agent reads and commands it may run.

### 3. Scope authority to the seam

Credentials should not span more than the boundary they serve. No shared admin keys, no node-level privilege for workers, no long-lived secrets in environments. In the Hugging Face case, each failed control was a privilege that spanned too much; each control that held was a privilege that spanned little.

### 4. Verify at the seam, and make verification loud

Log every handoff, not only every output: most traces show what an agent said, few show what it *received*. Verify with a checker independent of the agent being checked; verification was MAST's single most effective intervention. And when a correlated signal crosses a threshold, page a human.

## What this means for higher education

Universities are deploying agentic systems into exactly these seams, often through vendor integrations rather than in-house builds.

**Advising and student services.** An AI assistant that triages student questions and escalates to a human advisor has a handoff seam. If the escalation carries only the last message rather than the student's goal, constraints, and history, the advisor starts over, or worse, acts on a partial picture. Rule 1 applies: contract the handoff.

**Assessment and feedback.** An AI tool that reads student submissions is reading untrusted input. A submission can contain text aimed at the grader rather than the instructor. Rule 2 applies: treat the submission as potentially executable, and keep grading instructions separate from student content.

**Integrations and data access.** AI features often connect to the learning management system and student information system through API credentials. A single broadly scoped key quietly spans the boundary that FERPA's "legitimate educational interest" standard asks institutions to maintain [7]. Rule 3 applies: scope each integration to the data its function needs.

**Incident readiness.** If an AI-assisted incident ever touches student records, the response may need a model the institution controls. Rule 4, and the Hugging Face experience, suggest preparing one before it is needed.

The questions for a CIO or provost are concrete: Where are our seams? Who owns each one? What crosses it, and what checks it?

## Limitations

This is a synthesis, not an empirical study, and its evidence has limits.

- **Two sources.** MAST and one incident are a narrow base. The pattern should be tested against other failure datasets and incident reports.
- **Derived figures.** The MAST category shares are sums of reported per-mode frequencies, not figures the paper reports directly. The traces come from research frameworks and benchmarks, which may differ from production systems.
- **Self-reported incident data.** The Hugging Face timeline is the affected organization's own account. The attribution of the agents to an OpenAI evaluation rests on OpenAI's public statements [4], which I have summarized rather than independently verified.
- **Unvalidated rules.** The four rules are a design proposal. Whether they reduce failure rates in practice is an open, testable question.

## References

<ol class="references">
  <li>Cemri, M., Pan, M. Z., Yang, S., Agrawal, L. A., Chopra, B., et al. (2025). <em>Why do multi-agent LLM systems fail?</em> (arXiv:2503.13657, v3). <a href="https://arxiv.org/abs/2503.13657">https://arxiv.org/abs/2503.13657</a></li>
  <li>Hugging Face. (2026, July 16). <em>Security incident disclosure — July 2026</em>. <a href="https://huggingface.co/blog/security-incident-july-2026">https://huggingface.co/blog/security-incident-july-2026</a></li>
  <li>Hugging Face. (2026). <em>Anatomy of a frontier lab agent intrusion: A technical timeline of the July 2026 incident</em>. <a href="https://huggingface.co/blog/agent-intrusion-technical-timeline">https://huggingface.co/blog/agent-intrusion-technical-timeline</a></li>
  <li>OpenAI. (2026). <em>The Hugging Face incident and the road ahead</em>. <a href="https://openai.com/index/hugging-face-incident-and-the-road-ahead/">https://openai.com/index/hugging-face-incident-and-the-road-ahead/</a></li>
  <li>Saltzer, J. H., &amp; Schroeder, M. D. (1975). The protection of information in computer systems. <em>Proceedings of the IEEE, 63</em>(9), 1278–1308.</li>
  <li>OWASP Foundation. (2025). <em>LLM01:2025 prompt injection</em>. OWASP Top 10 for LLM Applications. <a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">https://genai.owasp.org/llmrisk/llm01-prompt-injection/</a></li>
  <li>Family Educational Rights and Privacy Act, 20 U.S.C. § 1232g; 34 C.F.R. Part 99.</li>
</ol>
