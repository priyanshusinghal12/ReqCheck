
import pdfplumber
import re

pdf_path = "transcript.pdf"
output_text = ""

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            for row in table:
                output_text += " | ".join(str(cell) if cell else "" for cell in row) + "\n"
        else:
            text = page.extract_text()
            if text:
                output_text += text + "\n\n"

# Saving to text file
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(output_text)


def extract_courses_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        transcript_text = file.read()
    
    course_pattern = re.compile(
        r"""(\b[A-Z]{1,9}\s*\d{1,5}[A-Z]?\b)  # Course code
              \s+(.+?)                          # Course name
              \s+(\d\.\d{2})                    # Attempted credits
              \s+(\d\.\d{2})                    # Earned credits
              \s+([A-Z]+|\d{1,3})               # Numeric or letter grade""",
        re.VERBOSE
    )
    
    # Non-credit grades to remove
    non_credit_grades = ['AUD', 'DNW', 'FTC', 'INC', 'IP', 'MM', 'NCR', 'NG', 'NMR', 'UR', 'WD', 'WF',]

    courses = []
    for match in course_pattern.finditer(transcript_text):
        course_code = match.group(1)
        grade = match.group(5)
        
        # Convert numeric grades to integers
        if grade.isdigit():
            grade = int(grade)
        
        # Remove non-credit grades and failed grades (below 50)
        if grade not in non_credit_grades:
            courses.append(course_code)
    
    courses = [course.replace('COMMST', 'SPCOM') for course in courses]

    return courses


# File path of the transcript
file_path = "transcript.txt"
parsed_data = extract_courses_from_file(file_path)
print(parsed_data)