from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_send_email():
    test_data = {
        "to": "test@example.com",
        "subject": "Test Subject",
        "message": "Test Message"
    }
    response = client.post("/send_email", json=test_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Message sent successfully!"}


def test_incorrect_data():
    test_data = {
        "to": "test@example.com",
        "message": "Test Message"
    }
    response = client.post("/send_email", json=test_data)
    assert response.status_code == 422
