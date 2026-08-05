from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Medical AI Assistant Pro"
    api_v1_prefix: str = "/api/v1"
    debug: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
