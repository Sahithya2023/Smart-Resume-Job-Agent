def calculate_match(resume_keywords, job_title):

    resume = set([x.lower() for x in resume_keywords])

    words = set(job_title.lower().split())

    if len(resume) == 0:
        return 0

    score = (
        len(resume.intersection(words))
        / len(resume)
    ) * 100

    return round(score, 2)