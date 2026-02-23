from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_echo():
    response = client.get("/echo?message=hello")
    assert response.status_code == 200
    assert response.json() == {"message": "hello"}

def test_echo_different_message():
    response = client.get("/echo?message=world")
    assert response.status_code == 200
    assert response.json() == {"message": "world"}

def test_echo_missing_parameter():
    response = client.get("/echo")
    assert response.status_code == 422 # Unprocessable Entity
