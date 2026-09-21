from fastapi.testclient import TestClient
from main import app

def test_hello_world():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_health_check():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

if __name__ == "__main__":
    test_hello_world()
    test_health_check()
    print("My Test: PASSED")