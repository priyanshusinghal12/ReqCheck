from course_logic.helper import *

def check_math_teaching_major(student_courses):

  # Define reqs

  reqs = {
    "Complete all of: ACTSC 221, CS 234, MTHEL 206": [False, []],
    "Complete one of: AMATH 250, AMATH 251, AMATH 343": [False, []],
    "Complete one of: AMATH 331, AMATH 332, PMATH 331, PMATH 332, PMATH 333, PMATH 351, PMATH 352": [False, []],
    "Complete one of: CO 250, CO 255": [False, []],
    "Complete one of: CO 380, CO 480": [False, []],
    "Complete one of: CS 230, CS 330, CS 338, CS 370, CS 371, CS 430, CS 436": [False, []],
    "Complete one of: MATH 237, MATH 247": [False, []],
    "Complete one of: MATH 239, MATH 249": [False, []],
    "Complete one of: PMATH 320, PMATH 321, PMATH 330, PMATH 340, PMATH 432, PMATH 440": [False, []],
    "Complete one of: PMATH 334, PMATH 336, PMATH 347, PMATH 348": [False, []],
    "Complete one of: PSYCH 101, PSYCH 101R": [False, []],
    "Complete one of: PSYCH 211, PSYCH 212, PSYCH 212R": [False, []],
    "Complete one of: STAT 331, STAT 332, STAT 333": [False, []],
    "Complete 8 math courses at the 300- or 400-level from the following subject codes (including any taken to satisfy the above requirements): ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [False, []],
  }


  # Check the last req first: check for at least 8 300/400 level math courses without deleting from student courses since overlap is allowed for this req
  eligible_subject_codes = ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"]
  eligible_courses = []

  for course in student_courses:
      subject_code = course.split(" ")[0]
      course_level = int(course.split(" ")[1][:3])

      if subject_code in eligible_subject_codes and course_level >= 300:
          eligible_courses.append(course)

  # Update reqs without removing courses from student_courses
  reqs["Complete 8 math courses at the 300- or 400-level from the following subject codes (including any taken to satisfy the above requirements): ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT"][1].extend(eligible_courses[:8])
  if len(eligible_courses) >= 8:
      reqs["Complete 8 math courses at the 300- or 400-level from the following subject codes (including any taken to satisfy the above requirements): ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT"][0] = True


  # Checking reqs
  check_complete_all("Complete all of: ACTSC 221, CS 234, MTHEL 206",
                     ["ACTSC 221", "CS 234", "MTHEL 206"],
                     student_courses, reqs)
  check_n_from_list("Complete one of: AMATH 250, AMATH 251, AMATH 343",
                    ["AMATH 250", "AMATH 251", "AMATH 343"],
                    1, student_courses, reqs)
  check_n_from_list("Complete one of: AMATH 331, AMATH 332, PMATH 331, PMATH 332, PMATH 333, PMATH 351, PMATH 352",
                    ["AMATH 331", "AMATH 332", "PMATH 331", "PMATH 332", "PMATH 333", "PMATH 351", "PMATH 352"],
                    1, student_courses, reqs)
  check_n_from_list("Complete one of: CO 250, CO 255",
                    ["CO 250", "CO 255"],
                    1, student_courses, reqs)
  check_n_from_list("Complete one of: CO 380, CO 480",
                    ["CO 380", "CO 480"],
                    1, student_courses, reqs)
  check_n_from_list("Complete one of: CS 230, CS 330, CS 338, CS 370, CS 371, CS 430, CS 436",
                    ["CS 230", "CS 330", "CS 338", "CS 370", "CS 371", "CS 430", "CS 436"],
                    1, student_courses, reqs)
  check_n_from_list("Complete one of: MATH 237, MATH 247",
                    ["MATH 237", "MATH 247"],
                    1, student_courses, reqs)
  check_n_from_list("Complete one of: MATH 239, MATH 249",
                    ["MATH 239", "MATH 249"],
                    1, student_courses, reqs)
  check_n_from_list("Complete one of: PMATH 320, PMATH 321, PMATH 330, PMATH 340, PMATH 432, PMATH 440",
                    ["PMATH 320", "PMATH 321", "PMATH 330", "PMATH 340", "PMATH 432", "PMATH 440"],
                    1, student_courses, reqs)
  check_n_from_list("Complete one of: PMATH 334, PMATH 336, PMATH 347, PMATH 348",
                    ["PMATH 334", "PMATH 336", "PMATH 347", "PMATH 348"],
                    1, student_courses, reqs)
  check_n_from_list("Complete one of: PSYCH 101, PSYCH 101R",
                    ["PSYCH 101", "PSYCH 101R"],
                    1, student_courses, reqs)
  check_n_from_list("Complete one of: PSYCH 211, PSYCH 212, PSYCH 212R",
                    ["PSYCH 211", "PSYCH 212", "PSYCH 212R"],
                    1, student_courses, reqs)
  check_n_from_list("Complete one of: STAT 331, STAT 332, STAT 333",
                    ["STAT 331", "STAT 332", "STAT 333"],
                    1, student_courses, reqs)
  return reqs
