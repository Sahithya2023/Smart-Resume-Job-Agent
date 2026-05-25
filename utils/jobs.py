from jobspy import scrape_jobs
import pandas as pd

def fetch_jobs(role="AI Engineer", location="India"):
    jobs = scrape_jobs(
        site_name=["linkedin", "indeed"],
        search_term=role,
        location=location,
        results_wanted=10,
        hours_old=72
    )

    df = pd.DataFrame(jobs)

    return df[["title", "company", "location", "job_url"]]
