import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Read API key
API_KEY = os.getenv("GOOGLE_API_KEY")

# Create client
client = genai.Client(
    api_key=API_KEY
)


def tailor_resume(resume, jd):

    prompt = f"""
You are an ATS resume optimization assistant.

Improve the resume according to the job description.

Resume:
{resume}

Job Description:
{jd}

Instructions:
- Improve wording
- Add relevant keywords naturally
- Preserve truthfulness
- Make resume ATS friendly
- Keep professional formatting

Return improved resume only.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"""
⚠ Resume generation failed

Error:
{str(e)}

Possible reasons:
• Gemini temporarily overloaded
• API limit reached
• Invalid API key
"""