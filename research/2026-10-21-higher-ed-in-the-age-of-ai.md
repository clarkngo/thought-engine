# Research notes: Higher education in the age of AI (2026-10-21)

Verified against primary sources unless marked. Use these exact figures in drafts.

## Digital Education Council, AI in Higher Education Global Survey 2026 (primary PDF, read directly)
- 45,398 responses: 27,284 students, 18,114 faculty, 35 countries.
- 61% of students say AI frees them to focus on thinking through ideas; 31% attempt more challenging work.
- 22% find it harder to work without AI; 20% depend on AI to produce better work; 19% say they are retaining less.
- 66% of students worry AI could make learning too shallow; >73% of faculty worry students use AI at the expense of developing their own skills.
- Only 15% of students say AI is integrated into many courses; 43% a few; 43% none.
- Where integrated: only 5% say it transformed how they learn; 28% say it enhances understanding; 42% only somewhat helpful; 24% no clear value. US & Canada: 42% say integration added no clear value.
- **Only 29% of students believe instructors are well equipped to guide them on AI use (17% in US & Canada), while 64% of faculty say they have participated in AI literacy training.**
- 60% worry classmates misuse AI for unfair advantage (73% US & Canada).
- Only 28% say most/many assessments reflect the work, skills, and judgement they expect to need in an AI-enabled workplace; 37% say none or only a few do.
- US & Canada faculty intent to use AI in teaching fell from 76% (2025) to 67% (2026), the lowest of any region.
- US & Canada: 26% of faculty excited about AI (APAC 57%); 55% see AI as a serious risk to intellectual development (APAC 29%); 43% of US & Canada students would support an institution-wide ban.
- 41% of students worry AI will reduce job opportunities in their field.
- 37% have serious doubts their programme is relevant for AI and the future; only 30% say it feels current (19% in US & Canada). Faculty: 43% globally not worried their teaching will be outdated; 58% in US & Canada (34% not worried at all).
- Cites DEC 2025 AI in the Workplace Report: 80% of employers say higher ed is not keeping up (secondary, via DEC).
- Source: https://www.digitaleducationcouncil.com (report PDF mirrored at actualidad.udla.cl). Note: DEC's March 2026 post with "92%" is the separate Latin America survey; don't mix.

## Bastani et al. (2025), PNAS 122(26), doi:10.1073/pnas.2422633122
- Randomized field experiment, ~1,000 high school math students (Turkey). Arms: control, GPT Base (ChatGPT-style), GPT Tutor (guardrailed: hints, teacher input).
- Practice: GPT Base +48%, GPT Tutor +127% vs control.
- Exam without AI: GPT Base 17% lower than control; GPT Tutor deficit essentially eliminated, but no gain over control.
- Caveat: high school, one country, one subject.

## Lumina Foundation–Gallup, State of Higher Education 2026 (published Apr 1, 2026; fieldwork Oct 2–31, 2025)
- 57% of U.S. college students use AI in coursework at least weekly; about 1 in 5 daily.
- 42% say their school discourages AI; 11% prohibit it; 35% encourage with limits; 7% encourage freely.
- n = 3,801 enrolled students.
- https://news.gallup.com/poll/704090/routine-college-students-despite-campus-limits.aspx

## Elon University / AAC&U faculty survey (Jan 21, 2026)
- 1,057 faculty; non-scientific sample (fieldwork Oct 29–Nov 26, 2025).
- 95% say GenAI will increase student overreliance (75% "large"); 90% say it will diminish critical thinking (66% "large"); 83% decrease attention spans.
- https://www.elon.edu/u/news/2026/01/21/elon-aacu-national-survey-95-of-college-faculty-fear-student-overreliance-on-ai/

## Weaker / secondary (verify before use)
- Tyton Partners, Time for Class 2026 (June 15, 2026): 47% of faculty redesigned assessments (press release, not read directly); "35% use AI as primary help source vs 4% in 2023" unverified.
- Manikonda et al. (2026), arXiv:2609.18676, under review: 118 students, 12 AI-related courses; evaluation literacy moderates reliance effects. Small, single institution.
- EDUCAUSE 2026 "The Impact of AI on Learning Assessment" (438 respondents, March 2026): page blocked; findings not read.
- Bouvier et al. (2026, ACM), "The Rest of the Robots": research gap on GenAI in upper-level computing courses.

