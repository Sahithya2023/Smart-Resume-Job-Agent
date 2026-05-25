import streamlit as st
import re

from utils.parser import extract_text_from_pdf
from utils.keywords import extract_keywords
from utils.ats import calculate_ats_score
from utils.llm import tailor_resume
from utils.jobs import fetch_jobs
from utils.db import init_db, save_job, get_jobs

# ==============================
# ⚙️ CONFIG
# ==============================
st.set_page_config(page_title="AI Placement Agent", layout="wide")
st.title("📄 AI Resume Analyzer")

# Initialize DB
init_db()

# ==============================
# 🧹 CLEAN TEXT FUNCTION
# ==============================
def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

# ==============================
# 📄 RESUME ANALYZER
# ==============================
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if uploaded_file and job_description:

    st.subheader("📊 Analysis")

    resume_text = extract_text_from_pdf(uploaded_file)
    resume_text = clean_text(resume_text)
    jd_text = clean_text(job_description.lower())

    score = calculate_ats_score(resume_text, jd_text)

    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    missing = list(set(jd_keywords) - set(resume_keywords))

    col1, col2 = st.columns(2)

    with col1:
        st.metric("ATS Score", f"{score}%")

    with col2:
        st.metric("Missing Keywords", len(missing))

    st.subheader("❌ Missing Keywords")
    st.write(missing[:20])

    st.subheader("✅ Resume Keywords")
    st.write(resume_keywords[:20])

    # 🚀 Tailor Resume
    if st.button("🚀 Tailor Resume"):
        with st.spinner("Optimizing resume..."):
            improved_resume = tailor_resume(resume_text, jd_text)

            st.subheader("✨ Improved Resume")
            st.write(improved_resume)

else:
    st.info("Upload resume + job description")

# ==============================
# 🔎 JOB RECOMMENDATIONS
# ==============================
st.subheader("💼 Job Recommendations")

# Step 1: Fetch jobs
if st.button("🔎 Find Jobs"):
    with st.spinner("Fetching jobs..."):
        st.session_state.jobs_df = fetch_jobs()

# Step 2: Display jobs (IMPORTANT: outside button)
if "jobs_df" in st.session_state:
    jobs_df = st.session_state.jobs_df

    for i, row in jobs_df.iterrows():
        st.markdown(f"""
        **{row['title']}** at {row['company']}  
        📍 {row['location']}  
        🔗 [Apply Here]({row['job_url']})
        """)

        if st.button(f"✅ Apply {i}", key=f"apply_{i}"):
            job_data = {
                "title": row["title"],
                "company": row["company"],
                "location": row["location"],
                "job_url": row["job_url"]
            }

            save_job(job_data)
            st.success("Saved to Applied Jobs!")

# ==============================
# 📊 APPLIED JOBS DASHBOARD
# ==============================
st.subheader("📊 Applied Jobs")

saved_jobs = get_jobs()

if not saved_jobs:
    st.warning("No jobs applied yet")

for job in saved_jobs:
    st.markdown(f"""
    **{job[1]}** at {job[2]}  
    📍 {job[3]}  
    🔗 {job[4]}
    """)