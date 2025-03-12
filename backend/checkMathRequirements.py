import json

def check_math_requirements(student_courses, degree_requirements):
    """
    Checks if a student's courses satisfy the Mathematics degree requirements.
    """
    satisfied_requirements = []
    missing_requirements = []
    used_courses = set()

    for requirement_group in degree_requirements["Requirements"]:
        satisfied = False
        for course in requirement_group:
            if course in student_courses:
                satisfied = True
                used_courses.add(course)  # Track used courses
                break
        
        if satisfied:
            satisfied_requirements.append(requirement_group)
        else:
            missing_requirements.append(requirement_group)

    return {
        "satisfied": satisfied_requirements,
        "missing": missing_requirements
    }

# Load Mathematics requirements
with open("./data/mathDegreeRequirements.json", "r") as f:
    math_requirements = json.load(f)["Mathematics_Degree_Requirements"]

# Example student course completion
student_courses = ['PMATH 333', 'CS 479', 'AFM 101', 'CS 135', 'MATH 135', 
                   'MATH 137', 'MTHEL 99', 'STAT 444', 'CS 136', 'CS 136L',
                   'ECON 102', 'STAT 443', 'MATH 136', 'MATH 138', 'SPCOM 223',
                   'CS 371', 'CS 486', 'MATH 235', 'CS 231', 'CS 234', 'MATH 237',
                   'PD 1', 'STAT 230', 'COOP 1', 'PD 11', 'AMATH 250', 'BET 100', 
                   'CLAS 104', 'CS 230', 'PSYCH 101', 'STAT 231', 'COOP 2', 'PD 13',
                   'BET 210', 'CS 330', 'ECON 101', 'STAT 330', 'STAT 331']

# Step 1: Check Mathematics Degree Requirements
math_results = check_math_requirements(student_courses, math_requirements)

# Print Results
print("\n=== Mathematics Degree Requirements ===")
print(json.dumps(math_results, indent=4))  # No used_courses in output
