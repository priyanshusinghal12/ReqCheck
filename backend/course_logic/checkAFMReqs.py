from course_logic.helper import *

def check_afm_ba_reqs(student_courses):
    """
    Checks if a student has completed the requirements for the AFM major.

    Args:
        student_courses: A list of student's completed courses.

    Returns:
        A dictionary of AFM program requirements and their completion status.
    """

    afm_ba_reqs = {
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102": [False, []],
        "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127": [False, []],
        "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273": [False, []],
        "Complete 1 of the following: AFM 311, SFM 309": [False, []],
        "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374": [False, []],
        "Complete 1 of the following AFM 345, AFM 346": [False, []],
        "Complete 2 of the following: ACTSC 423, AFM 323, AFM 341, AFM 345, AFM 346, AFM 347, AFM 423, AFM 444, AFM 445, AFM 446, AFM 447, AFM 448, STAT 374": [False, []],
    }

    # Req 1: Core AFM, BET, COMMST, ECON courses
    check_complete_all(
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102",
        [
            "AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191",
            "AFM 205", "AFM 206", "AFM 207", "AFM 208", "AFM 241", "AFM 244",
            "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
            "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101",
            "ECON 102"
        ],
        student_courses, afm_ba_reqs
    )

    # Req 2-5: One-of requirements
    check_n_from_list(
        "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127",
        ["ACTSC 127", "AFM 121", "AFM 127"], n=1, student_courses=student_courses,
        major_reqs=afm_ba_reqs
    )
    check_n_from_list(
        "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273",
        ["ACTSC 291", "AFM 272", "AFM 273"], n=1, student_courses=student_courses,
        major_reqs=afm_ba_reqs
    )
    check_n_from_list(
        "Complete 1 of the following: AFM 311, SFM 309",
        ["AFM 311", "SFM 309"], n=1, student_courses=student_courses,
        major_reqs=afm_ba_reqs
    )
    check_n_from_list(
        "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374",
        ["AFM 323", "AFM 341", "AFM 345", "AFM 346", "STAT 374"], n=1,
        student_courses=student_courses, major_reqs=afm_ba_reqs
    )
    check_n_from_list(
        "Complete 1 of the following AFM 345, AFM 346",
        ["AFM 345", "AFM 346"], n=1,
        student_courses=student_courses, major_reqs=afm_ba_reqs
    )
    check_n_from_list(
        "Complete 2 of the following: ACTSC 423, AFM 323, AFM 341, AFM 345, AFM 346, AFM 347, AFM 423, AFM 444, AFM 445, AFM 446, AFM 447, AFM 448, STAT 374",
        ["ACTSC 423", "AFM 323", "AFM 341", "AFM 345", "AFM 346", "AFM 347", "AFM 423", "AFM 444", "AFM 445", "AFM 446", "AFM 447", "AFM 448", "STAT 374"], 
        n=2, student_courses=student_courses, major_reqs=afm_ba_reqs
    )

    return afm_ba_reqs

