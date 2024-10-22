from fastapi import APIRouter
from engine_ia import openai_api

router = APIRouter(prefix="/openai", tags=["ia/openai"])


@router.get("", summary="Endpoint Integração Openai")
async def endpoint_openai(question: str):
    result = openai_api.chat.completions.create(
        model="gpt-4o", messages=[{"role": "user", "content": question}]
    )
    return result.choices[0].message.content
