---
draft: true
title: "Performance Is Not Learning"
subtitle: "Designing courses for the age of AI, and four principles from the evidence"
description: "AI raises scores during practice and can lower them once it is removed. Randomized trials and course studies point to design, not the model, as what decides the direction. Four principles follow."
date: 2026-11-13
pillar: "Higher Education & Pedagogy"
keywords: [learning versus performance, generative AI, AI tutoring, assessment, guardrails, verification, critical thinking, course design, higher education]
abstract: "Generative AI has made one of the oldest distinctions in learning science newly urgent: performance during practice is not the same as learning that lasts. In a randomized field experiment, students practicing with a ChatGPT-style assistant scored 48% higher during practice and 17% lower once the assistant was removed. In a randomized trial at Harvard, a structured AI tutor more than doubled median learning gains over an in-class active-learning lesson. The technology was comparable; the design was not. This article reads those trials alongside course-level studies of optional guardrails, oral code reviews, and the link between confidence and critical thinking. It proposes four design principles for courses where AI is present, considers what they mean for higher education institutions, and states the limits of the evidence."
visual: visual.svg
visual_type: image
alt: "Two lines over a semester. The performance line, with AI help, climbs steadily. The learning line, measured without AI, stays flat. A pixel student rides the performance line until the AI is removed at the exam, then drops to the learning line. Below: performance is what the student can do with help; learning is what remains without it."
related:
  - 2026-10-26-better-at-practice-worse-at-the-exam
  - 2026-10-28-same-ai-opposite-results
  - 2026-10-30-five-moves-for-teaching-with-ai
  - 2026-11-03-guardrails-have-an-off-switch
  - 2026-11-04-teach-verification-not-syntax
  - 2026-11-10-confidence-is-the-variable
---

## The score went up. The skill did not.

In a randomized field experiment with nearly 1,000 high school mathematics students, those who practiced with a ChatGPT-style assistant scored 48% higher than a no-AI control group during practice sessions. When the assistant was removed for the exam, the same students scored 17% *lower* than the control group [1].

That result is easy to read as a story about one tool, one subject, or one age group. It is better read as a measurement problem. During practice, the scores recorded what students could do *with* the assistant. The exam recorded what they could do *without* it. The two numbers moved in opposite directions.

Most higher education courses now sit in the first condition. In a 2026 Lumina Foundation–Gallup survey of 3,801 U.S. college students, 57% reported using AI in their coursework at least weekly [2]. If assignments are completed with AI and graded on their output, a course can record rising performance while learning stays flat or declines, and nothing in the gradebook will show it.

This article argues that the problem is not AI's presence in courses but a confusion between two measurements, and that course design, not the choice of model, decides which way AI pushes learning.

## Performance and learning are different measurements

The distinction is not new. Learning researchers have long separated *performance*, what a learner can do during or immediately after instruction, from *learning*, the relatively durable change that supports later retention and transfer. Soderstrom and Bjork's integrative review documents both directions of the gap: conditions that raise performance during practice can fail to produce learning, and conditions that slow practice down, sometimes called desirable difficulties, can produce more of it [3].

Generative AI widens this gap in a specific way. It does not only make practice easier; it can do the practice. When the tool produces the step, the student's score reflects the tool's competence. The 48% practice gain in the PNAS trial is, in that sense, a measurement of the assistant [1].

Students notice the difference. In the Digital Education Council's 2026 global survey of more than 27,000 university students, 19% said they retain less because of AI and 22% said they find it harder to work without it [4].

The design implication is direct: a course that wants evidence of learning has to measure, at least some of the time, without the tool.

## Same technology, opposite outcomes

If AI harmed learning in general, the story would end there. It does not.

In a randomized crossover trial with 194 students in introductory physics at Harvard, Kestin and colleagues compared an AI tutor used at home with an in-class active-learning lesson on the same material [5]. The median post-test score was 4.5 with the AI tutor and 3.5 in class, from a pre-test median of 2.75, which the authors describe as a median learning gain more than double that of the class. Students reached it in less time: a median of 49 minutes against a 60-minute class.

The two trials used comparable technology. What differed was the design around it.

- **In the PNAS trial,** the ChatGPT-style arm answered what students asked [1]. A second arm, a "tutor" configured to give hints rather than answers and built with teacher input, raised practice scores by 127% and essentially eliminated the exam deficit, but did not produce a gain over the no-AI group.
- **In the Harvard trial,** instructors wrote the system prompt to encode active engagement and manage cognitive load, the platform stepped students through each part of each problem in sequence, and expert-written step-by-step solutions were embedded so the tutor stayed accurate [5].

