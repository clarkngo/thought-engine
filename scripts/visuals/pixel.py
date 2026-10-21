"""Shared helpers for pixel-hybrid visuals (see "Visual Style & Production" in CLAUDE.md).

Each visual is its own script in this folder that imports from here and writes an
animated SVG into its post folder:

    python3 scripts/visuals/<name>.py
"""

PX = 8  # default: one sprite pixel = 8 units on the 1080 canvas

PALETTE = {
    "X": "#1b1d21",  # ink
    "W": "#eef1fb",  # face plate
    "E": "#2547d0",  # accent blue
    "M": "#2547d0",
    "B": "#4c6ef5",  # body blue
    "A": "#ffb703",  # antenna light
    "C": "#c08a52",  # crate wood
    "D": "#8a5a2b",  # crate dark wood
    "R": "#e8613c",  # alert
    "r": "#b8401f",  # alert dark
    "G": "#2f9e6a",  # success
    "g": "#1f7a50",  # success dark
    "Y": "#ffffff",
    "S": "#9aa1ad",  # steel
}

INK = PALETTE["X"]
ACCENT = PALETTE["E"]
ALERT = PALETTE["R"]
SUCCESS = PALETTE["G"]
FONT = "-apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"


def sprite(art, ox, oy, px=PX):
    """Return <rect>s for an ASCII sprite with its top-left at (ox, oy). '.' is transparent."""
    rows = art.strip("\n").split("\n")
    out = []
    for y, row in enumerate(rows):
        x = 0
        while x < len(row):
            ch = row[x]
            if ch == ".":
                x += 1
                continue
            run = 1  # merge horizontal runs of one color
            while x + run < len(row) and row[x + run] == ch:
                run += 1
            out.append(
                f'<rect x="{ox + x * px}" y="{oy + y * px}" width="{run * px}" height="{px}" fill="{PALETTE[ch]}"/>'
            )
            x += run
    return "\n      ".join(out)


def sprite_size(art, px=PX):
    rows = art.strip("\n").split("\n")
    return max(len(r) for r in rows) * px, len(rows) * px


def pixel_arrow(x1, x2, y, color=INK):
    """Marching dashed arrow from x1 to x2 with a stepped pixel head (needs the .march class)."""
    head = "".join(
        f'<rect x="{x2 + i * PX}" y="{y - (3 - i) * PX}" width="{PX}" height="{(7 - 2 * i) * PX}" fill="{color}"/>'
        for i in range(4)
    )
    return f'<path class="march" d="M{x1} {y + 4} H{x2}" stroke="{color}" stroke-width="{PX}" fill="none"/>{head}'


BASE_STYLE = """
    rect, path { shape-rendering: crispEdges; }
    .march { stroke-dasharray: 16 16; animation: march 0.6s steps(4) infinite; }
    @keyframes march { to { stroke-dashoffset: -32; } }
    .bob { animation: bob 0.6s steps(1) infinite; }
    @keyframes bob { 0% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
"""


def document(body, style, comment):
    """Wrap a visual in the house canvas: 1080 square, paper background, dot grid."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080" width="1080" height="1080" font-family="{FONT}">
  <!-- {comment} -->
  <style>{BASE_STYLE}{style}  </style>
  <defs>
    <pattern id="grid" width="16" height="16" patternUnits="userSpaceOnUse">
      <rect width="2" height="2" fill="#dcd8cd"/>
    </pattern>
  </defs>
  <rect width="1080" height="1080" fill="#f7f5f0"/>
  <rect width="1080" height="1080" fill="url(#grid)"/>
{body}
</svg>
"""


def title(line1, line2, subtitle=None):
    sub = (
        f'\n  <text x="100" y="236" font-size="24" fill="#5d6470">{subtitle}</text>' if subtitle else ""
    )
    return f"""
  <rect x="60" y="72" width="16" height="112" fill="{ACCENT}"/>
  <text x="100" y="122" font-size="58" font-weight="800" fill="{INK}">{line1}</text>
  <text x="100" y="186" font-size="58" font-weight="800" fill="{ACCENT}">{line2}</text>{sub}"""


def framework(heading, lines):
    """Dark takeaway panel with an offset accent shadow at the bottom of the canvas."""
    items = "\n    ".join(
        f'<text x="100" y="{928 + i * 36}">{i + 1}. {line}</text>' for i, line in enumerate(lines)
    )
    return f"""
  <rect x="68" y="838" width="960" height="190" fill="{ACCENT}"/>
  <rect x="60" y="830" width="960" height="190" fill="{INK}"/>
  <text x="100" y="878" font-size="30" font-weight="800" fill="#fff">{heading}</text>
  <g font-size="25" fill="#d9dce3">
    {items}
  </g>"""
