from fastapi import APIRouter, Request, Depends, Header
from pydantic import BaseModel
from typing import List, Dict, Any
from fastapi.responses import JSONResponse
import os
import json
import firebase_admin
from firebase_admin import credentials, auth, firestore

# Initialize Firebase Admin
try:
    firebase_admin.get_app()
except ValueError:
    firebase_key = os.environ.get("FIREBASE_ADMIN_KEY")
    if firebase_key:
        cred_dict = json.loads(firebase_key)
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
    else:
        raise ValueError("FIREBASE_ADMIN_KEY not found in environment variables")

# Firestore setup
db = firestore.client()
router = APIRouter()

# Request Model
class SaveResultRequest(BaseModel):
    id_token: str
    major: str
    completed_courses: List[str]
    requirements: Dict[str, Any]  # NOTE: This must be JSON-serializable!

# POST endpoint to save results
@router.post("/save-results/")
async def save_results(req: SaveResultRequest):
    try:
        decoded_token = auth.verify_id_token(req.id_token)
        uid = decoded_token["uid"]

        # Save results to Firestore under the user's document
        user_ref = db.collection("users").document(uid)
        user_ref.set({
            "results": {
                "major": req.major,
                "completed_courses": req.completed_courses,
                "requirements": json.loads(json.dumps(req.requirements))  # force JSON serializability
            }
        }, merge=True)

        return {"status": "success", "message": "Results saved."}
    except Exception as e:
        return JSONResponse(status_code=400, content={"status": "error", "message": str(e)})

# GET endpoint to retrieve saved results
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
