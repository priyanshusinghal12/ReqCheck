# save_results.py

from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import List, Dict, Any
import firebase_admin
from firebase_admin import credentials, auth, firestore
from fastapi import Depends, Header
from fastapi.responses import JSONResponse

# Initialize Firebase Admin SDK (once globally in your project)
try:
    firebase_admin.get_app()
except ValueError:
    cred = credentials.Certificate("backend/reqcheck-2d1b3-firebase-adminsdk-fbsvc-5e73788aec.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()
router = APIRouter()

class SaveResultRequest(BaseModel):
    id_token: str
    major: str
    completed_courses: List[str]
    requirements: Dict[str, Any]

@router.post("/save-results/")
async def save_results(req: SaveResultRequest):
    try:
        decoded_token = auth.verify_id_token(req.id_token)
        uid = decoded_token["uid"]

        user_ref = db.collection("users").document(uid)
        user_ref.set(
            {
                "results": {
                    "major": req.major,
                    "completed_courses": req.completed_courses,
                    "requirements": req.requirements,
                }
            },
            merge=True,
        )
        return {"status": "success", "message": "Results saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    
@router.get("/get-saved-results/")
async def get_saved_results(Authorization: str = Header(...)):
	try:
		id_token = Authorization.split("Bearer ")[-1]
		decoded_token = auth.verify_id_token(id_token)
		uid = decoded_token["uid"]

		doc = db.collection("users").document(uid).get()
		if doc.exists:
			return {"status": "success", "results": doc.to_dict().get("results", {})}
		else:
			return {"status": "error", "message": "No results saved."}
	except Exception as e:
		return JSONResponse(status_code=401, content={"status": "error", "message": str(e)})
