from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

OLLAMA_URL = "https://ollama.com/api/chat"
MODEL = "gpt-oss:120b-cloud"

PROMPTS = {
    "summary": "Summarize the following text into simple bullet points:",
    "email": "Convert the following text into a professional email:",
    "planner": "Create a prioritized daily task plan from the following text:",
    "study": "Explain the following topic in simple language with an example:"
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
            api_key = os.environ.get("OLLAMA_API_KEY")

            if not api_key:
                error = "AI service is not configured. Please try again later."

            else:
                try:
                    response = requests.post(
                        OLLAMA_URL,
                        headers={
                            "Authorization": f"Bearer {api_key}",
                            "Content-Type": "application/json"
                        },
                        json={
                            "model": MODEL,
                            "messages": [
                                {
                                    "role": "user",
                                    "content": (
                                        f"{PROMPTS[task]}\n\n{text}"
                                    )
                                }
                            ],
                            "stream": False
                        },
                        timeout=180
                    )

                    response.raise_for_status()

                    data = response.json()
                    result = data.get("message", {}).get("content", "")

                    if not result:
                        error = "The AI returned an empty response."

                except requests.Timeout:
                    error = "The AI request timed out. Please try again."

                except requests.RequestException:
                    error = (
                        "Unable to connect to the AI service. "
                        "Please try again later."
                    )

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)