---

# Round 2 (2026-10-21): design, guardrails, and teaching AI courses

## Kestin et al. (2025), "AI tutoring outperforms in-class active learning," Scientific Reports 15:17458 (primary, PMC12179260)
- Randomized crossover trial, Harvard intro physics for life sciences (PS2, Fall 2023); 194 eligible students; each student had both conditions (AI tutor at home vs in-class active learning).
- Median post-test 4.5 (AI) vs 3.5 (in-class), pre-test 2.75: AI median gain "over double." Mann-Whitney z = -5.6, p < 10^-8. Effect size 0.63 (regression; likely underestimate due to ceiling), 0.73–1.3 SD (quantile regression).
- Median time 49 min (AI) vs 60 min in class; time didn't correlate with scores.
- Engagement 4.1 vs 3.6; motivation 3.4 vs 3.1 (5-point). 83% rated AI explanations at least as good as human instructors'.
- Design: system prompt encoding active engagement, cognitive load, growth mindset; platform stepped students through each part of each problem; step-by-step answers pre-written into prompts for accuracy.
- Not clearly stated that the tutor withheld answers. Authors: do not presume structured AI tutoring always outperforms active learning, especially for complex synthesis.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/

## Kapoor, Diaz, MacNeil, Porter, Denny (2025), arXiv:2504.11146, "Exploring Student Behaviors and Motivations using AI TAs with Optional Guardrails"
- Large intro programming course, 885 students; a "See Solution" button turned guardrails off.
- 50% used it for at least one problem; 14% for all three.
- Low-performing students more likely to use it, started later, used it close to the deadline. Motivations: problem help, time pressure, lack of self-regulation, curiosity.
- https://arxiv.org/abs/2504.11146

## Azimi (2026), arXiv:2609.16784, "AI literacy over tool design" (pilot, n = 33 master's students, 7 weeks)
- Scaffolded AI "Study Coach" (hints, no code, hint budget, reflection) vs unrestricted AI: no difference in assignment performance.
- Students who set their own rules for AI use did better in both conditions; most model-literate students scored highest.
- Quote: "The design of the tool mattered less than the students' capacity to govern their own use of it." Small, single institution, associational.

## Anthropic Education Report (Apr 8, 2025), primary
- 574,740 academic conversations from ~1M student conversations on Claude.ai (18 days).
- ~47% "Direct" (resolve the query quickly) vs collaborative.
- Bloom's level of Claude's responses: Creating 39.8%, Analyzing 30.2%, Applying 10.9%, Understanding 10.0%, Remembering 1.8%.
- Computer science: 36.8% of conversations (38.6% in body text) vs 5.4% of U.S. bachelor's degrees.
- https://www.anthropic.com/research/anthropic-education-report-how-university-students-use-claude

## Lee et al. (CHI 2025), Microsoft Research / CMU (survey, self-report)
- 319 knowledge workers, 936 examples. Higher confidence in AI → less critical thinking; higher self-confidence → more. Critical thinking shifts toward verification, integration, and task stewardship.
- https://www.microsoft.com/en-us/research/?p=1135061

## Teaching CS / AI courses
- Lee, Soh, Denny, Burnett, et al. (2026), arXiv:2606.07545, NUS–Google workshop report (23 authors): implementation-level skills losing centrality; shift toward "understanding and verifying AI-generated artifacts"; emphasize system design, abstraction, critical evaluation; five reform prerequisites incl. "re-centering fundamental education" and "embracing new pedagogies."
- Fowles, Falor, Bhattarai, Edwards, Poulsen (2026), arXiv:2605.21374: CS1 allowed AI with weekly oral code-review interviews + flipped classroom; pasted-character share rose (more AI use) but exam averages showed no statistically significant change vs prior semesters; students positive about code reviews.
- Secondary-school "learning penalty" (CEPR VoxEU column, China grades 7–12): homework time down, homework scores up, exam scores down. Page blocked (403); not verified.
- EDUCAUSE 2026 assessment report (438 respondents, Mar 2–14, 2026): summary only, most respondents use AI to create/administer assessments and believe students use AI during them; students need clearer policies. No percentages verified.
