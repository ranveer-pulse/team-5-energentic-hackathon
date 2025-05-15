from pydantic import BaseModel
from datetime import datetime

class UserPreferences(BaseModel):
    user_id: str
    allow_auto_adjust: bool = True
    max_delay_minutes: int = 30
    priority_devices: list = ["medical"]

class DERAction(BaseModel):
    device_type: str  # "ev", "ac", "water_heater"
    action: str       # "on", "off", "delay"
    duration: int = 15  # minutes

class AuditLog(BaseModel):
    timestamp: datetime
    user_id: str
    action: str
    signature: str

class LLMExplanation(BaseModel):
    query: str
    response: str