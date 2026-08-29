from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_get_activities_returns_data():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]


def test_signup_adds_participant():
    response = client.post("/activities/Chess Club/signup?email=newstudent@mergington.edu")
    assert response.status_code == 200
    data = response.json()
    assert "newstudent@mergington.edu" in data["message"]

    activity = client.get("/activities").json()["Chess Club"]
    assert "newstudent@mergington.edu" in activity["participants"]
