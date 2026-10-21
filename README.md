🦥 LazyDesk AI
Slow down. Let your local AI handle the busywork.

LazyDesk AI is a local-first file organization assistant built for people who want to spend less time managing documents and more time doing what matters.

Using an open-weight AI model through Ollama, LazyDesk analyzes text and Markdown files, summarizes their contents, suggests categories and filenames, and helps users organize files after they approve the suggested actions.

✨ Features
AI-powered summaries: Turn long notes into short, useful summaries.
Smart categorization: Suggest categories such as Study, Work, Finance, Personal, and Other.
Filename suggestions: Generate clearer, more descriptive filenames.
Batch processing: Analyze multiple documents in one session.
Review before action: Approve file moves before the app changes their location.
CSV reports: Download analysis results for later reference.
Local inference: Run AI through Ollama on your own computer without a cloud AI API.
🎯 The Problem

Digital clutter builds up because organizing files takes time and attention. People often postpone sorting their notes, meeting records, study material, and personal documents.

LazyDesk reduces this repetitive work by turning documents into summaries and actionable organization suggestions.

🧠 How It Works
The user selects a local folder containing .txt or .md files.
LazyDesk reads supported documents from that folder.
Ollama sends each document to the locally running language model for analysis.
The app displays summaries, categories, suggested filenames, and next steps.
The user reviews the results and approves any file moves.
Approved files are organized into category folders, and the user can download a CSV report.
🛠️ Tech Stack
Python — application logic
Streamlit — web interface
Ollama — local model runtime
Qwen2.5-Coder 1.5B — open-weight language model
Requests — communication with the local Ollama API
💻 Requirements
Windows 10 or later
Python 3
Ollama installed
An internet connection for initial installation and model download
Enough available memory and disk space to run the selected model
🚀 Installation and Setup
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd LazyDesk


Replace YOUR_GITHUB_REPOSITORY_URL with your actual repository URL.

2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Download the AI model
ollama pull qwen2.5-coder:1.5b

5. Run LazyDesk
python -m streamlit run app.py


Open the local URL displayed in the terminal, usually:

http://localhost:8501

🔒 Privacy and Open Innovation

LazyDesk is designed around local inference rather than a hosted AI API.

Document analysis requests are sent to the local Ollama service.
After the model and dependencies are downloaded, inference can work without an internet connection.
Users can inspect and modify the source code.
The model can be replaced with another compatible Ollama model by changing the configuration.
No cloud AI subscription is required to run local inference.

Local execution gives users more control over their documents and AI workflow. Actual privacy depends on the runtime, system configuration, and any other software installed on the machine.

🌱 Why Slow and Steady?

Small, repetitive tasks are easy to postpone. LazyDesk helps users make progress on digital clutter without manually opening and sorting every document.

The goal is simple: let AI handle the tedious first pass while keeping important decisions in the user's hands.

🧪 Demo

Add your own screenshots here after testing the application.

screenshots/dashboard.png — application interface
screenshots/analysis-results.png — summaries and categories
screenshots/organized-folders.png — resulting folder structure
🗺️ Roadmap
Support for additional document formats
Better duplicate-file detection
Configurable category rules
File organization history and undo support
Improved model selection and resource usage
