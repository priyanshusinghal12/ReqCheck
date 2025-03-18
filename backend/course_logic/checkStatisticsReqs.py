from backend.course_logic.helper import *

def check_stats_major(student_courses):

  stat_reqs = {
    "Complete all of: STAT 330/331/332/333": [False, []],
    "Complete one of: ENGL 378/MTHEL 300": [False, []],
    "Complete one of: MATH 237/247": [False, []],
    "Complete one of: AMATH 231/AMATH 242/AMATH 250/AMATH 251/AMATH 350/CS 371/MATH 239/MATH 249": [False, []],
    "Complete 2 additional STAT courses at the 400 level": [False, []],
    "Complete 1 additional STAT courses at the 300/400 level": [False, []],
    "Complete either 1 additional STAT 400-level course or one of: CS457/485/486": [False, []],
    "Complete 4 additional 300/400 level courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [False, []],
    "Complete 3 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [False, []]
  }


  # First Initialize stat_reqs dictionary


  # Req 1: First, check for core courses
  check_complete_all("Complete all of: STAT 330/331/332/333",
                   ["STAT 330", "STAT 331", "STAT 332", "STAT 333"],
                   student_courses, stat_reqs)
  # print("Req 1: core")
  # print(student_courses)
  # print(stat_reqs)

  # Req 2: Check communication course
  check_n_from_list(current_requirement = "Complete one of: ENGL 378/MTHEL 300",
                  required_courses = ["ENGL 378", "MTHEL 300"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = stat_reqs)
  # print("Req 2: comms")
  # print(student_courses)
  # print(stat_reqs)

  # Req 3: Calc
  check_n_from_list(current_requirement = "Complete one of: MATH 237/247",
                  required_courses = ["MATH 237", "MATH 247"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = stat_reqs)
  # print("Req 3: calc")
  # print(student_courses)
  # print(stat_reqs)

  # Req 4: Advanced math
  check_n_from_list("Complete one of: AMATH 231/AMATH 242/AMATH 250/AMATH 251/AMATH 350/CS 371/MATH 239/MATH 249",
                                  ["AMATH 231", "AMATH 250", "AMATH 251", "MATH 239", "MATH 249", "AMATH 350", "AMATH 242", "CS 371"],
                                  n = 1,
                                  student_courses = student_courses,
                                  major_reqs = stat_reqs)
  # print("Req 4: Advanced math")
  # print(student_courses)
  # print(stat_reqs)

  # Req 5: 2 400 Level STAT
  check_n_courses("Complete 2 additional STAT courses at the 400 level",
                  eligible_levels = 400,
                  subject_codes = ["STAT"],
                  n = 2,
                  student_courses = student_courses,
                  major_reqs = stat_reqs
                  )

  # print("Req 5: 2 400 Level STAT")
  # print(student_courses)
  # print(stat_reqs)

  # Req 7: stats or cs - will check cs first, if still false (unmet, check stats)

  check_n_from_list("Complete either 1 additional STAT 400-level course or one of: CS457/485/486",
                    required_courses = ["CS 457", "CS 485", "CS 486"],
                    n = 1,
                    student_courses = student_courses,
                    major_reqs = stat_reqs)

  if not stat_reqs["Complete either 1 additional STAT 400-level course or one of: CS457/485/486"][0]:
    check_n_courses("Complete either 1 additional STAT 400-level course or one of: CS457/485/486",
                    eligible_levels = 400,
                    subject_codes = ["STAT"],
                    n = 1,
                    student_courses = student_courses,
                    major_reqs = stat_reqs
                    )
    # print("Req 7: stats")
    # print(student_courses)
    # print(stat_reqs)

  # Req 6: 1 STAT 300/400 Level
  check_n_courses("Complete 1 additional STAT courses at the 300/400 level",
                  eligible_levels = 300,
                  subject_codes = ["STAT"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = stat_reqs
                  )

  # print("Req 6: 1 STAT 300/400 Level")
  # print(student_courses)
  # print(stat_reqs)


    # Req 8: Complete 4 additional 300/400 courses from any math code
  check_n_courses("Complete 4 additional 300/400 level courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT",
                    eligible_levels = 300,
                    subject_codes = ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                    n = 4,
                    student_courses = student_courses,
                    major_reqs = stat_reqs)
  # print("Req 8: 4 additional 300/400 courses from any math code")
  # print(student_courses)
  # print(stat_reqs)

    # Req 9: Any 3 additiional math courses
  check_n_courses("Complete 3 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT",
                    eligible_levels = 100,
                    subject_codes = ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                    n = 3,
                    student_courses = student_courses,
                    major_reqs = stat_reqs)
  # print("Req 9: Any 3 additiional math courses")
  # print(student_courses)
  # print(stat_reqs)

  return stat_reqs


