import json
import re

def check_math_econ_requirements(student_courses, degree_requirements):
    """
    Checks if a student's courses satisfy the Mathematical Economics
    degree requirements, including specific ECON, MATH, AMATH, PMATH, 
    STAT, CO, and general additional course requirements.
    """
    satisfied_requirements = []
    missing_requirements = []
    used_courses = set()

    for requirement in degree_requirements["Requirements"]:
        requirement_name = requirement["Requirement"]
        if isinstance(requirement["Courses"], list):  # Specific courses
            satisfied = False
            for course in requirement["Courses"]:
                if course in student_courses and course not in used_courses:
                    satisfied = True
                    used_courses.add(course)
                    break
            if satisfied:
                satisfied_requirements.append(requirement_name)
            else:
                missing_requirements.append(requirement_name)

        elif "ECON 3XX" in requirement["Courses"] or "ECON 4XX" in requirement["Courses"]:
            econ_300_400_courses = {c for c in student_courses if re.search(r'\bECON\s[34]\d{2}\b', c)}
            if len(econ_300_400_courses) >= 4:
                satisfied_requirements.append(requirement_name)
                used_courses.update(list(econ_300_400_courses)[:4])
            else:
                missing_requirements.append(requirement_name)

        elif "ACTSC" in requirement["Courses"]:
            valid_courses = {c for c in student_courses if any(c.startswith(prefix) for prefix in ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"])}
            if len(valid_courses) >= 7:
                satisfied_requirements.append(requirement_name)
                used_courses.update(list(valid_courses)[:7])
            else:
                missing_requirements.append(requirement_name)

        elif "Any course" in requirement["Courses"]:
            additional_courses = set(student_courses) - used_courses
            if len(additional_courses) >= 2:
                satisfied_requirements.append(requirement_name)
                used_courses.update(list(additional_courses)[:2])
            else:
                missing_requirements.append(requirement_name)

    return {
        "satisfied": satisfied_requirements,
        "missing": missing_requirements,
        "used_courses": list(used_courses)  # Convert to list for JSON serialization
    }

# Load Mathematical Economics requirements
with open("../data/mathEcon.json", "r") as f:
    math_econ_requirements = json.load(f)["Mathematical_Economics_Degree_Requirements"]

# Example student course completion
student_courses = [
    "ECON 101", "ECON 102", "ECON 209", "ECON 306", "ECON 391", "ECON 393", "ECON 472",
    "ECON 491", "ECON 496", "ECON 406", "ECON 308", "ECON 342", "ECON 401", "ECON 411",
    "AMATH 350", "STAT 331", "STAT 443", "PMATH 351", "CO 255", "MATH 237",
    "ACTSC 231", "CO 350", "STAT 330", "MATH 239", "CS 330", "PMATH 333", "AMATH 242",
    "ECON 201", "PHYS 121"
]

# Check Mathematical Economics Degree Requirements
math_econ_results = check_math_econ_requirements(student_courses, math_econ_requirements)

# Print Results
print("\n=== Mathematical Economics Degree Requirements ===")
print(json.dumps(math_econ_results, indent=4))
