import streamlit as st
import PyPDF2
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Works both locally and on Streamlit cloud
api_key = os.getenv("OPENROUTER_API_KEY") or st.secrets.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def analyze_resume(resume_text, job_description):
    prompt = f"""
    You are an expert resume analyzer.
    
    Analyze this resume against the job description and provide:
    1. Match Score (0-100%)
    2. Strong Skills found in resume
    3. Missing Skills the job requires
    4. Top 3 Improvements to make
    5. Overall Summary
    
    Resume:
    {resume_text}
    
    Job Description:
    {job_description}
    
    Be specific and helpful.
    """

    models = [
        "google/gemma-3-4b-it:free",
        "meta-llama/llama-3.2-3b-instruct:free",
        "mistralai/mistral-7b-instruct:free",
        "qwen/qwen-2.5-7b-instruct:free"
    ]

    response = None
    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            break
        except Exception:
            continue

    if response is None:
        return "All models are currently rate limited. Please try again in a few minutes!"

    return response.choices[0].message.content

# UI
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🤖")
st.title("🤖 AI Resume Analyzer")
st.write("Upload your resume and paste a job description to get instant AI feedback!")
password = st.text_input("Enter Password to Use App", type="password")
correct_password = os.getenv("APP_PASSWORD") or st.secrets.get("APP_PASSWORD")
if password != correct_password:
    st.warning("Please enter the correct password to continue!")
    st.stop()
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")
job_description = st.text_area("Paste Job Description Here", height=200)

if st.button("Analyze Resume"):
    if uploaded_file and job_description:
        with st.spinner("Analyzing your resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            result = analyze_resume(resume_text, job_description)
            st.success("Analysis Complete!")
            st.markdown(result)
    else:
        st.warning("Please upload a resume AND paste a job description!")
