from course_logic.helper import *

def check_biostats_major(student_courses):

  refine_courses(student_courses, ["MATH 239", "MATH 249", "ENGL 378", "MTHEL 300", "MATH 237", "MATH 247"])

  reqs = {
    "Complete all of: STAT 330, STAT 331, STAT 332, STAT 333, STAT 337, STAT 431, STAT 437, STAT 438": [False, []],
    "Complete one of: AMATH 231, AMATH 242, AMATH 250, AMATH 251, AMATH 350, CS 371, MATH 239, MATH 249": [False, []],
    "Complete one of: BIOL 239, HLTH 101": [False, []],
    "Complete one of: ENGL 378, MTHEL 300": [False, []],
    "Complete one of: MATH 237, MATH 247": [False, []],
    "Complete 2 additional STAT courses at the 300- or 400-level": [False, []],
    "Complete 2 additional math courses at the 300-or 400-level from the following subject codes: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [False, []],
    "Complete 3 additional math courses from the following subject codes: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [False, []],
  }

  check_complete_all("Complete all of: STAT 330, STAT 331, STAT 332, STAT 333, STAT 337, STAT 431, STAT 437, STAT 438",
                     ["STAT 330", "STAT 331", "STAT 332", "STAT 333", "STAT 337", "STAT 431", "STAT 437", "STAT 438"],
                     student_courses, reqs)

  check_n_from_list("Complete one of: AMATH 231, AMATH 242, AMATH 250, AMATH 251, AMATH 350, CS 371, MATH 239, MATH 249",
                    ["AMATH 231", "AMATH 250", "AMATH 251", "MATH 239", "MATH 249", "AMATH 350", "AMATH 242", "CS 371"],
                                  1,
                                  student_courses,
                                  reqs)

  check_n_from_list("Complete one of: BIOL 239, HLTH 101",
                    ["BIOL 239", "HLTH 101"],
                    1, student_courses, reqs)

  check_n_from_list("Complete one of: ENGL 378, MTHEL 300",
                    ["ENGL 378", "MTHEL 300"],
                    1, student_courses, reqs)

  check_n_from_list("Complete one of: MATH 237, MATH 247",
                    ["MATH 237", "MATH 247"],
                    1, student_courses, reqs)

  check_n_courses("Complete 2 additional STAT courses at the 300- or 400-level",
                  300,
                  ["STAT"],
                  2, student_courses, reqs)

  check_n_courses("Complete 2 additional math courses at the 300-or 400-level from the following subject codes: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT",
                  300,
                  ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                  2, student_courses, reqs)

  check_n_courses("Complete 3 additional math courses from the following subject codes: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT",
                  100,
                  ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                  3, student_courses, reqs)

  return reqs

