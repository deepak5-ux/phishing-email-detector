from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.main import app


client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict():
    response = client.post(
        "/predict",
        headers={"Authorization": "Bearer your-secret-token"},
        json={"text": "Free money now!!!"}
    )
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_invalid_token():
    response = client.post("/predict", headers={"Authorization": "Bearer wrong-token"}, json={"text": "Click here!"})
    assert response.status_code == 401

def test_empty_input():
    response = client.post("/predict", headers={"Authorization": "Bearer your-secret-token"}, json={"text": ""})
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_missing_field():
    response = client.post("/predict", headers={"Authorization": "Bearer your-secret-token"}, json={})
    assert response.status_code == 422  # Unprocessable Entity

