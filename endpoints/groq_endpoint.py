from fastapi import APIRouter
from engine_ia import groq_api

router = APIRouter(prefix="/groq", tags=["ia/groq"])


@router.get("", summary="Endpoint Integração groq")
async def endpoint_groq(question: str):
    result = groq_api.chat.completions.create(
        model="gpt-4o", messages=[{"role": "user", "content": question}]
    )
    return result.choices[0].message.content


@router.post("/audio", summary="Endpoint Integração groq")
async def endpoint_audio_groq():
    with open("./audio/audio_tdc.wav", "rb") as audio_file:
        audio_bytes = audio_file
        response = await groq_api.audio.transcriptions.create(
            model="whisper-large-v3-turbo",
            file=audio_bytes,
            response_format="verbose_json",
        )
        print(response.text)
        return response.text