def check_afm_entrepreneurial_mindset_reqs(student_courses):
    """
    Checks if a student has completed the requirements for the AFM major.

    Args:
        student_courses: A list of student's completed courses.

    Returns:
        A dictionary of AFM program requirements and their completion status.
    """

    afm_entrepreneurial_mindset_reqs = {
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102": [False, []],
        "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127": [False, []],
        "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273": [False, []],
        "Complete 1 of the following: AFM 311, SFM 309": [False, []],
        "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374": [False, []],
        "Complete all of the following: BET 320, BET 340": [False, []],
        "Complete 3 courses from the following: AFM 326, AFM 377, AFM 426, AFM 470, BET 350, BET 400, BET 420, BET 430, BET 450, BET 460, BET 470, BET 580, ENBUS 203, MGMT 220": [False, []]
    }

    check_complete_all(
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102",
        [
            "AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191",
            "AFM 205", "AFM 206", "AFM 207", "AFM 208", "AFM 241", "AFM 244",
            "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
            "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101",
            "ECON 102"
        ],
        student_courses, afm_entrepreneurial_mindset_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127",
        ["ACTSC 127", "AFM 121", "AFM 127"], n=1, student_courses=student_courses,
        major_reqs=afm_entrepreneurial_mindset_reqs
    )
    check_n_from_list(
        "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273",
        ["ACTSC 291", "AFM 272", "AFM 273"], n=1, student_courses=student_courses,
        major_reqs=afm_entrepreneurial_mindset_reqs
    )
    check_n_from_list(
        "Complete 1 of the following: AFM 311, SFM 309",
        ["AFM 311", "SFM 309"], n=1, student_courses=student_courses,
        major_reqs=afm_entrepreneurial_mindset_reqs
    )
    check_n_from_list(
        "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374",
        ["AFM 323", "AFM 341", "AFM 345", "AFM 346", "STAT 374"], n=1,
        student_courses=student_courses, major_reqs=afm_entrepreneurial_mindset_reqs
    )

    check_complete_all(
        "Complete all of the following: BET 320, BET 340",
        ["BET 320", "BET 340"],
        student_courses, afm_entrepreneurial_mindset_reqs
    )

    check_n_from_list(
        "Complete 3 courses from the following: AFM 326, AFM 377, AFM 426, AFM 470, BET 350, BET 400, BET 420, BET 430, BET 450, BET 460, BET 470, BET 580, ENBUS 203, MGMT 220",
        [
            "AFM 326", "AFM 377", "AFM 426", "AFM 470", "BET 350", "BET 400", "BET 420",
            "BET 430", "BET 450", "BET 460", "BET 470", "BET 580", "ENBUS 203", "MGMT 220"
        ],
        n=3, student_courses=student_courses, major_reqs=afm_entrepreneurial_mindset_reqs
    )

    return afm_entrepreneurial_mindset_reqs

def check_afm_enterprise_performance_risk_reqs(student_courses):
    """
    Checks if a student has completed the requirements for the AFM: Enterprise Performance and Risk Specialization.

    Args:
        student_courses: A list of student's completed courses.

    Returns:
        A dictionary of AFM program requirements and their completion status.
    """
    afm_enterprise_performance_risk_reqs = {
        # Base AFM requirements
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102": [False, []],
        "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127": [False, []],
        "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273": [False, []],
        "Complete 1 of the following: AFM 311, SFM 309": [False, []],
        "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374": [False, []],

        # Specialization requirements
        "Complete all of the following: AFM 434, AFM 452, AFM 482": [False, []],
        "Complete 3 of the following: AFM 276, AFM 322, AFM 345, AFM 346, AFM 347, AFM 445, AFM 451, AFM 470, AFM 477, AFM 485, SFM 301, SFM 310, SFM 311": [False, []]
    }

    # Base checks
    check_complete_all(
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102",
        [
            "AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191",
            "AFM 205", "AFM 206", "AFM 207", "AFM 208", "AFM 241", "AFM 244",
            "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
            "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101",
            "ECON 102"
        ],
        student_courses, afm_enterprise_performance_risk_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127",
        ["ACTSC 127", "AFM 121", "AFM 127"], n=1,
        student_courses=student_courses, major_reqs=afm_enterprise_performance_risk_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273",
        ["ACTSC 291", "AFM 272", "AFM 273"], n=1,
        student_courses=student_courses, major_reqs=afm_enterprise_performance_risk_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: AFM 311, SFM 309",
        ["AFM 311", "SFM 309"], n=1,
        student_courses=student_courses, major_reqs=afm_enterprise_performance_risk_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374",
        ["AFM 323", "AFM 341", "AFM 345", "AFM 346", "STAT 374"], n=1,
        student_courses=student_courses, major_reqs=afm_enterprise_performance_risk_reqs
    )

    # Specialization checks
    check_complete_all(
        "Complete all of the following: AFM 434, AFM 452, AFM 482",
        ["AFM 434", "AFM 452", "AFM 482"],
        student_courses, afm_enterprise_performance_risk_reqs
    )

    check_n_from_list(
        "Complete 3 of the following: AFM 276, AFM 322, AFM 345, AFM 346, AFM 347, AFM 445, AFM 451, AFM 470, AFM 477, AFM 485, SFM 301, SFM 310, SFM 311",
        [
            "AFM 276", "AFM 322", "AFM 345", "AFM 346", "AFM 347", "AFM 445",
            "AFM 451", "AFM 470", "AFM 477", "AFM 485", "SFM 301", "SFM 310", "SFM 311"
        ],
        n=3, student_courses=student_courses, major_reqs=afm_enterprise_performance_risk_reqs
    )

    return afm_enterprise_performance_risk_reqs

