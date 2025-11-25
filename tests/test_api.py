import pytest
from fastapi.testclient import TestClient
from src.server import app

client = TestClient(app)

def test_home_page():
    """Test the landing page."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Thought-to-Software" in response.text

def test_pricing_page():
    """Test the pricing page."""
    response = client.get("/pricing")
    assert response.status_code == 200
    assert "Boss Mode" in response.text
    assert "$199" in response.text

def test_app_page():
    """Test the builder app page."""
    response = client.get("/app")
    assert response.status_code == 200
    assert "Ryha AI Builder" in response.text

def test_static_files():
    """Test that static CSS/JS files are served."""
    response = client.get("/static/css/style.css")
    assert response.status_code == 200

    response = client.get("/static/js/app.js")
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
