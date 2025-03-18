from course_logic.helper import *
# from helper import *

def check_math_finance_reqs(student_courses):

    math_finance_reqs = {
        "Complete all the following: ACTSC 231/372/445/446, PMATH 351/450/451, STAT 330/331/333/443": [False, []],
        "Complete one of the following: AFM 101, BUS 127W": [False, []],
        "Complete one of the following: AFM 102, BUS 247W": [False, []],
        "Complete one of the following: AFM 131, ARBUS 101, BUS 111W": [False, []],
        "Complete one of the following: AMATH 242, CS 335, CS 371": [False, []],
        "Complete one of the following: AMATH 250, AMATH 251, AMATH 350": [False, []],
        "Complete one of the following: AMATH 351, CO 250, CO 255, PMATH 352": [False, []],
        "Complete one of the following: AMATH 353, CO 372, CS 476, PMATH 453": [False, []],
        "Complete one of the following: ECON 101, ECON 120W": [False, []],
        "Complete one of the following: ECON 102, ECON 140W": [False, []],
        "Complete one of the following: ECON 201, ECON 260W": [False, []],
        "Complete one of the following: MATH 247 OR (MATH 237 AND PMATH 333)": [False, []]
    }

    # Req 1: Core ACTSC, PMATH, STAT courses
    check_complete_all("Complete all the following: ACTSC 231/372/445/446, PMATH 351/450/451, STAT 330/331/333/443",
                       ["ACTSC 231", "ACTSC 372", "ACTSC 445", "ACTSC 446", "PMATH 351", "PMATH 450", "PMATH 451", "STAT 330", "STAT 331", "STAT 333", "STAT 443"],
                       student_courses, math_finance_reqs)

    # Req 2: Financial Accounting course
    check_n_from_list("Complete one of the following: AFM 101, BUS 127W",
                      ["AFM 101", "BUS 127W"], n=1, student_courses=student_courses, major_reqs=math_finance_reqs)

    # Req 3: Managerial Accounting course
    check_n_from_list("Complete one of the following: AFM 102, BUS 247W",
                      ["AFM 102", "BUS 247W"], n=1, student_courses=student_courses, major_reqs=math_finance_reqs)

    # Req 4: Business Introduction course
    check_n_from_list("Complete one of the following: AFM 131, ARBUS 101, BUS 111W",
                      ["AFM 131", "ARBUS 101", "BUS 111W"], n=1, student_courses=student_courses, major_reqs=math_finance_reqs)

    # Req 5: Computational Mathematics course
    check_n_from_list("Complete one of the following: AMATH 242, CS 335, CS 371",
                      ["AMATH 242", "CS 335", "CS 371"], n=1, student_courses=student_courses, major_reqs=math_finance_reqs)

    # Req 6: Differential Equations course
    check_n_from_list("Complete one of the following: AMATH 250, AMATH 251, AMATH 350",
                      ["AMATH 250", "AMATH 251", "AMATH 350"], n=1, student_courses=student_courses, major_reqs=math_finance_reqs)

    # Req 7: Optimization/Advanced Math course
    check_n_from_list("Complete one of the following: AMATH 351, CO 250, CO 255, PMATH 352",
                      ["CO 250", "CO 255", "AMATH 351", "PMATH 352"], n=1, student_courses=student_courses, major_reqs=math_finance_reqs)

    # Req 8: Advanced Mathematics or Financial Modeling course
    check_n_from_list("Complete one of the following: AMATH 353, CO 372, CS 476, PMATH 453",
                      ["AMATH 353", "CO 372", "CS 476", "PMATH 453"], n=1, student_courses=student_courses, major_reqs=math_finance_reqs)

    # Req 9: Microeconomics courses
    check_n_from_list("Complete one of the following: ECON 101, ECON 120W",
                       ["ECON 101", "ECON 120W"], n=1, student_courses=student_courses, major_reqs=math_finance_reqs)

    # Req 10: Macroeconomics courses
    check_n_from_list("Complete one of the following: ECON 102, ECON 140W",
                       ["ECON 102", "ECON 140W"], n=1, student_courses=student_courses, major_reqs=math_finance_reqs)

    # Req 11: Advanced Microeconomics courses
    check_n_from_list("Complete one of the following: ECON 201, ECON 260W",
                       ["ECON 201", "ECON 260W"], n=1, student_courses=student_courses, major_reqs=math_finance_reqs)

    # Req 12: Special condition: MATH 247 OR (MATH 237 AND PMATH 333)
    if "MATH 247" in student_courses:
        math_finance_reqs["Complete one of the following: MATH 247 OR (MATH 237 AND PMATH 333)"][0] = True
        math_finance_reqs["Complete one of the following: MATH 247 OR (MATH 237 AND PMATH 333)"][1].append("MATH 247")
        student_courses.remove("MATH 247")
    elif "MATH 237" in student_courses and "PMATH 333" in student_courses:
        math_finance_reqs["Complete one of the following: MATH 247 OR (MATH 237 AND PMATH 333)"][0] = True
        math_finance_reqs["Complete one of the following: MATH 247 OR (MATH 237 AND PMATH 333)"][1].extend(["MATH 237", "PMATH 333"])
        student_courses.remove("MATH 237")
        student_courses.remove("PMATH 333")

    return math_finance_reqs

# math_finance_tests = [
#     "ACTSC 231", "ACTSC 372", "ACTSC 445", "ACTSC 446", "PMATH 351", "PMATH 450", "PMATH 451", "STAT 330",
#     "STAT 331", "STAT 333", "STAT 443",  # Core courses

#     "BUS 127W", "BUS 247W", "ARBUS 101", "AMATH 250", "CS 371", "CO 250", "CO 372",
#     "ECON 120W", "ECON 140W", "ECON 260W",  # Required business, finance, and econ courses

#     "MATH 247"  # Completing the special condition (MATH 237 and PMATH 333)
# ]

# print(check_math_finance_reqs(math_finance_tests))