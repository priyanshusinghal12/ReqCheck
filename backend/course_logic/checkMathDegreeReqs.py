from course_logic.helper import *

def check_math_degree_reqs(student_courses):

    math_degree_reqs = {
        "Complete one of the following: CS 115, CS 135, CS 145": [False, []],
        "Complete one of the following: CS 116, CS 136, CS 146": [False, []],
        "Complete one of the following: MATH 106, MATH 136, MATH 146": [False, []],
        "Complete one of the following: MATH 127, MATH 137, MATH 147": [False, []],
        "Complete one of the following: MATH 128, MATH 138, MATH 148": [False, []],
        "Complete one of the following: MATH 135, MATH 145": [False, []],
        "Complete one of the following: MATH 235, MATH 245": [False, []],
        "Complete one of the following: MATH 237, MATH 239, MATH 247, MATH 249": [False, []],
        "Complete one of the following: STAT 230, STAT 240": [False, []],
        "Complete one of the following: STAT 231, STAT 241": [False, []]
    }

    # Req 1: First Computer Science Course
    check_n_from_list("Complete one of the following: CS 115, CS 135, CS 145",
                      ["CS 115", "CS 135", "CS 145"], n=1, student_courses=student_courses, major_reqs=math_degree_reqs)

    # Req 2: Second Computer Science Course
    check_n_from_list("Complete one of the following: CS 116, CS 136, CS 146",
                      ["CS 116", "CS 136", "CS 146"], n=1, student_courses=student_courses, major_reqs=math_degree_reqs)

    # Req 3: First Linear Algebra Course
    check_n_from_list("Complete one of the following: MATH 106, MATH 136, MATH 146",
                      ["MATH 106", "MATH 136", "MATH 146"], n=1, student_courses=student_courses, major_reqs=math_degree_reqs)

    # Req 4: First Calculus Course
    check_n_from_list("Complete one of the following: MATH 127, MATH 137, MATH 147",
                      ["MATH 127", "MATH 137", "MATH 147"], n=1, student_courses=student_courses, major_reqs=math_degree_reqs)

    # Req 5: Second Calculus Course
    check_n_from_list("Complete one of the following: MATH 128, MATH 138, MATH 148",
                      ["MATH 128", "MATH 138", "MATH 148"], n=1, student_courses=student_courses, major_reqs=math_degree_reqs)

    # Req 6: Algebra Course
    check_n_from_list("Complete one of the following: MATH 135, MATH 145",
                      ["MATH 135", "MATH 145"], n=1, student_courses=student_courses, major_reqs=math_degree_reqs)

    # Req 7: Second Linear Algebra Course
    check_n_from_list("Complete one of the following: MATH 235, MATH 245",
                      ["MATH 235", "MATH 245"], n=1, student_courses=student_courses, major_reqs=math_degree_reqs)

    # Req 8: Advanced Math Course (Calculus 3 or Combinatorics)
    check_n_from_list("Complete one of the following: MATH 237, MATH 239, MATH 247, MATH 249",
                      ["MATH 237", "MATH 239", "MATH 247", "MATH 249"], n=1, student_courses=student_courses, major_reqs=math_degree_reqs)

    # Req 9: Stats & Prob Course 1
    check_n_from_list("Complete one of the following: STAT 230, STAT 240",
                      ["STAT 230", "STAT 240"], n=1, student_courses=student_courses, major_reqs=math_degree_reqs)

    # Req 10: Stats & Prob Course 2
    check_n_from_list("Complete one of the following: STAT 231, STAT 241",
                      ["STAT 231", "STAT 241"], n=1, student_courses=student_courses, major_reqs=math_degree_reqs)

    return math_degree_reqs
