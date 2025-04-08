from course_logic.helper import *

def check_data_science_major(student_courses):
 
    refine_courses(student_courses, ["CS 136L", "CS 136", "CS 146", "ENGL 378", "MTHEL 300",
     "MATH 237", "MATH 247", "MATH 239", "MATH 249"])
 
    data_science_reqs = {
        "Complete all of the following: CS 136L, CS 341, CS 348, CS 431, STAT 330, STAT 331, STAT 332, STAT 333, STAT 341": [False, []],
        "Complete 1 of the following: CS 136, CS 146": [False, []],
        "Complete 1 of the following: CS 240, CS 240E": [False, []],
        "Complete 1 of the following: CS 241, CS 241E": [False, []],
        "Complete 1 of the following: CS 245, CS 245E": [False, []],
        "Complete 1 of the following: CS 246, CS 246E": [False, []],
        "Complete 1 of the following: CS 251, CS 251E": [False, []],
        "Complete 1 of the following: CS 480, CS 484, CS 485, CS 486, STAT 441": [False, []],
        "Complete 2 of the following: STAT 431, STAT 440, STAT 441, STAT 442, STAT 443, STAT 444": [False, []],
        "Complete 1 of the following: ENGL 378, MTHEL 300": [False, []],
        "Complete 1 of the following: MATH 237, MATH 247": [False, []],
        "Complete 1 of the following: MATH 239, MATH 249": [False, []],
        "Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [False, []]
    }
 
    # Req 1: Core courses
    check_complete_all("Complete all of the following: CS 136L, CS 341, CS 348, CS 431, STAT 330, STAT 331, STAT 332, STAT 333, STAT 341",
                        ["CS 136L", "CS 341", "CS 348", "CS 431", "STAT 330", "STAT 331", "STAT 332", "STAT 333", "STAT 341"],
                        student_courses, data_science_reqs)
 
    # Req 2-7: One course from each list
    check_n_from_list("Complete 1 of the following: CS 136, CS 146",
                      ["CS 136", "CS 146"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
    check_n_from_list("Complete 1 of the following: CS 240, CS 240E",
                      ["CS 240", "CS 240E"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
    check_n_from_list("Complete 1 of the following: CS 241, CS 241E",
                      ["CS 241", "CS 241E"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
    check_n_from_list("Complete 1 of the following: CS 245, CS 245E",
                      ["CS 245", "CS 245E"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
    check_n_from_list("Complete 1 of the following: CS 246, CS 246E",
                      ["CS 246", "CS 246E"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
    check_n_from_list("Complete 1 of the following: CS 251, CS 251E",
                      ["CS 251", "CS 251E"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
 
    # Req 8: One course from machine learning list
    check_n_from_list("Complete 1 of the following: CS 480, CS 484, CS 485, CS 486, STAT 441",
                      ["CS 480", "CS 484", "CS 485", "CS 486", "STAT 441"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
 
    # Req 9: Two courses from stats list
    check_n_from_list("Complete 2 of the following: STAT 431, STAT 440, STAT 441, STAT 442, STAT 443, STAT 444",
                      ["STAT 431", "STAT 440", "STAT 441", "STAT 442", "STAT 443", "STAT 444"], n=2, student_courses=student_courses, major_reqs=data_science_reqs)
 
    #Req 10: Communication Course
    check_n_from_list("Complete 1 of the following: ENGL 378, MTHEL 300",
                      ["ENGL 378", "MTHEL 300"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
 
    #Req 11:  Calculus 2
    check_n_from_list("Complete 1 of the following: MATH 237, MATH 247",
                      ["MATH 237", "MATH 247"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
 
    #Req 12: C&O course
    check_n_from_list("Complete 1 of the following: MATH 239, MATH 249",
                      ["MATH 239", "MATH 249"], n=1, student_courses=student_courses, major_reqs=data_science_reqs)
 
    #Req 13: 1 additional course at 300/400 level from ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT
    check_n_courses("Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT",
                    eligible_levels=300,
                    subject_codes=["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                    n=1,
                    student_courses=student_courses,
                    major_reqs=data_science_reqs)
 
    return data_science_reqs