"""載入 Gemini 設定並提供單次文字問答功能。"""

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = PROJECT_ROOT / ".env"
SYSTEM_PROMPT = "你是一位友善且回答簡潔的 AI 助理。"


def ask_llm(message: str) -> str:
    try:
        from dotenv import load_dotenv
        from langchain_google_genai import ChatGoogleGenerativeAI
    except ImportError as error:
        raise RuntimeError(
            "AI dependencies are not installed; run pip install -r requirements.txt"
        ) from error

    load_dotenv(ENV_FILE)
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured")

    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    llm = ChatGoogleGenerativeAI(
        model=model,
        google_api_key=api_key,
    )
    response = llm.invoke(
        [
            ("system", SYSTEM_PROMPT),
            ("human", message),
        ]
    )
    return str(response.content)
