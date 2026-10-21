"""Visual for "Novel Attackers. Boring Defenses." (Hugging Face agent intrusion, July 2026).

A red agent swarm walks through four failed controls (each card turns red), then
drops onto three controls that held and bounces off them ("DENIED").
"""
from pathlib import Path

from pixel import ALERT, INK, SUCCESS, document, framework, pixel_arrow, sprite, sprite_size, title

OUT = Path(__file__).resolve().parents[2] / "content/posts/2026-10-22-hugging-face-boring-defenses/visual.svg"
ICON_PX = 6

AGENT = """
.X....X.
..X..X..
.XRRRRX.
XRYRRYRX
XRRRRRRX
XrRRRRrX
.XrrrrX.
.X.XX.X.
"""

ICONS = {
    "dataset": """
XXXXX...
XYYYXX..
XYYYYXX.
XYSSSYX.
XYYYYYX.
XYSSSYX.
XYYYYYX.
XXXXXXX.
""",
    "pod": """
.XXXXXX.
XBBBBBBX
XBYYYYBX
XBYBBYBX
XBYBBYBX
XBYYYYBX
XBBBBBBX
.XXXXXX.
""",
    "node": """
XXXXXXXX
XSSSSSGX
XXXXXXXX
XSSSSSGX
XXXXXXXX
XSSSSSGX
XXXXXXXX
..X..X..
""",
    "clusters": """
XXXX.XXXX
XSGX.XSGX
XXXX.XXXX
XSGX.XSGX
XXXX.XXXX
XSGX.XSGX
XXXX.XXXX
""",
}

SHIELD = """
XXXXXXXX
XGGGGGGX
XGYGGGGX
XGYGGGGX
XGGGGGGX
.XGGGGX.
..XGGX..
...XX...
"""

