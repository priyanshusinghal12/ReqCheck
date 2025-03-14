import json
import re

def check_statistics_requirements(student_courses, degree_requirements):
    """
    Checks if a student's courses satisfy the Statistics degree requirements,
    reading requirement details from a JSON file.
    """
    satisfied_requirements = []
    missing_requirements = []
    used_courses = set()

    for requirement in degree_requirements["Requirements"]:
        requirement_name = requirement["Requirement"]
        courses = requirement["Courses"]

        if isinstance(courses, list):  # Specific courses
            satisfied = False
            for course in courses:
                if course in student_courses and course not in used_courses:
                    satisfied = True
                    used_courses.add(course)
                    break
            if satisfied:
                satisfied_requirements.append(requirement_name)
            else:
                missing_requirements.append(requirement_name)

        elif "STAT 4XX" in courses:
            stat_400_courses = {c for c in student_courses if re.search(r'\bSTAT\s4\d{2}\b', c)}
            if len(stat_400_courses) >= 2:
                satisfied_requirements.append(requirement_name)
                used_courses.update(list(stat_400_courses)[:2])
            else:
                missing_requirements.append(requirement_name)

        elif "STAT 3XX or STAT 4XX" in courses:
            stat_300_400_courses = {c for c in student_courses if re.search(r'\bSTAT\s[34]\d{2}\b', c)}
            remaining_stat_300_400 = stat_300_400_courses - used_courses
            if len(remaining_stat_300_400) >= 1:
                satisfied_requirements.append(requirement_name)
                used_courses.add(next(iter(remaining_stat_300_400)))
            else:
                missing_requirements.append(requirement_name)

        elif "STAT 4XX, CS 457, CS 485, CS 486" in courses:
            remaining_stat_400 = {c for c in student_courses if re.search(r'\bSTAT\s4\d{2}\b', c)} - used_courses
            has_advanced_cs = {"CS 457", "CS 485", "CS 486"} & set(student_courses) - used_courses
            if len(remaining_stat_400) >= 1:
                satisfied_requirements.append(requirement_name)
                used_courses.add(next(iter(remaining_stat_400)))
            elif has_advanced_cs:
                satisfied_requirements.append(requirement_name)
                used_courses.add(next(iter(has_advanced_cs)))
            else:
                missing_requirements.append(requirement_name)

        elif "ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT (300 or 400 level)" in courses:
            valid_courses = {
                c for c in student_courses
                if any(c.startswith(prefix) for prefix in ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"])
                and re.search(r'\b[34]\d{2}\b', c)
            } - used_courses
            if len(valid_courses) >= 4:
                satisfied_requirements.append(requirement_name)
                used_courses.update(list(valid_courses)[:4])
            else:
                missing_requirements.append(requirement_name)

        elif "ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT (any level)" in courses:
            valid_courses_any_level = {
                c for c in student_courses
                if any(c.startswith(prefix) for prefix in ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"])
            } - used_courses
            if len(valid_courses_any_level) >= 3:
                satisfied_requirements.append(requirement_name)
                used_courses.update(list(valid_courses_any_level)[:3])
            else:
                missing_requirements.append(requirement_name)

    return {
        "satisfied": satisfied_requirements,
        "missing": missing_requirements,
        "used_courses": list(used_courses)  # Convert set to list for JSON serialization
    }

# Load Statistics requirements
with open("../data/statistics.json", "r") as f:
    statistics_requirements = json.load(f)["Statistics_Degree_Requirements"]

# Example student course completion
student_courses = ['PMATH 333', 'CS 479', 'AFM 101', 'CS 135', 'MATH 135', 'MATH 137', 'MTHEL 99', 'STAT 444', 
                   'CS 136', 'ECON 102', 'STAT 443', 'MATH 136', 'MATH 138', 'SPCOM 223', 'CS 371',
                   'MATH 235', 'CS 231', 'CS 234', 'MATH 237', 'AMATH 250', 'BET 100', 'CLAS 104',
                   'CS 230', 'PSYCH 101', 'STAT 231', 'BET 210', 'CS 330', 'ECON 101', 'STAT 330', 'STAT 331', 
                   'STAT 341', 'STAT 332', 'STAT 333', 'CS 485', 'MTHEL 300']

# Step 2: Check Statistics Degree Requirements
statistics_results = check_statistics_requirements(student_courses, statistics_requirements)

# Print Results
print("\n=== Statistics Degree Requirements ===")
print(json.dumps(statistics_results, indent=4))
