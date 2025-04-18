#Helper File
def refine_courses(student_courses, dont_remove=[]):
    # Replace "SPCOM" with "COMMST" in student_courses
    for i in range(len(student_courses)):
        if student_courses[i].startswith("SPCOM"):
            student_courses[i] = student_courses[i].replace("SPCOM", "COMMST")

    # Lists defined within the function
    math_core_courses = [
        "CS 115", "CS 135", "CS 145",
        "CS 116", "CS 136", "CS 146", "CS 136L",
        "MATH 106", "MATH 136", "MATH 146",
        "MATH 127", "MATH 137", "MATH 147",
        "MATH 128", "MATH 138", "MATH 148",
        "MATH 135", "MATH 145",
        "MATH 235", "MATH 245",
        "MATH 237", "MATH 239", "MATH 247", "MATH 249",
        "STAT 230", "STAT 240",
        "STAT 231", "STAT 241"
    ]

    list_1 = [
        "COMMST 100", 
        "COMMST 223", 
        "EMLS 101R", 
        "EMLS 102R", 
        "EMLS 129R", 
        "ENGL 109", 
        "ENGL 129R"
    ]

    list_1_and_2 = [
        "COMMST 100", 
        "COMMST 223", 
        "EMLS 101R", 
        "EMLS 102R", 
        "EMLS 129R", 
        "ENGL 109", 
        "ENGL 129R",
        "COMMST 225",
        "COMMST 227",
        "COMMST 228",
        "EMLS 103R",
        "EMLS 104R",
        "EMLS 110R",
        "ENGL 101B",
        "ENGL 108B",
        "ENGL 108D",
        "ENGL 119",
        "ENGL 208B",
        "ENGL 209",
        "ENGL 210E",
        "ENGL 210F",
        "ENGL 378",
        "MTHEL 300"
    ]
    
    # Remove all courses from math_core_courses (unless in dont_remove)
    for course in math_core_courses:
        if course in student_courses and course not in dont_remove:
            student_courses.remove(course)

    # Remove exactly one course from list_1 if present (unless in dont_remove)
    for course in list_1:
        if course in student_courses and course not in dont_remove:
            student_courses.remove(course)
            break  # remove only one course from list_1

    # Remove exactly one course from list_1_and_2 if present (unless in dont_remove)
    for course in list_1_and_2:
        if course in student_courses and course not in dont_remove:
            student_courses.remove(course)
            break  # remove only one course from list_1_and_2

    # Remove any courses with codes "COOP" or "PD"
    student_courses[:] = [
        course for course in student_courses 
        if not (course.startswith("COOP") or course.startswith("PD"))
    ]
    
    return student_courses


def check_complete_all(current_requirement, core_courses, student_courses, major_reqs):
    """
    Updates major_reqs and student_courses based on completed core courses.

    Args:
        student_courses: A list of student's completed courses.
        core_courses: A list of core courses for a specific requirement.
        major_reqs: A dictionary of PMATH program requirements.
        current_requirement: The requirement key to update in major_reqs.

    Returns:
        None. Modifies major_reqs and student_courses in-place.
    """
    # Find completed courses for the current requirement
    completed_courses = [course for course in core_courses if course in student_courses]

    # Update major_reqs with completed courses
    major_reqs[current_requirement][1].extend(completed_courses)

    # Set requirement status to True only if all core courses are completed
    major_reqs[current_requirement][0] = all(course in student_courses for course in core_courses)

    # Remove completed courses from student_courses
    for course in completed_courses:
        if course in student_courses:
            student_courses.remove(course)

def check_n_from_list_without_removing(current_requirement, required_courses, n, student_courses, major_reqs):
    """
    Checks if a student has completed n courses from a specified list.

    Args:
        current_requirement: The requirement key to update in major_reqs.
        required_courses: A list of courses required for the requirement.
        n: The minimum number of courses required to fulfill the requirement.
        student_courses: A list of student's completed courses.
        major_reqs: A dictionary of PMATH program requirements.

    Returns:
        None. Modifies major_reqs and student_courses in-place.
    """
    # Find completed courses from the required list
    completed_courses = [course for course in required_courses if course in student_courses]

    # Check if enough courses are completed
    if len(completed_courses) >= n:
        # Update major_reqs
        major_reqs[current_requirement][0] = True
        major_reqs[current_requirement][1].extend(completed_courses[:n])  # Add up to n courses



