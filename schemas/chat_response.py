from pydantic import BaseModel
from typing import Dict, Any, Optional

class ChatCompletionResponse(BaseModel):
    id: str
    model: str
    content: str
    usage: Optional[Dict[str, int]] = None
    raw: Optional[Dict[str, Any]] = None
    