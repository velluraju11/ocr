import pytest
from src.core.orchestrator import Orchestrator

def test_orchestrator_generator_flow():
    """Test the generator pattern of the Orchestrator."""
    orchestrator = Orchestrator()
    # Force mock for agents
    orchestrator.pm.llm.client = None
    orchestrator.architect.llm.client = None

    idea = "Test Idea"
    events = list(orchestrator.build_software_generator(idea))

    # Check that we received a sequence of events
    assert len(events) > 0

    # Check for specific event types
    event_types = [e["type"] for e in events]
    assert "log" in event_types
    assert "status" in event_types
    assert "artifact" in event_types
    assert "complete" in event_types

    # Check final result
    complete_event = next(e for e in events if e["type"] == "complete")
    assert "spec" in complete_event["result"]
    assert "architecture" in complete_event["result"]
