from pydantic_settings import BaseSettings


class ProjectSettings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    RABBITMQ_DSN: str

project_settings = ProjectSettings()