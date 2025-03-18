from course_logic.helper import *

def check_data_science_major(student_courses):
    """
    Checks if a student has completed the requirements for the BMath Data Science major.

    Args:
        student_courses: A list of student's completed courses.

    Returns:
        A dictionary of the program requirements and their completion status.
    """

    #Core Courses Check required
    
    #modify student courses to remove core courses 

    data_science_reqs = {
        "Complete all of the following: CS136L, CS341, CS348, CS431, STAT330, STAT331, STAT332, STAT333, STAT341": [False, []],
        "Complete 1 of the following: CS136, CS146": [False, []],
        "Complete 1 of the following: CS240, CS240E": [False, []],
        "Complete 1 of the following: CS241, CS241E": [False, []],
        "Complete 1 of the following: CS245, CS245E": [False, []],
        "Complete 1 of the following: CS246, CS246E": [False, []],
        "Complete 1 of the following: CS251, CS251E": [False, []],
        "Complete 1 of the following: CS480, CS484, CS485, CS486, STAT441": [False, []],
        "Complete 2 of the following: STAT431, STAT440, STAT441, STAT442, STAT443, STAT444": [False, []],
        "Complete 1 of the following: ENGL378, MTHEL300": [False, []],
        "Complete 1 of the following: MATH237, MATH247": [False, []],
        "Complete 1 of the following: MATH239, MATH249": [False, []],
        "Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [False, []]
    }

    # Req 1: Core courses
    check_complete_all("Complete all of the following: CS136L, CS341, CS348, CS431, STAT330, STAT331, STAT332, STAT333, STAT341",
                        ["CS136L", "CS341", "CS348", "CS431", "STAT330", "STAT331", "STAT332", "STAT333", "STAT341"],
                        student_courses, data_science_reqs)

    # Req 2-7: One course from each list
    check_n_from_list("Complete 1 of the following: CS136, CS146",
                      ["CS136", "CS146"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
    check_n_from_list("Complete 1 of the following: CS240, CS240E",
                      ["CS240", "CS240E"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
    check_n_from_list("Complete 1 of the following: CS241, CS241E",
                      ["CS241", "CS241E"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
    check_n_from_list("Complete 1 of the following: CS245, CS245E",
                      ["CS245", "CS245E"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
    check_n_from_list("Complete 1 of the following: CS246, CS246E",
                      ["CS246", "CS246E"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
    check_n_from_list("Complete 1 of the following: CS251, CS251E",
                      ["CS251", "CS251E"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)

    # Req 8: One course from machine learning list
    check_n_from_list("Complete 1 of the following: CS480, CS484, CS485, CS486, STAT441",
                      ["CS480", "CS484", "CS485", "CS486", "STAT441"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)

    # Req 9: Two courses from stats list
    check_n_from_list("Complete 2 of the following: STAT431, STAT440, STAT441, STAT442, STAT443, STAT444",
                      ["STAT431", "STAT440", "STAT441", "STAT442", "STAT443", "STAT444"], n=2, student_courses=student_courses, major_reqs=data_science_reqs)

    #Req 10: Communication Course
    check_n_from_list("Complete 1 of the following: ENGL378, MTHEL300",
                      ["ENGL378", "MTHEL300"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)

    #Req 11:  Calculus 2
    check_n_from_list("Complete 1 of the following: MATH237, MATH247",
                      ["MATH237", "MATH247"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)

    #Req 12: C&O course
    check_n_from_list("Complete 1 of the following: MATH239, MATH249",
                      ["MATH239", "MATH249"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)

    #Req 13: 1 additional course at 300/400 level from ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT
    check_n_courses("Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT",
                    eligible_levels=300,
                    subject_codes=["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                    n=1,
                    student_courses=student_courses,
                    major_reqs=data_science_reqs)

    return data_science_reqs

