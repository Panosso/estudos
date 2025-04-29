from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_weather_endpoint():
    response = client.get("/weather?city=Sao Paulo")
    assert response.status_code == 200
    assert "message" in response.json()