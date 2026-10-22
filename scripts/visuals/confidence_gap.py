"""Visual for "Faculty Are Most Confident Where Students Are Least" (2026-11-11): DEC Global Survey 2026."""
from hybrid_stats import build
from people import CHECK, PROFESSOR, QUESTION, STUDENT
from pixel import ACCENT, ALERT

if __name__ == "__main__":
    build(
        slug="2026-11-11-faculty-confident-students-not",
        script="confidence_gap.py",
        lines=("Faculty: it's current.", "Students: it's not.", "Digital Education Council · Global Survey 2026"),
        cards=[(PROFESSOR, "Faculty", CHECK), (STUDENT, "Students", QUESTION)],
        section="IS THE CURRICULUM CURRENT?",
        groups=[
            {"title": "US & CANADA", "max": 100, "rows": [
                ("Faculty: content won't go stale", 58, ACCENT, "58%"),
                ("Students: program feels current", 19, ALERT, "19%"),
            ]},
            {"title": "GLOBAL", "max": 100, "rows": [
                ("Faculty: content won't go stale", 43, ACCENT, "43%"),
                ("Students: program feels current", 30, ALERT, "30%"),
            ]},
        ],
        panel=("Let the market grade the curriculum", [
            "Ask students and employers every term",
            "Rewrite one assessment per course for AI-era work",
            "Publish what changed",
        ]),
        bar_x=470, bar_max=420,
    )
