from collections import defaultdict
from course_logic.helper import *
 
# Helper function to check List 1 req
def evaluate_list1_requirement(student_courses, computational_math_reqs):
    requirement_key = "List 1 Requirement - Complete 2 courses from these options: AMATH 250/251/350, CO 250/255, CS 245/CS 245E/PMATH 330/PMATH 432, CS 246/246E"
 
    list1_groups = {
        "AMATH": ["AMATH 250", "AMATH 251", "AMATH 350"],
        "CO": ["CO 250", "CO 255"],
        "LOGIC": ["CS 245", "CS 245E", "PMATH 330", "PMATH 432"],
        "OOP": ["CS 246", "CS 246E"]
    }
 
    fulfilled_groups = []
    used_courses = []
    used_subjects = set()
 
    for group_name, group_courses in list1_groups.items():
        for course in group_courses:
            if course in student_courses:
                subject = course.split()[0]
                if group_name not in fulfilled_groups and subject not in used_subjects:
                    fulfilled_groups.append(group_name)
                    used_subjects.add(subject)
                    computational_math_reqs[requirement_key][1].append(course)
                    used_courses.append(course)
                    break  # Only one course per group
 
        if len(fulfilled_groups) >= 2:
            break
 
    for course in used_courses:
        student_courses.remove(course)
 
    if len(fulfilled_groups) >= 2:
        computational_math_reqs[requirement_key][0] = True
 
# Helper for last req (list 2 and 3)
def check_additional_courses(student_courses, list2_and_3_courses):
    # Initialize the dictionary as provided
    computational_math_reqs = {
        "Complete 4 additional courses in at least 2 different subject codes, at least 2 of which are 400 level": [False, []]
    }
    
    # Filter student courses that are in list2_and_3_courses
    eligible_courses = [course for course in student_courses if course in list2_and_3_courses]
    
    # Special case handling for CS courses (only one of CS 431 or CS 451 may count)
    if "CS 431" in eligible_courses and "CS 451" in eligible_courses:
        eligible_courses.remove("CS 451")  # Remove CS 451 if both are present
    
    # Categorize the courses by subject code and 400-level courses
    subject_codes = {}
    for course in eligible_courses:
        subject_code, course_num = course.split(' ', 1)
        if subject_code not in subject_codes:
            subject_codes[subject_code] = {'courses': [], 'is_400_level': 0}
        subject_codes[subject_code]['courses'].append(course)
        if int(course_num) >= 400:
            subject_codes[subject_code]['is_400_level'] += 1
    
    # Count the total number of eligible courses
    total_courses = []
    for code, data in subject_codes.items():
        total_courses.extend(data['courses'])
    
    # Check if the requirements are met
    # We need at least 4 courses, from at least 2 different subject codes, and at least 2 of them should be 400-level
    subject_code_count = len(subject_codes)
    four_courses_met = len(total_courses) >= 4
    two_subject_codes_met = subject_code_count >= 2
    two_400_level_met = sum([data['is_400_level'] >= 2 for data in subject_codes.values()]) >= 1
    
    # If all requirements are met
    if four_courses_met and two_subject_codes_met and two_400_level_met:
        computational_math_reqs["Complete 4 additional courses in at least 2 different subject codes, at least 2 of which are 400 level"] = [True, total_courses]
    else:
        # If not all requirements are met, add partial progress
        computational_math_reqs["Complete 4 additional courses in at least 2 different subject codes, at least 2 of which are 400 level"] = [False, total_courses]
 
    return computational_math_reqs
 
def check_list2_3_requirement(student_courses, major_reqs, current_requirement):
    list2_and_3_courses = [
        "AMATH 342", "CS 475", "PMATH 370", "CO 353", "CO 367", "STAT 340", "STAT 341",
        "AMATH 343", "AMATH 382", "AMATH 383", "AMATH 391", "AMATH 442", "AMATH 455", "AMATH 477",
        "BIOL 382", "CO 351", "CO 370", "CO 372", "CO 450", "CO 452", "CO 454", "CO 456", "CO 463",
        "CO 466", "CO 471", "CO 485", "CO 487", "CS 341", "CS 431", "CS 451", "CS 466", "CS 476",
        "CS 479", "CS 480", "CS 482", "CS 485", "CS 487", "STAT 440", "STAT 441", "STAT 442", "STAT 444"
    ]
 
    # Determine which of CS 431 and CS 451 to keep
    cs_conflict = None
    if "CS 431" in student_courses and "CS 451" in student_courses:
        cs_conflict = "CS 431"  # pick one arbitrarily
    elif "CS 431" in student_courses:
        cs_conflict = "CS 431"
    elif "CS 451" in student_courses:
        cs_conflict = "CS 451"
 
    valid_courses = []
    used_subject_codes = set()
    num_400_level = 0
 
    # Build the list of valid completed courses
    for course in student_courses:
        if course not in list2_and_3_courses:
            continue
        if course in ["CS 431", "CS 451"] and course != cs_conflict:
            continue
 
        try:
            subject, number = course.split()
            level = int(number)
        except:
            continue
 
        valid_courses.append((course, subject, level))
        if level >= 400:
            num_400_level += 1
        used_subject_codes.add(subject)
 
    # Select up to 4 courses
    selected_courses = [course for course, _, _ in valid_courses[:4]]
    selected_subjects = {sub for _, sub, _ in valid_courses[:4]}
    selected_400s = [lvl for _, _, lvl in valid_courses[:4] if lvl >= 400]
 
    # Record partial completion always
    major_reqs[current_requirement][1].extend(selected_courses)
 
    # Remove used courses
    for course in selected_courses:
        if course in student_courses:
            student_courses.remove(course)
 
    # Determine if requirement is fully satisfied
    if len(selected_courses) >= 4 and len(selected_subjects) >= 2 and len(selected_400s) >= 2:
        major_reqs[current_requirement][0] = True
    else:
        major_reqs[current_requirement][0] = False
 
