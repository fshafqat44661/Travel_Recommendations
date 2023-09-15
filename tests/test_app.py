import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def valid_recommendation_request():
    return {
        "country": "England",
        "season": "summer",
    }

@pytest.fixture
def invalid_recommendation_request():
    return {
        "country": "InvalidCountry",
        "season": "invalid_season",
    }

def test_get_recommendations_valid_request(valid_recommendation_request):
    response = client.post("/recommendations/", json=valid_recommendation_request)
    assert response.status_code == 200
    data = response.json()
    assert "country" in data
    assert "season" in data
    assert "recommendations" in data
    assert isinstance(data["recommendations"], list)

def test_get_recommendations_invalid_request(invalid_recommendation_request):
    response = client.post("/recommendations/", json=invalid_recommendation_request)
    assert response.status_code == 400
    error_data = response.json()
    assert "detail" in error_data

def test_get_recommendations_openai_error():
    # Simulate an OpenAI API error by setting an invalid API key
    app.dependency_overrides[openai.api_key] = "invalid_key"
    response = client.post("/recommendations/", json={"country": "USA", "season": "spring"})
    assert response.status_code == 500
    error_data = response.json()
    assert "detail" in error_data
