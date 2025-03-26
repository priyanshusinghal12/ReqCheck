from course_logic.helper import *
# from helper import *

def check_pmath_major(student_courses):

  refine_courses(student_courses, ["MATH 237", "MATH 247", "MATH 239", "MATH 249"])

  pmath_reqs = {
    "Complete all of: PMATH 347, PMATH 348, PMATH 351, PMATH 352, PMATH 450": [False, []],
    "Complete one of: MATH 237, MATH 247": [False, []],
    "Complete one of: MATH 239, MATH 249": [False, []],
    "Complete one of: PMATH 365, PMATH 367": [False, []],
    "Complete 3 additional PMATH courses at the 400 level": [False, []],
    "Complete 2 additional 400 level courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [False, []]
  }

  check_complete_all("Complete all of: PMATH 347, PMATH 348, PMATH 351, PMATH 352, PMATH 450",
                   ["PMATH 347", "PMATH 348", "PMATH 351", "PMATH 352", "PMATH 450"],
                   student_courses, pmath_reqs)

  check_n_from_list(current_requirement = "Complete one of: MATH 237, MATH 247",
                  required_courses = ["MATH 237", "MATH 247"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = pmath_reqs)

  check_n_from_list(current_requirement = "Complete one of: MATH 239, MATH 249",
                  required_courses = ["MATH 239", "MATH 249"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = pmath_reqs)

  check_n_from_list(current_requirement = "Complete one of: PMATH 365, PMATH 367",
                  required_courses = ["PMATH 365", "PMATH 367"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = pmath_reqs)

  check_n_courses(current_requirement = "Complete 3 additional PMATH courses at the 400 level",
                  eligible_levels = 400,
                  subject_codes = ["PMATH"],
                  n = 3,
                  student_courses = student_courses,
                  major_reqs = pmath_reqs)

  check_n_courses(current_requirement = "Complete 2 additional 400 level courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT",
                  eligible_levels = 400,
                  subject_codes = ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                  n = 2,
                  student_courses = student_courses,
                  major_reqs = pmath_reqs)

  return pmath_reqs

# test = ["ECON 201", "AFM 101", "PMATH 347", "PMATH 348", "PMATH 351", "PMATH 352", "PMATH 450", "MATH 237", "MATH 239", "PMATH 365", "PMATH 451", "PMATH 452", "PMATH 453", "STAT 440", "CS 486"]

# print(check_pmath_major(test))