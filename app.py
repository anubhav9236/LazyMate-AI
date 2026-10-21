from flask import Flask, render_template, request
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"

PROMPTS = {
    "summary": "Summarize this text into simple bullet points:",
    "email": "Convert this text into a professional email:",
    "planner": "Create a prioritized daily task plan:",
    "study": "Explain this topic in simple language with an example:"
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    error = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        task = request.form.get("task", "summary")

        if not text:
            error = "Please enter some text."
        elif task not in PROMPTS:
            error = "Invalid task selected."
        else:
            try:
                response = requests.post(
                    OLLAMA_URL,
                    json={
                        "model": MODEL,
                        "prompt": f"{PROMPTS[task]}\n\n{text}",
                        "stream": False
                    },
                    timeout=180
                )
                response.raise_for_status()
                result = response.json().get("response", "")

            except requests.RequestException:
                error = "Ollama is not running or the AI model is unavailable."

    return render_template(
        "index.html",
        result=result,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)