def check_afm_financial_markets_reqs(student_courses):
    """
    Checks if a student has completed the requirements for the AFM: Financial Markets Specialization.

    Args:
        student_courses: A list of student's completed courses.

    Returns:
        A dictionary of AFM program requirements and their completion status.
    """
    afm_financial_markets_reqs = {
        # Base AFM requirements
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102": [False, []],
        "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127": [False, []],
        "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273": [False, []],
        "Complete 1 of the following: AFM 311, SFM 309": [False, []],
        "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374": [False, []],

        # Specialization requirement
        "Complete 1 of the following: ACTSC 423, AFM 276, AFM 322, AFM 324, AFM 326, AFM 328, AFM 329, AFM 377, AFM 422, AFM 423, AFM 425, AFM 426, AFM 427, AFM 428, AFM 429, AFM 434, AFM 470, AFM 477, AFM 478, SFM 310, SFM 412": [False, []]
    }

    # Base checks
    check_complete_all(
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102",
        [
            "AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191",
            "AFM 205", "AFM 206", "AFM 207", "AFM 208", "AFM 241", "AFM 244",
            "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
            "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101",
            "ECON 102"
        ],
        student_courses, afm_financial_markets_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127",
        ["ACTSC 127", "AFM 121", "AFM 127"], n=1,
        student_courses=student_courses, major_reqs=afm_financial_markets_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273",
        ["ACTSC 291", "AFM 272", "AFM 273"], n=1,
        student_courses=student_courses, major_reqs=afm_financial_markets_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: AFM 311, SFM 309",
        ["AFM 311", "SFM 309"], n=1,
        student_courses=student_courses, major_reqs=afm_financial_markets_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374",
        ["AFM 323", "AFM 341", "AFM 345", "AFM 346", "STAT 374"], n=1,
        student_courses=student_courses, major_reqs=afm_financial_markets_reqs
    )

    # Specialization requirement: 1 course from financial markets list
    check_n_from_list(
        "Complete 1 of the following: ACTSC 423, AFM 276, AFM 322, AFM 324, AFM 326, AFM 328, AFM 329, AFM 377, AFM 422, AFM 423, AFM 425, AFM 426, AFM 427, AFM 428, AFM 429, AFM 434, AFM 470, AFM 477, AFM 478, SFM 310, SFM 412",
        [
            "ACTSC 423", "AFM 276", "AFM 322", "AFM 324", "AFM 326", "AFM 328",
            "AFM 329", "AFM 377", "AFM 422", "AFM 423", "AFM 425", "AFM 426",
            "AFM 427", "AFM 428", "AFM 429", "AFM 434", "AFM 470", "AFM 477",
            "AFM 478", "SFM 310", "SFM 412"
        ],
        n=1, student_courses=student_courses, major_reqs=afm_financial_markets_reqs
    )

    return afm_financial_markets_reqs

