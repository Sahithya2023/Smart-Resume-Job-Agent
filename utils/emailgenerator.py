from utils.llm import client


def generate_email(
    role,
    company,
    resume,
    skills
):

    prompt = f"""
You are a recruiter and career coach.

Write a highly personalized application email.

Job Role:
{role}

Company:
{company}

Candidate Resume:
{resume}

Skills:
{skills}

Rules:
- Mention company naturally
- Mention 2–3 relevant skills
- Explain WHY candidate fits
- Avoid generic phrases
- Sound human
- 120–180 words
- Professional tone

Return only email.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception:

        skill_text = ", ".join(skills[:5])

        return f"""
Subject: Application for {role}

Dear Hiring Team,

I was excited to come across the opportunity for the {role} role at {company}.

Through my experience working with {skill_text}, I have developed practical problem-solving and technical capabilities that align with this position.

I would welcome the opportunity to contribute and continue learning while creating meaningful impact.

Thank you for your consideration.

Best Regards
"""