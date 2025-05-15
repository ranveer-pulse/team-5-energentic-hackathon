import requests
from config import settings
from schemas.models import DERAction

class DEROrchestrator:
    @staticmethod
    def execute_action(action: DERAction):
        """World Engine integration for DER control"""
        response = requests.post(
            f"{settings.world_engine_url}/toggle_appliance",
            json=action.dict()
        )
        return response.status_code == 200

    @classmethod
    def reduce_load(cls, deficit_kw: float = 10.0):
        """Grid emergency response"""
        requests.post(
            f"{settings.world_engine_url}/emergency",
            json={"action": "shed_load", "deficit_kw": deficit_kw}
        )