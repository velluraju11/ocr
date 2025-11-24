import os
from src.core.config import settings

def test_boss_mode_default():
    """Test that Boss Mode is active by default as per requirements."""
    assert settings.BOSS_MODE is True

def test_default_model():
    """Test default AI model configuration."""
    assert settings.DEFAULT_MODEL == "gpt-4o"

def test_env_loading(monkeypatch):
    """Test that environment variables override defaults."""
    monkeypatch.setenv("BOSS_MODE", "False")
    # We need to reload the config or instantiate a new one to test env var loading
    # since settings is instantiated at import time.
    from src.core.config import RyhaConfig
    new_settings = RyhaConfig()
    assert new_settings.BOSS_MODE is False
