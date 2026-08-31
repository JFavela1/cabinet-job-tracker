from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    app_password: str = "changeme"
    session_secret: str = "dev-only-not-secret"


settings = Settings()
