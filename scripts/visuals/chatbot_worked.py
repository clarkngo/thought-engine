"""Visual for "The Chatbot Worked. The Outcomes Didn't Move." (2026-11-02): Mata, Russell & Page (2026), EdWorkingPaper 26-1409.

Registration: control 31.5%, effect +34.2 points (Table 3, n = 621). Graduation: control 19.0%, effect +0.4 points, not significant.
"""
from handoff import ROBOT
from hybrid_stats import build
from people import CHECK, PROFESSOR, QUESTION, STUDENT
from pixel import ACCENT, ALERT, SUCCESS

GRAY = "#9aa1ad"

if __name__ == "__main__":
    build(
        slug="2026-11-02-chatbot-worked-outcomes-didnt-move",
        script="chatbot_worked.py",
        lines=("The chatbot worked.", "The outcomes didn't move.", "Randomized trial · 8,708 students · four years · Cal State Northridge"),
        cards=[(ROBOT, "Reminder sent", CHECK), (STUDENT, "Registered", CHECK), (PROFESSOR, "Time reinvested?", QUESTION)],
        section="REGISTERED ON TIME (STUDENTS NOT YET ENROLLED)",
        groups=[
            {"title": None, "max": 100, "rows": [
                ("No reminder", 32, GRAY, "32%"),
                ("Chatbot reminder", 66, SUCCESS, "66%"),
            ]},
            {"title": "GRADUATED IN FOUR YEARS", "max": 100, "rows": [
                ("No chatbot", 19.0, GRAY, "19.0%"),
                ("Chatbot", 19.4, ALERT, "19.4%"),
            ]},
        ],
        caption="Graduation difference not statistically significant",
        panel=("Freed time is not reinvested time", [
            "Automate the deadline",
            "Decide where the hours go first",
            "Measure outcomes, not messages",
        ]),
    )
