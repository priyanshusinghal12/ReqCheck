from collections import defaultdict

def check_comp_math_reqs(student_courses):
    computational_math_reqs = {
        "Complete all of: CS 230, CS 234": [False, []],
        "Complete one of: AMATH 242, CS 371": [False, []],
        "Complete one of: MATH 237, MATH 247": [False, []],
        "Complete one of: MATH 239, MATH 249": [False, []],
        "Complete 3 non-math courses from the same subject code (AE, BIOL, BME, CHE, " +
        "CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME, MNS, MSE, MTE, NE, PHYS, SYDE)": [False, []],
        "List 1 Requirements": [False, []],
        "List 2: Complete 2 courses from: AMATH 342, CS 475, PMATH 370, CO 367/CO 353, STAT 340/341": [False, []],
        "Complete 4 additional courses (2 different subject codes, 2 at 400-level)": [
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
    list1_reqs = {
        "Complete one of: AMATH 250, AMATH 251, AMATH 350": [False, []],
        "Complete one of: CO 250, CO 255": [False, []],
        "Complete one of: CS 245, CS 245E, PMATH 330, PMATH 432": [False, []],
        "Complete one of: CS 246, CS 246E":[False, []]
    }
    check_n_from_list("Complete one of: AMATH 250, AMATH 251, AMATH 350",
                      ["AMATH 250", "AMATH 251", "AMATH 350"], n=1, student_courses=student_courses, major_reqs=list1_reqs)
    check_n_from_list("Complete one of: CO 250, CO 255",
                      ["CO 250", "CO 255"], n=1, student_courses=student_courses, major_reqs=list1_reqs)
    check_n_from_list("Complete one of: CS 245, CS 245E, PMATH 330, PMATH 432",
                      ["CS 245", "CS 245E", "PMATH 330", "PMATH 432"], n=1, student_courses=student_courses, major_reqs=list1_reqs)
    check_n_from_list("Complete one of: CS 246, CS 246E",
                      ["CS 246", "CS 246E"], n=1, student_courses=student_courses, major_reqs=list1_reqs)

    num_true_reqs = sum(req[0] for req in list1_reqs.values())

    if num_true_reqs >= 2:
        computational_math_reqs["List 1 Requirements"][0] = True  # Set overall requirement to True
        # Add courses from fulfilled sub-requirements
        computational_math_reqs["List 1 Requirements"][1].extend(
            [course for req in list1_reqs.values() if req[0] for course in req[1]]
        )
    elif num_true_reqs == 1:
        computational_math_reqs["List 1 Requirements"][0] = False  # Specifically set to False
        # Add courses from the single fulfilled sub-requirement
        computational_math_reqs["List 1 Requirements"][1].extend(
            [course for req in list1_reqs.values() if req[0] for course in req[1]]
        )

    # Req 7: List 2 Requirements

    if "STAT 340" in student_courses and "STAT 341" in student_courses:
        student_courses.remove("STAT 341")

    if "CO 353" in student_courses and "CO 367" in student_courses:
        student_courses.remove("CO 367")

    check_n_from_list("List 2: Complete 2 courses from: AMATH 342, CS 475, PMATH 370, CO 367/CO 353, STAT 340/341",
                      ["AMATH 342", "PMATH 370", "CO 367", "CO 353", "STAT 340", "STAT 341", "CS 475"],
                      n=2, student_courses=student_courses, major_reqs=computational_math_reqs)

    # Req 8: Complete 4 additional courses (2 different subject codes, 2 at 400-level) (last)

    list2_and_3_courses = [
        "AMATH 342", "CS 475", "PMATH 370", "CO 353", "CO 367", "STAT 340", "STAT 341",
        "AMATH 343", "AMATH 382", "AMATH 383", "AMATH 391", "AMATH 442", "AMATH 455", "AMATH 477",
        "BIOL 382", "CO 351", "CO 370", "CO 372", "CO 450", "CO 452", "CO 454", "CO 456", "CO 463",
        "CO 466", "CO 471", "CO 485", "CO 487", "CS 341", "CS 431", "CS 451", "CS 466", "CS 476",
        "CS 479", "CS 480", "CS 482", "CS 485", "CS 487", "STAT 440", "STAT 441", "STAT 442", "STAT 444"
    ]


    print("student_courses:", student_courses)

    eligible_courses = [course for course in student_courses if course in list2_and_3_courses]

    print("eligible_courses:", eligible_courses)

    subject_code_map = defaultdict(list)
    num_400_level = 0
    courses_to_add = []

    # Categorize courses by subject and level
    for course in eligible_courses:
        subject_code, number = course.split(" ")
        number = int(number)
        subject_code_map[subject_code].append((course, number))

    # Flatten and sort to prioritize 400-level courses first
    sorted_courses = sorted(eligible_courses, key=lambda c: -int(c.split()[1]) // 100)

    for course in sorted_courses:
        if course in courses_to_add:
            continue
        subject_code = course.split(" ")[0]
        course_level = int(course.split(" ")[1]) // 100

        # Add course if we don't have 4 yet
        if len(courses_to_add) < 4:
            courses_to_add.append(course)

    # Recalculate final conditions
    final_subject_codes = set(course.split(" ")[0] for course in courses_to_add)
    final_400_level_count = sum(1 for course in courses_to_add if int(course.split(" ")[1]) >= 400)

    # Update requirement
    computational_math_reqs["Complete 4 additional courses (2 different subject codes, 2 at 400-level)"][1].extend(courses_to_add)

    if len(courses_to_add) == 4 and len(final_subject_codes) >= 2 and final_400_level_count >= 2:
        computational_math_reqs["Complete 4 additional courses (2 different subject codes, 2 at 400-level)"][0] = True

    return computational_math_reqs
