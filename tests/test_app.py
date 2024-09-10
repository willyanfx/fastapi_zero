from http import HTTPStatus


def test_root_returns_200_and_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'mari',
            'email': 'mari@example.com',
            'password': 'veryscret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'mari',
        'email': 'mari@example.com',
    }
