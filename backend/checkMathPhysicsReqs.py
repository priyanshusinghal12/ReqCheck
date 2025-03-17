def check_math_physics_reqs(student_courses):

    math_physics_reqs = {
        "Complete all the following: AMATH 231/271/351/353/361/373, PHYS 121/122/234/242": [False, []],
        "Complete one of the following: AMATH 242, CS 371": [False, []],
        "Complete one of the following: AMATH 250, AMATH 251": [False, []],
        "Complete one of the following: AMATH 331, PMATH 331, PMATH 333, PMATH 351": [False, []],
        "Complete one of the following: AMATH 332, PMATH 332, PMATH 352": [False, []],
        "Complete one of the following: AMATH 473, PHYS 454": [False, []],
        "Complete one of the following: AMATH 475, PHYS 476": [False, []],
        "Complete one of the following: MATH 237, MATH 247": [False, []],
        "Complete two of the following: ECE 403, PHYS 342, PHYS 358, PHYS 359, PHYS 363": [False, []],
        "Complete 2 additional courses at 300/400 level from AMATH, PHYS": [False, []],
        "Complete 5 additional courses from AMATH or PHYS": [False, []]
    }

    # Req 1: Core AMATH and PHYS courses
    check_complete_all("Complete all the following: AMATH 231/271/351/353/361/373, PHYS 121/122/234/242",
                       ["AMATH 231", "AMATH 271", "AMATH 351", "AMATH 353", "AMATH 361", "AMATH 373",
                        "PHYS 121", "PHYS 122", "PHYS 234", "PHYS 242"],
                       student_courses, math_physics_reqs)

    # Req 2: Computational Mathematics course
    check_n_from_list("Complete one of the following: AMATH 242, CS 371",
                      ["AMATH 242", "CS 371"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)

    # Req 3: Differential Equations course
    check_n_from_list("Complete one of the following: AMATH 250, AMATH 251",
                      ["AMATH 250", "AMATH 251"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)

    # Req 4: Real Analysis course
    check_n_from_list("Complete one of the following: AMATH 331, PMATH 331, PMATH 333, PMATH 351",
                      ["AMATH 331", "PMATH 331", "PMATH 333", "PMATH 351"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)

    # Req 5: Complex Analysis course
    check_n_from_list("Complete one of the following: AMATH 332, PMATH 332, PMATH 352",
                      ["AMATH 332", "PMATH 332", "PMATH 352"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)

    # Req 6: Quantum Theory 2 course
    check_n_from_list("Complete one of the following: AMATH 473, PHYS 454",
                      ["AMATH 473", "PHYS 454"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)

    # Req 7: General Relativity course
    check_n_from_list("Complete one of the following: AMATH 475, PHYS 476",
                      ["AMATH 475", "PHYS 476"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)

    # Req 8: Advanced Calculus course
    check_n_from_list("Complete one of the following: MATH 237, MATH 247",
                      ["MATH 237", "MATH 247"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)

    # Req 9: Two advanced physics/electrical engineering courses
    check_n_from_list("Complete two of the following: ECE 403, PHYS 342, PHYS 358, PHYS 359, PHYS 363",
                      ["PHYS 342", "PHYS 358", "PHYS 359", "PHYS 363", "ECE 403"], n=2, student_courses=student_courses, major_reqs=math_physics_reqs)

    # Req 10: Two additional 300/400 level AMATH or PHYS courses
    check_n_courses("Complete 2 additional courses at 300/400 level from AMATH, PHYS",
                    eligible_levels=300,
                    subject_codes=["AMATH", "PHYS"],
                    n=2,
                    student_courses=student_courses,
                    major_reqs=math_physics_reqs)

    # Req 11: Five additional AMATH or PHYS courses
    check_n_courses("Complete 5 additional courses from AMATH or PHYS",
                    eligible_levels=100,
                    subject_codes=["AMATH", "PHYS"],
                    n=5,
                    student_courses=student_courses,
                    major_reqs=math_physics_reqs)

    return math_physics_reqs
