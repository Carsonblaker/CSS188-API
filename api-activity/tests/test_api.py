import pytest
from api_activity.app import create_app


@pytest.fixture
def client():
    with create_app().test_client() as client:
        yield client


def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello World!"}


def test_square(client):
    response = client.get('/square/5')
    assert response.status_code == 200
    assert response.json == {'Shape': 'Square', 'Area': 25}


def test_echo(client):
    response = client.get('/echo?arg1=Hello&arg2=World')
    assert response.status_code == 200
    assert response.json == {'arg1': 'Hello', 'arg2': 'World'}

@pytest.fixture
def client():
    with create_app().test_client() as client:
        yeild client
def test_hellow(client):
    response = client.get('/')
    assert response.status_code == 200

@pytest.ficture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_profile_requires_aiuth(client):
    response = client.get('/profile')
    assert response.status_code == 401

def test_profile_with_valid_auth(client):
    client.put(
        '/register',
        json={'username': 'testuser', 'password': 'testpass123'}
    )

    response = client.get(
        '/profile',
        auth=('testuser', 'testpass123')
    )
    assert response.status_code == 200
    assert "testuser" in response.json["message"]
