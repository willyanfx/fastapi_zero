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


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'id': 1, 'username': 'mari', 'email': 'mari@example.com'}]
    }


def test_update_user(client):
    response = client.put(
        'users/1/',
        json={
            'username': 'mari',
            'email': 'mari@example.com',
            'password': 'new_password',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'mari',
        'email': 'mari@example.com',
    }
