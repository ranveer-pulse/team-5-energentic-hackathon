import requests

BECKN_GATEWAY = "https://bap-ps-network-deg-team5.becknprotocol.io"

class BecknClient:
    @staticmethod
    def fetch_flex_programs():
        """Discover Demand Flexibility Programs (DFPs)"""
        response = requests.post(
            f"{BECKN_GATEWAY}/search",
            json={
                "context": {"domain": "energy"},
                "message": {
                    "intent": {
                        "item": {
                            "descriptor": {
                                "name": "Demand Flexibility"
                            }
                        }
                    }
                }
            }
        )
        return response.json().get("dfps", [])