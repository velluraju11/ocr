from src.agents.base_agent import RyhaAgent

class ArchitectAgent(RyhaAgent):
    def __init__(self):
        super().__init__(name="Arch-01", role="System Architect")

    def run(self, product_spec: str) -> str:
        self.log("Designing system architecture based on spec...")

        system_prompt = """You are an expert System Architect for Ryha AI Builder.
Your goal is to design a robust, scalable technical architecture based on the provided Product Specification.

Decide on:
1. Tech Stack (Frontend, Backend, Database)
2. Database Schema (Tables, Fields)
3. API Design (Endpoints)
4. Security Considerations

Output in Markdown format."""

        response = self.llm.generate_response(system_prompt, product_spec)
        self.log("Architecture design completed.")
        return response
