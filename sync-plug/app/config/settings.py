from pydantic_settings import BaseSettings


class ProjectSettings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    CONFIGURE_ADDR: str
    DELAY: int

project_settings = ProjectSettings()