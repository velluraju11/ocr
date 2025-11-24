from typing import Any
from abc import ABC, abstractmethod
from src.core.llm import LLMService

class RyhaAgent(ABC):
    """
    Base class for all Ryha AI Agents.
    """
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.llm = LLMService()

    @abstractmethod
    def run(self, input_data: Any) -> Any:
        """
        Execute the agent's task.
        """
        pass

    def log(self, message: str):
        """
        Log agent activity.
        """
        print(f"[{self.role}] {self.name}: {message}")
