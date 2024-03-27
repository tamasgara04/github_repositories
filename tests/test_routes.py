import pytest
from ..app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_popular_repositories(client):
    response = client.get('/repositories/popular')
    assert response.status_code == 200
