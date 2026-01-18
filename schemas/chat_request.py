from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Dict[str, Any]]
    max_tokens: Optional[int] = None