# Complete n courses from given list
def check_n_from_list(current_requirement, required_courses, n, student_courses, major_reqs):
    """
    Checks if a student has completed n courses from a specified list.

    Args:
        current_requirement: The requirement key to update in major_reqs.
        required_courses: A list of courses required for the requirement.
        n: The minimum number of courses required to fulfill the requirement.
        student_courses: A list of student's completed courses.
        major_reqs: A dictionary of PMATH program requirements.

    Returns:
        None. Modifies major_reqs and student_courses in-place.
    """
    # Find completed courses from the required list
    completed_courses = [course for course in required_courses if course in student_courses]

    # Check if enough courses are completed
    if len(completed_courses) >= n:
        # Update major_reqs
        major_reqs[current_requirement][0] = True
        major_reqs[current_requirement][1].extend(completed_courses[:n])  # Add up to n courses

        # Remove completed courses from student_courses
        for course in completed_courses[:n]:
            if course in student_courses:
                student_courses.remove(course)

def check_n_courses(current_requirement, eligible_levels, subject_codes, n, student_courses, major_reqs):
    """
    Checks if a student has completed n courses with eligible subject codes and levels.

    Args:
        current_requirement: The requirement key to update in major_reqs.
        eligible_levels: An integer representing the minimum eligible course level (100, 200, 300, or 400).
        subject_codes: A list of eligible subject codes (e.g., ["PMATH", "STAT"]).
        n: The minimum number of courses required to fulfill the requirement.
        student_courses: A list of student's completed courses.
        major_reqs: A dictionary of PMATH program requirements.

    Returns:
        None. Modifies major_reqs and student_courses in-place.
    """
    eligible_courses = []
    for course in student_courses:
        try:
            course_subject_code = course.split(" ")[0]  # Extract the subject code
            course_level = int(course.split(" ")[1][:3])  # Extract the course level (first 3 digits)

            if course_subject_code in subject_codes and course_level >= eligible_levels:
                eligible_courses.append(course)

        except (ValueError, IndexError):
            pass  # Ignore courses with invalid formats

    # Update major_reqs and student_courses
    major_reqs[current_requirement][1].extend(eligible_courses[:n]) # Add up to n eligible courses to the requirement

    # Remove courses used towards the requirement from student_courses
    for course in eligible_courses[:n]:
        if course in student_courses:
            student_courses.remove(course)

    # Set requirement status to True only if enough courses are completed
    if len(eligible_courses) >= n:
        major_reqs[current_requirement][0] = True

#######MY HELPER FUNCTIONS###############

def check_concentration(current_requirement, eligible_levels, subject_codes, n, student_courses, major_reqs):
    """
    Checks if a student has completed n courses with eligible subject codes and levels,
    with at least one course at or above eligible_levels.

    Args:
        current_requirement: The requirement key to update in major_reqs.
        eligible_levels: An integer representing the minimum eligible course level for one course (100, 200, 300, or 400).
        subject_codes: A list of eligible subject codes (e.g., ["PMATH", "STAT"]).
        n: The minimum number of courses required to fulfill the requirement.
        student_courses: A list of student's completed courses.
        major_reqs: A dictionary of the program requirements.

    Returns:
        None. Modifies major_reqs and student_courses in-place.
    """

    for code in subject_codes:
        eligible_courses = []
        high_level_courses = [] # store courses at or above eligible_levels

        for course in student_courses:
            if code in course:  # Check if the subject code is eligible
                try:
                    course_level = int(course.split(" ")[1])  # Extract the course level (after the space)
                    if course_level >= eligible_levels:  # Check if the course level is eligible
                        high_level_courses.append(course)
                    eligible_courses.append(course) # add all eligible courses to this list
                except (ValueError, IndexError):
                    pass  # Ignore courses with invalid formats

        # Check if enough eligible courses are completed for the current subject code
        # At least one course at or above eligible_levels and n total courses
        if len(high_level_courses) >= 1 and len(eligible_courses) >= n:

            # Update major_reqs
            major_reqs[current_requirement][0] = True

            # Add the high_level_courses to the courses to be removed
            courses_to_remove = high_level_courses[:1]  #add 1 high level course

            # Remove the courses to be removed from eligible_courses and add to the courses to be removed
            num_remaining = n - len(courses_to_remove)  # calculate remaining courses needed
            remaining_courses = [c for c in eligible_courses if c not in courses_to_remove]  # filter out already counted courses
            courses_to_remove.extend(remaining_courses[:num_remaining])  # add remaining courses up to n


            major_reqs[current_requirement][1].extend(courses_to_remove)  # Add up to n courses

            # Remove completed courses from student_courses
            for course in courses_to_remove:
                if course in student_courses:
                    student_courses.remove(course)
            return  # Exit the function after finding a concentration

