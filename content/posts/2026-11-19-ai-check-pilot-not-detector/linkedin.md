# LinkedIn copy: An AI Check Pilot, Not an AI Detector

## Post

I won't run AI detectors on my students' work.

I'm going to use AI to decide whose work I ask them to explain.

Here's my plan for a course I teach next term.

Students submit code every two weeks. Most of the grade isn't for getting it to run. It's for evaluating, analyzing, and explaining what they built.

Reviewing every submission deeply, every time, isn't realistic. Without help, most students would get a score and a sentence.

That's yesterday's problem: expert attention is the scarce resource.

The plan:

• AI does the first pass on every submission. It flags what needs a person: an explanation that doesn't match the code, a claim with no test behind it, a thin evaluation.
• I read the flags, not everything. That's where I add what the AI can't: why this would break at work, and what a senior engineer would do instead.
• A flag starts a conversation, not a penalty. "Walk me through this line." If it's your work, that takes a minute or two.

Why not a detector?

Detectors are unreliable. And a verdict teaches nothing.

A two-minute conversation is a check and a lesson at the same time.

It's the design from yesterday's JAMA Surgery trial: the AI collects the error data, a person turns it into coaching.

This hasn't met students yet.

Would you rather be checked by a detector, or asked to explain your work for two minutes?

[🔗 Link to research in the first comment]

#HigherEd #AIinEducation #Assessment #AcademicIntegrity #TeachingWithAI

## First comment

🔗 The study behind the design: Giglio et al., "Artificial Intelligence–Augmented Human Instruction and Surgical Simulation Performance: A Randomized Clinical Trial," JAMA Surgery 2025: https://doi.org/10.1001/jamasurg.2025.2564

In that trial, medical students who got personalized feedback from a human instructor, built from the AI's error data, outperformed students taught by the AI tutor alone, in practice and on a realistic transfer task. This post describes a plan for next term, not results.

## Visual

Upload `visual.gif` (or `visual.mp4`). Re-render: python3 scripts/visuals/check_pilot_funnel.py, then npm run render -- content/posts/2026-11-19-ai-check-pilot-not-detector/visual.svg
