from pickle import FALSE

# # Test case currently being used is the one where a student has met all the requirements
# stat_tests1 = [
#     "STAT 330", "STAT 331", "STAT 332", "STAT 333",  # Core STAT courses
#     "ENGL 378",  # Communication option 1
#     "MATH 237",  # Calculus option 1
#     "CS 371",
#     "AMATH 250",  #  IMPORTANT: CS 371 placed first to check it's not used, AMATH 250 should be used for advanced math requirement
#     "STAT 440", "STAT 441",  # 2 STAT courses at the 400-level
#     "STAT 341",# 1 additional STAT course at the 300/400 level
#     "CS 486", # USING CS 486 INSTEAD OF 1 additional STAT 400-level course
#     "ACTSC 371", "AMATH 350", "CO 487", # after including CS 371 this should form 4 additional 300/400 level courses
#     "ACTSC 231", "AMATH 242", "CO 250" # 3 additional courses
# ]

# # Calling the function
# check_stats_major(stat_tests1)

# # Test case currently being used is the one where a student has met all the requirements
# stat_tests2 = [
#     "STAT 330", "STAT 331", "STAT 332", "STAT 333",  # Core STAT courses
#     "ENGL 378",  # Communication option 1
#     "MATH 237",  # Calculus,
#     "AMATH 250",  #  IMPORTANT: CS 371 placed first to check it's not used, AMATH 250 should be used for advanced math requirement
#     "STAT 440", "STAT 441",  # 2 STAT courses at the 400-level
#     "STAT 300","STAT 467",  # 1 additional STAT course at the 300/400 level, # USING CS 486 INSTEAD OF 1 additional STAT 400-level course
#     "ACTSC 371", "AMATH 350", "CO 487", "CS 371", # after including CS 371 this should form 4 additional 300/400 level courses
#     "ACTSC 231", "STAT 242", "STAT 100" # 3 additional courses
# ]

# # Calling the function
# requirements_dict = check_stats_major(stat_tests2)

# math_econ_tests = [
#     "ECON 101", "ECON 102", "ECON 290", "ECON 306", "ECON 391", "ECON 393", "ECON 472", "ECON 491", "ECON 496",  # Core ECON courses
#     "ECON 406",  # One advanced ECON course
#     "ECON 310", "ECON 320", "ECON 330", "ECON 440",  # 4 additional ECON 300/400 level courses
#     "AMATH 350", "STAT 331", "STAT 443",  # Core math/stat courses
#     "PMATH 331",  # One advanced math course
#     "CO 250",  # One combinatorics/optimization course
#     "MATH 237",  # One advanced calculus course
#     "AMATH 101", "AMATH 450", "CO 487", "CS 371", "MATBUS 471", "MATH 340", "PMATH 450",  # 7 additional math-related courses
#     "BET 100", "CLAS 104"  # 2 additional courses
# ]

# requirements_dict = check_math_econ_reqs(math_econ_tests)

# math_finance_tests = [
#     "ACTSC 231", "ACTSC 372", "ACTSC 445", "ACTSC 446", "PMATH 351", "PMATH 450", "PMATH 451", "STAT 330",
#     "STAT 331", "STAT 333", "STAT 443",  # Core courses

#     "BUS 127W", "BUS 247W", "ARBUS 101", "AMATH 250", "CS 371", "CO 250", "CO 372",
#     "ECON 120W", "ECON 140W", "ECON 260W",  # Required business, finance, and econ courses

#     "MATH 247"  # Completing the special condition (MATH 237 and PMATH 333)
# ]

# requirements_dict = check_math_finance_reqs(math_finance_tests)

