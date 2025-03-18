from helper import *
def check_computer_science_major(student_courses):
    """
    Checks if a student has completed the requirements for the Computer Science Major.

    Args:
        student_courses: A list of student's completed courses.

    Returns:
        A dictionary of major requirements and their completion status.
    """

    cs_major_reqs = {
        "Complete all of: CS 136L, CS 341, CS 350": [False, []],
        "Complete one of: AMATH 242, CS 370, CS 371": [False, []],
        "Complete one of: CS 240, CS 240E": [False, []],
        "Complete one of: CS 241, CS 241E": [False, []],
        "Complete one of: CS 245, CS 245E": [False, []],
        "Complete one of: CS 246, CS 246E": [False, []],
        "Complete one of: CS 251, CS 251E": [False, []],
        "Complete one of: CS 360, CS 365": [False, []],
        "Complete one of: MATH 237, MATH 247": [False, []],
        "Complete one of: MATH 239, MATH 249": [False, []],
        "Complete 1 additional CS course chosen from CS340-CS398, CS440-CS489": [False, []],
        "Complete 2 additional CS courses chosen from CS440-CS489": [False, []],
        "Complete 3 additional courses from: ACTSC, AMATH, CO, PMATH, STAT": [False, []],
        "Complete 1 of: CO487, CS499T, STAT440, CS440-CS498, CS600-CS700": [False, []],
        "1.0 unit of humanities": [False, []],
        "1.0 unit of social sciences": [False, []],
        "0.5 unit of pure sciences": [False, []],
        "0.5 unit of pure and applied sciences": [False, []],
        "1.5 units with the same subject, including at least 0.5 unit at 300-level or higher": [False, []], 
        "Non-math course": [False, []] 
    
    }

    math_course_codes = ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"]

    courses_to_remove = ["ACTSC 221", "CO 353", "CO 380", "CO 480"]

    # Check and remove only if the course exists in student_courses
    for course in courses_to_remove:
        if course in student_courses:
            student_courses.remove(course)

    # Req 1: Core courses
    check_complete_all("Complete all of: CS 136L, CS 341, CS 350",
                       ["CS 136L", "CS 341", "CS 350"],
                       student_courses, cs_major_reqs)

    # Req 2: Computational Mathematics
    check_n_from_list("Complete one of: AMATH 242, CS 370, CS 371",
                      ["AMATH 242", "CS 370", "CS 371"], n=1, student_courses=student_courses, major_reqs=cs_major_reqs)

    # Req 3-7: Core CS courses (Data Structures, Sequential Programs, Logic, OOP, Computer Organization)
    check_n_from_list("Complete one of: CS 240, CS 240E",
                      ["CS 240", "CS 240E"], n=1, student_courses=student_courses, major_reqs=cs_major_reqs)
    check_n_from_list("Complete one of: CS 241, CS 241E",
                      ["CS 241", "CS 241E"], n=1, student_courses=student_courses, major_reqs=cs_major_reqs)
    check_n_from_list("Complete one of: CS 245, CS 245E",
                      ["CS 245", "CS 245E"], n=1, student_courses=student_courses, major_reqs=cs_major_reqs)
    check_n_from_list("Complete one of: CS 246, CS 246E",
                      ["CS 246", "CS 246E"], n=1, student_courses=student_courses, major_reqs=cs_major_reqs)
    check_n_from_list("Complete one of: CS 251, CS 251E",
                      ["CS 251", "CS 251E"], n=1, student_courses=student_courses, major_reqs=cs_major_reqs)

    # Req 8: Theory of Computation
    check_n_from_list("Complete one of: CS 360, CS 365",
                      ["CS 360", "CS 365"], n=1, student_courses=student_courses, major_reqs=cs_major_reqs)

    # Req 9-10: Calculus 3 and Combinatorics
    check_n_from_list("Complete one of: MATH 237, MATH 247",
                      ["MATH 237", "MATH 247"], n=1, student_courses=student_courses, major_reqs=cs_major_reqs)
    check_n_from_list("Complete one of: MATH 239, MATH 249",
                      ["MATH 239", "MATH 249"], n=1, student_courses=student_courses, major_reqs=cs_major_reqs)

    # Req 11: 1 additional CS course chosen from CS340-CS398, CS440-CS489
    check_course_range("Complete 1 additional CS course chosen from CS340-CS398, CS440-CS489", "CS", 340, 398, student_courses, cs_major_reqs)
    if not cs_major_reqs["Complete 1 additional CS course chosen from CS340-CS398, CS440-CS489"][0]:
      check_course_range("Complete 1 additional CS course chosen from CS340-CS398, CS440-CS489", "CS", 440, 489, student_courses, cs_major_reqs)

    # Req 12: 2 additional CS courses chosen from CS440-CS489
    check_course_range("Complete 2 additional CS courses chosen from CS440-CS489", "CS", 440, 489, student_courses, cs_major_reqs, num_courses_required=2)

    # Req 13: 3 additional courses from: ACTSC, AMATH, CO, PMATH, STAT
    check_n_courses("Complete 3 additional courses from: ACTSC, AMATH, CO, PMATH, STAT",
                    eligible_levels=100,
                    subject_codes=["ACTSC", "AMATH", "CO", "PMATH", "STAT"],
                    n=3,
                    student_courses=student_courses,
                    major_reqs=cs_major_reqs)
    
    # Req 14: New requirement
    check_n_from_list("Complete 1 of: CO487, CS499T, STAT440, CS440-CS498, CS600-CS700",
                      ["CO 487", "CS 499T", "STAT 440"], n=1, student_courses=student_courses, major_reqs=cs_major_reqs)

    if not cs_major_reqs["Complete 1 of: CO487, CS499T, STAT440, CS440-CS498, CS600-CS700"][0]:
        check_course_range("Complete 1 of: CO487, CS499T, STAT440, CS440-CS498, CS600-CS700", "CS", 440, 498, student_courses, cs_major_reqs)

    if not cs_major_reqs["Complete 1 of: CO487, CS499T, STAT440, CS440-CS498, CS600-CS700"][0]:
        check_course_range("Complete 1 of: CO487, CS499T, STAT440, CS440-CS498, CS600-CS700", "CS", 600, 700, student_courses, cs_major_reqs)

    
    # Non Math Course Requirements
    check_n_from_list("1.0 unit of humanities",
                                  ["CHINA", "CLAS", "CMW", "COMMST", "CROAT", "DAC", "DUTCH", "EASIA", "ENGL", "FINE", "FR", "GER", "GRK", "HIST", "HUMSC", "ITAL", "ITALST", "JAPAN", "JS", "KOREA", "LAT", "MEDVL", "MUSIC", "PHIL", "PORT", "REES", "RS", "RUSS", "SI", "SPAN", "THPERF", "VCULT"],
                                  2, student_courses, cs_major_reqs)  # Use cs_major_reqs

    check_n_from_list("1.0 unit of social sciences", ["AFM", "ANTH", "APPLS", "ARBUS", "BET", "BUS", "COMM", "ECON", "ENBUS", "GEOG", "GSJ", "HRM", "INDEV", "INDG", "INTST", "LS", "MSCI", "PACS", "PSCI", "PSYCH", "REC", "SDS", "SMF", "SOC", "SOCWK", "STV"],
                        2, student_courses, cs_major_reqs)  # Use cs_major_reqs

    check_one_course_from_list("0.5 unit of pure sciences",
                                  ["BIOL", "CHEM", "EARTH", "PHYS", "SCI"],
                                  student_courses, cs_major_reqs)  # Use cs_major_reqs

    check_one_course_from_list("0.5 unit of pure and applied sciences",
                                  ["BIOL", "CHEM", "EARTH", "PHYS", "SCI", "ENVS", "ERS", "HEALTH", "KIN", "MNS", "PLAN"],
                                  student_courses, cs_major_reqs)  # Use cs_major_reqs

    # Elective depth requirements
    # Note: We're ignoring the prerequisite chain part. 
    check_concentration("1.5 units with the same subject, including at least 0.5 unit at 300-level or higher",
                                   eligible_levels=300, subject_codes=["CHINA", "CLAS", "CMW", "COMMST", "CROAT", "DAC", 
                                                                       "DUTCH", "EASIA", "ENGL", "FINE", "FR", "GER", "GRK",
                                                                       "HIST", "HUMSC", "ITAL", "ITALST", "JAPAN", "JS", "KOREA", "LAT", 
                                                                       "MEDVL", "MUSIC", "PHIL", "PORT", "REES", "RS", "RUSS", "SI", "SPAN", 
                                                                       "THPERF", "VCULT", "AFM", "ANTH", "APPLS", "ARBUS", "BET", "BUS", "COMM",
                                                                       "ECON", "ENBUS", "GEOG", "GSJ", "HRM", "INDEV", "INDG", "INTST", "LS", 
                                                                       "MSCI", "PACS", "PSCI", "PSYCH", "REC", "SDS", "SMF", "SOC", "SOCWK", 
                                                                       "STV", "BIOL", "CHEM", "EARTH", "PHYS", "SCI", "ENVS", "ERS", "HEALTH", "KIN", "MNS", "PLAN"],
                                   n=3, student_courses=student_courses, major_reqs=cs_major_reqs)  # Use cs_major_reqs

    non_math_courses = [course for course in student_courses 
                            if course.split(" ")[0] not in ["ACTSC", "AMATH", "CO", "CS", "MATH", "PMATH", "STAT"]]
    
    if non_math_courses:
        cs_major_reqs["Non-math course"][0] = True
        cs_major_reqs["Non-math course"][1].extend(non_math_courses[:1])  # Add the first non-math course
        student_courses.remove(non_math_courses[0])  # Remove the course from student_courses

    

    return cs_major_reqs