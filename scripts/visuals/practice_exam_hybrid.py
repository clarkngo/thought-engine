"""Hybrid visual for "Better at Practice. Worse at the Exam." (2026-10-28).

Top (pixel): one card per arm of Bastani et al. (PNAS 2025). During practice the AI sits beside the student:
the ChatGPT-style robot hands over answers (student: check), the tutor robot gives a hint (student: works the steps).
At the exam the robots leave: the ChatGPT-style student is left with a question mark, the others keep working.
Bottom (flat): scores relative to the no-AI group. Practice bars grow (+48%, +127%), then the AI is removed
and the bars shrink to exam results (-17%, no drop).
"""
from pathlib import Path

from handoff import ROBOT
from people import CHECK, STEPS
from pixel import ALERT, BASE_STYLE, FONT, INK, PALETTE, SUCCESS, sprite, title

OUT = Path(__file__).resolve().parents[2] / "content/posts/2026-10-26-better-at-practice-worse-at-the-exam/visual-hybrid.svg"
SPLIT_Y = 500
BUBBLE_PX = 5
ACTOR_PX = 6  # student and robot share a card, so both are drawn smaller

PALETTE.update({"K": "#f2c9a0", "H": "#3b2a20"})  # skin, hair

STUDENT = """
...HHHHHH...
..HHHHHHHH..
..HKKKKKKH..
..KKXKKXKK..
..KKKKKKKK..
...KKXXKK...
....KKKK....
..BBBBBBBB..
.BBBBBBBBBB.
.BBBBBBBBBB.
.KBBBBBBBBK.
..XX....XX..
"""

ANSWER = """
.XXXXXXX.
XYYYYYYYX
XYYRRRYYX
XYRYYYRYX
XYRRRRRYX
XYRYYYRYX
XYRYYYRYX
.XXXXXXX.
....XX...
....X....
"""

QUESTION = """
.XXXXXXX.
XYYYYYYYX
XYYRRRYYX
XYRYYYRYX
XYYYYRYYX
XYYYRYYYX
XYYYYYYYX
XYYYRYYYX
.XXXXXXX.
....XX...
"""

BULB = """
..XXX..
.XAAAX.
XAAYAAX
XAAAAAX
XAAAAAX
.XAAAX.
..XSX..
..XSX..
...X...
"""

# (card label, bar label, practice index, exam index, practice text, exam text, bar color)
ARMS = [
    ("No AI", "No AI", 100, 100, "baseline", "baseline", "#9aa1ad"),
    ("ChatGPT-style", "ChatGPT-style", 148, 83, "+48%", "−17%", ALERT),
    ("Guardrailed tutor", "Guardrailed tutor", 227, 100, "+127%", "no drop", "#2547d0"),
]
CENTERS = [180, 540, 900]
BAR_X, BAR_SCALE = 300, 2.6  # bar width = index * scale
ROW_Y = [586, 646, 706]
BAR_H = 40


