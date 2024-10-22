from openai import OpenAI
from groq import Groq
from settings import settings

openai_api = OpenAI(api_key=settings.OPENAI_API_KEY)
groq_api = Groq(api_key=settings.GROQ_API_KEY)
