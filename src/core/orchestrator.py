from src.agents.product_manager import ProductManagerAgent
from src.agents.architect import ArchitectAgent
from src.core.config import settings
import time

class Orchestrator:
    def __init__(self):
        self.pm = ProductManagerAgent()
        self.architect = ArchitectAgent()
        # Future agents: Backend, Frontend, DevOps

    def build_software(self, user_idea: str):
        print("\n🚀 Ryha AI Builder Initialized...")
        if settings.BOSS_MODE:
            print("🃏 Boss Mode Active: Prioritizing Security & Optimization.")

        # Step 1: Product Manager
        print("\n--- Step 1: Product Specification ---")
        spec = self.pm.run(user_idea)
        print(spec)
        time.sleep(1)

        # Step 2: System Architect
        print("\n--- Step 2: System Architecture ---")
        architecture = self.architect.run(spec)
        print(architecture)

        # Future steps:
        # backend_code = self.backend.run(architecture)
        # frontend_code = self.frontend.run(architecture)

        return {
            "spec": spec,
            "architecture": architecture
        }
