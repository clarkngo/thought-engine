"""Flat alternate of the Hugging Face incident visual (see hf_incident.py for the pixel one).

Same layout, data, and timing; rounded cards, vector icons, and linear motion.
"""
from pathlib import Path

from hf_incident import (
    CARD_H, CARD_W, CARD_X, CARD_Y, CENTERS, FAILED, HELD, LANE_Y,
    SHIELD_H, SHIELD_W, SHIELD_X, SHIELD_Y, agent_keyframes, card_hit_time,
)
from pixel import ACCENT, ALERT, FONT, INK, SUCCESS

OUT = Path(__file__).resolve().parents[2] / "content/posts/2026-10-22-hugging-face-boring-defenses/visual-flat.svg"
MUTED = "#5d6470"
STEEL = "#9aa1ad"


def icon(kind, cx, top):
    """48px vector icon centered on cx."""
    x = cx - 24
    if kind == "dataset":
        return f"""<path d="M{x + 6} {top} H{x + 30} L{x + 42} {top + 12} V{top + 48} H{x + 6} Z" fill="#fff" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
    <path d="M{x + 30} {top} V{top + 12} H{x + 42}" fill="none" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
    <g stroke="{STEEL}" stroke-width="3" stroke-linecap="round"><path d="M{x + 14} {top + 24} H{x + 34}"/><path d="M{x + 14} {top + 34} H{x + 34}"/></g>"""
    if kind == "pod":
        return f"""<rect x="{x + 2}" y="{top + 2}" width="44" height="44" rx="10" fill="#e8ecfb" stroke="{ACCENT}" stroke-width="3"/>
    <rect x="{x + 14}" y="{top + 14}" width="20" height="20" rx="4" fill="{ACCENT}"/>"""
    if kind == "node":
        rows = "".join(
            f'<rect x="{x + 2}" y="{top + 2 + r * 15}" width="44" height="12" rx="4" fill="#fff" stroke="{INK}" stroke-width="3"/>'
            f'<circle cx="{x + 38}" cy="{top + 8 + r * 15}" r="2.5" fill="{SUCCESS}"/>'
            for r in range(3)
        )
        return rows
    if kind == "clusters":
        stacks = ""
        for sx in (x - 4, x + 28):
            stacks += "".join(
                f'<rect x="{sx}" y="{top + 2 + r * 15}" width="24" height="12" rx="4" fill="#fff" stroke="{INK}" stroke-width="3"/>'
                f'<circle cx="{sx + 17}" cy="{top + 8 + r * 15}" r="2.5" fill="{SUCCESS}"/>'
                for r in range(3)
            )
        return stacks
    raise ValueError(kind)


def shield_icon(x, y):
    return f"""<path d="M{x} {y} H{x + 40} V{y + 22} C{x + 40} {y + 36} {x + 30} {y + 44} {x + 20} {y + 48} C{x + 10} {y + 44} {x} {y + 36} {x} {y + 22} Z" fill="{SUCCESS}"/>
    <path d="M{x + 11} {y + 23} L{x + 18} {y + 30} L{x + 30} {y + 16}" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>"""


def agent():
    """48x48 flat agent: red head, white eyes, two antennae."""
    return f"""<g stroke="{ALERT}" stroke-width="3" stroke-linecap="round"><path d="M16 10 L12 3"/><path d="M32 10 L36 3"/></g>
    <circle cx="24" cy="28" r="19" fill="{ALERT}"/>
    <circle cx="17" cy="26" r="5" fill="#fff"/><circle cx="31" cy="26" r="5" fill="#fff"/>
    <circle cx="18" cy="27" r="2.5" fill="{INK}"/><circle cx="32" cy="27" r="2.5" fill="{INK}"/>"""


def failed_card(i):
    kind, label, how = FAILED[i]
    x, cx = CARD_X[i], CENTERS[i]
    return f"""
  <g>
    <rect x="{x}" y="{CARD_Y}" width="{CARD_W}" height="{CARD_H}" rx="18" fill="#fff" stroke="{INK}" stroke-width="3"/>
    <rect class="hit" style="animation-name: hit{i}" x="{x + 2}" y="{CARD_Y + 2}" width="{CARD_W - 4}" height="{CARD_H - 4}" rx="16" fill="{ALERT}"/>
    {icon(kind, cx, CARD_Y + 22)}
    <text x="{cx}" y="{CARD_Y + 122}" font-size="24" font-weight="700" fill="{INK}" text-anchor="middle">{label}</text>
    <text x="{cx}" y="{CARD_Y + CARD_H + 36}" font-size="22" font-weight="700" fill="{ALERT}" text-anchor="middle">{how}</text>
  </g>"""


