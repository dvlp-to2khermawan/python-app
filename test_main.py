import pytest
from main import app # Assuming your Flask app instance is named 'app' in main.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_ip_endpoint(client):
    response = client.get('/ip')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    
    data = response.get_json()
    assert 'server_ip' in data
    assert 'client_ip' in data
    assert isinstance(data['server_ip'], str)
    assert isinstance(data['client_ip'], str)
