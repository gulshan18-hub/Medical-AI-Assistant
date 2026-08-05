from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'Medical AI Assistant Pro'
    debug: bool = False
    llm_provider: str = 'gemini'
    database_url: str = 'sqlite:///medical_ai.db'

    class Config:
        env_file = '.env'
        case_sensitive = False


settings = Settings()
