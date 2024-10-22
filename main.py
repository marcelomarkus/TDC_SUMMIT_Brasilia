from fastapi import FastAPI
from endpoints import router

app = FastAPI(title="Server IA", swagger_ui_parameters={"defaultModelsExpandDepth": -1})
app.include_router(router)
