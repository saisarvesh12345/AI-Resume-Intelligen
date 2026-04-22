import spacy

nlp = spacy.load("en_core_web_sm")

skills_db = [
    "python", "java", "machine learning", "data science",
    "autocad", "excel",

    # Add these (VERY IMPORTANT)
    "software development", "technical support",
    "systems design", "troubleshooting",
    "project management", "operations management",
    "customer relations", "quality management"
]

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return list(set(found))