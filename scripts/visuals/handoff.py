"""Visual for "Agents Don't Fail. Handoffs Do." (2026-10-21).

Three pixel robots pass a context crate (goal / constraints / history). At the
second handoff two blocks fall out and the Executor acts on 1 of 3.
"""
from pathlib import Path

from pixel import ALERT, INK, SUCCESS, document, framework, pixel_arrow, sprite, title

OUT = Path(__file__).resolve().parents[2] / "content/posts/2026-10-21-agents-dont-fail-handoffs-do/visual.svg"

ROBOT = """
.....AA.....
.....XX.....
..XXXXXXXX..
.XWWWWWWWWX.
.XWEEWWEEWX.
.XWEEWWEEWX.
.XWWWWWWWWX.
.XWWMMMMWWX.
..XXXXXXXX..
.XXBBBBBBXX.
X.XBBBBBBX.X
...XX..XX...
"""

CRATE = """
XXXXXXXXXXXXX
XDCCCCCCCCCDX
XDXXXXXXXXXDX
XD.........DX
XD.........DX
XD.........DX
XD.........DX
XD.........DX
XD.........DX
XDCCCCCCCCCDX
XXXXXXXXXXXXX
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
....X....
"""


def card(cx, label, delay):
    x = cx - 120
    return f"""
  <g>
    <rect x="{x + 8}" y="278" width="240" height="220" fill="{INK}"/>
    <rect x="{x}" y="270" width="240" height="220" fill="#fff" stroke="{INK}" stroke-width="4"/>
    <g class="bob" style="animation-delay:{delay}s">
      {sprite(ROBOT, cx - 48, 300)}
    </g>
    <text x="{cx}" y="458" font-size="30" font-weight="700" fill="{INK}" text-anchor="middle">{label}</text>
  </g>"""


crate_blocks = "\n      ".join(
    f'<rect class="{cls}" x="-36" y="{-28 + i * 20}" width="72" height="16" fill="{color}"/>'
    for i, (color, cls) in enumerate([("#2547d0", "keep"), ("#e3a52b", "lost"), ("#8f5bd8", "lost b")])
)

STYLE = """
    .packet { animation: travel 6s infinite; }
    @keyframes travel {
      0%   { transform: translate(180px, 640px); opacity: 0; animation-timing-function: steps(1); }
      6%   { transform: translate(180px, 640px); opacity: 1; animation-timing-function: steps(45); }
      25%  { transform: translate(540px, 640px); animation-timing-function: steps(1); }
      35%  { transform: translate(540px, 640px); animation-timing-function: steps(45); }
      60%  { transform: translate(900px, 640px); opacity: 1; animation-timing-function: steps(1); }
      90%  { transform: translate(900px, 640px); opacity: 0; }
      100% { transform: translate(900px, 640px); opacity: 0; }
    }
    .lost { animation: drop 6s infinite; }
    .lost.b { animation-delay: 0.1s; }
    @keyframes drop {
      0%   { transform: translate(0, 0); opacity: 1; animation-timing-function: steps(1); }
      46%  { transform: translate(0, 0); opacity: 1; animation-timing-function: steps(6); }
      56%  { transform: translate(-16px, 56px); opacity: 0; }
      100% { transform: translate(-16px, 56px); opacity: 0; }
    }
    .flash { animation: flash 6s steps(1) infinite; }
    @keyframes flash {
      0% { opacity: 0.18; } 45% { opacity: 1; } 48% { opacity: 0.5; } 51% { opacity: 1; }
      54% { opacity: 0.5; } 57% { opacity: 1; } 64% { opacity: 0.18; }
    }
    .ok { animation: ok 6s steps(1) infinite; }
    @keyframes ok { 0% { opacity: 0; } 25% { opacity: 1; } 38% { opacity: 0; } }
    .warn { animation: warn 6s steps(1) infinite; }
    @keyframes warn { 0% { opacity: 0; } 61% { opacity: 1; } 92% { opacity: 0; } }
"""

body = f"""{title("Agents don't fail.", "Handoffs do.")}

  <!-- Agent cards -->
  {card(180, "Intake", 0)}
  {card(540, "Planner", 0.2)}
  {card(900, "Executor", 0.4)}

  {pixel_arrow(312, 384, 376)}
  {pixel_arrow(672, 744, 376)}

  <!-- Handoff zones -->
  <rect x="304" y="592" width="112" height="96" fill="{SUCCESS}" opacity="0.18"/>
  <rect class="flash" x="664" y="592" width="112" height="96" fill="{ALERT}"/>
  <g font-size="22" font-weight="700" text-anchor="middle">
    <text x="360" y="720" fill="{SUCCESS}">handoff 1</text>
    <text x="720" y="720" fill="{ALERT}">handoff 2</text>
  </g>

  <!-- Context lane -->
  <path class="march" d="M180 640 H900" stroke="#9aa1ad" stroke-width="8" fill="none"/>
  <g fill="#9aa1ad">
    <rect x="168" y="628" width="24" height="24"/><rect x="528" y="628" width="24" height="24"/><rect x="888" y="628" width="24" height="24"/>
  </g>

  <!-- Status callouts -->
  <g class="ok">
    <rect x="440" y="508" width="200" height="48" fill="{SUCCESS}" stroke="{INK}" stroke-width="4"/>
    <text x="540" y="541" font-size="24" font-weight="700" fill="#fff" text-anchor="middle">✓ full context</text>
  </g>
  <g class="warn">
    <rect x="770" y="508" width="260" height="48" fill="{ALERT}" stroke="{INK}" stroke-width="4"/>
    <text x="900" y="541" font-size="24" font-weight="700" fill="#fff" text-anchor="middle">⚠ acting on 1 of 3</text>
    {sprite(QUESTION, 952, 176)}
  </g>

  <!-- Context crate: goal / constraints / history -->
  <g class="packet">
    {sprite(CRATE, -52, -44)}
    {crate_blocks}
  </g>

  <!-- Legend -->
  <g font-size="24" fill="#5d6470">
    <rect x="200" y="768" width="24" height="24" fill="#2547d0"/><text x="234" y="788">goal</text>
    <rect x="330" y="768" width="24" height="24" fill="#e3a52b"/><text x="364" y="788">constraints</text>
    <rect x="520" y="768" width="24" height="24" fill="#8f5bd8"/><text x="554" y="788">history</text>
    <text x="680" y="788">= the context packet</text>
  </g>
{framework("Design the seams, not just the steps", [
    "Write a handoff contract: what must cross",
    "Log every handoff, not only every output",
    "Verify at the seam, with a separate checker",
])}"""

OUT.write_text(document(body, STYLE, "Generated by scripts/visuals/handoff.py. One 6s loop."))
print(f"Wrote {OUT}")
