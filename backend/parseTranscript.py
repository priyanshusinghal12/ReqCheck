import pdfplumber
import re

def extract_courses_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        transcript_text = file.read()

    course_pattern = re.compile(
        r"""(\b[A-Z]{1,9}\s*\d{1,5}[A-Z]?\b)  # Course code
              \s+(.+?)                          # Course name
              \s+(\d\.\d{2})                    # Attempted credits
              \s+(\d\.\d{2})                    # Earned credits
              \s+([A-Z]+|\d{1,3})               # Grade
        """,
        re.VERBOSE
    )

    non_credit_grades = [
        'AUD', 'DNW', 'FTC', 'INC', 'IP', 'MM', 'NCR', 'NG', 'NMR', 'UR', 'WD', 'WF',
    ]

    courses = []
    for match in course_pattern.finditer(transcript_text):
        course_code = match.group(1)
        grade = match.group(5)

        if grade.isdigit():
            grade = int(grade)

        if grade not in non_credit_grades and not (isinstance(grade, int) and grade < 50):
            courses.append(course_code)

    courses = [course.replace("COMMST", "SPCOM") for course in courses]
    return courses