The useful question is therefore not "does AI help students learn?" but "what does the AI make the student do?" When it does the step, performance rises and learning may not. When it sequences the student through the step, the evidence suggests learning can rise too.

Two cautions apply. The trials differ in age, subject, setting, and outcome measure, so their effect sizes cannot be compared head to head. And Kestin and colleagues explicitly do not claim that structured AI tutoring will always outperform active learning, particularly for complex synthesis [5].

## Guardrails are behavior, not configuration

The guardrailed tutor in the PNAS trial suggests that configuration matters. A course-level study suggests that configuration is not enough.

Kapoor and colleagues deployed an AI teaching assistant in an introductory programming course of 885 students, with an optional "See Solution" button that turned the guardrails off [6]. Half the students used it on at least one problem, and 14% used it on all three. Lower-performing students were more likely to use it, started later, and used it close to the deadline. The motivations students reported included time pressure and difficulty regulating their own use.

Guardrails, in other words, are tested under deadline pressure, and they fail for the students with the most to lose. A small pilot points in the same direction: in a seven-week study with 33 master's students, a scaffolded study coach and an unrestricted assistant produced no difference in assignment performance, while students who set their own rules for AI use did better in both conditions [7]. The sample is too small to generalize from, but the pattern is consistent: what students do with the tool depends on more than how the tool is configured.

For course design, this shifts part of the work from the tool to the course: deadlines, checkpoints, and the habits students are taught for deciding when to use AI.

## Assessment has to move from the artifact to the explanation

If AI can produce a correct artifact, grading the artifact grades the AI. One response is to ban the tool. Another is to change what is assessed.

Fowles and colleagues describe an introductory computer science course that allowed generative AI and added weekly oral code review interviews, with a flipped classroom to make time for them [8]. Students explained the code they submitted, whoever or whatever wrote it. Keystroke logs showed significantly more pasted code than in earlier semesters, a sign of more AI use. Exam averages showed no statistically significant change, and students were broadly positive about the reviews.

This is one course, reported in a preprint, and it compares averages across semesters rather than running a controlled trial. But it illustrates a design move that does not depend on detecting AI use: assess the student's explanation and reasoning, not only the work product.

A 2026 report drawing on two workshops with 23 computing educators and practitioners argues that the field is moving the same way, with implementation-level skills such as coding and debugging losing their central place and the evaluation of AI-generated work gaining it [9].

## Confidence and critical thinking

Verification is a skill, but it is also a disposition. In a survey of 319 knowledge workers describing 936 real uses of generative AI at work, Lee and colleagues found that higher confidence in the AI was associated with less critical thinking, while higher self-confidence was associated with more [10].

The data are self-reported and correlational. Still, they carry a warning for AI literacy programs: training that mainly builds trust in the tool may work against the habit of checking it. The goal is learners who trust their own judgment enough to question the output.

## Four principles for designing for learning

The evidence above is uneven in strength, and it comes from different populations and disciplines. Read together, it supports four design principles. They are proposals, not validated interventions.

**1. Make the student do the step.** Configure or choose AI tools that hint and sequence rather than answer, and write the prompts and reference solutions yourself where possible [1, 5]. The test is simple: in each AI-assisted task, who performed the cognitive step the task exists to practice?

**2. Measure without the tool at least once.** Include at least one assessment per course in which students work without AI. Without it, the course has no measurement of learning, only of performance with help [1, 3].

**3. Assess the explanation, not only the artifact.** Short oral reviews, annotated reasoning, or required extensions of AI-assisted work give evidence of understanding that survives regardless of who typed the first draft [8, 9].

**4. Build judgment, not trust.** Teach verification as an explicit skill, and design for the deadline, when guardrails are most likely to be switched off [6, 10]. Checkpoints spread across an assignment reduce the late-night conditions under which students bypass their own safeguards.

## What this means for higher education

**For instructors,** the four principles are course-level changes that do not require new technology or institutional approval. The smallest version is a single assignment redesigned so that AI produces a draft and the grade rests on evaluation, explanation, and extension.

**For teaching and learning centers,** the evidence argues for shifting faculty development from tool training to assessment design. Adding AI to a course is not the same as redesigning it. In the Digital Education Council's 2026 survey, only 5% of students whose courses included AI said it had transformed how they learn [4].

