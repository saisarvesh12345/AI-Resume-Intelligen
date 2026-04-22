def detect_domain(skills):
    if "python" in skills or "machine learning" in skills:
        return "CSE/AIML"
    elif "autocad" in skills:
        return "Mechanical"
    elif "excel" in skills:
        return "MBA"
    else:
        return "General"