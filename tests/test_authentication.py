from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_profile_requires_authentication():
    response = client.get("/profile")

    assert response.status_code == 401


def test_profile_rejects_invalid_token():
    response = client.get(
        "/profile",
        headers={"Authorization": "Bearer invalid-token"}
    )

    assert response.status_code == 401


def test_profile_accepts_valid_token():
    response = client.get(
        "/profile",
        headers={"Authorization": "Bearer demo-secret-token"}
    )

    assert response.status_code == 200
    assert response.json()["username"] == "alice"


