from src.agents.base_agent import RyhaAgent

class ProductManagerAgent(RyhaAgent):
    def __init__(self):
        super().__init__(name="PM-01", role="Product Manager")

    def run(self, idea: str) -> str:
        self.log(f"Analyzing idea: {idea}")

        system_prompt = """You are an expert Product Manager for Ryha AI Builder.
Your goal is to convert a raw idea into a comprehensive Product Specification.
Include:
1. Executive Summary
2. User Roles
3. Core Features
4. User Flow
5. Edge Cases

Output in Markdown format."""

        response = self.llm.generate_response(system_prompt, idea)
        self.log("Product Specification generated.")
        return response
