from course_logic.helper import *

def check_econ_minor(student_courses):

    reqs = {
        "Complete all of: ECON 101, ECON 102, ECON 201": [False, []],
        "Complete 1 of: ECON 206, ECON 207": [False, []],
        "Complete 2.0 additional units of ECON courses at the 200-level or above": [False, []],
    }

    check_complete_all("Complete all of: ECON 101, ECON 102, ECON 201",
                       ["ECON 101", "ECON 102", "ECON 201"],
                       student_courses, reqs)
    
    check_n_from_list("Complete 1 of: ECON 206, ECON 207",
                      ["ECON 206", "ECON 207"],
                      1, student_courses, reqs)
    
    check_n_courses("Complete 2.0 additional units of ECON courses at the 200-level or above",
                    200, ["ECON"], 4, student_courses, reqs)
    
    return reqs