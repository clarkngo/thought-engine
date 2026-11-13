"""Visual for "Pilots Don't Learn on the 737" (2026-11-18). Source: 14 CFR 121.434 and Appendix H to Part 121.

Layout: stage flow, two rows. Pilots: simulator, then real flights with a check pilot, then consolidation on the line.
Graduates: AI simulator, then a missing stage (no check pilot), then the first job. A highlight walks each row;
the pilots' reaches the end, the graduates' stalls at the gap. No takeaway panel.
"""
from pathlib import Path

from handoff import ROBOT
from people import PROFESSOR, STUDENT
from pixel import ACCENT, ALERT, INK, SUCCESS, document, sprite, title
from sim_sprites import PLANE, SIM
from start_small import BAG

OUT = Path(__file__).resolve().parents[2] / "content/posts/2026-11-18-pilots-dont-learn-on-the-737/visual.svg"
GRAY = "#5d6470"
CARD_W, CARD_H, GAP = 280, 200, 60
XS = [60 + i * (CARD_W + GAP) for i in range(3)]
ROW_PILOT, ROW_GRAD = 304, 594

STYLE = f"""    .walk {{ animation: walk 6s steps(1) infinite; }}
    @keyframes walk {{ 0% {{ transform: translateX(0); }} 33% {{ transform: translateX({CARD_W + GAP}px); }} 66% {{ transform: translateX({2 * (CARD_W + GAP)}px); }} }}
    .stall {{ animation: stall 6s steps(1) infinite; }}
    @keyframes stall {{ 0% {{ transform: translateX(0); }} 33% {{ transform: translateX({CARD_W + GAP}px); }} }}
    .blink {{ animation: blink 1s steps(1) infinite; }}
    @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.2; }} }}
"""


def card(x, y, art, art_px, art_w, name, detail, color=INK):
    return f"""
  <rect x="{x + 8}" y="{y + 8}" width="{CARD_W}" height="{CARD_H}" fill="{INK}"/>
  <rect x="{x}" y="{y}" width="{CARD_W}" height="{CARD_H}" fill="#fff" stroke="{INK}" stroke-width="4"/>
  {sprite(art, x + (CARD_W - art_w) // 2, y + 24, art_px)}
  <text x="{x + CARD_W // 2}" y="{y + 144}" font-size="30" font-weight="800" fill="{color}" text-anchor="middle">{name}</text>
  <text x="{x + CARD_W // 2}" y="{y + 180}" font-size="22" fill="{GRAY}" text-anchor="middle">{detail}</text>"""


def arrows(y):
    out = ""
    for x in XS[:2]:
        ax = x + CARD_W + 14
        out += f'\n  <rect x="{ax}" y="{y + CARD_H // 2 - 4}" width="24" height="8" fill="{INK}"/>'
        out += "".join(
            f'<rect x="{ax + 24 + i * 6}" y="{y + CARD_H // 2 - 4 - (2 - i) * 6}" width="6" height="{8 + (2 - i) * 12}" fill="{INK}"/>'
            for i in range(3)
        )
    return out


def main():
    body = title("Simulator first.", "Then a check pilot.", "What U.S. airline rules require after simulator training")

    body += f'\n  <text x="60" y="{ROW_PILOT - 18}" font-size="24" font-weight="800" fill="{GRAY}" letter-spacing="2">AIRLINE PILOTS</text>'
    body += card(XS[0], ROW_PILOT, SIM, 6, 72, "Simulator", "Train and pass checks")
    body += f"""
  <rect x="{XS[1] + 8}" y="{ROW_PILOT + 8}" width="{CARD_W}" height="{CARD_H}" fill="{INK}"/>
  <rect x="{XS[1]}" y="{ROW_PILOT}" width="{CARD_W}" height="{CARD_H}" fill="#fff" stroke="{INK}" stroke-width="4"/>
  {sprite(PLANE, XS[1] + 40, ROW_PILOT + 40, 6)}
  {sprite(PROFESSOR, XS[1] + 168, ROW_PILOT + 24, 6)}
  <text x="{XS[1] + CARD_W // 2}" y="{ROW_PILOT + 144}" font-size="30" font-weight="800" fill="{INK}" text-anchor="middle">Real flights</text>
  <text x="{XS[1] + CARD_W // 2}" y="{ROW_PILOT + 180}" font-size="22" fill="{GRAY}" text-anchor="middle">25 hrs with a check pilot</text>"""
    body += card(XS[2], ROW_PILOT, PLANE, 6, 90, "On the line", "100 hrs within 120 days")
    body += arrows(ROW_PILOT)
    body += f'\n  <rect class="walk" x="{XS[0] - 10}" y="{ROW_PILOT - 10}" width="{CARD_W + 20}" height="{CARD_H + 20}" fill="none" stroke="{ACCENT}" stroke-width="8"/>'

    body += f'\n  <text x="60" y="{ROW_GRAD - 18}" font-size="24" font-weight="800" fill="{GRAY}" letter-spacing="2">GRADUATES</text>'
    body += card(XS[0], ROW_GRAD, ROBOT, 6, 72, "AI simulator", "Practice with feedback")
    body += f"""
  <rect x="{XS[1]}" y="{ROW_GRAD}" width="{CARD_W}" height="{CARD_H}" fill="none" stroke="{ALERT}" stroke-width="4" stroke-dasharray="14 10"/>
  <text class="blink" x="{XS[1] + CARD_W // 2}" y="{ROW_GRAD + 92}" font-size="64" font-weight="800" fill="{ALERT}" text-anchor="middle">?</text>
  <text x="{XS[1] + CARD_W // 2}" y="{ROW_GRAD + 144}" font-size="30" font-weight="800" fill="{ALERT}" text-anchor="middle">Who's the</text>
  <text x="{XS[1] + CARD_W // 2}" y="{ROW_GRAD + 180}" font-size="30" font-weight="800" fill="{ALERT}" text-anchor="middle">check pilot?</text>"""
    body += card(XS[2], ROW_GRAD, BAG, 6, 60, "First job", "On your own")
    body += arrows(ROW_GRAD)
    body += f'\n  <rect class="stall" x="{XS[0] - 10}" y="{ROW_GRAD - 10}" width="{CARD_W + 20}" height="{CARD_H + 20}" fill="none" stroke="{ALERT}" stroke-width="8"/>'

    body += f"""
  <text x="60" y="878" font-size="36" font-weight="800" fill="{INK}">Pilots never go from simulator to solo.</text>
  <text x="60" y="926" font-size="36" font-weight="800" fill="{ACCENT}">Who flies beside our graduates?</text>
  <text x="60" y="1004" font-size="22" fill="{GRAY}">14 CFR 121.434: turbojet initial training. Appendix H bars simulator credit for this stage.</text>
  <text x="60" y="1036" font-size="22" fill="{GRAY}">Simplified; details vary by training program.</text>"""

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(document(body, STYLE, "Generated by scripts/visuals/check_pilot.py. One 6s loop."))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
