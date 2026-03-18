from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_process_task_success():
    response = client.post("/task", json={"task": "Write a short blog on AI in healthcare"})
    body = response.json()

    assert response.status_code == 200
    assert body["status"] == "completed"
    assert body["task"] == "Write a short blog on AI in healthcare"
    assert len(body["plan"]) > 0
    assert "execution" in body


def test_process_task_validation_error():
    response = client.post("/task", json={"task": ""})
    assert response.status_code == 422
