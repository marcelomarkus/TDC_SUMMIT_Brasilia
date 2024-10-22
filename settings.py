from pydantic_settings import BaseSettings
from pydantic import Field


class ConfigEnv(BaseSettings):
    OPENAI_API_KEY: str = Field(validation_alias="OPENAI_API_KEY")
    GROQ_API_KEY: str = Field(validation_alias="GROQ_API_KEY")


settings = ConfigEnv()
