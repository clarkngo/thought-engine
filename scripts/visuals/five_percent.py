"""Visual for "Only 5% Say It Transformed Learning" (2026-10-27): DEC AI in Higher Education Global Survey 2026.

Top (pixel): 100 students, one per percentage point. Each answer group fills in as its bar grows;
only the 5 "transformed" students bob at full strength; the other 95 are dimmed. The reported shares sum to 99%, so one seat stays empty.
Bottom (flat): the four answers, plus the US and Canada "no clear value" share.
"""
from hybrid_stats import build
from pixel import ACCENT, ALERT, PALETTE, SUCCESS, sprite

GRAY = "#9aa1ad"
PALETTE.update({"K": "#f2c9a0", "H": "#3b2a20"})  # skin, hair (same as people.py)

HEAD = """
.HHHH.
HKKKKH
KXKKXK
KKKKKK
.CCCC.
CCCCCC
"""

# (count, shirt color char, bar color, label)
ANSWERS = [
    (5, "G", SUCCESS, "Transformed how I learn"),
    (28, "E", ACCENT, "Enhanced my understanding"),
    (42, "S", GRAY, "Only somewhat helpful"),
    (24, "R", ALERT, "No clear value"),
]
COLS, CELL_W, CELL_H, X0, Y0, PX = 20, 48, 46, 66, 260, 6

STYLE = """
    .seat { animation: seat 6s steps(1) infinite both; }
    @keyframes seat { 0% { opacity: 0; } 10% { opacity: 1; } 94% { opacity: 0; } }
"""


def grid():
    out, n = "", 0
    for group, (count, shirt, _, _) in enumerate(ANSWERS):
        art = HEAD.replace("C", shirt)
        cells = ""
        for _ in range(count):
            x, y = X0 + (n % COLS) * CELL_W, Y0 + (n // COLS) * CELL_H
            cell = sprite(art, x, y, PX)
            cells += f'\n    <g class="bob" style="animation-delay:{n % 4 * 0.15:.2f}s">{cell}</g>' if group == 0 else f"\n    {cell}"
            n += 1
        dim = "" if group == 0 else ' opacity="0.45"'  # the 5 stand out; the other 95 recede
        out += f'\n  <g class="seat" style="animation-delay:{group * 0.15:.2f}s"><g{dim}>{cells}\n  </g></g>'
    x, y = X0 + (n % COLS) * CELL_W, Y0 + (n // COLS) * CELL_H  # the 100th seat: shares sum to 99%
    out += f'\n  <rect x="{x + 6}" y="{y}" width="24" height="40" fill="none" stroke="#c9c4b8" stroke-width="2" stroke-dasharray="4 4"/>'
    return out


if __name__ == "__main__":
    build(
        slug="2026-10-27-only-five-percent-transformed",
        script="five_percent.py",
        lines=("Only 5% say AI", "transformed learning.", "Students with AI in their courses · DEC Global Survey 2026"),
        cards=[],
        top=grid(),
        style=STYLE,
        section="DID AI IN YOUR COURSES HELP YOU LEARN?",
        groups=[
            {"title": None, "max": 50, "rows": [(label, count, color, f"{count}%") for count, _, color, label in ANSWERS]},
            {"title": "US & CANADA", "max": 50, "rows": [("No clear value", 42, ALERT, "42%")]},
        ],
        panel=("Redesign, don't bolt on", [
            "Change what students do, not just the tool",
            "Measure learning without the AI",
            "Ask students what actually helped",
        ]),
    )
