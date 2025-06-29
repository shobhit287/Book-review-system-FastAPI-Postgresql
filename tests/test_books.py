from fastapi.testclient import TestClient
from app.app_factory import initialize_app  

from app.map_modules import URL_PREFIX
client = TestClient(initialize_app())

def test_create_book():
    payload = {
        "title": "Test Book",
        "author": "John Doe",
        "description": "A mysterious adventure unfolds."
    }
    response = client.post(f"{URL_PREFIX}/books/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["author"] == payload["author"]
    assert data["description"] == payload["description"]
    assert "createdAt" in data
    assert "updatedAt" in data

def test_get_all_books():
    response = client.get(f"{URL_PREFIX}/books/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for book in data:
        assert "id" in book
        assert "title" in book
        assert "author" in book
        assert "description" in book
        assert "createdAt" in book
        assert "updatedAt" in book