def check_course_range(current_requirement, subject_code, min_course_num, max_course_num, student_courses, major_reqs, num_courses_required=1):
    """
    Checks if a student has completed a specified number of courses within a given range
    of course codes (e.g., CS440-CS498).

    Args:
        current_requirement: The requirement key to update in major_reqs.
        subject_code: The subject code (e.g., "CS").
        min_course_num: The minimum course number in the range.
        max_course_num: The maximum course number in the range.
        student_courses: A list of student's completed courses.
        major_reqs: A dictionary of program requirements.
        num_courses_required: The number of courses required within the range (default is 1).

    Returns:
        None. Modifies major_reqs and student_courses in-place.
    """
    completed_courses = []
    for course in student_courses:
        if course.startswith(subject_code):
            try:
                course_num = int(course.split(subject_code)[1])  # Extract course number
                if min_course_num <= course_num <= max_course_num:
                    completed_courses.append(course)
            except (ValueError, IndexError):
                pass  # Ignore courses with invalid formats

    # Update major_reqs and student_courses if enough courses are completed
    if len(completed_courses) >= num_courses_required:
        major_reqs[current_requirement][0] = True
        major_reqs[current_requirement][1].extend(completed_courses[:num_courses_required])

        # Remove completed courses from student_courses
        for course in completed_courses[:num_courses_required]:
            if course in student_courses:
                student_courses.remove(course)

def remove_courses(student_courses):
      '''
      Removes courses that end with 'L' or start with 'COOP' or 'PD' from the
      student's list of completed courses, and removed core courses except MATH 237, MATH 239.
      '''
      course_lists = [
          ["CS 115", "CS 135", "CS 145"],
          ["CS 116", "CS 136", "CS 146"],
          ["MATH 106", "MATH 136", "MATH 146"],
          ["MATH 127", "MATH 137", "MATH 147"],
          ["MATH 128", "MATH 138", "MATH 148"],
          ["MATH 135", "MATH 145"],
          ["MATH 235", "MATH 245"],
          ["STAT 230", "STAT 240"],
          ["STAT 231", "STAT 241"]
      ]

      # Loop over each list of courses
      for course_list in course_lists:
          # Find the intersection between the student's completed courses and the course list
          common_courses = list(set(student_courses) & set(course_list))

          # If there are any common courses, remove one of them from the student's courses
          if common_courses:
              course_to_remove = common_courses[0]
              student_courses.remove(course_to_remove)

      # Remove courses that end with 'L' or start with 'COOP' or 'PD'
      student_courses = [course for course in student_courses if not (course.endswith('L') or course.startswith('COOP') or course.startswith('PD'))]

      return student_courses

def check_one_course_from_list(current_requirement, subject_codes, student_courses, major_reqs):
      """
      Checks if a student has completed at least one course from a specified list of subject codes.

      Args:
          current_requirement: The requirement key to update in major_reqs.
          subject_codes: A list of eligible subject codes (e.g., ["AFM", "BUS", "COMM"]).
          student_courses: A list of student's completed courses.
          major_reqs: A dictionary of program requirements.

      Returns:
          None. Modifies major_reqs and student_courses in-place.
      """
      # Find completed courses from the required subject codes
      completed_courses = [course for course in student_courses
                          if any(code in course for code in subject_codes)]

      # Check if at least one course is completed
      if len(completed_courses) >= 1:
          # Update major_reqs
          major_reqs[current_requirement][0] = True
          major_reqs[current_requirement][1].extend(completed_courses[:1])  # Add up to 1 course

          # Remove completed course from student_courses
          for course in completed_courses[:1]:
              if course in student_courses:
                  student_courses.remove(course)


def check_one_group_complete_all(requirement_name, groups, student_courses, major_reqs):
    """
    Checks if a student has completed all courses in at least one of the provided groups.

    Args:
        requirement_name: Descriptive name of the requirement.
        groups: A list of lists, where each sublist is a group of required courses.
        student_courses: A list of student's completed courses.
        major_reqs: The dictionary where the result will be updated.
    """
    for group in groups:
        if all(course in student_courses for course in group):
            major_reqs[requirement_name] = [True, group]
            return
    major_reqs[requirement_name] = [False, []]
