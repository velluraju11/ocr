import os
from typing import Optional
from pydantic_settings import BaseSettings

class RyhaConfig(BaseSettings):
    """Configuration for Ryha AI Builder."""

    # AI Model Settings
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    DEFAULT_MODEL: str = "gpt-4o"

    # Project Settings
    WORKSPACE_DIR: str = os.getenv("WORKSPACE_DIR", "./ryha_workspace")

    # Modes
    BOSS_MODE: bool = True
    DEBUG_MODE: bool = False

    class Config:
        env_file = ".env"

settings = RyhaConfig()
