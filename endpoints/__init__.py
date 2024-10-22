from fastapi import APIRouter
from endpoints import local_endpoint, openai_endpoint, groq_endpoint

router = APIRouter(prefix="/ia", tags=None)

router.include_router(openai_endpoint.router)
router.include_router(groq_endpoint.router)
router.include_router(local_endpoint.router)
