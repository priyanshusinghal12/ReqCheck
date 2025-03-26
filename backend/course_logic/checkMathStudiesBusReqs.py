from course_logic.helper import *

def math_studies_business_reqs(student_courses):
    """
    Checks if a student has completed the requirements for the General Math Major.

    Args:
        student_courses: A list of student's completed courses.

    Returns:
        A dictionary of the program requirements and their completion status.
    """

    math_studies_business_specialization_reqs = {
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
        "Complete one of the following: STAT 321, STAT 371, STAT 373, STAT 322": [False, []],
        "Complete one of the following: CO 227, CO 250, CO 255": [False, []],
        "Complete one of the following: CO 327, CO 370": [False, []],
        "Complete one of the following: AFM 272, ACTSC 291, ACTSC 221, ACTSC 231, or ACTSC 371": [False, []],
        "Complete two of the following: CS 200, CS 338, CS 430, CS 432, STAT 340": [False, []],
        "Seven mathematics 3XX and/or 4XX courses": [False, []],
        "Complete all of: CS 330, AFM 101, AFM 102, BUS 121W, ECON 101, ECON 102": [False, []],
        "Complete one of: AFM 131, ARBUS 101, BUS 111W": [False, []],
        "Complete one of: ARBUS 302, ECON 344, MGMT 244, BUS 352W": [False, []],
        "Complete one of: LS 271, PACS 202": [False, []],
        "Complete one of: LS 319, PACS 323": [False, []],
        "Complete one course from AFM, BUS, COMM, ECON, HRM, MSE, STV": [False, []],
        "Four additional free-choice electives": [False, []]
    }

    math_subject_codes = ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"]

    # Requirements 1-10: Specific course requirements
    check_n_from_list("Complete one of the following: MATH 106, MATH 136, MATH 146",
                      ["MATH 106", "MATH 136", "MATH 146"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of the following: MATH 127, MATH 137, MATH 147",
                      ["MATH 127", "MATH 137", "MATH 147"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of the following: MATH 128, MATH 138, MATH 148",
                      ["MATH 128", "MATH 138", "MATH 148"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of the following: MATH 135, MATH 145",
                      ["MATH 135", "MATH 145"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of the following: MATH 225, MATH 235, MATH 245",
                      ["MATH 225", "MATH 235", "MATH 245"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of the following: MATH 207, MATH 237, MATH 247, MATH 229, MATH 239, MATH 249",
                      ["MATH 207", "MATH 237", "MATH 247", "MATH 229", "MATH 239", "MATH 249"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of the following: STAT 220, STAT 230, STAT 240",
                      ["STAT 220", "STAT 230", "STAT 240"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of the following: STAT 221, STAT 231, STAT 241",
                      ["STAT 221", "STAT 231", "STAT 241"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of the following: STAT 321 or STAT 322",
                      ["STAT 321", "STAT 322"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of the following: CS 115, CS 135, CS 145",
                      ["CS 115", "CS 135", "CS 145"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of the following: CS 116, CS 136, CS 146",
                      ["CS 116", "CS 136", "CS 146"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)

    # Requirement 11: Two EMLS/ENGL/SPCOM courses satisfying the Communication Skills requirement

    # Lists of courses for the communication skills requirement
    list1_courses = ["SPCOM 100", "SPCOM 223", "EMLS 101R", "EMLS 102R", "EMLS 129R", "ENGL 109", "ENGL 129R"]

    list2_courses = ["SPCOM 225", "SPCOM 227", "SPCOM 228", "EMLS 103R", "EMLS 104R", "EMLS 110R",
                     "ENGL 101B", "ENGL 108B", "ENGL 108D", "ENGL 119", "ENGL 208B", "ENGL 209", "ENGL 210E",
                     "ENGL 210F", "ENGL 378", "MTHEL 300"]

    # Check for the first communication skills course (from List 1)
    check_n_from_list("1st Communication Skills Requirement",
                      list1_courses, n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)

    check_n_from_list("2nd Communication Skills Requirement",
                      list1_courses + list2_courses, n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)

    # Requirements 12: Specific course requirements
    check_n_from_list("Complete one of the following: STAT 321, STAT 371, STAT 373, STAT 322",
                      ["STAT 321", "STAT 371", "STAT 373", "STAT 322"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of the following: CO 227, CO 250, CO 255",
                      ["CO 227", "CO 250", "CO 255"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of the following: CO 327, CO 370",
                      ["CO 327", "CO 370"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of the following: AFM 272, ACTSC 291, ACTSC 221, ACTSC 231, or ACTSC 371",
                      ["AFM 272", "ACTSC 291", "ACTSC 221", "ACTSC 231", "ACTSC 371"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete two of the following: CS 200, CS 338, CS 430, CS 432, STAT 340",
                      ["CS 200", "CS 338", "CS 430", "CS 432", "STAT 340"], n=2, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)

    # Req: Seven mathematics 3XX and/or 4XX courses
    check_n_courses("Seven mathematics 3XX and/or 4XX courses",
                    eligible_levels=300,
                    subject_codes=math_subject_codes,
                    n=7,
                    student_courses=student_courses,
                    major_reqs=math_studies_reqs)

    # Requirements: Specific course requirements
    check_complete_all("Complete all of: CS 330, AFM 101, AFM 102, BUS 121W, ECON 101, ECON 102",
                       ["CS 330", "AFM 101", "AFM 102", "BUS 121W", "ECON 101", "ECON 102"],
                       student_courses, math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of: AFM 131, ARBUS 101, BUS 111W",
                      ["AFM 131", "ARBUS 101", "BUS 111W"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of: ARBUS 302, ECON 344, MGMT 244, BUS 352W",
                      ["ARBUS 302", "ECON 344", "MGMT 244", "BUS 352W"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of: LS 271, PACS 202",
                      ["LS 271", "PACS 202"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)
    check_n_from_list("Complete one of: LS 319, PACS 323",
                      ["LS 319", "PACS 323"], n=1, student_courses=student_courses, major_reqs=math_studies_business_specialization_reqs)

    #Req: Complete one course from AFM, BUS, COMM, ECON, HRM, MSE, STV
    check_one_course_from_list(
                      current_requirement="Complete one course from AFM, BUS, COMM, ECON, HRM, MSE, STV",
                      subject_codes=["AFM", "BUS", "COMM", "ECON", "HRM", "MSE", "STV"],
                      student_courses=student_courses,
                      major_reqs=math_studies_reqs)

    # Last Req: Four additional free-choice electives (placeholder)
    if len(student_courses) >= 4:
        student_courses = student_courses[:4]
        math_studies_reqs["Four free-choice electives"][0] = True
        math_studies_reqs["Four free-choice electives"][1].extend(student_courses)
        student_courses = student_courses[4:]
    else:
        math_studies_reqs["Four free-choice electives"][0] = False
        math_studies_reqs["Four free-choice electives"][1].extend(student_courses)
        student_courses = []



    return math_studies_business_specialization_reqs