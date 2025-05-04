from course_logic.helper import *
# from helper import *

def check_stat_330_or_334_req(current_requirement, student_courses, major_reqs):
    """
    Checks if a student has completed one of the following options:
    1. STAT 330, STAT 333, and one additional 300/400-level course from specified subject codes.
    2. STAT 334 and two additional 300/400-level courses from specified subject codes.

    If only partially completed, the contributing courses are still recorded.
    """
    eligible_subject_codes = ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"]

    def is_valid_extra_course(course):
        try:
            subject, number = course.split(" ")
            return subject in eligible_subject_codes and 300 <= int(number) <= 499
        except:
            return False

    partial_courses = []

    # Option 1: STAT 330 + STAT 333 + one extra
    has_330 = "STAT 330" in student_courses
    has_333 = "STAT 333" in student_courses
    option1_ready = has_330 and has_333

    if option1_ready:
        additional_courses = [
            course for course in student_courses
            if course not in ["STAT 330", "STAT 333"] and is_valid_extra_course(course)
        ]

        if additional_courses:
            major_reqs[current_requirement][0] = True
            major_reqs[current_requirement][1].extend(["STAT 330", "STAT 333", additional_courses[0]])
            student_courses.remove("STAT 330")
            student_courses.remove("STAT 333")
            student_courses.remove(additional_courses[0])
            return
        else:
            partial_courses.extend(["STAT 330", "STAT 333"])

    # Option 2: STAT 334 + two extras
    if "STAT 334" in student_courses:
        additional_courses = [
            course for course in student_courses
            if course != "STAT 334" and is_valid_extra_course(course)
        ]

        if len(additional_courses) >= 2:
            major_reqs[current_requirement][0] = True
            major_reqs[current_requirement][1].extend(["STAT 334", additional_courses[0], additional_courses[1]])
            student_courses.remove("STAT 334")
            student_courses.remove(additional_courses[0])
            student_courses.remove(additional_courses[1])
            return
        else:
            partial_courses.append("STAT 334")
            if additional_courses:
                partial_courses.extend(additional_courses[:2])  # at most 2

    # If neither is fully complete, record partial contribution
    major_reqs[current_requirement][1].extend(partial_courses)

