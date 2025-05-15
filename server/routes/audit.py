from fastapi import APIRouter
import pandas as pd
from datetime import datetime

router = APIRouter()
audit_logs = []

@router.get("/actions")
def get_audit_logs(user_id: str):
    """Fetch tamper-proof action logs"""
    return [log for log in audit_logs if log["user_id"] == user_id]