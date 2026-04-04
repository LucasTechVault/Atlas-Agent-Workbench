from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str
    openai_model: str = "gpt-4.1-mini"

    langsmith_tracing: bool = True
    langsmith_api_key: str | None = None
    langsmith_project: str = "atlas-workbench"

    embed_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    app_host: str = "0.0.0.0"
    app_port: int = 8000

    max_research_rounds: int = 2
    max_initial_tasks: int = 3
    max_tasks_per_cluster: int = 2

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()