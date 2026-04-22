def ats_score(skills, jd_skills, text):
    match = len(set(skills) & set(jd_skills))
    total = len(jd_skills)

    skill_score = (match / total) * 100 if total > 0 else 0

    # Bonus: resume length
    length_score = 20 if len(text) > 1000 else 10

    # Final ATS score
    final_score = int((0.7 * skill_score) + (0.3 * length_score))

    return final_score