def check_afm_professional_accountant_reqs(student_courses):
    """
    Checks if a student has completed the requirements for the AFM: Professional Accountant Specialization.

    Args:
        student_courses: A list of student's completed courses.

    Returns:
        A dictionary of AFM program requirements and their completion status.
    """
    afm_professional_accountant_reqs = {
        # Base AFM requirements
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102": [False, []],
        "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127": [False, []],
        "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273": [False, []],
        "Complete 1 of the following: AFM 311, SFM 309": [False, []],
        "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374": [False, []],

        # Specialization-specific requirement
        "Complete all of the following: AFM 362, AFM 382, AFM 451, AFM 462, AFM 482, AFM 491": [False, []]
    }

    # Base checks
    check_complete_all(
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102",
        [
            "AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191",
            "AFM 205", "AFM 206", "AFM 207", "AFM 208", "AFM 241", "AFM 244",
            "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
            "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101",
            "ECON 102"
        ],
        student_courses, afm_professional_accountant_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127",
        ["ACTSC 127", "AFM 121", "AFM 127"], n=1,
        student_courses=student_courses, major_reqs=afm_professional_accountant_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273",
        ["ACTSC 291", "AFM 272", "AFM 273"], n=1,
        student_courses=student_courses, major_reqs=afm_professional_accountant_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: AFM 311, SFM 309",
        ["AFM 311", "SFM 309"], n=1,
        student_courses=student_courses, major_reqs=afm_professional_accountant_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374",
        ["AFM 323", "AFM 341", "AFM 345", "AFM 346", "STAT 374"], n=1,
        student_courses=student_courses, major_reqs=afm_professional_accountant_reqs
    )

    # Specialization check
    check_complete_all(
        "Complete all of the following: AFM 362, AFM 382, AFM 451, AFM 462, AFM 482, AFM 491",
        ["AFM 362", "AFM 382", "AFM 451", "AFM 462", "AFM 482", "AFM 491"],
        student_courses, afm_professional_accountant_reqs
    )

    return afm_professional_accountant_reqs

def check_afm_sustainability_reqs(student_courses):
    """
    Checks if a student has completed the requirements for the AFM: Sustainability Specialization.

    Args:
        student_courses: A list of student's completed courses.

    Returns:
        A dictionary of AFM program requirements and their completion status.
    """
    afm_sustainability_reqs = {
        # AFM base requirements
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102": [False, []],
        "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127": [False, []],
        "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273": [False, []],
        "Complete 1 of the following: AFM 311, SFM 309": [False, []],
        "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374": [False, []],

        # Sustainability specialization requirements
        "Complete 1 of the following: ENBUS 102, ENVS 195, ENVS 220, INDEV 100": [False, []],
        "Complete 2 of the following: ENVS 200, ENVS 205, ENVS 220, INDEV 200": [False, []],
        "Complete all of the following either (AFM 485, ENBUS 202, ENBUS 407) or (ENBUS 310, ENBUS 408, ENBUS 410)": [False, []]
    }

    # === AFM BASE REQUIREMENTS ===
    check_complete_all(
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102",
        [
            "AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191",
            "AFM 205", "AFM 206", "AFM 207", "AFM 208", "AFM 241", "AFM 244",
            "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
            "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101",
            "ECON 102"
        ],
        student_courses, afm_sustainability_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127",
        ["ACTSC 127", "AFM 121", "AFM 127"], n=1,
        student_courses=student_courses, major_reqs=afm_sustainability_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273",
        ["ACTSC 291", "AFM 272", "AFM 273"], n=1,
        student_courses=student_courses, major_reqs=afm_sustainability_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: AFM 311, SFM 309",
        ["AFM 311", "SFM 309"], n=1,
        student_courses=student_courses, major_reqs=afm_sustainability_reqs
    )

    check_n_from_list(
        "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374",
        ["AFM 323", "AFM 341", "AFM 345", "AFM 346", "STAT 374"], n=1,
        student_courses=student_courses, major_reqs=afm_sustainability_reqs
    )

    # === SPECIALIZATION REQUIREMENTS ===
    check_n_from_list(
        "Complete 1 of the following: ENBUS 102, ENVS 195, ENVS 220, INDEV 100",
        ["ENBUS 102", "ENVS 195", "ENVS 220", "INDEV 100"], n=1,
        student_courses=student_courses, major_reqs=afm_sustainability_reqs
    )

    check_n_from_list(
        "Complete 2 of the following: ENVS 200, ENVS 205, ENVS 220, INDEV 200",
        ["ENVS 200", "ENVS 205", "ENVS 220", "INDEV 200"], n=2,
        student_courses=student_courses, major_reqs=afm_sustainability_reqs
    )

    group_1 = ["AFM 485", "ENBUS 202", "ENBUS 407"]
    group_2 = ["ENBUS 310", "ENBUS 408", "ENBUS 410"]

    check_one_group_complete_all(
        "Complete all of the following either (AFM 485, ENBUS 202, ENBUS 407) or (ENBUS 310, ENBUS 408, ENBUS 410)",
        [group_1, group_2], student_courses,
        major_reqs=afm_sustainability_reqs
    )

    return afm_sustainability_reqs
