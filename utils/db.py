import sqlite3

def init_db():
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            job_url TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_job(job):
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()

    c.execute("""
        INSERT INTO jobs (title, company, location, job_url)
        VALUES (?, ?, ?, ?)
    """, (job["title"], job["company"], job["location"], job["job_url"]))

    conn.commit()
    conn.close()

def get_jobs():
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()

    c.execute("SELECT * FROM jobs")   # ✅ FIXED
    rows = c.fetchall()

    conn.close()
    return rows