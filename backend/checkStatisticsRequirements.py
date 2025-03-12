import json
import re

def check_statistics_requirements(student_courses, degree_requirements):
    """
    Checks if a student's courses satisfy the Statistics degree requirements,
    including explicit requirements for STAT 400-level, additional STAT courses,
    advanced CS courses, and 300/400-level courses.
    """
    satisfied_requirements = []
    missing_requirements = []
    used_courses = set()

    # Track STAT courses at different levels
    stat_400_courses = {c for c in student_courses if re.search(r'\bSTAT\s4\d{2}\b', c)}
    stat_300_400_courses = {c for c in student_courses if re.search(r'\bSTAT\s[34]\d{2}\b', c)}

    # Check required STAT courses from the JSON file
    for requirement_group in degree_requirements["Requirements"]:
        satisfied = False
        for course in requirement_group:
            if course in student_courses and course not in used_courses:
                satisfied = True
                used_courses.add(course)  # Ensure it's marked as used
                break
        
        if satisfied:
            satisfied_requirements.append(requirement_group)
        else:
            missing_requirements.append(requirement_group)

    #Requirement: Complete 2 STAT courses at the 400-level
    if len(stat_400_courses) >= 2:
        satisfied_requirements.append(["STAT 400-level (2 courses)"])
        used_courses.update(list(stat_400_courses)[:2])  # Mark two as used
    else:
        missing_requirements.append(["STAT 400-level (2 courses)"])
    
    #Requirement: Complete 1 additional STAT course at the 300- or 400-level
    remaining_stat_300_400 = stat_300_400_courses - used_courses
    if len(remaining_stat_300_400) >= 1:
        satisfied_requirements.append(["STAT 300/400-level additional course"])
        used_courses.add(next(iter(remaining_stat_300_400)))
    else:
        missing_requirements.append(["STAT 300/400-level additional course"])
    
    #Requirement: Complete 1 additional STAT course at the 400-level (OR case left open)
    remaining_stat_400 = stat_400_courses - used_courses
    has_advanced_cs = {"CS 457", "CS 485", "CS 486"} & set(student_courses) - used_courses
    if len(remaining_stat_400) >= 1:
        satisfied_requirements.append(["STAT 400-level additional OR Advanced CS Course"])
        used_courses.add(next(iter(remaining_stat_400)))
    elif has_advanced_cs:
        satisfied_requirements.append(["Advanced CS Course OR STAT 400-level additional"])
        used_courses.add(next(iter(has_advanced_cs)))
    else:
        missing_requirements.append(["STAT 400-level additional OR Advanced CS Course"])

    #Requirement: Complete 4 additional 300/400-level courses
    valid_courses = {
        c for c in student_courses
        if any(c.startswith(prefix) for prefix in ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"])
        and re.search(r'\b[34]\d{2}\b', c)  # Ensures course number is 300 or 400 level
    } - used_courses

    if len(valid_courses) >= 4:
        satisfied_requirements.append(["4 additional 300/400-level courses"])
        used_courses.update(list(valid_courses)[:4])
    else:
        missing_requirements.append(["4 additional 300/400-level courses"])
    
    #Requirement: Complete 3 additional courses from the specified departments (NO LEVEL RESTRICTION)
    valid_courses_any_level = {
        c for c in student_courses
        if any(c.startswith(prefix) for prefix in ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"])
    } - used_courses  # Remove already used courses

    if len(valid_courses_any_level) >= 3:
        satisfied_requirements.append(["3 additional courses"])
        used_courses.update(list(valid_courses_any_level)[:3])
    else:
        missing_requirements.append(["3 additional courses"])

    
    return {
        "satisfied": satisfied_requirements,
        "missing": missing_requirements,
        "used_courses": list(used_courses)  # Convert set to list for JSON serialization
    }

# Load Statistics requirements
with open("./data/statistics.json", "r") as f:
    statistics_requirements = json.load(f)["Statistics_Degree_Requirements"]

def remove_courses(student_courses):
    course_lists = [
        ["CS 115", "CS 135", "CS 145"],
        ["CS 116", "CS 136", "CS 146"],
        ["MATH 106", "MATH 136", "MATH 146"],
        ["MATH 127", "MATH 137", "MATH 147"],
        ["MATH 128", "MATH 138", "MATH 148"],
        ["MATH 135", "MATH 145"],
        ["MATH 235", "MATH 245"],
        ["STAT 230", "STAT 240"],
        ["STAT 231", "STAT 241"]
    ]
    
    # Loop over each list of courses
    for course_list in course_lists:
        # Find the intersection between the student's completed courses and the course list
        common_courses = list(set(student_courses) & set(course_list))
        
        # If there are any common courses, remove one of them from the student's courses
        if common_courses:
            course_to_remove = common_courses[0]
            student_courses.remove(course_to_remove)
    
    # Remove courses that end with 'L' or start with 'COOP' or 'PD'
    student_courses = [course for course in student_courses if not (course.endswith('L') or course.startswith('COOP') or course.startswith('PD'))]
    
    return student_courses
 
# Example student course completion
student_courses = ['PMATH 333', 'CS 479', 'AFM 101', 'CS 135', 'MATH 135', 'MATH 137', 'MTHEL 99', 'STAT 444', 
                   'CS 136', 'CS 136L', 'ECON 102', 'STAT 443', 'MATH 136', 'MATH 138', 'SPCOM 223', 'CS 371',
                   'CS 486', 'MATH 235', 'CS 231', 'CS 234', 'MATH 237', 'PD 1', 'STAT 230', 'COOP 1', 'PD 11',
                   'AMATH 250', 'BET 100', 'CLAS 104', 'CS 230', 'PSYCH 101', 'STAT 231', 'COOP 2', 'PD 13',
                   'BET 210', 'CS 330', 'ECON 101', 'STAT 330', 'STAT 331', 'STAT 341', 'STAT 332', 'STAT 333',
                   'MTHEL 300']
 
student_courses = remove_courses(student_courses)

# Step 2: Check Statistics Degree Requirements
statistics_results = check_statistics_requirements(student_courses, statistics_requirements)

# Print Results
print("\n=== Statistics Degree Requirements ===")
print(json.dumps(statistics_results, indent=4))  # Now includes used_courses in output
