"""Hybrid of the handoff visual: pixel agents on top, flat handoff process flow below.

Top half (on the dot grid): the pixel robot cards, stepped arrows, and the "?" bubble from handoff.py.
Bottom half (plain paper): the flat context lane, packet, handoff zones, callouts, legend, and framework.
Same 6s timeline as the other two versions.
"""
from handoff import OUT as PIXEL_OUT, QUESTION, card
from pixel import ALERT, BASE_STYLE, FONT, INK, SUCCESS, pixel_arrow, sprite, title

OUT = PIXEL_OUT.with_name("visual-hybrid.svg")
SPLIT_Y = 500  # pixel world above, flat world below

STYLE = """
    .lane { stroke-dasharray: 14 10; animation: lane 0.6s linear infinite; }
    @keyframes lane { to { stroke-dashoffset: -24; } }

    .packet { animation: travel 6s linear infinite; }
    @keyframes travel {
      0%   { transform: translate(180px, 640px); opacity: 0; }
      6%   { transform: translate(180px, 640px); opacity: 1; }
      25%  { transform: translate(540px, 640px); }
      35%  { transform: translate(540px, 640px); }
      60%  { transform: translate(900px, 640px); opacity: 1; }
      88%  { transform: translate(900px, 640px); opacity: 1; }
      96%  { transform: translate(900px, 640px); opacity: 0; }
      100% { transform: translate(900px, 640px); opacity: 0; }
    }

    .lost { animation: drop 6s linear infinite; }
    .lost.b { animation-delay: 0.1s; }
    @keyframes drop {
      0%, 46% { transform: translate(0, 0) rotate(0); opacity: 1; }
      56%     { transform: translate(-20px, 50px) rotate(-35deg); opacity: 0; }
      100%    { transform: translate(-20px, 50px) rotate(-35deg); opacity: 0; }
    }

    .flash { animation: flash 6s linear infinite; }
    @keyframes flash {
      0%, 43%   { opacity: 0.18; }
      48%, 58%  { opacity: 1; }
      66%, 100% { opacity: 0.18; }
    }

    .ok { animation: ok 6s linear infinite; }
    @keyframes ok { 0%, 23% { opacity: 0; } 27%, 36% { opacity: 1; } 40%, 100% { opacity: 0; } }

    /* The pixel "?" pops on (steps) while the flat callout fades in, so each half keeps its own motion. */
    .warn { animation: warn 6s linear infinite; }
    @keyframes warn { 0%, 59% { opacity: 0; } 63%, 90% { opacity: 1; } 96%, 100% { opacity: 0; } }
    .huh { animation: huh 6s steps(1) infinite; }
    @keyframes huh { 0% { opacity: 0; } 61% { opacity: 1; } 92% { opacity: 0; } }
"""

PIXEL_TOP = f"""
  <!-- Pixel world: agents -->
  <rect width="1080" height="{SPLIT_Y}" fill="url(#grid)"/>
  {title("Agents don't fail.", "Handoffs do.")}
  {card(180, "Intake", 0)}
  {card(540, "Planner", 0.2)}
  {card(900, "Executor", 0.4)}
  {pixel_arrow(312, 384, 376)}
  {pixel_arrow(672, 744, 376)}
  <g class="huh">{sprite(QUESTION, 952, 176)}</g>"""

FLAT_BOTTOM = f"""
  <!-- Flat world: the handoff process -->
  <path d="M60 {SPLIT_Y + 20} H1020" stroke="#d8d4c9" stroke-width="2"/>
  <text x="60" y="{SPLIT_Y + 52}" font-size="20" font-weight="800" fill="#5d6470" letter-spacing="2">THE HANDOFF</text>

  <rect x="300" y="590" width="120" height="100" rx="14" fill="{SUCCESS}" opacity="0.18"/>
  <rect class="flash" x="660" y="590" width="120" height="100" rx="14" fill="{ALERT}"/>
  <g font-size="22" font-weight="700" text-anchor="middle">
    <text x="360" y="720" fill="{SUCCESS}">handoff 1</text>
    <text x="720" y="720" fill="{ALERT}">handoff 2</text>
  </g>

  <path class="lane" d="M180 640 H900" stroke="#9aa1ad" stroke-width="4" fill="none"/>
  <g fill="#9aa1ad"><circle cx="180" cy="640" r="9"/><circle cx="540" cy="640" r="9"/><circle cx="900" cy="640" r="9"/></g>

  <g class="ok">
    <rect x="440" y="528" width="200" height="44" rx="22" fill="{SUCCESS}"/>
    <text x="540" y="558" font-size="22" font-weight="700" fill="#fff" text-anchor="middle">✓ full context</text>
  </g>
  <g class="warn">
    <rect x="780" y="528" width="240" height="44" rx="22" fill="{ALERT}"/>
    <text x="900" y="558" font-size="22" font-weight="700" fill="#fff" text-anchor="middle">⚠ acting on 1 of 3</text>
  </g>

  <g class="packet">
    <rect x="-54" y="-44" width="108" height="88" rx="12" fill="#fff" stroke="{INK}" stroke-width="3"/>
    <rect x="-40" y="-30" width="80" height="16" rx="4" fill="#2547d0"/>
    <rect class="lost" x="-40" y="-8" width="80" height="16" rx="4" fill="#e3a52b"/>
    <rect class="lost b" x="-40" y="14" width="80" height="16" rx="4" fill="#8f5bd8"/>
  </g>

  <g font-size="24" fill="#5d6470">
    <rect x="200" y="768" width="22" height="22" rx="4" fill="#2547d0"/><text x="232" y="787">goal</text>
    <rect x="330" y="768" width="22" height="22" rx="4" fill="#e3a52b"/><text x="362" y="787">constraints</text>
    <rect x="520" y="768" width="22" height="22" rx="4" fill="#8f5bd8"/><text x="552" y="787">history</text>
    <text x="680" y="787">= the context packet</text>
  </g>

  <rect x="60" y="830" width="960" height="190" rx="20" fill="{INK}"/>
  <text x="100" y="878" font-size="30" font-weight="800" fill="#fff">Design the seams, not just the steps</text>
  <g font-size="25" fill="#d9dce3">
    <text x="100" y="928">1. Write a handoff contract: what must cross</text>
    <text x="100" y="964">2. Log every handoff, not only every output</text>
    <text x="100" y="1000">3. Verify at the seam, with a separate checker</text>
  </g>"""


def main():
    # Pixel crispness only applies to the pixel half; the flat half keeps smooth edges.
    base = BASE_STYLE.replace("rect, path { shape-rendering: crispEdges; }", ".px rect, .px path { shape-rendering: crispEdges; }")
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080" width="1080" height="1080" font-family="{FONT}">
  <!-- Generated by scripts/visuals/handoff_hybrid.py. Pixel agents, flat process flow; one 6s loop. -->
  <style>{base}{STYLE}  </style>
  <defs>
    <pattern id="grid" width="16" height="16" patternUnits="userSpaceOnUse">
      <rect width="2" height="2" fill="#dcd8cd"/>
    </pattern>
  </defs>
  <rect width="1080" height="1080" fill="#f7f5f0"/>
  <g class="px">{PIXEL_TOP}
  </g>{FLAT_BOTTOM}
</svg>
"""
    OUT.write_text(svg)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
