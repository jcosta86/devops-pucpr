from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"
    assert "id"  in data

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_list_users():
    response = client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_update_user():
    response = client.put("/users/1", json={"name": "Alice Updated", "email": "alice@new.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice Updated"
    assert data["email"] == "alice@new.com"

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"

def test_get_nonexistent_user():
    response = client.get("/users/999")
    assert response.status_code == 404
