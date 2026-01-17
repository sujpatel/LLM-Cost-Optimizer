from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import httpx
import os

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_URL = "https://api.openai.com/v1/chat/completions"

class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Dict[str, Any]]
    max_tokens: int | None = None
    
    
@app.post("/v1/chat/completions")
async def OpenAIRequest(body: ChatCompletionRequest):
    
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(
            OPENAI_URL,
            headers=headers,
            json=body.dict(exclude_none=True)
        )
    
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.json(),
        )
    return response.json()
    