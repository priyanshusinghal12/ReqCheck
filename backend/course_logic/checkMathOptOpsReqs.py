from course_logic.helper import *

def check_math_opt_ops_specialization(student_courses):

  reqs = {
    "Complete all of: AFM 101, CO 370, ECON 101, MSE 211, STAT 340": [False, []],
    "Complete one of: AMATH 242, CS 370, CS 371": [False, []],
    "Complete one of: CO 250, CO 255": [False, []],
    "Complete 3 of: CO 342, 351, 353, 367, 372, 450, 452, 454, 456, 463, 466, 471": [False, []],
    "Complete one of: CS 330, CS 490": [False, []],
    "Complete one of: MATH 237, MATH 247": [False, []],
    "Complete one of: MATH 239, MATH 249": [False, []],
    # Specialization reqs
    "Complete all of: CS 234, STAT 331, STAT 333": [False, []],
    "Complete 2 of: AFM 102, ECON 102, MSE 311, MSE 432": [False, []],
    "Complete one of: AMATH 250, AMATH 251, CO 487, CS 338, CS 430, STAT 332, STAT 433, STAT 435, STAT 443": [False, []],
    "Complete one of: CO 351, CO 353 or, if CO 255 is taken, one of: CO 450, CO 452, CO 454, CO 456, CO 459, CO 463, CO 466, CO 471": [False, []],
    "Complete 2 additional math courses from the following subject codes: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [False, []],
  }

  # Check the second last specialization req first since it is most restrictive, then check as usual in order
  check_n_from_list(current_requirement = "Complete one of: CO 351, CO 353 or, if CO 255 is taken, one of: CO 450, CO 452, CO 454, CO 456, CO 459, CO 463, CO 466, CO 471",
                  required_courses = ["CO 351", "CO 353"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = reqs)
  if not (reqs["Complete one of: CO 351, CO 353 or, if CO 255 is taken, one of: CO 450, CO 452, CO 454, CO 456, CO 459, CO 463, CO 466, CO 471"][0] and "CO 255" in student_courses):
    check_n_from_list(current_requirement = "Complete one of: CO 351, CO 353 or, if CO 255 is taken, one of: CO 450, CO 452, CO 454, CO 456, CO 459, CO 463, CO 466, CO 471",
                    required_courses = ["CO 450", "CO 452", "CO 454", "CO 456", "CO 459", "CO 463", "CO 466", "CO 471"],
                    n = 1,
                    student_courses = student_courses,
                    major_reqs = reqs)

  # Now check remaining reqs in usual order


  # Check major (non specialization) reqs

  check_complete_all(current_requirement="Complete all of: AFM 101, CO 370, ECON 101, MSE 211, STAT 340",
                     core_courses=["AFM 101", "CO 370", "ECON 101", "MSE 211", "STAT 340"],
                     student_courses=student_courses, major_reqs=reqs)

  check_n_from_list(current_requirement = "Complete one of: AMATH 242, CS 370, CS 371",
                  required_courses = ["AMATH 242", "CS 370" ,"CS 371"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = reqs)

  check_n_from_list(current_requirement = "Complete one of: CO 250, CO 255",
                  required_courses = ["CO 250", "CO 255"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = reqs)

  check_n_from_list(current_requirement = "Complete 3 of: CO 342, 351, 353, 367, 372, 450, 452, 454, 456, 463, 466, 471",
                  required_courses = ["CO 342", "CO 351", "CO 353", "CO 367", "CO 372", "CO 450", "CO 452", "CO 454", "CO 456", "CO 463", "CO 466", "CO 471"],
                  n = 3,
                  student_courses = student_courses,
                  major_reqs = reqs)

  check_n_from_list(current_requirement = "Complete one of: CS 330, CS 490",
                  required_courses = ["CS 330" ,"CS 490"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = reqs)

  check_n_from_list(current_requirement = "Complete one of: MATH 237, MATH 247",
                  required_courses = ["MATH 237", "MATH 247"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = reqs)

  check_n_from_list(current_requirement = "Complete one of: MATH 239, MATH 249",
                  required_courses = ["MATH 239", "MATH 249"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = reqs)
  check_complete_all("Complete all of: CS 234, STAT 331, STAT 333",
                     ["CS 234", "STAT 331", "STAT 333"],
                     student_courses, reqs)
  check_n_from_list("Complete 2 of: AFM 102, ECON 102, MSE 311, MSE 432",
                    required_courses = ["AFM 102", "ECON 102", "MSE 311", "MSE 432"],
                    n = 2,
                    student_courses = student_courses,
                    major_reqs = reqs)
  check_n_from_list("Complete one of: AMATH 250, AMATH 251, CO 487, CS 338, CS 430, STAT 332, STAT 433, STAT 435, STAT 443",
                    required_courses = ["AMATH 250", "AMATH 251", "CO 487", "CS 338", "CS 430", "STAT 332", "STAT 433", "STAT 435", "STAT 443"],
                    n = 1,
                    student_courses = student_courses,
                    major_reqs = reqs)
  check_n_courses(current_requirement = "Complete 2 additional math courses from the following subject codes: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT",
                  eligible_levels = 100,
                  subject_codes = ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                  n = 2,
                  student_courses = student_courses, major_reqs = reqs)
  return reqs
