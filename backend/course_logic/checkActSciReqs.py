from course_logic.helper import *
 
def check_actsci_major(student_courses):
 
  refine_courses(student_courses, ["ENGL 378", "MTHEL 300", "MATH 237", "MATH 247"])
 
  reqs = {
    "Complete all of: ACTSC 231, ACTSC 232, ACTSC 331, ACTSC 363, ACTSC 372, ACTSC 431, ACTSC 446, AFM 101, ECON 101, ECON 102, MTHEL 131, STAT 330, STAT 331, STAT 333": [False, []],
    "Complete one of: AMATH 250, AMATH 251, AMATH 350": [False, []],
    "Complete one of: ENGL 378, MTHEL 300": [False, []],
    "Complete one of: MATH 237, MATH 247": [False, []],
    "Complete one of: STAT 340, STAT 341": [False, []],
    "Complete 2 additional ACTSC courses at the 400-level": [False, []],
    "Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [False, []],
    "Complete 2 additional courses from these options: any ACTSC 3XX/4XX, AFM 424, STAT 431, STAT 433, STAT 441, STAT 443": [False, []],
  }
 
  check_complete_all("Complete all of: ACTSC 231, ACTSC 232, ACTSC 331, ACTSC 363, ACTSC 372, ACTSC 431, ACTSC 446, AFM 101, ECON 101, ECON 102, MTHEL 131, STAT 330, STAT 331, STAT 333",
                     ["ACTSC 231", "ACTSC 232", "ACTSC 331", "ACTSC 363", "ACTSC 372", "ACTSC 431", "ACTSC 446", "AFM 101", "ECON 101", "ECON 102", "MTHEL 131", "STAT 330", "STAT 331", "STAT 333"],
                     student_courses, reqs)
 
  check_n_from_list("Complete one of: AMATH 250, AMATH 251, AMATH 350",
                    ["AMATH 250", "AMATH 251", "AMATH 350"],
                    1,
                    student_courses, reqs)
 
  check_n_from_list("Complete one of: ENGL 378, MTHEL 300",
                    ["ENGL 378", "MTHEL 300"],
                    1,
                    student_courses, reqs)
 
  check_n_from_list("Complete one of: MATH 237, MATH 247",
                    ["MATH 237", "MATH 247"],
                    1,
                    student_courses, reqs)
 
  check_n_from_list("Complete one of: STAT 340, STAT 341",
                    ["STAT 340", "STAT 341"],
                    1,
                    student_courses, reqs)
 
  check_n_courses("Complete 2 additional ACTSC courses at the 400-level",
                  eligible_levels = 400,
                  subject_codes = ["ACTSC"],
                  n = 2,
                  student_courses = student_courses, major_reqs = reqs)
  
    # Check for the "Two additional courses" requirement:
  eligible_courses = ["AFM 424", "STAT 431", "STAT 433", "STAT 441", "STAT 443"]
 
  # Add 300/400 level ACTSC courses to eligible courses
  for course in student_courses:
    if course.startswith("ACTSC"):
      try:
        # Handle Waterloo course code format
        course_level = int(course.split(" ")[1][:3])  # Extract course level (e.g., 121 from "BUS 121W")
        if course_level >= 300:
          eligible_courses.append(course)
      except (ValueError, IndexError):
        pass
 
  completed_courses = [course for course in eligible_courses if course in student_courses]
  reqs["Complete 2 additional courses from these options: any ACTSC 3XX/4XX, AFM 424, STAT 431, STAT 433, STAT 441, STAT 443"][1].extend(completed_courses[:2])
  if len(completed_courses) >= 2:
    reqs["Complete 2 additional courses from these options: any ACTSC 3XX/4XX, AFM 424, STAT 431, STAT 433, STAT 441, STAT 443"][0] = True
    for course in completed_courses[:2]:
        if course in student_courses:
            student_courses.remove(course)
 
  check_n_courses("Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT",
                  300,
                  ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                  1,
                  student_courses, reqs)
 
  return reqs