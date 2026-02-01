from flask import Flask, render_template, request
import re
import os
from core.llm_engine import ask_llm
from agents.pro_agent import PRO_PROMPT
from agents.con_agent import CON_PROMPT
from agents.judge_agent import JUDGE_PROMPT

app = Flask(__name__)


# -------------------------------
# Utility: extract scores safely
# -------------------------------
def extract_scores(text):
    a_score = re.search(r"Agent A Score:\s*(\d+)", text)
    b_score = re.search(r"Agent B Score:\s*(\d+)", text)
    winner = re.search(r"Winner:\s*(Agent A|Agent B)", text)

    return {
        "a_score": int(a_score.group(1)) if a_score else 0,
        "b_score": int(b_score.group(1)) if b_score else 0,
        "winner": winner.group(1) if winner else "N/A"
    }


# -------------------------------
# Main Route
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    topic = None

    if request.method == "POST":
        topic = request.form.get("topic")

        # Agent A — Supporting (statement is TRUE)
        pro = ask_llm(
            PRO_PROMPT + f"\nStatement:\n{topic}"
        )

        # Agent B — Opposing (statement is FALSE)
        con = ask_llm(
            CON_PROMPT + f"\nStatement:\n{topic}"
        )

        # Judge Prompt
        judge_prompt = f"""
Statement:
{topic}

Agent A Argument:
{pro}

Agent B Argument:
{con}

{JUDGE_PROMPT}
"""

        verdict_text = ask_llm(judge_prompt)

        scores = extract_scores(verdict_text)

        result = {
            "pro": pro,
            "con": con,
            "verdict": verdict_text,
            "a_score": scores["a_score"],
            "b_score": scores["b_score"],
            "winner": scores["winner"]
        }

    return render_template(
        "index.html",
        result=result,
        topic=topic
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