def check_farm_professional_risk_management_reqs(student_courses):
    """
    Checks if a student has completed the requirements for the FARM Professional Risk Management Specialization.

    Args:
        student_courses: A list of student's completed courses.

    Returns:
        A dictionary of FARM specialization requirements and their completion status.
    """

    farm_risk_reqs = {
        # Required
        "Complete all of the following: ACTSC 231, ACTSC 372, AFM 101, AFM 102, AFM 131, AMATH 350, CO 372, COMM 101, CS 330, ECON 101, ECON 102, MATBUS 371, STAT 371": [False, []],
        "Complete 1 of the following: ACTSC 446, MATBUS 470": [False, []],
        "Complete 1 of the following: AFM 231, LS 283": [False, []],
        "Complete 1 of the following: CO 250, CO 255": [False, []],
        "Complete 1 of the following: CS 335, CS 476": [False, []],
        "Complete 1 of the following: MATH 237, MATH 247": [False, []],
        
        # STAT path choice (Group A or B)
        "Complete one of the following: all of (STAT 330, STAT 333, additional ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT) or (STAT 334, 2 additional courses from ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT)": [False, []],
        
        # Specialization Requirements
        "Complete all of the following: CS 338": [False, []],
        "Complete 1 of the following: ACTSC 445, MATBUS 472": [False, []],
        "Complete 1 of the following: AMATH 331, PMATH 331, PMATH 333, PMATH 351": [False, []],
        "Complete 1 of the following: STAT 340, STAT 341": [False, []],
        
        # Additional electives
        "Complete 1 course from BUS, COMM, ECON, HRM, MSE": [False, []],
        "Complete 3 additional courses": [False, []]
    }

    # Base course requirements
    check_complete_all(
        "Complete all of the following: ACTSC 231, ACTSC 372, AFM 101, AFM 102, AFM 131, AMATH 350, CO 372, COMM 101, CS 330, ECON 101, ECON 102, MATBUS 371, STAT 371",
        [
            "ACTSC 231", "ACTSC 372", "AFM 101", "AFM 102", "AFM 131", "AMATH 350",
            "CO 372", "COMM 101", "CS 330", "ECON 101", "ECON 102", "MATBUS 371", "STAT 371"
        ],
        student_courses, farm_risk_reqs
    )

    check_n_from_list("Complete 1 of the following: ACTSC 446, MATBUS 470",
        ["ACTSC 446", "MATBUS 470"], n=1,
        student_courses=student_courses, major_reqs=farm_risk_reqs
    )

    check_n_from_list("Complete 1 of the following: AFM 231, LS 283",
        ["AFM 231", "LS 283"], n=1,
        student_courses=student_courses, major_reqs=farm_risk_reqs
    )

    check_n_from_list("Complete 1 of the following: CO 250, CO 255",
        ["CO 250", "CO 255"], n=1,
        student_courses=student_courses, major_reqs=farm_risk_reqs
    )

    check_n_from_list("Complete 1 of the following: CS 335, CS 476",
        ["CS 335", "CS 476"], n=1,
        student_courses=student_courses, major_reqs=farm_risk_reqs
    )

    check_n_from_list("Complete 1 of the following: MATH 237, MATH 247",
        ["MATH 237", "MATH 247"], n=1,
        student_courses=student_courses, major_reqs=farm_risk_reqs
    )
    
    # Specialization
    check_complete_all("Complete all of the following: CS 338",
        ["CS 338"], student_courses, farm_risk_reqs
    )

    check_n_from_list("Complete 1 of the following: ACTSC 445, MATBUS 472",
        ["ACTSC 445", "MATBUS 472"], n=1,
        student_courses=student_courses, major_reqs=farm_risk_reqs
    )

    check_n_from_list("Complete 1 of the following: AMATH 331, PMATH 331, PMATH 333, PMATH 351",
        ["AMATH 331", "PMATH 331", "PMATH 333", "PMATH 351"], n=1,
        student_courses=student_courses, major_reqs=farm_risk_reqs
    )

    check_n_from_list("Complete 1 of the following: STAT 340, STAT 341",
        ["STAT 340", "STAT 341"], n=1,
        student_courses=student_courses, major_reqs=farm_risk_reqs
    )

    check_stat_330_or_334_req("Complete one of the following: all of (STAT 330, STAT 333, additional ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT) or (STAT 334, 2 additional courses from ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT)",
                              student_courses=student_courses, major_reqs=farm_risk_reqs)

    # Additional electives
    check_n_courses(
        "Complete 1 course from BUS, COMM, ECON, HRM, MSE",
        eligible_levels=100,
        subject_codes=["BUS", "COMM", "ECON", "HRM", "MSE"],
        n=1,
        student_courses=student_courses,
        major_reqs=farm_risk_reqs
    )
    
    if len(student_courses)>=3:
        farm_risk_reqs["Complete 3 additional courses"][0] = True
        
    farm_risk_reqs["Complete 3 additional courses"][1].extend(student_courses[:3])

    return farm_risk_reqs

