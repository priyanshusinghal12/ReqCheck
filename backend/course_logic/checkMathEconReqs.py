from course_logic.helper import *


def check_math_econ_reqs(student_courses):

    refine_courses(student_courses, ["MATH 237", "MATH 247"])

    math_econ_reqs = {
        "Complete all the following: ECON 101, 102, 290, 306, 391, 393, 472, 491, 496": [False, []],
        "Complete one of the following: ECON 406, 407, 408, 409": [False, []],
        "Complete 4 additional ECON courses at the 300/400 level": [False, []],
        "Complete all the following: AMATH 350, STAT 331, STAT 443": [False, []],
        "Complete one of the following: AMATH 331, PMATH 331, PMATH 333, PMATH 351": [False, []],
        "Complete one of the following: CO 250, CO 255": [False, []],
        "Complete one of the following: MATH 237, MATH 247": [False, []],
        "Complete 7 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [False, []],
        "Complete 2 additional courses": [False, []]
    }

    # Req 1: Core ECON courses
    check_complete_all("Complete all the following: ECON 101, 102, 290, 306, 391, 393, 472, 491, 496",
                       ["ECON 101", "ECON 102", "ECON 290", "ECON 306", "ECON 391", "ECON 393", "ECON 472", "ECON 491", "ECON 496"],
                       student_courses, math_econ_reqs)

    # Req 2: One advanced ECON course
    check_n_from_list("Complete one of the following: ECON 406, 407, 408, 409",
                      ["ECON 406", "ECON 407", "ECON 408", "ECON 409"],
                      n=1, student_courses=student_courses, major_reqs=math_econ_reqs)

    # Req 3: 4 additional ECON 300/400 level courses
    check_n_courses("Complete 4 additional ECON courses at the 300/400 level",
                    eligible_levels=300,
                    subject_codes=["ECON"],
                    n=4,
                    student_courses=student_courses,
                    major_reqs=math_econ_reqs)

    # Req 4: Core math/stat courses
    check_complete_all("Complete all the following: AMATH 350, STAT 331, STAT 443",
                       ["AMATH 350", "STAT 331", "STAT 443"],
                       student_courses, math_econ_reqs)

    # Req 5: One advanced math course
    check_n_from_list("Complete one of the following: AMATH 331, PMATH 331, PMATH 333, PMATH 351",
                      ["AMATH 331", "PMATH 331", "PMATH 333", "PMATH 351"],
                      n=1, student_courses=student_courses, major_reqs=math_econ_reqs)

    # Req 6: One combinatorics/optimization course
    check_n_from_list("Complete one of the following: CO 250, CO 255",
                      ["CO 250", "CO 255"],
                      n=1, student_courses=student_courses, major_reqs=math_econ_reqs)

    # Req 7: One advanced calculus course
    check_n_from_list("Complete one of the following: MATH 237, MATH 247",
                      ["MATH 237", "MATH 247"],
                      n=1, student_courses=student_courses, major_reqs=math_econ_reqs)

    # Req 8: 7 additional math-related courses at any level
    check_n_courses("Complete 7 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT",
                    eligible_levels=100,
                    subject_codes=["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                    n=7,
                    student_courses=student_courses,
                    major_reqs=math_econ_reqs)

    # Req 9: Any 2 additional courses
    if len(student_courses) >= 2:
        math_econ_reqs["Complete 2 additional courses"][0] = True
        math_econ_reqs["Complete 2 additional courses"][1].extend(student_courses[:2])

    return math_econ_reqs
    