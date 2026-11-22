"""Alternate visual for "67% Less Escalation" (2026-11-17): the rehearsal as a branching path. Writes visual-tree.svg.

Layout: a shape that is the idea. One conversation path with three turns. At each turn a red "what if?" branch
drops toward escalation, and a ghost of the student tries it; then feedback checks the cooperative move and the
student walks on. The path ends at the real conflict. Below: the result vs. the lecture group (Shaikh et al.,
CHI 2024). Rehearsal's own features: a simulated interlocutor, "what if?" paths, and strategy feedback.
"""
from pathlib import Path

from handoff import ROBOT
from people import BUBBLE_PX, CHECK, STUDENT
from pixel import ACCENT, ALERT, INK, SUCCESS, document, sprite, title
from sim_sprites import BOLT, HEART

OUT = Path(__file__).resolve().parents[2] / "content/posts/2026-11-17-rehearse-the-conflict/visual-tree.svg"
GRAY = "#5d6470"
LINE_Y = 470
START_X, END_X = 200, 1000
NODES = [360, 580, 800]
ARRIVE = [15, 40, 65]  # % of the loop when the student reaches each turn
FINISH = 85
BRANCH_Y = 660


def student_x(node_x):
    return node_x - 48


def build_style():
    walk = [(0, 0)] + [(a, student_x(n) - student_x(NODES[0]) + (student_x(NODES[0]) - (START_X - 48)))
                       for a, n in zip(ARRIVE, NODES)] + [(FINISH, END_X - 120 - (START_X - 48))]
    frames = " ".join(f"{p}% {{ transform: translateX({dx}px); }}" for p, dx in walk)
    css = f"    .walk {{ animation: walk 6s steps(1) infinite; }}\n    @keyframes walk {{ {frames} }}\n"
    for k, a in enumerate(ARRIVE):
        css += (f"    .g{k} {{ animation: g{k} 6s steps(1) infinite; }}\n"
                f"    @keyframes g{k} {{ 0% {{ opacity: 0; }} {a + 2}% {{ opacity: 1; }} {a + 12}% {{ opacity: 0; }} }}\n"
                f"    .c{k} {{ animation: c{k} 6s steps(1) infinite; }}\n"
                f"    @keyframes c{k} {{ 0% {{ opacity: 0; }} {a + 12}% {{ opacity: 1; }} }}\n"
                f"    .s{k} {{ animation: s{k} 6s steps(1) infinite; }}\n"
                f"    @keyframes s{k} {{ 0% {{ opacity: 0; }} {a}% {{ opacity: 1; }} }}\n")
    css += f"    .end {{ animation: end 6s steps(1) infinite; }}\n    @keyframes end {{ 0% {{ opacity: 0.2; }} {FINISH}% {{ opacity: 1; }} }}\n"
    return css


def main():
    body = title("Rehearse the conflict.", "Try the what-ifs first.", "Stanford's Rehearsal: an AI plays the other side, with feedback on strategy")

    # The AI opponent, at the start of the path.
    body += f"""
  {sprite(ROBOT, 60, LINE_Y - 96)}
  <text x="108" y="{LINE_Y + 44}" font-size="22" font-weight="800" fill="{INK}" text-anchor="middle">AI opponent</text>"""

    # Main path; green segments fill in as the student passes each turn.
    body += f'\n  <rect x="{START_X}" y="{LINE_Y - 4}" width="{END_X - START_X}" height="8" fill="{INK}"/>'
    xs = [START_X] + NODES
    for k in range(3):
        body += f'\n  <rect class="s{k}" x="{xs[k]}" y="{LINE_Y - 4}" width="{xs[k + 1] - xs[k]}" height="8" fill="{SUCCESS}"/>'

    for k, nx in enumerate(NODES):
        body += f"""
  <path d="M{nx} {LINE_Y} V{BRANCH_Y - 70}" stroke="{ALERT}" stroke-width="6" stroke-dasharray="12 10"/>
  {sprite(BOLT, nx - 20, BRANCH_Y - 60, 5)}
  <text x="{nx}" y="{BRANCH_Y + 18}" font-size="22" font-weight="800" fill="{ALERT}" text-anchor="middle">escalate?</text>
  <rect x="{nx - 12}" y="{LINE_Y - 12}" width="24" height="24" fill="{INK}"/>
  <text x="{nx}" y="{LINE_Y - 128}" font-size="22" font-weight="800" fill="{GRAY}" text-anchor="middle">Turn {k + 1}</text>
  <g class="g{k}"><g opacity="0.4">{sprite(STUDENT, nx + 16, LINE_Y + 40, 6)}</g></g>
  <text class="g{k}" x="{nx + 110}" y="{LINE_Y + 90}" font-size="22" font-weight="800" fill="{ALERT}">what if?</text>
  <g class="c{k}">{sprite(CHECK, nx - 27, LINE_Y - 112, BUBBLE_PX)}</g>"""

    # The real conflict at the end of the path.
    body += f"""
  <g class="end">{sprite(HEART, END_X - 44, LINE_Y - 110, 6)}
  <text x="{END_X - 20}" y="{LINE_Y + 44}" font-size="22" font-weight="800" fill="{SUCCESS}" text-anchor="end">Real conflict</text></g>
  <g class="walk">{sprite(STUDENT, START_X - 48, LINE_Y - 100)}</g>"""

    # Result card.
    body += f"""
  <rect x="68" y="738" width="952" height="170" fill="{ACCENT}"/>
  <rect x="60" y="730" width="952" height="170" fill="#fff" stroke="{INK}" stroke-width="4"/>
  <text x="90" y="776" font-size="24" font-weight="800" fill="{GRAY}" letter-spacing="2">THEN A REAL CONFLICT, NO AI. VS. A LECTURE GROUP:</text>
  <text x="90" y="864" font-size="88" font-weight="800" fill="{ACCENT}" letter-spacing="-3">−67%</text>
  <text x="330" y="830" font-size="30" font-weight="800" fill="{INK}">escalating tactics</text>
  <text x="330" y="874" font-size="30" font-weight="800" fill="{SUCCESS}">2× the cooperative ones</text>"""

    body += f"""
  <text x="60" y="960" font-size="34" font-weight="800" fill="{INK}">Make the mistakes where they're free.</text>
  <text x="60" y="1004" font-size="22" fill="{GRAY}">Shaikh et al., CHI 2024 (Stanford), 40 participants. Lab study; short-term effects.</text>
  <text x="60" y="1036" font-size="22" fill="{GRAY}">Path is illustrative.</text>"""

    OUT.write_text(document(body, build_style(), "Generated by scripts/visuals/rehearsal_tree.py. One 6s loop."))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
