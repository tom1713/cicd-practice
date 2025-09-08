from fastapi.testclient import TestClient
from main import app, VERSION

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello CI/CD"}
    
def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": VERSION}