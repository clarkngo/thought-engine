"""Visual for "Same AI. Opposite Results." (2026-11-02): Bastani et al. (PNAS 2025) vs Kestin et al. (Sci. Reports 2025)."""
from hybrid_stats import build
from people import ANSWER, STEPS, STUDENT
from pixel import ACCENT, ALERT

GRAY = "#9aa1ad"

if __name__ == "__main__":
    build(
        slug="2026-11-02-same-ai-opposite-results",
        script="same_ai_opposite.py",
        lines=("Same AI.", "Opposite results.", "Two randomized trials · PNAS 2025 · Scientific Reports 2025"),
        cards=[(STUDENT, "Unguarded AI", ANSWER), (STUDENT, "Structured tutor", STEPS)],
        section="THE TWO TRIALS",
        groups=[
            {"title": "EXAM SCORE · HIGH SCHOOL MATH (PNAS)", "max": 100, "rows": [
                ("No AI", 100, GRAY, "baseline"),
                ("Unguarded assistant", 83, ALERT, "−17%"),
            ]},
            {"title": "MEDIAN LEARNING GAIN · HARVARD PHYSICS", "max": 1.75, "rows": [
                ("In-class active learning", 0.75, GRAY, "baseline"),
                ("Structured AI tutor", 1.75, ACCENT, "over 2×"),
            ]},
        ],
        panel=("Design decides the direction", [
            "Sequence the work: one step at a time",
            "Write the expert prompts and answers yourself",
            "Measure learning without the AI",
        ]),
    )
