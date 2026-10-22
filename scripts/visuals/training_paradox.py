"""Visual for "The Training Paradox" (2026-11-09): DEC AI in Higher Education Global Survey 2026."""
from hybrid_stats import build
from people import CERT, PROFESSOR, QUESTION, STUDENT
from pixel import ACCENT, ALERT

if __name__ == "__main__":
    build(
        slug="2026-11-09-the-training-paradox",
        script="training_paradox.py",
        lines=("Trained.", "Not ready.", "Digital Education Council · Global Survey 2026"),
        cards=[(PROFESSOR, "Faculty", CERT), (STUDENT, "Students", QUESTION)],
        section="THE GAP",
        groups=[{"title": None, "max": 100, "rows": [
            ("Faculty trained in AI literacy", 64, ACCENT, "64%"),
            ("Students: faculty can guide them", 29, ALERT, "29%"),
            ("Same, US & Canada", 17, ALERT, "17%"),
        ]}],
        caption="45,398 responses from students and faculty in 35 countries",
        panel=("Readiness is what students can see", [
            "Put an AI policy on every assignment",
            "Train for course redesign, not tool tours",
            "Show students how you use AI yourself",
        ]),
        bar_x=470, bar_max=420,
    )