# What failed: (icon, label, how it failed)
FAILED = [
    ("dataset", "Dataset config", "template injection"),
    ("pod", "Worker pod", "secrets in env"),
    ("node", "Node root", "privileged pod"),
    ("clusters", "2 clusters", "shared admin key"),
]
CARD_X = [40, 300, 560, 820]
CARD_W, CARD_Y, CARD_H = 220, 306, 150
CENTERS = [x + CARD_W // 2 for x in CARD_X]  # 150, 410, 670, 930

# What held: (heading, detail)
HELD = [
    ("IAM policy", "every write denied"),
    ("Credential store", "84 attempts denied"),
    ("Hub prod DB", "network blocked"),
]
SHIELD_X = [40, 390, 740]
SHIELD_W, SHIELD_Y, SHIELD_H = 300, 650, 130

LANE_Y = 548
AGENT_W, AGENT_H = sprite_size(AGENT, ICON_PX)  # 48 x 48
OFFSETS = [-78, -24, 30]  # each agent's x offset inside the swarm
LANDING = [0, 0, -60]  # x nudge where each agent lands on its shield (keeps clear of labels)


def card_hit_time(i):
    return 4 + 12 * i  # % of the loop when the swarm reaches card i


def agent_keyframes(i):
    """Keyframes for agent i: walk the lane card by card, then dive onto shield i and bounce."""
    dx = OFFSETS[i]
    y = LANE_Y - AGENT_H // 2
    frames = [(0, CENTERS[0], y, 0, "steps(1)"), (4, CENTERS[0], y, 1, "steps(1)")]
    for k in range(1, 4):
        start = card_hit_time(k - 1) + 6
        frames.append((start, CENTERS[k - 1], y, 1, "steps(8)"))
        frames.append((card_hit_time(k), CENTERS[k], y, 1, "steps(1)"))
    sx = SHIELD_X[i] + SHIELD_W // 2 - AGENT_W // 2 + LANDING[i]
    hit_y = SHIELD_Y - AGENT_H + 4
    frames += [
        (48, CENTERS[3], y, 1, "steps(8)"),
        (58, sx - dx, hit_y, 1, "steps(3)"),
        (62, sx - dx, hit_y - 40, 1, "steps(3)"),
        (66, sx - dx, hit_y - 8, 1, "steps(1)"),
        (90, sx - dx, hit_y - 8, 1, "steps(1)"),
        (96, sx - dx, hit_y - 8, 0, "steps(1)"),
        (100, sx - dx, hit_y - 8, 0, "steps(1)"),
    ]
    body = "\n".join(
        f"      {p}% {{ transform: translate({x + dx}px, {yy}px); opacity: {o}; animation-timing-function: {t}; }}"
        for p, x, yy, o, t in frames
    )
    return f"    .agent{i} {{ animation: agent{i} 6s infinite; }}\n    @keyframes agent{i} {{\n{body}\n    }}\n"


def failed_card(i):
    icon, label, how = FAILED[i]
    x, cx = CARD_X[i], CENTERS[i]
    w, _ = sprite_size(ICONS[icon], ICON_PX)
    return f"""
  <g>
    <rect x="{x + 8}" y="{CARD_Y + 8}" width="{CARD_W}" height="{CARD_H}" fill="{INK}"/>
    <rect x="{x}" y="{CARD_Y}" width="{CARD_W}" height="{CARD_H}" fill="#fff" stroke="{INK}" stroke-width="4"/>
    <rect class="hit" style="animation-name: hit{i}" x="{x + 2}" y="{CARD_Y + 2}" width="{CARD_W - 4}" height="{CARD_H - 4}" fill="{ALERT}"/>
    {sprite(ICONS[icon], cx - w // 2, CARD_Y + 22, ICON_PX)}
    <text x="{cx}" y="{CARD_Y + 122}" font-size="24" font-weight="700" fill="{INK}" text-anchor="middle">{label}</text>
    <text x="{cx}" y="{CARD_Y + CARD_H + 36}" font-size="22" font-weight="700" fill="{ALERT}" text-anchor="middle">{how}</text>
  </g>"""


def held_card(i):
    heading, detail = HELD[i]
    x = SHIELD_X[i]
    return f"""
  <g>
    <rect x="{x + 8}" y="{SHIELD_Y + 8}" width="{SHIELD_W}" height="{SHIELD_H}" fill="{SUCCESS}"/>
    <rect x="{x}" y="{SHIELD_Y}" width="{SHIELD_W}" height="{SHIELD_H}" fill="#fff" stroke="{INK}" stroke-width="4"/>
    {sprite(SHIELD, x + 22, SHIELD_Y + 41, ICON_PX)}
    <text x="{x + 90}" y="{SHIELD_Y + 58}" font-size="24" font-weight="700" fill="{INK}">{heading}</text>
    <text x="{x + 90}" y="{SHIELD_Y + 92}" font-size="22" fill="#5d6470">{detail}</text>
    <g class="denied">
      <rect x="{x + SHIELD_W - 112}" y="{SHIELD_Y - 18}" width="104" height="34" fill="{SUCCESS}" stroke="{INK}" stroke-width="4"/>
      <text x="{x + SHIELD_W - 60}" y="{SHIELD_Y + 7}" font-size="20" font-weight="800" fill="#fff" text-anchor="middle">DENIED</text>
    </g>
  </g>"""


hit_keyframes = "".join(
    f"    @keyframes hit{i} {{ 0% {{ opacity: 0; }} {card_hit_time(i)}% {{ opacity: 0.22; }} 94% {{ opacity: 0; }} }}\n"
    for i in range(4)
)

STYLE = (
    """
    .hit { opacity: 0; animation-duration: 6s; animation-iteration-count: infinite; animation-timing-function: steps(1); }
    .denied { animation: denied 6s steps(1) infinite; }
    @keyframes denied { 0% { opacity: 0; } 58% { opacity: 1; } 92% { opacity: 0; } }
"""
    + hit_keyframes
    + "".join(agent_keyframes(i) for i in range(3))
)

agents = "\n  ".join(f'<g class="agent{i}">{sprite(AGENT, 0, 0, ICON_PX)}</g>' for i in range(3))
arrows = "\n  ".join(pixel_arrow(CARD_X[i] + CARD_W + 4, CARD_X[i] + CARD_W + 6, CARD_Y + 74) for i in range(3))

body = f"""{title("Novel attackers.", "Boring defenses.", "Hugging Face agent intrusion · July 9–13, 2026")}

  <text x="1040" y="292" font-size="22" font-weight="800" fill="{ALERT}" letter-spacing="2" text-anchor="end">WHAT FAILED</text>
  {"".join(failed_card(i) for i in range(4))}
  {arrows}

  <!-- Attack lane -->
  <path class="march" d="M{CENTERS[0]} {LANE_Y} H{CENTERS[3]}" stroke="{ALERT}" stroke-width="8" fill="none" opacity="0.5"/>

  <text x="1040" y="608" font-size="22" font-weight="800" fill="{SUCCESS}" letter-spacing="2" text-anchor="end">WHAT HELD</text>
  {"".join(held_card(i) for i in range(3))}

  <!-- Agent swarm -->
  {agents}
{framework("Draw the blast radius before an agent does", [
    "Treat datasets and configs as executable code",
    "Kill shared admin keys; scope every credential",
    "Pre-stage a self-hosted model for incident response",
])}"""

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(document(body, STYLE, "Generated by scripts/visuals/hf_incident.py. One 6s loop."))
print(f"Wrote {OUT}")
