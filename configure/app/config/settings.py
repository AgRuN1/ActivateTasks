from pydantic_settings import BaseSettings


class ProjectSettings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str

project_settings = ProjectSettings()