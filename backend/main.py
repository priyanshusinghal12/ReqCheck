import sys
import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Ensure backend is in Python path

from course_logic.checkStatisticsReqs import check_stats_major  # Keep relative import

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
