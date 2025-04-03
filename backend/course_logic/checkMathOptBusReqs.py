from course_logic.helper import *

def check_math_opt_bus_specialization(student_courses):

  refine_courses(student_courses, ["MATH 237", "MATH 247", "MATH 239", "MATH 249"])

  reqs = {
    "Complete all of: AFM 101, CO 370, ECON 101, MSE 211, STAT 340": [False, []],
    "Complete one of: AMATH 242, CS 370, CS 371": [False, []],
    "Complete one of: CO 250, CO 255": [False, []],
    "Complete 3 of: CO 342, CO 351, CO 353, CO 367, CO 372, CO 450, CO 452, CO 454, CO 456, CO 463, CO 466, CO 471": [False, []],
    "Complete one of: CS 330, CS 490": [False, []],
    "Complete one of: MATH 237, MATH 247": [False, []],
    "Complete one of: MATH 239, MATH 249": [False, []],
    # Specialization reqs
    "Complete all of: ACTSC 231, AFM 102, BUS 111W, BUS 121W, BUS 252W, BUS 381W, CS 338, ECON 102, MSE 432, STAT 371, STAT 372": [False, []],
    "Complete 2 of: AMATH 350, BUS 435W, BUS 445W, BUS 455W, BUS 485W, CS 230, CS 234, MSE 311, MSE 436, STAT 440, STAT 442, STAT 444": [False, []],
  }

  check_complete_all("Complete all of: AFM 101, CO 370, ECON 101, MSE 211, STAT 340",
                     ["AFM 101", "CO 370", "ECON 101", "MSE 211", "STAT 340"],
                     student_courses, reqs)

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

  check_n_from_list(current_requirement = "Complete 3 of: CO 342, CO 351, CO 353, CO 367, CO 372, CO 450, CO 452, CO 454, CO 456, CO 463, CO 466, CO 471",
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

  # Check business specialization courses

  check_complete_all("Complete all of: ACTSC 231, AFM 102, BUS 111W, BUS 121W, BUS 252W, BUS 381W, CS 338, ECON 102, MSE 432, STAT 371, STAT 372",
                     ["ACTSC 231", "AFM 102", "BUS 111W", "BUS 121W", "BUS 252W", "BUS 381W", "CS 338", "ECON 102", "MSE 432", "STAT 371", "STAT 372"],
                     student_courses, reqs)

  check_n_from_list("Complete 2 of: AMATH 350, BUS 435W, BUS 445W, BUS 455W, BUS 485W, CS 230, CS 234, MSE 311, MSE 436, STAT 440, STAT 442, STAT 444",
                    ["ACTSC 231", "AFM 102", "BUS 111W", "BUS 121W", "BUS 252W", "BUS 381W", "CS 338", "ECON 102", "MSE 432", "STAT 371", "STAT 372"],
                    ,n = 2, student_courses, reqs)

  return reqs



# moor_test1 = ["AFM 101", "CO 370", "ECON 101", "MSE 211", "STAT 340", "CS 371", "CO 255", "CO 342", "CO 372", "CO 471", "CS 490", "MATH 247", "MATH 249", "CS 234", "STAT 331", "STAT 333", "ECON 102", "MSE 311", "STAT 435", "CO 450", "MATBUS 112W", "ACTSC 231"]


# print(check_math_opt_bus_specialization(moor_test1))
