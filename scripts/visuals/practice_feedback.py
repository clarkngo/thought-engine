"""Visual for "Practice Without Feedback Made Them Worse" (2026-11-16). Source: Louie et al., CHI '26 (CARE).

Layout: split screen. Two identical practice scenes (a trainee talking with an AI patient). Only the right one gets
feedback cards. Below each, two pixel meters: empathy drains on the left; reflections and questions grow on the right.
Directions follow the paper's significant within-group changes; segment counts are illustrative. No takeaway panel.
"""
from pathlib import Path

from handoff import ROBOT
from people import STUDENT
from pixel import ACCENT, ALERT, INK, SUCCESS, document, sprite, title

OUT = Path(__file__).resolve().parents[2] / "content/posts/2026-11-16-practice-without-feedback/visual.svg"
GRAY = "#5d6470"
STEEL = "#9aa1ad"

TALK = """
.XXXXXXX.
XYYYYYYYX
XYXYXYXYX
XYYYYYYYX
.XXXXXXX.
...XX....
...X.....
"""

PANELS = [(60, "PRACTICE ALONE", False), (560, "PRACTICE + FEEDBACK", True)]
TOP, BOTTOM, W = 270, 836, 460
SEG, GAP, NSEG = 40, 6, 9
CHANGES = [25, 50, 75]  # % of the loop when a meter steps

STYLE = """    .you { animation: you 6s steps(1) infinite; }
    @keyframes you { 0% { opacity: 1; } 25% { opacity: 0; } 50% { opacity: 1; } 75% { opacity: 0; } }
    .bot { animation: bot 6s steps(1) infinite; }
    @keyframes bot { 0% { opacity: 0; } 25% { opacity: 1; } 50% { opacity: 0; } 75% { opacity: 1; } }
    .fb { animation: fb 6s steps(1) infinite; }
    @keyframes fb { 0% { opacity: 0; } 12% { opacity: 1; } 25% { opacity: 0; } 37% { opacity: 1; } 50% { opacity: 0; } 62% { opacity: 1; } 75% { opacity: 0; } 87% { opacity: 1; } }
""" + "".join(
    f"    .lose{k} {{ animation: lose{k} 6s steps(1) infinite; }}\n    @keyframes lose{k} {{ 0% {{ opacity: 1; }} {p}% {{ opacity: 0; }} }}\n"
    f"    .gain{k} {{ animation: gain{k} 6s steps(1) infinite; }}\n    @keyframes gain{k} {{ 0% {{ opacity: 0; }} {p}% {{ opacity: 1; }} }}\n"
    for k, p in enumerate(CHANGES)
)


def meter(x, y, label, tag, tag_color, base, color, change=None):
    """Label line, then a row of segments. `change` = ("lose" | "gain", color) animates three segments."""
    out = f"""
  <text x="{x + 24}" y="{y}" font-size="24" font-weight="800" fill="{INK}">{label}</text>
  <text x="{x + W - 24}" y="{y}" font-size="22" font-weight="800" fill="{tag_color}" text-anchor="end" letter-spacing="1">{tag}</text>"""
    for i in range(NSEG):
        sx = x + 24 + i * (SEG + GAP)
        out += f'\n  <rect x="{sx}" y="{y + 16}" width="{SEG}" height="32" fill="#e6e3da"/>'
        if change and change[0] == "lose" and base - 3 <= i < base:
            out += f'\n  <rect class="lose{base - 1 - i}" x="{sx}" y="{y + 16}" width="{SEG}" height="32" fill="{change[1]}"/>'
        elif change and change[0] == "gain" and base <= i < base + 3:
            out += f'\n  <rect class="gain{i - base}" x="{sx}" y="{y + 16}" width="{SEG}" height="32" fill="{change[1]}"/>'
        elif i < base:
            out += f'\n  <rect x="{sx}" y="{y + 16}" width="{SEG}" height="32" fill="{color}"/>'
    return out


def main():
    body = title("Same AI patient.", "Only one group got better.", "94 novice counselors, randomized: practice alone vs. practice with AI feedback")

    for x, head, feedback in PANELS:
        body += f"""
  <rect x="{x + 8}" y="{TOP + 8}" width="{W}" height="{BOTTOM - TOP}" fill="{ACCENT if feedback else INK}"/>
  <rect x="{x}" y="{TOP}" width="{W}" height="{BOTTOM - TOP}" fill="#fff" stroke="{INK}" stroke-width="4"/>
  <text x="{x + 24}" y="{TOP + 46}" font-size="24" font-weight="800" fill="{ACCENT if feedback else GRAY}" letter-spacing="2">{head}</text>
  <g class="you">{sprite(TALK, x + 96, 344, 5)}</g>
  <g class="bot">{sprite(TALK, x + 312, 344, 5)}</g>
  <g class="bob">{sprite(STUDENT, x + 60, 400)}</g>
  {sprite(ROBOT, x + 304, 424, 6)}
  <text x="{x + 108}" y="{524}" font-size="22" font-weight="800" fill="{INK}" text-anchor="middle">Trainee</text>
  <text x="{x + 340}" y="{524}" font-size="22" font-weight="800" fill="{INK}" text-anchor="middle">AI patient</text>"""
        if feedback:
            body += f"""
  <g class="fb"><rect x="{x + 24}" y="548" width="{W - 48}" height="56" fill="{INK}"/>
  <text x="{x + W // 2}" y="584" font-size="22" font-weight="800" fill="#fff" text-anchor="middle">Coach: name the feeling first.</text></g>"""
            body += meter(x, 664, "Reflections &amp; questions", "BETTER", SUCCESS, 4, INK, ("gain", SUCCESS))
            body += meter(x, 756, "Empathy", "HELD", GRAY, 6, INK)
        else:
            body += f"""
  <rect x="{x + 24}" y="548" width="{W - 48}" height="56" fill="none" stroke="{STEEL}" stroke-width="4" stroke-dasharray="12 10"/>
  <text x="{x + W // 2}" y="584" font-size="22" font-weight="800" fill="{GRAY}" text-anchor="middle">No feedback</text>"""
            body += meter(x, 664, "Reflections &amp; questions", "NO GAIN", GRAY, 4, INK)
            body += meter(x, 756, "Empathy", "WORSE", ALERT, 6, INK, ("lose", ALERT))

    body += f"""
  <text x="60" y="900" font-size="38" font-weight="800" fill="{INK}">The simulator gives the reps.</text>
  <text x="60" y="950" font-size="38" font-weight="800" fill="{ACCENT}">Feedback turns them into skill.</text>
  <text x="60" y="1004" font-size="22" fill="{GRAY}">Louie et al., CHI 2026 (Stanford). One 75-minute session; short-term effects.</text>
  <text x="60" y="1036" font-size="22" fill="{GRAY}">Meters show direction of change, not scale.</text>"""

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(document(body, STYLE, "Generated by scripts/visuals/practice_feedback.py. One 6s loop."))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
