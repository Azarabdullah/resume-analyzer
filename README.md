🤖 AI Resume Analyzer

A Streamlit-based web app that analyzes your resume against a job description using AI and provides actionable feedback.

🚀 Features
Upload PDF resume
Get match score (0–100%)
Identify strong & missing skills
Get improvement suggestions
Password-protected access

----Live Link----|   https://resume-analyzer-ugaskgdxdacfmpy6nymty8.streamlit.app/    -----------------------

-----------------------------------------------------------------------------------------------------------------------------

What it does
Paste any job description, upload your resume as a PDF, and the app returns:

Match Score — percentage fit for the role
Strong Skills — what you already have that the job wants
Missing Skills — gaps to address before applying
Top 3 Improvements — specific, actionable resume edits
Overall Summary — plain-English verdict

------------------------------------------------------------------------------------------------------------------------------
🛠️ Tech Stack

Python, Streamlit,
PyPDF2,
OpenRouter (LLMs),
dotenv

-------------------------------------------------------------------------------------------------------------------------------
Key Features

Automatic model fallback — cycles through 4 free LLM models (Gemma, LLaMA, Mistral, Qwen) to guarantee a response even when one is rate-limited
Secure API key management — credentials stored in Streamlit Secrets, never hardcoded
Password protection — prevents API abuse from public traffic
PDF text extraction — handles multi-page resumes automatically