def actor(art, x, delay, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f"""
    <g{c}><g class="bob" style="animation-delay:{delay:.1f}s">{sprite(art, x, 344, ACTOR_PX)}</g></g>"""


def bubble(art, x, cls):
    return f'\n    <g class="{cls}">{sprite(art, x, 284, BUBBLE_PX)}</g>'


def student_card(i):
    """No AI: student alone, working. With AI: student left, robot right; the robot leaves at the exam."""
    cx = CENTERS[i]
    x = cx - 120
    label = ARMS[i][0]
    if i == 0:
        body = actor(STUDENT, cx - 36, 0) + bubble(STEPS, cx - 22, "always")
    else:
        sx, rx = cx - 96, cx + 24
        body = actor(STUDENT, sx, i * 0.2) + actor(ROBOT, rx, i * 0.2 + 0.3, "robot")
        if i == 1:  # hands over the answer; at the exam the student is stuck
            body += bubble(ANSWER, rx + 14, "practice-px") + bubble(CHECK, sx + 14, "practice-px")
            body += bubble(QUESTION, sx + 14, "exam-px")
        else:  # gives a hint; the student does the steps, with or without it
            body += bubble(BULB, rx + 18, "practice-px") + bubble(STEPS, sx + 14, "always")
    return f"""
  <g>
    <rect x="{x + 8}" y="278" width="240" height="220" fill="{INK}"/>
    <rect x="{x}" y="270" width="240" height="220" fill="#fff" stroke="{INK}" stroke-width="4"/>{body}
    <text x="{cx}" y="458" font-size="25" font-weight="700" fill="{INK}" text-anchor="middle">{label}</text>
  </g>"""


def bar_row(i):
    _, label, practice, exam, p_text, e_text, color = ARMS[i]
    y = ROW_Y[i]
    width = practice * BAR_SCALE
    ratio = exam / practice
    return (
        f"""
  <text x="60" y="{y + 29}" font-size="24" font-weight="700" fill="{INK}">{label}</text>
  <rect class="bar" style="animation-name: bar{i}" x="{BAR_X}" y="{y}" width="{width:.0f}" height="{BAR_H}" rx="8" fill="{color}"/>
  <text class="practice-label" x="1020" y="{y + 29}" font-size="24" font-weight="800" fill="{color if i else '#5d6470'}" text-anchor="end">{p_text}</text>
  <text class="exam-label" x="1020" y="{y + 29}" font-size="24" font-weight="800" fill="{color if i else '#5d6470'}" text-anchor="end">{e_text}</text>""",
        f"    @keyframes bar{i} {{ 0% {{ transform: scaleX(0); }} 12%, 46% {{ transform: scaleX(1); }} 54%, 92% {{ transform: scaleX({ratio:.3f}); }} 98%, 100% {{ transform: scaleX(0); }} }}\n",
    )


STYLE = """
    /* Pixel half: stepped. */
    .practice-px { animation: practice-px 6s steps(1) infinite; }
    @keyframes practice-px { 0% { opacity: 0; } 8% { opacity: 1; } 48% { opacity: 0; } }
    .exam-px { animation: exam-px 6s steps(1) infinite; }
    @keyframes exam-px { 0% { opacity: 0; } 56% { opacity: 1; } 94% { opacity: 0; } }
    .robot { animation: robot 6s steps(1) infinite; }
    @keyframes robot { 0% { opacity: 1; } 50% { opacity: 0; } 96% { opacity: 1; } }

    /* Flat half: smooth. */
    .bar { transform-box: fill-box; transform-origin: left center; animation-duration: 6s; animation-iteration-count: infinite; animation-timing-function: linear; }
    .practice-label, .phase-practice { animation: practice 6s linear infinite; }
    @keyframes practice { 0%, 6% { opacity: 0; } 12%, 44% { opacity: 1; } 50%, 100% { opacity: 0; } }
    .exam-label, .phase-exam { animation: exam 6s linear infinite; }
    @keyframes exam { 0%, 50% { opacity: 0; } 56%, 90% { opacity: 1; } 96%, 100% { opacity: 0; } }
"""


def main():
    rows = [bar_row(i) for i in range(3)]
    style = STYLE + "".join(k for _, k in rows)
    base = BASE_STYLE.replace("rect, path { shape-rendering: crispEdges; }", ".px rect, .px path { shape-rendering: crispEdges; }")

    pixel_top = f"""
  <!-- Pixel world: the three groups of students -->
  <rect width="1080" height="{SPLIT_Y}" fill="url(#grid)"/>
  {title("Better at practice.", "Worse at the exam.", "Randomized trial · ~1,000 students · PNAS 2025")}
  {"".join(student_card(i) for i in range(3))}"""

    flat_bottom = f"""
  <!-- Flat world: the scores -->
  <path d="M60 {SPLIT_Y + 20} H1020" stroke="#d8d4c9" stroke-width="2"/>
  <text x="60" y="{SPLIT_Y + 52}" font-size="20" font-weight="800" fill="#5d6470" letter-spacing="2">THE SCORES</text>
  <text class="phase-practice" x="1020" y="{SPLIT_Y + 52}" font-size="22" font-weight="800" fill="{SUCCESS}" letter-spacing="1" text-anchor="end">PRACTICE · AI AVAILABLE</text>
  <text class="phase-exam" x="1020" y="{SPLIT_Y + 52}" font-size="22" font-weight="800" fill="{ALERT}" letter-spacing="1" text-anchor="end">EXAM · AI REMOVED</text>
  <path d="M{BAR_X} 576 V756" stroke="#9aa1ad" stroke-width="2" stroke-dasharray="4 6"/>
  {"".join(r for r, _ in rows)}
  <text x="{BAR_X}" y="792" font-size="22" fill="#5d6470">Score relative to the no-AI group</text>

  <rect x="60" y="830" width="960" height="190" rx="20" fill="{INK}"/>
  <text x="100" y="878" font-size="30" font-weight="800" fill="#fff">Design for learning, not performance</text>
  <g font-size="25" fill="#d9dce3">
    <text x="100" y="928">1. Tutors give hints, not answers</text>
    <text x="100" y="964">2. Assess without AI at least once</text>
    <text x="100" y="1000">3. Grade the reasoning, not just the output</text>
  </g>"""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080" width="1080" height="1080" font-family="{FONT}">
  <!-- Generated by scripts/visuals/practice_exam_hybrid.py. Pixel students, flat scores; one 6s loop. -->
  <style>{base}{style}  </style>
  <defs>
    <pattern id="grid" width="16" height="16" patternUnits="userSpaceOnUse">
      <rect width="2" height="2" fill="#dcd8cd"/>
    </pattern>
  </defs>
  <rect width="1080" height="1080" fill="#f7f5f0"/>
  <g class="px">{pixel_top}
  </g>{flat_bottom}
</svg>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(svg)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
