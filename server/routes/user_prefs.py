from fastapi import APIRouter
from schemas.models import UserPreferences

router = APIRouter()
prefs_db = {}  # Simulated database

@router.get("/preferences/{user_id}")
def get_preferences(user_id: str):
    return prefs_db.get(user_id, UserPreferences(user_id=user_id).dict())

@router.post("/preferences")
def update_preferences(prefs: UserPreferences):
    prefs_db[prefs.user_id] = prefs
    return {"status": "updated"}