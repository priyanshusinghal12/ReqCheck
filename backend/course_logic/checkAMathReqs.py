from course_logic.helper import *

# Checks if a student has completed 4 additional courses, all from the same subject code, treating "BME/SYDE" and "ME/MTE" as combined subject codes.
def check_amath_concentration(current_req, student_courses, amath_reqs):
    
    subject_codes = ["AE", "BIOL", "BME/SYDE", "CHE", "CHEM", "CIVE", "EARTH", "ECE",
                     "ECON", "ENVE", "GEOE", "ME/MTE", "MNS", "MSE", "NE", "PHYS"]
    n = 4

    for code in subject_codes:
        eligible_courses = []
        for course in student_courses:
            # Check for combined subject codes
            if code == "BME/SYDE" and (course.startswith("BME") or course.startswith("SYDE")):
                eligible_courses.append(course)
            elif code == "ME/MTE" and (course.startswith("ME") or course.startswith("MTE")):
                eligible_courses.append(course)
            elif code in course:
                eligible_courses.append(course)

        # Check if enough eligible courses are completed
        if len(eligible_courses) >= n:
            # Update amath_reqs
            amath_reqs[current_req][0] = True
            amath_reqs[current_req][1].extend(eligible_courses[:n])


            for course in eligible_courses[:n]:
                if course in student_courses:
                    student_courses.remove(course)
            return


def check_amath_major(student_courses):

  refine_courses(student_courses, ["MATH 237", "MATH 247"])

  amath_reqs = {
    "Complete all of: AMATH 231, AMATH 342, AMATH 351, AMATH 353, PHYS 121": [False, []],
    "Complete one of: AMATH 242, CS 371": [False, []],
    "Complete one of: AMATH 250, AMATH 251": [False, []],
    "Complete one of: AMATH 332, PMATH 332, PMATH 352": [False, []],
    "Complete one of: MATH 237, MATH 247": [False, []],
    "Complete 3 AMATH courses at the 400 level": [False, []],
    "Complete 1 additional AMATH course at the 300/400 level": [False, []],
    "Complete 5 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [False, []],
    "Complete 4 additional courses, all from the same subject code from: AE, BIOL, BME/SYDE, CHE, CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME/MTE, MNS, MSE, NE, PHYS": [False, []],
  }



  check_complete_all("Complete all of: AMATH 231, AMATH 342, AMATH 351, AMATH 353, PHYS 121",
                   ["AMATH 231", "AMATH 342", "AMATH 351", "AMATH 353", "PHYS 121"],
                   student_courses, amath_reqs)


  check_n_from_list(current_requirement = "Complete one of: AMATH 242, CS 371",
                  required_courses = ["AMATH 242", "CS 371"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = amath_reqs)

  check_n_from_list(current_requirement = "Complete one of: AMATH 250, AMATH 251",
                  required_courses = ["AMATH 250", "AMATH 251"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = amath_reqs)

  check_n_from_list("Complete one of: AMATH 332, PMATH 332, PMATH 352",
                                  ["AMATH 332", "PMATH 332", "PMATH 352"],
                                  n = 1,
                                  student_courses = student_courses,
                                  major_reqs = amath_reqs)

  check_n_from_list(current_requirement = "Complete one of: MATH 237, MATH 247",
                  required_courses = ["MATH 237", "MATH 247"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = amath_reqs)

  check_n_courses("Complete 3 AMATH courses at the 400 level",
                  eligible_levels = 400,
                  subject_codes = ["AMATH"],
                  n = 3,
                  student_courses = student_courses,
                  major_reqs = amath_reqs
                  )

  check_n_courses("Complete 1 additional AMATH course at the 300/400 level",
                  eligible_levels = 300,
                  subject_codes = ["AMATH"],
                  n = 1,
                  student_courses = student_courses,
                  major_reqs = amath_reqs
                  )

  check_n_courses("Complete 5 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT",
                    eligible_levels = 100,
                    subject_codes = ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                    n = 5,
                    student_courses = student_courses,
                    major_reqs = amath_reqs)



  check_amath_concentration("Complete 4 additional courses, all from the same subject code from: AE, BIOL, BME/SYDE, CHE, CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME/MTE, MNS, MSE, NE, PHYS", student_courses, amath_reqs)


  return amath_reqs


