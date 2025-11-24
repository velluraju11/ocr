from src.agents.product_manager import ProductManagerAgent
from src.agents.architect import ArchitectAgent
from src.core.config import settings
import time
from typing import Generator, Dict, Any

class Orchestrator:
    def __init__(self):
        self.pm = ProductManagerAgent()
        self.architect = ArchitectAgent()
        # Future agents: Backend, Frontend, DevOps

    def build_software_generator(self, user_idea: str) -> Generator[Dict[str, Any], None, None]:
        """
        Yields events during the build process for real-time UI updates.
        """
        yield {"type": "log", "message": "🚀 Ryha AI Builder Initialized..."}

        if settings.BOSS_MODE:
            yield {"type": "log", "message": "🃏 Boss Mode Active: Prioritizing Security & Optimization."}

        # Step 1: Product Manager
        yield {"type": "log", "message": "\n--- Step 1: Product Specification ---"}
        yield {"type": "status", "agent": "Product Manager", "status": "working"}

        spec = self.pm.run(user_idea)

        yield {"type": "artifact", "name": "Product Specification", "content": spec}
        yield {"type": "log", "message": "Product Specification generated."}
        yield {"type": "status", "agent": "Product Manager", "status": "done"}

        time.sleep(1)

        # Step 2: System Architect
        yield {"type": "log", "message": "\n--- Step 2: System Architecture ---"}
        yield {"type": "status", "agent": "System Architect", "status": "working"}

        architecture = self.architect.run(spec)

        yield {"type": "artifact", "name": "System Architecture", "content": architecture}
        yield {"type": "log", "message": "Architecture design completed."}
        yield {"type": "status", "agent": "System Architect", "status": "done"}

        # Final Result
        yield {"type": "complete", "result": {"spec": spec, "architecture": architecture}}

    def build_software(self, user_idea: str):
        """Legacy method for CLI"""
        results = {}
        for event in self.build_software_generator(user_idea):
            if event["type"] == "log":
                print(event["message"])
            elif event["type"] == "artifact":
                print(f"\n[Generated {event['name']}]\n{event['content']}")
            elif event["type"] == "complete":
                results = event["result"]
        return results
