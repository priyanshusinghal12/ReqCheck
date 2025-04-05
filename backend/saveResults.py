from fastapi import APIRouter, Header, Body, Request, HTTPException  
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse
import os, json, firebase_admin
from firebase_admin import credentials, auth, firestore
from datetime import datetime

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
        raise ValueError("FIREBASE_ADMIN_KEY not found in env")

db = firestore.client()
router = APIRouter()

# === Pydantic Models ===
class RequirementItem(BaseModel):
    name: str
    met: bool
    courses: List[str]

class SaveResultRequest(BaseModel):
    id_token: str
    major: str
    name: str
    completed_courses: List[str]
    requirements: List[RequirementItem]
    
class EditNameRequest(BaseModel):
    id_token: str
    index: int
    new_name: str

class DeleteResultRequest(BaseModel):
    id_token: str
    index: int



# === POST: Save Results ===
@router.post("/save-results/")
async def save_results(req: SaveResultRequest):
    try:
        decoded = auth.verify_id_token(req.id_token)
        uid = decoded["uid"]
        timestamp = datetime.utcnow().isoformat()

        result_data = {
            "timestamp": timestamp,
            "name": req.name,
            "major": req.major,
            "completed_courses": req.completed_courses,
            "requirements": [r.dict() for r in req.requirements]  # FIXED
        }


        user_ref = db.collection("users").document(uid)
        user_doc = user_ref.get()
        current = user_doc.to_dict().get("results", []) if user_doc.exists else []

        current.append(result_data)
        user_ref.set({"results": current}, merge=True)

        return {"status": "success", "message": "Result saved."}
    except Exception as e:
        return JSONResponse(status_code=400, content={"status": "error", "message": str(e)})

# === GET: Get Saved Results ===
@router.get("/get-saved-results/")
async def get_saved_results(Authorization: str = Header(...)):
    try:
        id_token = Authorization.split("Bearer ")[-1]
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token["uid"]

        doc = db.collection("users").document(uid).get()
        if doc.exists:
            return {
                "status": "success",
                "results": doc.to_dict().get("results", [])
            }
        else:
            return {"status": "error", "message": "No results found"}
    except Exception as e:
        return JSONResponse(status_code=401, content={"status": "error", "message": str(e)})
    
    
    
@router.patch("/edit-result-name/")
async def edit_result_name(req: EditNameRequest):
    try:
        decoded = auth.verify_id_token(req.id_token)
        uid = decoded["uid"]

        user_ref = db.collection("users").document(uid)
        user_doc = user_ref.get()
        if not user_doc.exists:
            raise HTTPException(status_code=404, detail="User not found.")

        results = user_doc.to_dict().get("results", [])
        if req.index < 0 or req.index >= len(results):
            raise HTTPException(status_code=400, detail="Invalid index.")

        results[req.index]["name"] = req.new_name
        user_ref.set({"results": results}, merge=True)
        return {"status": "success", "message": "Name updated."}

    except Exception as e:
        return JSONResponse(status_code=400, content={"status": "error", "message": str(e)})

@router.delete("/delete-result/")
async def delete_result(req: DeleteResultRequest):
    try:
        decoded = auth.verify_id_token(req.id_token)
        uid = decoded["uid"]

        user_ref = db.collection("users").document(uid)
        user_doc = user_ref.get()
        if not user_doc.exists:
            raise HTTPException(status_code=404, detail="User not found.")

        results = user_doc.to_dict().get("results", [])
        if req.index < 0 or req.index >= len(results):
            raise HTTPException(status_code=400, detail="Invalid index.")

        results.pop(req.index)
        user_ref.set({"results": results}, merge=True)
        return {"status": "success", "message": "Result deleted."}

    except Exception as e:
        return JSONResponse(status_code=400, content={"status": "error", "message": str(e)})


@router.delete("/delete-account/")
def delete_account(request: Request, id_token: str = Body(...)):
    try:
        decoded_token = auth.verify_id_token(id_token)
        user_id = decoded_token["uid"]
        db.collection("users").document(user_id).delete()
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
