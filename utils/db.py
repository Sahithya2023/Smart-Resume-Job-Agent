import sqlite3


# ==========================
# Create DB
# ==========================
def init_db():

    conn = sqlite3.connect("jobs.db")

    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS jobs(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT,

        company TEXT,

        location TEXT,

        job_url TEXT,

        status TEXT
    )
    """)

    conn.commit()

    conn.close()


# ==========================
# Save Job
# ==========================
def save_job(job):

    conn = sqlite3.connect("jobs.db")

    c = conn.cursor()

    c.execute("""
    INSERT INTO jobs
    (
    title,
    company,
    location,
    job_url,
    status
    )

    VALUES(?,?,?,?,?)
    """,

    (
        job["title"],
        job["company"],
        job["location"],
        job["job_url"],
        "Applied"
    ))

    conn.commit()

    conn.close()


# ==========================
# Get Jobs
# ==========================
def get_jobs():

    conn = sqlite3.connect("jobs.db")

    c = conn.cursor()

    c.execute("SELECT * FROM jobs")

    rows = c.fetchall()

    conn.close()

    return rows