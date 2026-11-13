from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_user_cannot_access_another_users_profile():
    response = client.get(
        "/users/2",
        headers={"Authorization": "Bearer demo-secret-token"}
    )

    assert response.status_code == 403


def test_user_can_access_own_profile():
    response = client.get(
        "/users/1",
        headers={"Authorization": "Bearer demo-secret-token"}
    )

    assert response.status_code == 200
    assert response.json()["username"] == "alice"


def test_user_endpoint_requires_authentication():
    response = client.get("/users/1")

    assert response.status_code == 401


def test_bob_can_access_own_profile():
    response = client.get(
        "/users/2",
        headers={"Authorization": "Bearer bob-demo-token"}
    )

    assert response.status_code == 200
    assert response.json()["username"] == "bob"


def test_bob_cannot_access_alice_profile():
    response = client.get(
        "/users/1",
        headers={"Authorization": "Bearer bob-demo-token"}
    )

    assert response.status_code == 403

