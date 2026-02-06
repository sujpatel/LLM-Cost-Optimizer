import os
import httpx
from providers.base import BaseProvider
from schemas.chat_request import ChatCompletionRequest
from schemas.chat_response import ChatCompletionResponse
from fastapi import HTTPException 

    class ClaudeProvider(BaseProvider):
        def __init__(self):
            self.api_key = os.environ.get("ANTHROPIC KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC KEY NOT SET")
    async def chat_completion(self, request):
        headers = {
            "api-key": self.api_key,
            "anthropic-version": "date",
            "Content-Type": "application/json",
        }
        
        async with httpx.AsyncClient(timeout=30) as client:
            response= await client.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload,)
        
        if response.status_code != 200:
            raise HTTPException(
                status_coe=response.status_code,
                detail=response.json(),
            )
        return response.json()