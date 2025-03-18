from course_logic.helper import *

def math_studies_reqs(student_courses,minorDoing):
    """
    Checks if a student has completed the requirements for the General Math Major.

    Args:
        student_courses: A list of student's completed courses.

    Returns:
        A dictionary of the program requirements and their completion status.
    """

    math_studies_reqs = {
        "Complete one of the following: MATH 106, MATH 136, MATH 146": [False, []],
        "Complete one of the following: MATH 127, MATH 137, MATH 147": [False, []],
        "Complete one of the following: MATH 128, MATH 138, MATH 148": [False, []],
        "Complete one of the following: MATH 135, MATH 145": [False, []],
        "Complete one of the following: MATH 225, MATH 235, MATH 245": [False, []],
        "Complete one of the following: MATH 207, MATH 237, MATH 247, MATH 229, MATH 239, MATH 249": [False, []],
        "Complete one of the following: STAT 220, STAT 230, STAT 240": [False, []],
        "Complete one of the following: STAT 221, STAT 231, STAT 241": [False, []],
        "Complete one of the following: CS 115, CS 135, CS 145": [False, []],
        "Complete one of the following: CS 116, CS 136, CS 146": [False, []],
        "1st Communication Skills Requirement": [False, []],
        "2nd Communication Skills Requirement": [False, []],
        "Ten mathematics 3XX and/or 4XX courses": [False, []],
        "Four additional mathematics courses": [False, []],
        "Eight additional non-math courses": [False, []],
        "Two additional math courses or two courses that contribute to a minor outside of Mathematics": [False, []],
        "Four free-choice electives": [False, []]
    }

    math_subject_codes = ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"]

    # Requirements 1-10: Specific course requirements
    check_n_from_list("Complete one of the following: MATH 106, MATH 136, MATH 146",
                      ["MATH 106", "MATH 136", "MATH 146"], n=1, student_courses=student_courses, major_reqs=math_studies_reqs)
    check_n_from_list("Complete one of the following: MATH 127, MATH 137, MATH 147",
                      ["MATH 127", "MATH 137", "MATH 147"], n=1, student_courses=student_courses, major_reqs=math_studies_reqs)
    check_n_from_list("Complete one of the following: MATH 128, MATH 138, MATH 148",
                      ["MATH 128", "MATH 138", "MATH 148"], n=1, student_courses=student_courses, major_reqs=math_studies_reqs)
    check_n_from_list("Complete one of the following: MATH 135, MATH 145",
                      ["MATH 135", "MATH 145"], n=1, student_courses=student_courses, major_reqs=math_studies_reqs)
    check_n_from_list("Complete one of the following: MATH 225, MATH 235, MATH 245",
                      ["MATH 225", "MATH 235", "MATH 245"], n=1, student_courses=student_courses, major_reqs=math_studies_reqs)
    check_n_from_list("Complete one of the following: MATH 207, MATH 237, MATH 247, MATH 229, MATH 239, MATH 249",
                      ["MATH 207", "MATH 237", "MATH 247", "MATH 229", "MATH 239", "MATH 249"], n=1, student_courses=student_courses, major_reqs=math_studies_reqs)
    check_n_from_list("Complete one of the following: STAT 220, STAT 230, STAT 240",
                      ["STAT 220", "STAT 230", "STAT 240"], n=1, student_courses=student_courses, major_reqs=math_studies_reqs)
    check_n_from_list("Complete one of the following: STAT 221, STAT 231, STAT 241",
                      ["STAT 221", "STAT 231", "STAT 241"], n=1, student_courses=student_courses, major_reqs=math_studies_reqs)
    check_n_from_list("Complete one of the following: CS 115, CS 135, CS 145",
                      ["CS 115", "CS 135", "CS 145"], n=1, student_courses=student_courses, major_reqs=math_studies_reqs)
    check_n_from_list("Complete one of the following: CS 116, CS 136, CS 146",
                      ["CS 116", "CS 136", "CS 146"], n=1, student_courses=student_courses, major_reqs=math_studies_reqs)

    # Requirement 11: Two EMLS/ENGL/SPCOM courses satisfying the Communication Skills requirement

    # Lists of courses for the communication skills requirement
    list1_courses = ["SPCOM 100", "SPCOM 223", "EMLS 101R", "EMLS 102R", "EMLS 129R", "ENGL 109", "ENGL 129R"]

    list2_courses = ["SPCOM 225", "SPCOM 227", "SPCOM 228", "EMLS 103R", "EMLS 104R", "EMLS 110R",
                     "ENGL 101B", "ENGL 108B", "ENGL 108D", "ENGL 119", "ENGL 208B", "ENGL 209", "ENGL 210E",
                     "ENGL 210F", "ENGL 378", "MTHEL 300"]

    # Check for the first communication skills course (from List 1)
    check_n_from_list("1st Communication Skills Requirement",
                      list1_courses, n=1, student_courses=student_courses, major_reqs=math_studies_reqs)

    check_n_from_list("2nd Communication Skills Requirement",
                      list1_courses + list2_courses, n=1, student_courses=student_courses, major_reqs=math_studies_reqs)


    # Requirement 12: Ten mathematics 3XX and/or 4XX courses
    check_n_courses("Ten mathematics 3XX and/or 4XX courses",
                    eligible_levels=300,
                    subject_codes=math_subject_codes,
                    n=10,
                    student_courses=student_courses,
                    major_reqs=math_studies_reqs)

    # Requirement 13: Four additional mathematics courses
    check_n_courses("Four additional mathematics courses",
                    eligible_levels=100,
                    subject_codes=math_subject_codes,
                    n=4,
                    student_courses=student_courses,
                    major_reqs=math_studies_reqs)

    # Requirement 14: Eight additional non-math courses
    non_math_courses = [course for course in student_courses if course.split(" ")[0] not in math_subject_codes]
    if len(non_math_courses) >= 8:
        math_studies_reqs["Eight additional non-math courses"][0] = True
        math_studies_reqs["Eight additional non-math courses"][1].extend(non_math_courses)
        student_courses = [course for course in student_courses if course not in non_math_courses[:8]]

    # Requirements 15: 2 additional math courses or 2 courses contributing to a minor.

    if (minorDoing):
        math_studies_reqs["Two additional math courses or two courses that contribute to a minor outside of Mathematics"][0] = True
        #code to add the courses

    else: #we just check for the 2 additional math courses.
        print("in here")
        check_n_courses("Two additional math courses or two courses that contribute to a minor outside of Mathematics",
          eligible_levels=100,
          subject_codes=math_subject_codes,
          n=2,
          student_courses=student_courses,
          major_reqs=math_studies_reqs)


    #Req 16 - 4 free choice electives.
    if len(student_courses) >= 4:
        math_studies_reqs["Four free-choice electives"][0] = True
        math_studies_reqs["Four free-choice electives"][1].extend(student_courses)
        student_courses = student_courses[4:]

    return math_studies_reqs

