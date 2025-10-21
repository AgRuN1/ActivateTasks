from pydantic_settings import BaseSettings


class ProjectSettings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    DEBUG: bool = False
    RABBITMQ_DSN: str

project_settings = ProjectSettings()