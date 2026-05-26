# 🤖 Smart Resume Job Agent

An AI-powered career assistant that helps users optimize resumes, discover relevant jobs, generate personalized application emails, and track applications in one workflow.

---

## 🚀 Features

### 📄 ATS Resume Analyzer
- Upload resume (PDF)
- Calculate ATS compatibility score
- Detect missing keywords

### ✨ AI Resume Tailoring
- Optimize resume using LLMs
- Align resume with job descriptions
- Improve recruiter visibility

### 💼 Job Recommendation Engine
- Fetch real-time job opportunities
- Generate direct apply links
- Calculate resume–job match score

### 📧 AI Application Email Generator
- Generate personalized application emails
- Uses resume + role + company context

### 📊 Application Tracker
- Save applied jobs
- Track application status
- Export applications as CSV

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Database | SQLite |
| AI | Gemini API |
| Data Processing | Pandas |
| Job Fetching | JobSpy |

---

## 📂 Project Structure

```plaintext
Smart-Resume-Job-Agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
└── utils/
    ├── parser.py
    ├── keywords.py
    ├── ats.py
    ├── llm.py
    ├── jobs.py
    ├── db.py
    ├── matcher.py
    └── emailgenerator.py
```

---

## ▶️ Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔮 Future Roadmap

### Phase 1 — User Personalization
- User account creation
- Email / GitHub / LinkedIn login
- Resume storage
- Profile management

### Phase 2 — Career Intelligence
- Preferred roles & location setup
- AI-based job ranking
- Personalized recommendations

### Phase 3 — Agentic Workflow
- One-click apply pipeline
- Application timeline
- Interview preparation assistant
- Mock interview generator

### Phase 4 — Analytics
- Application success dashboard
- Resume performance insights
- Skill gap analysis

---

## 🎯 Goal

Build an end-to-end AI placement assistant that supports students from resume creation to job application tracking.
