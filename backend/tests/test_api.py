from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_translate_executive():
    payload = {
        "text": "EDR detected suspicious PowerShell activity and blocked the process on two endpoints.",
        "audience": "executive",
    }
    r = client.post("/translate", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["audience"] == "executive"
    assert "summary" in data and isinstance(data["summary"], str)
    assert "risks" in data and isinstance(data["risks"], list)
    assert "recommended_actions" in data and isinstance(data["recommended_actions"], list)


def test_history_returns_list():
    r = client.get("/history?limit=5")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) <= 5

