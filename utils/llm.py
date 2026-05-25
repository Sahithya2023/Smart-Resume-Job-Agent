from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def tailor_resume(resume_text, jd_text):
    prompt = f"""
    You are an expert resume optimizer.

    Improve the following resume based on the job description.

    Resume:
    {resume_text}

    Job Description:
    {jd_text}

    Make it ATS-friendly, add missing keywords naturally, and improve clarity.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text