def arrow(i):
    x = CARD_X[i] + CARD_W
    y = CARD_Y + CARD_H // 2
    return (
        f'<path d="M{x + 6} {y} H{x + 24}" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
        f'<path d="M{x + 24} {y - 9} L{x + 35} {y} L{x + 24} {y + 9} Z" fill="{INK}"/>'
    )


def held_card(i):
    heading, detail = HELD[i]
    x = SHIELD_X[i]
    return f"""
  <g>
    <rect x="{x}" y="{SHIELD_Y}" width="{SHIELD_W}" height="{SHIELD_H}" rx="18" fill="#fff" stroke="{INK}" stroke-width="3"/>
    {shield_icon(x + 24, SHIELD_Y + 41)}
    <text x="{x + 90}" y="{SHIELD_Y + 58}" font-size="24" font-weight="700" fill="{INK}">{heading}</text>
    <text x="{x + 90}" y="{SHIELD_Y + 92}" font-size="22" fill="{MUTED}">{detail}</text>
    <g class="denied">
      <rect x="{x + SHIELD_W - 112}" y="{SHIELD_Y - 17}" width="104" height="34" rx="17" fill="{SUCCESS}"/>
      <text x="{x + SHIELD_W - 60}" y="{SHIELD_Y + 7}" font-size="20" font-weight="800" fill="#fff" text-anchor="middle">DENIED</text>
    </g>
  </g>"""


def main():
    hit_keyframes = "".join(
        f"    @keyframes hit{i} {{ 0%, {card_hit_time(i) - 2}% {{ opacity: 0; }} {card_hit_time(i)}%, 92% {{ opacity: 0.18; }} 96%, 100% {{ opacity: 0; }} }}\n"
        for i in range(4)
    )
    style = (
        """
    .march { stroke-dasharray: 14 10; animation: march 0.6s linear infinite; }
    @keyframes march { to { stroke-dashoffset: -24; } }
    .hit { opacity: 0; animation-duration: 6s; animation-iteration-count: infinite; animation-timing-function: linear; }
    .denied { animation: denied 6s linear infinite; }
    @keyframes denied { 0%, 56% { opacity: 0; } 60%, 90% { opacity: 1; } 94%, 100% { opacity: 0; } }
"""
        + hit_keyframes
        + "".join(agent_keyframes(i, smooth=True) for i in range(3))
    )
    agents = "\n  ".join(f'<g class="agent{i}">{agent()}</g>' for i in range(3))

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080" width="1080" height="1080" font-family="{FONT}">
  <!-- Generated by scripts/visuals/hf_incident_flat.py. Flat alternate of visual.svg; one 6s loop. -->
  <style>{style}  </style>
  <rect width="1080" height="1080" fill="#f7f5f0"/>

  <!-- Title -->
  <rect x="60" y="72" width="10" height="112" rx="5" fill="{ACCENT}"/>
  <text x="96" y="122" font-size="58" font-weight="800" fill="{INK}">Novel attackers.</text>
  <text x="96" y="186" font-size="58" font-weight="800" fill="{ACCENT}">Boring defenses.</text>
  <text x="96" y="236" font-size="24" fill="{MUTED}">Hugging Face agent intrusion · July 9–13, 2026</text>

  <text x="1040" y="292" font-size="22" font-weight="800" fill="{ALERT}" letter-spacing="2" text-anchor="end">WHAT FAILED</text>
  {"".join(failed_card(i) for i in range(4))}
  {"".join(arrow(i) for i in range(3))}

  <!-- Attack lane -->
  <path class="march" d="M{CENTERS[0]} {LANE_Y} H{CENTERS[3]}" stroke="{ALERT}" stroke-width="4" fill="none" opacity="0.5"/>

  <text x="1040" y="608" font-size="22" font-weight="800" fill="{SUCCESS}" letter-spacing="2" text-anchor="end">WHAT HELD</text>
  {"".join(held_card(i) for i in range(3))}

  <!-- Agent swarm -->
  {agents}

  <!-- Framework -->
  <rect x="60" y="830" width="960" height="190" rx="20" fill="{INK}"/>
  <text x="100" y="878" font-size="30" font-weight="800" fill="#fff">Draw the blast radius before an agent does</text>
  <g font-size="25" fill="#d9dce3">
    <text x="100" y="928">1. Treat datasets and configs as executable code</text>
    <text x="100" y="964">2. Kill shared admin keys; scope every credential</text>
    <text x="100" y="1000">3. Pre-stage a self-hosted model for incident response</text>
  </g>
</svg>
"""
    OUT.write_text(svg)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
