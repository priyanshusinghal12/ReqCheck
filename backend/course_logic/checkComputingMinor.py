from course_logic.helper import *

# Function to check second req
def check_second_requirement(student_courses, reqs):
    key = "Complete 1 of: CS 114, CS 116, CS 136 and CS 136L, CS 146 and CS 136L"
    
    options = [
        ["CS 114"],
        ["CS 116"],
        ["CS 136", "CS 136L"],
        ["CS 146", "CS 136L"]
    ]
    
    for option in options:
        matched = [course for course in option if course in student_courses]
        if matched:
            # Add matched courses
            reqs[key][1].extend(matched)
            # Remove them from student_courses
            for course in matched:
                student_courses.remove(course)
            # Check if all were matched
            if len(matched) == len(option):
                reqs[key][0] = True
                break  # Stop after a full match

    return reqs, student_courses



def check_computing_minor(student_courses):

    reqs = {
        "Complete 1 of: CS 115, CS 135, CS 145": [False, []],
        "Complete 1 of: CS 114, CS 116, CS 136 and CS 136L, CS 146 and CS 136L": [False, []],
        "Complete either 1 CS course at the 200-, 300-, or 400-level or COMM 432": [False, []],
        "Complete 1 additional CS course at the 100-, 200-, 300-, or 400-level": [False, []],
        "Complete 3 additional CS courses at the 200-, 300-, or 400-level": [False, []],
        "Complete 1 additional CS course at the 300- or 400-level": [False, []],
    }

    # Note: CS 399, CS 499R, CS 499T cannot be used towards this plan
    student_courses = [course for course in student_courses if course not in ["CS 399", "CS 499R", "CS 499T"]]

    check_n_from_list("Complete 1 of: CS 115, CS 135, CS 145",
                      ["CS 115", "CS 135", "CS 145"],
                      1, student_courses, reqs)
    
    check_second_requirement(student_courses, reqs)

    # Check most restrictive reqs first to ensure optimal distribution

    check_n_courses("Complete 1 additional CS course at the 300- or 400-level",
                        300, ["CS"], 1,
                        student_courses, reqs)
    
    check_n_courses("Complete 3 additional CS courses at the 200-, 300-, or 400-level",
                        200, ["CS"], 3,
                        student_courses, reqs)

    # First checking COMM 432
    check_complete_all("Complete either 1 CS course at the 200-, 300-, or 400-level or COMM 432",
                       ["COMM 432"],
                       student_courses, reqs)
    
    if not reqs["Complete either 1 CS course at the 200-, 300-, or 400-level or COMM 432"][1]:
        check_n_courses("Complete either 1 CS course at the 200-, 300-, or 400-level or COMM 432",
                        200, ["CS"], 1,
                        student_courses, reqs)
        
    check_n_courses("Complete 1 additional CS course at the 100-, 200-, 300-, or 400-level",
                        100, ["CS"], 1,
                        student_courses, reqs)
    
    
    return reqs


