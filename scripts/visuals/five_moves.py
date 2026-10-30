"""Carousel for "Five Moves for Teaching With AI" (2026-10-30): a cover, one slide per move, and a closing slide.

Writes static slide SVGs into the post's slides/ folder. Then build the PDF and cover with:

    npm run carousel -- content/posts/2026-10-30-five-moves-for-teaching-with-ai
"""
from pathlib import Path

from handoff import ROBOT
from people import ANSWER, CHECK, CODE, PROFESSOR, QUESTION, STEPS, STUDENT
from pixel import ACCENT, ALERT, INK, SUCCESS, document, sprite
from practice_exam_hybrid import BULB

OUT = Path(__file__).resolve().parents[2] / "content/posts/2026-10-30-five-moves-for-teaching-with-ai/slides"
GRAY = "#5d6470"
ACTOR_PX, BUBBLE_PX = 12, 9
TOTAL = 7


def footer(n):
    """Progress squares on the left, author in the middle-right, a swipe arrow until the last slide."""
    dots = "".join(
        f'<rect x="{60 + i * 34}" y="1000" width="22" height="22" fill="{ACCENT if i == n else "#d8d4c9"}"/>'
        for i in range(TOTAL)
    )
    arrow = f'<text x="1020" y="1020" font-size="30" font-weight="800" fill="{ACCENT}" text-anchor="end">→</text>' if n < TOTAL - 1 else ""
    return f"""
  {dots}
  <text x="{1020 if n == TOTAL - 1 else 970}" y="1019" font-size="24" font-weight="700" fill="{GRAY}" text-anchor="end">Clark Ngo</text>
  {arrow}"""


def text_lines(lines, y, size, fill, weight=400, gap=None):
    gap = gap or round(size * 1.35)
    return "".join(
        f'\n  <text x="60" y="{y + i * gap}" font-size="{size}" font-weight="{weight}" fill="{fill}">{line}</text>'
        for i, line in enumerate(lines)
    )


def scene_card(body):
    return f"""
  <rect x="68" y="338" width="952" height="320" fill="{INK}"/>
  <rect x="60" y="330" width="952" height="320" fill="#fff" stroke="{INK}" stroke-width="4"/>{body}"""


def actor(art, x, y=440):
    return sprite(art, x, y, ACTOR_PX)


def bubble(art, x, y=345):
    return sprite(art, x, y, BUBBLE_PX)


def no_robot(x, y=440):
    """The robot, faded and crossed out: the AI is not in the room."""
    return f"""
  <g opacity="0.3">{actor(ROBOT, x, y)}</g>
  <path d="M{x - 8} {y - 8} L{x + 152} {y + 152} M{x + 152} {y - 8} L{x - 8} {y + 152}" stroke="{ALERT}" stroke-width="12"/>"""


# (title lines, scene, evidence lines, source)
MOVES = [
    (["Hints,", "not answers."],
     actor(ROBOT, 190) + bubble(BULB, 320) + actor(STUDENT, 650) + bubble(STEPS, 770),
     ["ChatGPT-style help: 17% lower on the exam.", "Guardrailed tutor: that drop essentially disappeared."],
     "Bastani et al., PNAS 2025"),
    (["Sequence", "the work."],
     actor(STUDENT, 190) + bubble(STEPS, 310) + bubble(CHECK, 480, 400) + bubble(CHECK, 620, 400) + bubble(CHECK, 760, 400),
     ["Harvard's instructor-built tutor went one step at a time.", "Median learning gains more than doubled over an", "in-class active-learning lesson."],
     "Kestin et al., Scientific Reports 2025"),
    (["Assess without AI", "at least once."],
     actor(STUDENT, 190) + bubble(STEPS, 310) + no_robot(650),
     ["Scores with AI show performance.", "Scores without it show what stuck."],
     "Design recommendation drawn from Bastani et al., PNAS 2025"),
    (["Grade the explanation,", "not the artifact."],
     actor(STUDENT, 190) + bubble(CODE, 310) + actor(PROFESSOR, 650) + bubble(QUESTION, 770),
     ["One intro CS course added weekly oral code reviews.", "AI use rose. Exam averages held steady."],
     "Fowles et al., 2026 (preprint, one course)"),
    (["Teach verification", "as a skill."],
     actor(ROBOT, 190) + bubble(ANSWER, 310) + actor(STUDENT, 650) + bubble(QUESTION, 770),
     ["Verifying AI-generated work is gaining ground", "as implementation-level coding loses it."],
     "Lee et al., 2026 (report from 23 computing educators)"),
]


def cover():
    return f"""
  <rect x="60" y="120" width="16" height="250" fill="{ACCENT}"/>
  <text x="100" y="196" font-size="84" font-weight="800" fill="{INK}">Five moves for</text>
  <text x="100" y="284" font-size="84" font-weight="800" fill="{INK}">teaching</text>
  <text x="100" y="372" font-size="84" font-weight="800" fill="{ACCENT}">with AI.</text>
  {actor(ROBOT, 300, 470)}{bubble(BULB, 460, 390)}
  {actor(STUDENT, 640, 470)}{bubble(STEPS, 800, 380)}""" + text_lines(
        ["AI in a course can lower exam scores", "or double learning gains."], 720, 40, INK, 700
    ) + text_lines(["The difference is design, not the model."], 840, 40, ACCENT, 800)


def move(i):
    title_lines, scene, evidence, source = MOVES[i]
    return (
        f'\n  <text x="60" y="96" font-size="24" font-weight="800" fill="{GRAY}" letter-spacing="2">MOVE {i + 1} OF 5</text>'
        + text_lines(title_lines, 176, 72, ACCENT, 800, 84)
        + scene_card(scene)
        + text_lines(evidence, 722, 34, INK, 600, 46)
        + f'\n  <text x="60" y="934" font-size="24" fill="{GRAY}">{source}</text>'
    )


def closing():
    return (
        text_lines(["Only 5%"], 220, 150, SUCCESS, 800)
        + text_lines(["of students with AI in their courses", "say it transformed how they learn."], 310, 40, INK, 600, 54)
        + text_lines(["Adding AI isn't redesigning."], 510, 60, ACCENT, 800)
        + text_lines(["Which of the five would be hardest", "at your institution?"], 660, 46, INK, 700, 62)
        + f'\n  <text x="60" y="934" font-size="24" fill="{GRAY}">Digital Education Council, Global Survey 2026</text>'
    )


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    slides = [cover()] + [move(i) for i in range(5)] + [closing()]
    for n, body in enumerate(slides):
        path = OUT / f"slide-{n + 1}.svg"
        path.write_text(document(body + footer(n), "", "Generated by scripts/visuals/five_moves.py."))
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
