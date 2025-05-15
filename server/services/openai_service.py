import openai
from config import settings

class OpenAIService:
    def __init__(self):
        openai.api_key = settings.openai_api_key

    def explain_action(self, action: str, context: str) -> str:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Explain energy actions simply."},
                {"role": "user", "content": f"Why did the agent {action}? Context: {context}"}
            ]
        )
        return response.choices[0].message.content