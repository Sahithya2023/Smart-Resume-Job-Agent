import streamlit as st
import re
import pandas as pd

from utils.parser import extract_text_from_pdf
from utils.keywords import extract_keywords
from utils.ats import calculate_ats_score
from utils.llm import tailor_resume
from utils.jobs import fetch_jobs
from utils.db import init_db, save_job, get_jobs
from utils.matcher import calculate_match
from utils.emailgenerator import generate_email


# ==============================
# ⚙️ CONFIG
# ==============================
st.set_page_config(
    page_title="Smart Resume Job Agent",
    layout="wide"
)

st.title("🤖 Smart Resume Job Agent")

# Initialize Database
init_db()


# ==============================
# 🧹 CLEAN TEXT
# ==============================
def clean_text(text):
    return re.sub(r"[^a-zA-Z0-9\s]", " ", text)


# ==============================
# 📄 RESUME ANALYZER
# ==============================
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

resume_keywords = []

if uploaded_file and job_description:

    st.subheader("📊 Resume Analysis")

    resume_text = extract_text_from_pdf(uploaded_file)

    resume_text = clean_text(resume_text)

    jd_text = clean_text(
        job_description.lower()
    )

    score = calculate_ats_score(
        resume_text,
        jd_text
    )

    resume_keywords = extract_keywords(
        resume_text
    )

    jd_keywords = extract_keywords(
        jd_text
    )

    missing = list(
        set(jd_keywords)
        -
        set(resume_keywords)
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "ATS Score",
            f"{score}%"
        )

    with col2:
        st.metric(
            "Missing Keywords",
            len(missing)
        )

    st.subheader("❌ Missing Keywords")
    st.write(missing[:20])

    st.subheader("✅ Resume Keywords")
    st.write(resume_keywords[:20])

    # Tailor Resume
    if st.button("🚀 Tailor Resume"):

        with st.spinner(
            "Optimizing Resume..."
        ):

            improved = tailor_resume(
                resume_text,
                jd_text
            )

            st.subheader(
                "✨ Improved Resume"
            )

            st.write(improved)

else:
    st.info(
        "Upload Resume + Job Description"
    )


# ==============================
# 💼 JOB RECOMMENDATIONS
# ==============================
st.subheader("💼 Job Recommendations")

if st.button("🔎 Find Jobs"):

    with st.spinner(
        "Fetching Jobs..."
    ):

        st.session_state.jobs_df = fetch_jobs()


if "jobs_df" in st.session_state:

    jobs_df = st.session_state.jobs_df

    for i, row in jobs_df.iterrows():

        match = calculate_match(
            resume_keywords,
            row["title"]
        )

        st.markdown(f"""
### {row['title']}

🏢 {row['company']}

📍 {row['location']}

🎯 Match Score: {match}%

🔗 [Apply Here]({row['job_url']})
""")

        # APPLY BUTTON
        if st.button(
            f"✅ Apply {i}",
            key=f"apply_{i}"
        ):

            save_job(
                {
                    "title": row["title"],
                    "company": row["company"],
                    "location": row["location"],
                    "job_url": row["job_url"]
                }
            )

            st.success(
                "Saved to Applied Jobs!"
            )

        # EMAIL BUTTON
        if st.button(
            f"📧 Generate Email {i}",
            key=f"email_{i}"
        ):

            email = generate_email(
                row["title"],
                row["company"],
                resume_text if uploaded_file else "",
                 resume_keywords
            )

            st.subheader("📧 Personalized Application Email")
            st.write(email)

        st.divider()


# ==============================
# 📊 APPLIED JOBS
# ==============================
st.subheader("📊 Applied Jobs")

saved_jobs = get_jobs()

if not saved_jobs:

    st.warning(
        "No jobs applied yet"
    )

else:

    for job in saved_jobs:

        st.markdown(f"""
### {job[1]}

🏢 {job[2]}

📍 {job[3]}

🟢 Status:
{job[5]}
""")

    # ==============================
    # ⬇ EXPORT CSV
    # ==============================

    df = pd.DataFrame(

        saved_jobs,

        columns=[
            "ID",
            "Title",
            "Company",
            "Location",
            "URL",
            "Status"
        ]
    )

    st.download_button(
        label="⬇ Export Applications",
        data=df.to_csv(
            index=False
        ),
        file_name="applications.csv",
        mime="text/csv"
    )
