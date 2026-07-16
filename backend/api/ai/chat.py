"""接收 AI Chat 請求，並呼叫 Gemini 產生回答。"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from backend.ai.gemini import ask_llm

router = APIRouter(prefix="/ai")


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)


@router.post("/chat")
def chat(request: ChatRequest) -> dict[str, str]:
    try:
        reply = ask_llm(request.message)
    except RuntimeError as error:
        raise HTTPException(status_code=503, detail=str(error)) from error
    except Exception as error:
        raise HTTPException(status_code=502, detail="Gemini request failed") from error

    return {"reply": reply}
