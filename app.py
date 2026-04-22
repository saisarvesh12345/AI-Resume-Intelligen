import streamlit as st
from parser.pdf_parser import extract_text_from_pdf
from nlp.skill_extractor import extract_skills
from nlp.domain_detector import detect_domain
from ats.ats_score import ats_score

st.title("AI Resume Intelligence System 🚀")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])
jd = st.text_area("Enter Job Description")

def extract_jd_skills(jd):
    jd = jd.lower()

    skills_db = [
        "python", "java", "machine learning", "data science",
        "sql", "html", "css", "javascript"
    ]

    skills = []
    for skill in skills_db:
        if skill in jd:
            skills.append(skill)

    return skills

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    skills = extract_skills(text)
    domain = detect_domain(skills)

    st.subheader("Extracted Skills")
    st.write(skills)

    st.subheader("Detected Domain")
    st.write(domain)

    if jd:
        jd_skills = extract_jd_skills(jd)

        match = len(set(skills) & set(jd_skills))
        total = len(jd_skills)
        match_score = int((match / total) * 100) if total > 0 else 0

        ats = ats_score(skills, jd_skills, text)
        missing = list(set(jd_skills) - set(skills))

        st.subheader("Match Score")
        st.write(f"{match_score}%")

        st.subheader("ATS Score")
        st.write(f"{ats}%")

        st.subheader("Missing Skills")
        st.success(", ".join(missing) if missing else "None 🎉")