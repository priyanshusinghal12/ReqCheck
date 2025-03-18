import sys
import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Ensure backend is in Python path

from course_logic.checkStatisticsReqs import check_stats_major  # Keep relative import

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
from course_logic.checkStatisticsReqs import check_stats_major


app = FastAPI()

# Define the request structure
class TranscriptRequest(BaseModel):
    major: str
    minor: str = None
    completed_courses: List[str]

# API endpoint for checking requirements
@app.post("/check-requirements/")
def check_requirements(request: TranscriptRequest):
    major = request.major.lower()
    completed_courses = request.completed_courses
    
    if major == "statistics":
        result = check_stats_major(completed_courses)
    else:
        return {"error": "Major not supported"}
    
    return {"major": major, "requirements": result}
