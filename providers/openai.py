import os
import httpx
from providers.base import BaseProvider
from schemas.chat_request import ChatCompletionRequest
from schemas.chat_response import ChatCompletionResponse
from fastapi import HTTPException 



class OpenAIProvider(BaseProvider):
    def __init__(self):
        self.api_key = os.environ.get("MY_API_KEY")
        if not self.api_key:
            raise ValueError("MY_API_KEY environ variable not yet set")
    
    async def chat_completion(self, request):
        headers = {
        "Authorization": f"Bearer {self.api_key}",
        "Content-Type": "application/json",
    }
        async with httpx.AsyncClient(timeout=30) as client:
            OPENAI_URL = "https://api.openai.com/v1/chat/completions"
            response = await client.post(
                OPENAI_URL,
                headers=headers,
                json=request.dict(exclude_none=True)
            )
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=response.json(),
        )
            return response.json()
