import sys
import os
import base64
import tempfile
import pdfplumber
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# Add backend and logic directories to path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "course_logic")))

# Imports
from parseTranscript import extract_courses_from_file


from course_logic.checkStatisticsReqs import check_stats_major  
from course_logic.checkActSciReqs import check_actsci_major
from course_logic.checkAMathReqs import check_amath_major
from course_logic.checkBioStatsReqs import check_biostats_major
from course_logic.checkCompMathReqs import check_comp_math_reqs
from course_logic.checkCSReqs import check_computer_science_major
from course_logic.checkDataScienceReqs import check_data_science_major
from course_logic.checkMathDegreeReqs import check_math_degree_reqs
from course_logic.checkMathEconReqs import check_math_econ_reqs
from course_logic.checkMathFinanceReqs import check_math_finance_reqs
from course_logic.checkMathOptBusReqs import check_math_opt_bus_specialization
from course_logic.checkMathOptOpsReqs import check_math_opt_ops_specialization
from course_logic.checkMathPhysicsReqs import check_math_physics_reqs
from course_logic.checkMathStudiesBusReqs import math_studies_business_reqs
from course_logic.checkMathStudiesReqs import math_studies_reqs
from course_logic.checkMathTeachReqs import check_math_teaching_major
from course_logic.checkPMathReqs import check_pmath_major
from course_logic.checkCOReqs import check_co_major
from course_logic.checkCSReqs import check_computer_science_major
from saveResults import router as save_router

app.include_router(save_router)



app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://req-check.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Data models
class TranscriptRequest(BaseModel):
    major: str
    minor: str = None
    completed_courses: List[str]

class TranscriptUpload(BaseModel):
    base64_pdf: str

# === MAIN ENDPOINT ===
@app.post("/check-requirements/")
def check_requirements(request: TranscriptRequest):
    major = request.major.lower()
    completed_courses = request.completed_courses

    match major:
        case "math degree requirements":
            result = check_math_degree_reqs(completed_courses)
        case "statistics":
            result = check_stats_major(completed_courses)
        case "actuarial science":
            result = check_actsci_major(completed_courses)
        case "applied mathematics":
            result = check_amath_major(completed_courses)
        case "biostatistics":
            result = check_biostats_major(completed_courses)
        case "computational mathematics":
            result = check_comp_math_reqs(completed_courses)
        case "computer science":
            result = check_computer_science_major(completed_courses)
        case "bmath data science":
            result = check_data_science_major(completed_courses)
        case "mathematical studies":
            result = math_studies_reqs(completed_courses)
        case "mathematical studies (business)":
            result = math_studies_business_reqs(completed_courses)
        case "mathematical economics":
            result = check_math_econ_reqs(completed_courses)
        case "mathematical finance":
            result = check_math_finance_reqs(completed_courses)
        case "mathematical physics":
            result = check_math_physics_reqs(completed_courses)
        case "pure mathematics":
            result = check_pmath_major(completed_courses)
        case "mathematical optimization (business specialization)":
            result = check_math_opt_bus_specialization(completed_courses)
        case "mathematical optimization (operations specialization)":
            result = check_math_opt_ops_specialization(completed_courses)
        case "mathematics teaching":
            result = check_math_teaching_major(completed_courses)
        case "combinatorics and optimization":
            result = check_co_major(completed_courses)
        case "bcs computer science":
            result = check_computer_science_major(completed_courses)
        case _:
            return {"error": "Major not supported"}
    
    return {"major": major, "requirements": result}


# === TRANSCRIPT PARSING ENDPOINT ===
@app.post("/parse-transcript/")
def parse_transcript(upload: TranscriptUpload):
    pdf_data = base64.b64decode(upload.base64_pdf)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(pdf_data)
        temp_pdf_path = temp_pdf.name

    transcript_txt_path = temp_pdf_path.replace(".pdf", ".txt")

    with pdfplumber.open(temp_pdf_path) as pdf:
        with open(transcript_txt_path, "w", encoding="utf-8") as f:
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    for row in table:
                        f.write(" | ".join(str(cell) if cell else "" for cell in row) + "\n")
                else:
                    text = page.extract_text()
                    if text:
                        f.write(text + "\n\n")

    courses = extract_courses_from_file(transcript_txt_path)
    return {"courses": courses}
