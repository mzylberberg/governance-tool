from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_translate_executive():
    text = (
        "EDR detected suspicious PowerShell activity and blocked the process "
        "on two endpoints."
    )
    payload = {"text": text, "audience": "executive"}

    r = client.post("/translate", json=payload)
    assert r.status_code == 200

    data = r.json()
    assert data["audience"] == "executive"
    assert isinstance(data["summary"], str)
    assert isinstance(data["risks"], list)
    assert isinstance(data["recommended_actions"], list)



def test_history_returns_list():
    r = client.get("/history?limit=5")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) <= 5

