from src.core.llm import LLMService
from src.agents.product_manager import ProductManagerAgent
from src.agents.architect import ArchitectAgent

def test_llm_mock_fallback():
    """Test that LLMService falls back to mock when no API key is present."""
    # Ensure no API key for this test
    service = LLMService()
    service.api_key = None
    service.client = None

    response = service.generate_response("Test System Prompt", "Test User Prompt")
    assert isinstance(response, str)
    assert len(response) > 0

def test_pm_agent_mock():
    """Test Product Manager agent mock generation."""
    pm = ProductManagerAgent()
    # Force mock
    pm.llm.client = None

    idea = "A simple to-do list app"
    spec = pm.run(idea)

    assert "# Product Specification" in spec
    assert "User Roles" in spec
    assert "Core Features" in spec

def test_architect_agent_mock():
    """Test Architect agent mock generation."""
    arch = ArchitectAgent()
    # Force mock
    arch.llm.client = None

    spec = "# Product Specification\n..."
    architecture = arch.run(spec)

    assert "# System Architecture" in architecture
    assert "Tech Stack" in architecture
    assert "API Structure" in architecture
