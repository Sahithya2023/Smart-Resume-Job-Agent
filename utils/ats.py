from sklearn.feature_extraction.text import CountVectorizer

def calculate_ats_score(resume, jd):
    vectorizer = CountVectorizer().fit([resume, jd])
    vectors = vectorizer.transform([resume, jd]).toarray()

    resume_vector = vectors[0]
    jd_vector = vectors[1]

    match = sum((resume_vector > 0) & (jd_vector > 0))
    total = sum(jd_vector > 0)

    score = (match / total) * 100 if total != 0 else 0
    return round(score, 2)