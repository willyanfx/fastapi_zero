from http import HTTPStatus

from fastapi.testclient import TestClient

from app import app


def test_root_returns_200_and_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}
