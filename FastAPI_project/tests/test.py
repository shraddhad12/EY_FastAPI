import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app.app)

def test_add_lists():
    response = client.post("/process_addition", json={"batchid": "123", "payload": [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]})
    assert response.status_code == 200
    assert response.json()["response"] == [6,15,24,33]

def test_add_lists_with_empty_lists():
    response = client.post("/process_addition", json={"batchid": "123", "payload": [[]]})
    assert response.status_code == 200
    assert response.json()["response"] == [0]

def test_add_lists_with_invalid_data():
    response = client.post("/process_addition", json={"batchid": "123", "payload": [[1, 2, "three"]]})
    assert response.status_code == 422

def test_add_lists_with_missing_id():
    response = client.post("/process_addition", json={"payload": [[1, 2,]]})
    assert response.status_code == 422