def check_farm_professional_fin_analyst_reqs(student_courses):
    """
    Checks if a student has completed the requirements for the FARM Professional Risk Management Specialization.

    Args:
        student_courses: A list of student's completed courses.

    Returns:
        A dictionary of FARM specialization requirements and their completion status.
    """

    farm_fin_reqs = {
        # Required (Base Courses)
        "Complete all of the following: ACTSC 231, ACTSC 372, AFM 101, AFM 102, AFM 131, AMATH 350, CO 372, COMM 101, CS 330, ECON 101, ECON 102, MATBUS 471, STAT 371": [False, []],
        "Complete 1 of the following: ACTSC 446, MATBUS 470": [False, []],
        "Complete 1 of the following: AFM 231, LS 283": [False, []],
        "Complete 1 of the following: CO 250, CO 255": [False, []],
        "Complete 1 of the following: CS 335, CS 476": [False, []],
        "Complete 1 of the following: MATH 237, MATH 247": [False, []],

        # STAT path choice (Group A or Group B)
        "Complete one of the following: all of (STAT 330, STAT 333, additional ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT) or (STAT 334, 2 additional courses from ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT)": [False, []],

        # Specialization Requirements (Chartered Financial Analyst)
        "Complete all of the following: COMM 321, COMM 421, COMM 433": [False, []],
        "Complete 1 of the following: ARBUS 302, MGMT 244": [False, []],
        "Complete 1 of the following: ECON 206, ECON 207, ECON 290": [False, []],
        "Complete 1 of the following: HRM 200, MSE 211, PSYCH 238": [False, []],
        "Complete 2 additional courses": [False, []]
    }


    # Base course requirements
    check_complete_all(
        "Complete all of the following: ACTSC 231, ACTSC 372, AFM 101, AFM 102, AFM 131, AMATH 350, CO 372, COMM 101, CS 330, ECON 101, ECON 102, MATBUS 471, STAT 371",
        [
            "ACTSC 231", "ACTSC 372", "AFM 101", "AFM 102", "AFM 131", "AMATH 350",
            "CO 372", "COMM 101", "CS 330", "ECON 101", "ECON 102", "MATBUS 371", "STAT 371"
        ],
        student_courses, farm_fin_reqs
    )

    check_n_from_list("Complete 1 of the following: ACTSC 446, MATBUS 470",
        ["ACTSC 446", "MATBUS 470"], n=1,
        student_courses=student_courses, major_reqs=farm_fin_reqs
    )

    check_n_from_list("Complete 1 of the following: AFM 231, LS 283",
        ["AFM 231", "LS 283"], n=1,
        student_courses=student_courses, major_reqs=farm_fin_reqs
    )

    check_n_from_list("Complete 1 of the following: CO 250, CO 255",
        ["CO 250", "CO 255"], n=1,
        student_courses=student_courses, major_reqs=farm_fin_reqs
    )

    check_n_from_list("Complete 1 of the following: CS 335, CS 476",
        ["CS 335", "CS 476"], n=1,
        student_courses=student_courses, major_reqs=farm_fin_reqs
    )

    check_n_from_list("Complete 1 of the following: MATH 237, MATH 247",
        ["MATH 237", "MATH 247"], n=1,
        student_courses=student_courses, major_reqs=farm_fin_reqs
    )
    
    check_complete_all(
        "Complete all of the following: COMM 321, COMM 421, COMM 433",
        ["COMM 321", "COMM 421", "COMM 433"],
        student_courses,
        farm_fin_reqs
    )

    # Marketing: ARBUS or MGMT
    check_n_from_list(
        "Complete 1 of the following: ARBUS 302, MGMT 244",
        ["ARBUS 302", "MGMT 244"],
        n=1,
        student_courses=student_courses,
        major_reqs=farm_fin_reqs
    )

    # Economics electives
    check_n_from_list(
        "Complete 1 of the following: ECON 206, ECON 207, ECON 290",
        ["ECON 206", "ECON 207", "ECON 290"],
        n=1,
        student_courses=student_courses,
        major_reqs=farm_fin_reqs
    )

    # HR/Organizational Behavior electives
    check_n_from_list(
        "Complete 1 of the following: HRM 200, MSE 211, PSYCH 238",
        ["HRM 200", "MSE 211", "PSYCH 238"],
        n=1,
        student_courses=student_courses,
        major_reqs=farm_fin_reqs
    )
    
    check_stat_330_or_334_req("Complete one of the following: all of (STAT 330, STAT 333, additional ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT) or (STAT 334, 2 additional courses from ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT)",
            student_courses=student_courses, major_reqs=farm_fin_reqs)

    additional_courses = student_courses[:2]  # Pick any two remaining courses
    if len(additional_courses) >= 2:
        farm_fin_reqs["Complete 2 additional courses"][0] = True
        farm_fin_reqs["Complete 2 additional courses"][1].extend(additional_courses)
        for course in additional_courses:
            student_courses.remove(course)

    return farm_fin_reqs


