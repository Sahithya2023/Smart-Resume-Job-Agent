# 🤖 Smart-Resume-Job-Agent

An intelligent AI-powered system that helps students optimize resumes, discover job opportunities, and track applications efficiently.

---

## 🚀 Features

- 📄 **ATS Resume Analyzer**
  - Calculates ATS score
  - Identifies missing keywords

- 🔎 **Job Recommendation System**
  - Fetches real-time job listings
  - Provides direct apply links

- 💾 **Applied Jobs Tracker**
  - Save and manage applied jobs
  - Persistent storage using SQLite

- ✨ **AI Resume Tailoring**
  - Enhances resume based on job description
  - Improves keyword matching

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Database:** SQLite  
- **AI/NLP:** Custom keyword extraction + LLM integration  

---

## 📂 Project Structure
ai-placement-agent/
│── app.py
│── utils/
│ ├── parser.py
│ ├── keywords.py
│ ├── ats.py
│ ├── llm.py
│ ├── jobs.py
│ ├── db.py
│── requirements.txt
│── README.md


---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