**For academic leaders,** the gap is also one of perception. In the same survey, only 19% of U.S. and Canadian students said their program feels current for an AI-enabled world, while 58% of faculty in the region were not worried that their teaching would become outdated, and only 28% of students said most of their assessments reflect the work they expect to do [4]. Program review can ask a direct question: where in this program do students demonstrate learning without AI, and where do they demonstrate judgment with it?

**For procurement and IT,** institutionally licensed AI tools should be evaluated on what they can be configured to do: whether instructors can require hints over answers, sequence work, and supply their own reference material. A default general-purpose assistant corresponds to the arm of the PNAS trial that lowered exam scores [1].

**For institutional research,** the measurement problem scales up. Grade distributions in AI-assisted courses may rise without any change in learning. Tracking performance on assessments taken without AI, over time and across course sections, is one way to tell the two apart.

## Limitations

This article is a synthesis, not an empirical study, and its evidence has limits.

- **Different populations.** The two randomized trials involved high school students in one country [1] and undergraduates at one selective university [5]. Neither is a typical higher education population, and their results cannot be combined into one effect size.
- **Preprints and pilots.** The oral code review study [8], the computing educators' report [9], the guardrails study [6], and the study coach pilot [7] are preprints, and the last involved 33 students. They illustrate design options; they do not establish them.
- **Self-report.** The critical-thinking findings [10] and the student survey data [2, 4] are self-reported and associational.
- **Unvalidated principles.** The four principles are a design proposal drawn from this evidence. Whether they improve learning as a set, in typical courses, is an open and testable question, and a natural target for a course-level study.

## References

<ol class="references">
  <li>Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., &amp; Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. <em>Proceedings of the National Academy of Sciences, 122</em>(26). <a href="https://doi.org/10.1073/pnas.2422633122">https://doi.org/10.1073/pnas.2422633122</a></li>
  <li>Lumina Foundation &amp; Gallup. (2026). <em>State of higher education 2026</em> [Survey findings]. <a href="https://news.gallup.com/poll/704090/routine-college-students-despite-campus-limits.aspx">https://news.gallup.com/poll/704090/routine-college-students-despite-campus-limits.aspx</a></li>
  <li>Soderstrom, N. C., &amp; Bjork, R. A. (2015). Learning versus performance: An integrative review. <em>Perspectives on Psychological Science, 10</em>(2), 176–199. <a href="https://doi.org/10.1177/1745691615569000">https://doi.org/10.1177/1745691615569000</a></li>
  <li>Digital Education Council. (2026). <em>AI in higher education global survey 2026</em>. <a href="https://www.digitaleducationcouncil.com">https://www.digitaleducationcouncil.com</a></li>
  <li>Kestin, G., Miller, K., Klales, A., Milbourne, T., &amp; Ponti, G. (2025). AI tutoring outperforms in-class active learning: An RCT introducing a novel research-based design in an authentic educational setting. <em>Scientific Reports, 15</em>, 17458. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/">https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/</a></li>
  <li>Kapoor, A., Diaz, M., MacNeil, S., Porter, L., &amp; Denny, P. (2025). <em>Exploring student behaviors and motivations using AI TAs with optional guardrails</em> (arXiv:2504.11146). <a href="https://arxiv.org/abs/2504.11146">https://arxiv.org/abs/2504.11146</a></li>
  <li>Azimi. (2026). <em>AI literacy over tool design: A mixed-methods study of scaffolded versus unrestricted generative AI in programming education</em> (arXiv:2609.16784). <a href="https://arxiv.org/abs/2609.16784">https://arxiv.org/abs/2609.16784</a></li>
  <li>Fowles, M., et al. (2026). <em>Allowing generative AI in CS1 with code review interviews and a flipped classroom</em> (arXiv:2605.21374). <a href="https://arxiv.org/abs/2605.21374">https://arxiv.org/abs/2605.21374</a></li>
  <li>Lee, et al. (2026). <em>Reshaping undergraduate computer science education in the generative AI era</em> (arXiv:2606.07545). <a href="https://arxiv.org/abs/2606.07545">https://arxiv.org/abs/2606.07545</a></li>
  <li>Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., &amp; Wilson, N. (2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey of knowledge workers. In <em>Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems</em>. ACM. <a href="https://www.microsoft.com/en-us/research/?p=1135061">https://www.microsoft.com/en-us/research/?p=1135061</a></li>
</ol>
