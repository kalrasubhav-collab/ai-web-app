import os
from flask import Flask, render_template, request, jsonify
import anthropic

app = Flask(__name__)

SYSTEM_PROMPTS = {
    "coding": "You are an expert programmer who writes clean, efficient, and well-documented code. You help users with coding tasks, debug issues, and explain technical concepts clearly.",
    "writing": "You are a writing coach who helps improve writing style and clarity. You offer constructive feedback on tone, structure, grammar, and word choice while preserving the author's voice.",
    "socratic": "You are a Socratic teacher. You never give direct answers. Instead, you guide students to discover answers themselves by asking thoughtful, probing questions that build understanding step by step.",
    "general": "You are a helpful assistant.",
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Message is required."}), 400

    role = request.json.get("role", "general")
    system_prompt = SYSTEM_PROMPTS.get(role, SYSTEM_PROMPTS["general"])

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return jsonify({"error": "ANTHROPIC_API_KEY is not set."}), 500

    try:
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        reply = response.content[0].text
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
