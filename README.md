# 🤖 AI Resume Analyzer

> **Paste a job description. Upload your resume. Get instant, actionable AI feedback in seconds.**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://resume-analyzer-ugaskgdxdacfmpy6nymty8.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## ✨ What It Does

The AI Resume Analyzer compares your resume against any job description and returns a structured, actionable report — no signup, no fluff.

| Output | Description |
|---|---|
| 📊 **Match Score** | 0–100% fit rating for the role |
| ✅ **Strong Skills** | What you already have that the job wants |
| ❌ **Missing Skills** | Gaps to close before applying |
| 🛠️ **Top 3 Improvements** | Specific, concrete resume edits |
| 📝 **Overall Summary** | Plain-English verdict on your candidacy |

---

## 🚀 Quick Start

### Try the live app

👉 [resume-analyzer-ugaskgdxdacfmpy6nymty8.streamlit.app](https://resume-analyzer-ugaskgdxdacfmpy6nymty8.streamlit.app/)

**Demo password:** `Azardev7890`

### Run locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables
cp .env.example .env
# Add your OPENROUTER_API_KEY and APP_PASSWORD to .env

# 4. Launch
streamlit run app.py
```

---

## ⚙️ Configuration

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_key_here
APP_PASSWORD=your_chosen_password_here
```

For Streamlit Cloud deployment, add these same keys under **Settings → Secrets**.

Get a free OpenRouter API key at [openrouter.ai](https://openrouter.ai).

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit |
| **PDF Parsing** | PyPDF2 |
| **AI Backend** | OpenRouter API (multi-model) |
| **HTTP Client** | OpenAI Python SDK |
| **Config** | python-dotenv + Streamlit Secrets |

---

## 🔁 How the AI Model Fallback Works

One of the core reliability features: the app cycles through **4 free LLMs** automatically if any one is rate-limited.

```
Request comes in
      │
      ▼
 Gemma 3 4B  ──(fail)──▶  LLaMA 3.2 3B  ──(fail)──▶  Mistral 7B  ──(fail)──▶  Qwen 2.5 7B
      │                         │                          │                          │
   (success)                (success)                  (success)                  (success)
      │                         │                          │                          │
      └─────────────────────────┴──────────────────────────┴──────────────┬───────────┘
                                                                           ▼
                                                                    Return analysis
```

This means you almost always get a response, even during peak usage hours — no paid API key required.

---

## 📁 Project Structure

```
ai-resume-analyzer/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── .gitignore
└── README.md
```

---

## 🔒 Security

- **Password protection** — prevents API abuse from public traffic
- **No hardcoded secrets** — all credentials stored in `.env` or Streamlit Secrets
- **No data retention** — resumes are processed in memory only and never stored

---

## 📦 Requirements

```
streamlit
PyPDF2
openai
python-dotenv
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Here are a few ideas to get started:

- Add support for DOCX resume uploads
- Export the analysis as a PDF report
- Add a comparison mode (multiple job descriptions vs. one resume)
- Improve section parsing with structured JSON output

To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes and open a pull request

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<p align="center">Built by <a href="https://github.com/your-username">Azardev</a> · Powered by <a href="https://openrouter.ai">OpenRouter</a> · Deployed on <a href="https://streamlit.io/cloud">Streamlit Cloud</a></p>
