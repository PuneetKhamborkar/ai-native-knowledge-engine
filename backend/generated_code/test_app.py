from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_create_task():
    response = client.post("/tasks", json={
        "title": "Test Task",
        "description": "Test Desc"
    })

    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == "Test Task"


def test_get_task():
    create = client.post("/tasks", json={
        "title": "Get Task",
        "description": "Desc"
    })

    task_id = create.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_update_task():
    create = client.post("/tasks", json={
        "title": "Old",
        "description": "Old Desc"
    })

    task_id = create.json()["id"]

    response = client.put(f"/tasks/{task_id}", json={
        "title": "New",
        "description": "New Desc"
    })

    assert response.status_code == 200
    assert response.json()["title"] == "New"


def test_delete_task():
    create = client.post("/tasks", json={
        "title": "Delete Me",
        "description": "Desc"
    })

    task_id = create.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404