# Major function
def check_comp_math_reqs(student_courses):
 
    refine_courses(student_courses, ["MATH 237", "MATH 247", "MATH 239", "MATH 249"])
 
    computational_math_reqs = {
        "Complete all of: CS 230, CS 234": [False, []],
        "Complete one of: AMATH 242, CS 371": [False, []],
        "Complete one of: MATH 237, MATH 247": [False, []],
        "Complete one of: MATH 239, MATH 249": [False, []],
        "Complete 3 non-math courses from the same subject code (AE, BIOL, BME, CHE, " +
        "CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME, MNS, MSE, MTE, NE, PHYS, SYDE)": [False, []],
        "List 1 Requirement - Complete 2 courses from these options: AMATH 250/251/350, CO 250/255, CS 245/CS 245E/PMATH 330/PMATH 432, CS 246/246E": [False, []],
        "List 2 requirement - Complete 2 courses from these options: AMATH 342, CS 475, PMATH 370, CO 367/CO 353, STAT 340/341": [False, []],
        "Complete 4 additional courses in at least 2 different subject codes, at least 2 of which are 400 level": [
            False, []]
    }
 
    # Req 1-4: Core CS, Computational Math, Calculus 3, Combinatorics
    check_complete_all("Complete all of: CS 230, CS 234",
                       ["CS 230", "CS 234"],
                       student_courses, computational_math_reqs)
    check_n_from_list("Complete one of: AMATH 242, CS 371",
                      ["AMATH 242", "CS 371"], n=1, student_courses=student_courses, major_reqs=computational_math_reqs)
    check_n_from_list("Complete one of: MATH 237, MATH 247",
                      ["MATH 237", "MATH 247"], n=1, student_courses=student_courses, major_reqs=computational_math_reqs)
    check_n_from_list("Complete one of: MATH 239, MATH 249",
                      ["MATH 239", "MATH 249"], n=1, student_courses=student_courses, major_reqs=computational_math_reqs)
 
    subject_codes = ["AE", "BIOL", "BME", "CHE", "CHEM", "CIVE", "EARTH", "ECE", "ECON", "ENVE", "GEOE", "ME", "MNS", "MSE", "MTE", "NE", "PHYS", "SYDE"]
 
    #Req 5: 3 Non-Math Courses from the same subject, with at least one at the 200+ level
    check_concentration("Complete 3 non-math courses from the same subject code (AE, BIOL, BME, CHE, " +
        "CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME, MNS, MSE, MTE, NE, PHYS, SYDE)", eligible_levels = 200,
                        subject_codes = subject_codes, n=3, student_courses=student_courses, major_reqs=computational_math_reqs)
 
    # Req 6: List 1 Requirements
    evaluate_list1_requirement(student_courses, computational_math_reqs)
 
    # Req 7: List 2 Requirements
 
    if "STAT 340" in student_courses and "STAT 341" in student_courses:
        student_courses.remove("STAT 341")
 
    if "CO 353" in student_courses and "CO 367" in student_courses:
        student_courses.remove("CO 367")
 
    check_n_from_list("List 2 requirement - Complete 2 courses from these options: AMATH 342, CS 475, PMATH 370, CO 367/CO 353, STAT 340/341",
                      ["AMATH 342", "PMATH 370", "CO 367", "CO 353", "STAT 340", "STAT 341", "CS 475"],
                      n=2, student_courses=student_courses, major_reqs=computational_math_reqs)
 
 
    # Req 8: Complete 4 additional courses (2 different subject codes, 2 at 400-level) (last)
    check_list2_3_requirement(
        student_courses,
        computational_math_reqs,
        "Complete 4 additional courses in at least 2 different subject codes, at least 2 of which are 400 level"
    )
 
 
    return computational_math_reqs