# math_physics_tests = [
#     "AMATH 231", "AMATH 271", "AMATH 351", "AMATH 353", "AMATH 361", "AMATH 373", "PHYS 121", "PHYS 122", "PHYS 234", "PHYS 242",  # Core courses
#     "CS 371", "AMATH 251", "PMATH 331", "PMATH 332", "PHYS 454", "PHYS 476", "MATH 237", "PHYS 359", "PHYS 363",  # Required courses
#     "PHYS 358", "AMATH 465", "PHYS 363", "PHYS 400", "AMATH 450", "AMATH 460", "PHYS 101"  # Additional required AMATH/PHYS courses
# ]

# # Running test
# requirements_dict = check_math_physics_reqs(math_physics_tests)

# comp_math_tests = [
#     "CS 230", "CS 234",  # Core CS courses
#     "AMATH 242",  # Computational Mathematics requirement
#     "MATH 237",  # Calculus 3 requirement
#     "MATH 239",  # Combinatorics requirement
#     "ECON 101", "ECON 102", "ECON 254",  # Non-math courses with at least one 200+ level
#     "AMATH 250", "CO 250",  # List 1 requirements
#     "AMATH 342", "CS 475",  # List 2 requirements
#     "PMATH 370", "STAT 340", "CO 487", "STAT 442"  # 4 courses, from List 2 or List 3, at least two
#                                                     # different subject codes (AMATH, CO, CS, PMATH, STAT), 2 400 level
# ]

# # Running test
# requirements_dict = check_comp_math_reqs(comp_math_tests)
# Test case for Mathematics Major where a student meets all requirements

# math_studies_test = [
#     # Core Math Requirements
#     "MATH 136", "MATH 137", "MATH 138", "MATH 145", "MATH 225",
#     "MATH 237", "STAT 220", "STAT 221",

#     # Core CS Requirements
#     "CS 135", "CS 116",

#     # Communication Skills Requirement (Two EMLS/ENGL/SPCOM courses)
#     "ENGL 109", "MTHEL 300",

#     # Ten 300/400 Level Math Courses (5.0 units)
#     "MATH 313", "STAT 320", "CS 330", "AMATH 345", "CO 365",
#     "MATH 441", "ACTSC 443", "PMATH 370", "MATBUS 432", "STAT 340",

#     # Four additional Mathematics courses (2.0 units)
#     "AMATH 250", "PMATH 330", "CS 234", "CS 231",

#     # Eight additional non-math courses (4.0 units)
#     "ECON 102", "ECON 101", "CLAS 104", "PHYS 121",
#     "ECON 254", "ECON 201", "BUS 111", "BET 100",

#     # Two additional Math courses or two contributing to a minor (1.0 units)
#     "CS 230", "CS 321",

#     # Four free-choice electives (2.0 units)
#     "MATH 140", "HIST 250", "PSCI 100", "SOC 101"
# ]

# # Running test
# requirements_dict = math_studies_reqs(math_studies_test, False)

# Test case for Combinatorics and Optimization where a student meets all requirements
# combinatorics_optimization_test = [
#     "MATH 239", "CO 255", "CO 330", "CO 450", "PMATH 336",
#     "CO 440", "CO 439", "CO 487",
#     "MATH 247", "PMATH 331", "PMATH 348", "PMATH 334",
#     "ACTSC 331", "CS 487",  
#     "MATBUS 487",  
#     "CS 234", "CS 231", "AMATH 250"
# ]


#AMATH 331/PMATH 331/PMATH 333, AMATH 332/PMATH 332, CS 462, CS 466, CS 487, PMATH 334/348, PMATH 340

def format_course_requirements(requirements_dict):
    formatted_output = "Course Requirements:\n"

    for requirement, details in requirements_dict.items():
        completed, courses = details
        status = "✅ Completed" if completed else "❌ Not Completed"

        formatted_output += f"\n- {requirement}: {status}\n"
        if courses:
            formatted_output += "  Courses taken: " + ", ".join(courses) + "\n"
        else:
            formatted_output += "  No courses taken yet.\n"

    return formatted_output


# requirements_dict = check_co_major(combinatorics_optimization_test)


# print(format_course_requirements(requirements_dict))