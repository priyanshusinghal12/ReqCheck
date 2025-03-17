def check_co_major(student_courses):
    """
    Checks if a student has completed the requirements for the Combinatorics and Optimization Major.

    Args:
        student_courses: A list of student's completed courses.

    Returns:
        A dictionary of the program requirements and their completion status.
    """
    co_reqs = {
        "Complete one of: MATH 239, MATH 249": [False, []],
        "Complete one of: CO 250, CO 255": [False, []],
        "Complete one of: CO 330, CO 342": [False, []],
        "Complete one of: CO 351, CO 353, CO 367, or CO 255+ list": [False, []],  # Initial list
        "Complete one of: PMATH 336, PMATH 347": [False, []],
        "Complete 3 additional CO courses (see list below)": [False, []], 
        "3 of: MATH 237/247, AMATH 331/PMATH 331/PMATH 333, AMATH 332/PMATH 332, CS 462, CS 466, CS 487, PMATH 334/348, PMATH 340": [False, []],
        "Two additional 300- or 400-level math courses": [False, []],
        "One additional 300- or 400-level math course": [False, []],
        "Three additional math courses": [False, []]
    }

    # Req 1: Combinatorics course
    check_n_from_list("Complete one of: MATH 239, MATH 249",
                      ["MATH 239", "MATH 249"], n=1, student_courses=student_courses, major_reqs=co_reqs)

    # Req 2: Optimization course
    check_n_from_list("Complete one of: CO 250, CO 255",
                      ["CO 250", "CO 255"], n=1, student_courses=student_courses, major_reqs=co_reqs)

    # Req 3: Combinatorial Enumeration or Graph Theory
    check_n_from_list("Complete one of: CO 330, CO 342",
                      ["CO 330", "CO 342"], n=1, student_courses=student_courses, major_reqs=co_reqs)
    
    # Req 4: Three additional CO courses CO 255 case
    if "CO 255" in co_reqs["Complete one of: CO 250, CO 255"][1]: #255 check
        eligible_courses = ["CO 351", "CO 353", "CO 367", "CO 450", "CO 452",
                            "CO 454", "CO 456", "CO 459", "CO 463", "CO 466", "CO 471"]
    else:
        eligible_courses = ["CO 351", "CO 353", "CO 367"]

    # Find completed eligible courses and update requirements
    check_n_from_list("Complete one of: CO 351, CO 353, CO 367, or CO 255+ list",
                      eligible_courses, n=1, student_courses=student_courses, major_reqs=co_reqs)
    

    # print("student_courses:", student_courses)

    # Req 5: Group Theory course
    check_n_from_list("Complete one of: PMATH 336, PMATH 347",
                      ["PMATH 336", "PMATH 347"], n=1, student_courses=student_courses, major_reqs=co_reqs)

    #Req 6: Complete 3 additional CO courses
    co_courses = [ "CO 330", "CO 331", "CO 342", "CO 351", "CO 353", "CO 367", "CO 430", "CO 431",
                   "CO 432", "CO 434", "CO 439", "CO 440", "CO 442", "CO 444", "CO 446", "CO 450", "CO 452",
                   "CO 454", "CO 456", "CO 459", "CO 463", "CO 466", "CO 471", "CO 481",
                   "CS 467", "PHYS 467", "CO 485", "CO 486", "CO 487"]

    check_n_from_list("Complete 3 additional CO courses (see list below)",
                      co_courses, n=3, student_courses=student_courses, major_reqs=co_reqs)
    

    # Req 7: 3 of the specified courses (using the copy)

    if "PMATH 331" in student_courses:
      student_courses[student_courses.index("PMATH 331")] = "AMATH 331"

    if "PMATH 332" in student_courses:
        student_courses[student_courses.index("PMATH 332")] = "AMATH 332"

    remaining_courses = student_courses.copy() #copy created

    # Remove AMATH 331/PMATH 333 and PMATH 334/PMATH 348 from the copy
    if "AMATH 331" in remaining_courses and "PMATH 333" in remaining_courses:
        remaining_courses.remove("PMATH 333")  # Count as one course
    if "PMATH 334" in remaining_courses and "PMATH 348" in remaining_courses:
        remaining_courses.remove("PMATH 348")  # Count as one course

    eligible_courses = [
        "MATH 237", "MATH 247", "AMATH 331", "PMATH 333",
        "AMATH 332", "CS 462", "CS 466", "CS 487",
        "PMATH 334", "PMATH 348", "PMATH 340"
    ]

    # print("remaining_courses:", remaining_courses)

    completed_courses_req1 = [course for course in eligible_courses if course in remaining_courses]

    # print("completed_courses_req1:", completed_courses_req1)

    if len(completed_courses_req1) >= 3:
        co_reqs["3 of: MATH 237/247, AMATH 331/PMATH 331/PMATH 333, AMATH 332/PMATH 332, CS 462, CS 466, CS 487, PMATH 334/348, PMATH 340"][0] = True
        co_reqs["3 of: MATH 237/247, AMATH 331/PMATH 331/PMATH 333, AMATH 332/PMATH 332, CS 462, CS 466, CS 487, PMATH 334/348, PMATH 340"][1].extend(completed_courses_req1[:3])  # Add up to 3 courses

        # Remove the courses used for Req 1 from student_courses
        for course in completed_courses_req1[:3]:
            if course in student_courses:
                student_courses.remove(course)

    # Req 8,9,10: Additional Courses 
    check_n_courses("Two additional 300- or 400-level math courses",
                    eligible_levels=300,
                    subject_codes=["ACTSC", "AMATH", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                    n=2,
                    student_courses=student_courses,  # Use student_courses
                    major_reqs=co_reqs)

    check_n_courses("One additional 300- or 400-level math course",
                    eligible_levels=300,
                    subject_codes=["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                    n=1,
                    student_courses=student_courses,  # Use student_courses
                    major_reqs=co_reqs)

    check_n_courses("Three additional math courses",
                    eligible_levels=100,
                    subject_codes=["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"],
                    n=3,
                    student_courses=student_courses,  # Use student_courses
                    major_reqs=co_reqs)
  
    return co_reqs