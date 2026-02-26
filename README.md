# AI Chat — Your Personal AI Assistant

A web-based AI chatbot with 4 distinct personalities, each specialized 
for different tasks. Built with Python, Flask, and the Anthropic Claude API.

## What it does

Chat with Claude AI through a clean browser interface. Switch between 
4 personalities depending on what you need help with:

- 🧑‍💻 **Coding Assistant** — writes clean code and solves programming problems
- ✍️ **Writing Coach** — improves your writing style and clarity
- 🧠 **Socratic Teacher** — teaches by asking questions, helping you think deeper
- 💬 **General Assistant** — everyday questions and tasks

Each personality has full conversation memory — Claude remembers 
everything said in the session. Switching roles starts a fresh conversation.

## Built with

- Python 3
- Flask
- Anthropic Claude API (claude-haiku-4-5-20251001)

## How to run

1. Clone the repo:
   git clone https://github.com/kalrasubhav-collab/ai-web-app.git
   cd ai-web-app

2. Install dependencies:
   pip install -r requirements.txt

3. Add your Anthropic API key:
   export ANTHROPIC_API_KEY="your-key-here"

4. Run the app:
   python app.py

5. Open your browser at:
   http://127.0.0.1:5000

## What I learned building this

- Building web apps with Flask
- Calling the Anthropic Claude API from Python
- Managing conversation history and context
- Building and iterating on a real product with Claude Code
