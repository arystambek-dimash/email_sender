from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_send_email():
    response = client.post("/send_email",
                           json={"to": "test@example.com", "subject": "Test Subject", "body": "Test Body"})
    assert response.status_code == 200
    assert response.json() == {"message": "Message sent successfully"}
