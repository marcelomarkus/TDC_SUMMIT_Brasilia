from fastapi import APIRouter
from settings import settings
from llama_index.llms.groq import Groq
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

router = APIRouter(prefix="/local", tags=["ia/local"])


@router.get("", summary="Enpoint ia com data local")
async def endpoint_local(question: str):
    groq_api = Groq(
        model="llama-3.1-70b-versatile",
        api_key=settings.GROQ_API_KEY,
        is_function_calling_model=True,
    )
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine(groq_api)
    result = query_engine.query(question)
    return result.response
