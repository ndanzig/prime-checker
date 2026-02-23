import pytest
from HelloWorldServer import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200

def test_prime_number(client):
    response = client.post("/", data={"number": "7"})
    assert b"is a prime number" in response.data

def test_not_prime_number(client):
    response = client.post("/", data={"number": "4"})
    assert b"is not a prime number" in response.data

def test_number_one(client):
    response = client.post("/", data={"number": "1"})
    assert b"is not a prime number" in response.data