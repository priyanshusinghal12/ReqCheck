from course_logic.helper import *
 
def check_math_physics_reqs(student_courses):
 
    refine_courses(student_courses, ["MATH 237", "MATH 247"])
 
    math_physics_reqs = {
        "Complete all the following: AMATH 231, AMATH 271, AMATH 353, AMATH 361, PHYS 121, PHYS 122, PHYS 242": [False, []],
        "Complete one of the following: AMATH 242, AMATH 345, AMATH 391, AMATH 445, CS 371": [False, []],
        "Complete one of the following: AMATH 250, AMATH 251": [False, []],
        "Complete one of the following: AMATH 331, PMATH 331, PMATH 333, PMATH 351": [False, []],
        "Complete one of the following: AMATH 332, PMATH 332, PMATH 352": [False, []],
        "Complete either AMATH 373, or both of PHYS 234 and PHYS 334": [False, []],
        "Complete one of the following: AMATH 473, PHYS 454": [False, []],
        "Complete one of the following: AMATH 475, PHYS 476": [False, []],
        "Complete 2 of the following: AMATH 333, AMATH 474, PHYS 359, PHYS 484": [False, []],
        "Complete one of the following: ECE 403, PHYS 358": [False, []],
        "Complete one of the following: MATH 237, MATH 247": [False, []],
        "Complete 1.5 additional units from AMATH or PHYS at the 300 or 400 level": [False, []],
        "Complete 1.5 additional units from AMATH or PHYS at any level": [False, []]
    }
 
    # Req 1: Core AMATH and PHYS courses
    check_complete_all("Complete all the following: AMATH 231, AMATH 271, AMATH 353, AMATH 361, PHYS 121, PHYS 122, PHYS 242",
                       ["AMATH 231", "AMATH 271", "AMATH 353", "AMATH 361", "PHYS 121", "PHYS 122", "PHYS 242"],
                       student_courses, math_physics_reqs)
 
    # Req 2
    check_n_from_list("Complete one of the following: AMATH 242, AMATH 345, AMATH 391, AMATH 445, CS 371",
                      ["AMATH 242", "AMATH 345", "AMATH 391", "AMATH 445", "CS 371"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)
 
    # Req 3: Differential Equations course
    check_n_from_list("Complete one of the following: AMATH 250, AMATH 251",
                      ["AMATH 250", "AMATH 251"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)
 
    # Req 4: Real Analysis course
    check_n_from_list("Complete one of the following: AMATH 331, PMATH 331, PMATH 333, PMATH 351",
                      ["AMATH 331", "PMATH 331", "PMATH 333", "PMATH 351"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)
 
    # Req 5: Complex Analysis course
    check_n_from_list("Complete one of the following: AMATH 332, PMATH 332, PMATH 352",
                      ["AMATH 332", "PMATH 332", "PMATH 352"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)
 
    # Req 6: Quantum Theory 2 course
    check_n_from_list("Complete either AMATH 373, or both of PHYS 234 and PHYS 334",
                      ["AMATH 373"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)
 
    if not math_physics_reqs["Complete either AMATH 373, or both of PHYS 234 and PHYS 334"][0]:
        check_n_from_list("Complete either AMATH 373, or both of PHYS 234 and PHYS 334",
                      ["PHYS 234", "PHYS 334"], n=2, student_courses=student_courses, major_reqs=math_physics_reqs)
 
    check_n_from_list("Complete one of the following: AMATH 473, PHYS 454",
                      ["AMATH 473", "PHYS 454"], 1, student_courses, math_physics_reqs)
 
    # Req: General Relativity course
    check_n_from_list("Complete one of the following: AMATH 475, PHYS 476",
                      ["AMATH 475", "PHYS 476"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)
 
    check_n_from_list("Complete 2 of the following: AMATH 333, AMATH 474, PHYS 359, PHYS 484",
                      ["AMATH 333", "AMATH 474", "PHYS 359", "PHYS 484"], n=2, student_courses=student_courses, major_reqs=math_physics_reqs)
 
    check_n_from_list("Complete one of the following: ECE 403, PHYS 358",
                      ["ECE 403", "PHYS 358"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)
 
    # Req 9: Advanced Calculus course
    check_n_from_list("Complete one of the following: MATH 237, MATH 247",
                      ["MATH 237", "MATH 247"], n=1, student_courses=student_courses, major_reqs=math_physics_reqs)
 
    check_n_courses("Complete 1.5 additional units from AMATH or PHYS at the 300 or 400 level",
                    300, ["AMATH", "PHYS"], 3, student_courses, math_physics_reqs)
 
    check_n_courses("Complete 1.5 additional units from AMATH or PHYS at any level",
                    100, ["AMATH", "PHYS"], 3, student_courses, math_physics_reqs)
 
    return math_physics_reqs