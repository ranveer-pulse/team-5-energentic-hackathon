from fastapi import APIRouter, BackgroundTasks
from services.beckn_client import BecknClient
from services.der_orchestrator import DEROrchestrator
from schemas.models import DERAction

router = APIRouter()

@router.get("/status")
def get_grid_status():
    return {"status": "peak" if 18 <= datetime.now().hour < 21 else "normal"}

@router.post("/recommendations")
def generate_recommendations(user_id: str):
    """Provide energy-saving suggestions"""
    return {
        "actions": [
            {"device": "ev", "action": "delay", "savings": "₹150"},
            {"device": "ac", "action": "adjust", "savings": "₹75"}
        ]
    }

@router.post("/respond")
def handle_grid_peak(background_tasks: BackgroundTasks):
    """Trigger DER actions during grid stress"""
    background_tasks.add_task(DEROrchestrator.reduce_load)
    return {"status": "mitigation_triggered"}