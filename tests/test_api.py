import pytest
from fastapi.testclient import TestClient
from src.server import app

client = TestClient(app)

def test_read_main():
    """Test the root endpoint serving the UI."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Ryha AI Builder" in response.text
    assert "Boss Mode" in response.text

def test_static_files():
    """Test that static CSS/JS files are served."""
    response = client.get("/static/styles.css")
    assert response.status_code == 200

    response = client.get("/static/script.js")
    assert response.status_code == 200

def test_websocket_endpoint():
    """Test the WebSocket build endpoint."""
    with client.websocket_connect("/ws/build") as websocket:
        # Send an idea
        websocket.send_text("Build a test app")

        # We expect a series of JSON messages
        messages = []
        try:
            while True:
                data = websocket.receive_json()
                messages.append(data)
                if data.get("type") in ["done", "complete"] and data.get("type") == "done":
                    break
        except Exception:
            pass

        # Verify we got messages
        assert len(messages) > 0

        # Verify structure of at least one log message
        log_msg = next((m for m in messages if m["type"] == "log"), None)
        assert log_msg is not None

        # Verify completion
        done_msg = messages[-1]
        assert done_msg["type"] == "done"
