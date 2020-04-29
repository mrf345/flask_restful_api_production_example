import pytest
from random import choice
from http import HTTPStatus

from . import get_random_user
from requester.database.models import User
from requester.constants import LIMIT_PER_PAGE, TOKENS


@pytest.mark.usefixtures('c')
def test_get_user(c):
    user = get_random_user(c)

    response = c.get(f'/users/{user.id}')
    fetched_user = response.json

    assert fetched_user is not None and fetched_user != {}
    for key, value in fetched_user.items():
        assert getattr(user, key, None) == value


@pytest.mark.usefixtures('c')
def test_get_users(c):
    response = c.get('/users/', follow_redirects=True)
    users = response.json

    assert [
        {'id': u.id, 'name': u.name, 'address': u.address, 'role': u.role}
        for u in User.query.limit(LIMIT_PER_PAGE)
    ] == users


@pytest.mark.usefixtures('c')
def test_update_user_fail_with_wrong_token(c):
    user = get_random_user(c)
    new_data = {'id': user.id, 'name': 'testing', 'address': 'testing', 'role': 'Admin'}
    headers = {'Authorization': f'Schema wrong-token-should-fails'}
    response = c.put(f'/users/{user.id}',
                     json=new_data,
                     headers=headers,
                     follow_redirects=True)

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json.get('message') == 'Authentication is required'


@pytest.mark.usefixtures('c')
def test_update_user(c):
    user = get_random_user(c)
    new_data = {'id': user.id, 'name': 'testing', 'address': 'testing', 'role': 'Admin'}
    token = choice(TOKENS)
    headers = {'Authorization': f'Schema {token}'}
    response = c.put(f'/users/{user.id}',
                     json=new_data,
                     headers=headers,
                     follow_redirects=True)
    fetched_user = response.json

    assert fetched_user is not None and fetched_user != {}
    for key, value in fetched_user.items():
        assert new_data.get(key) == value
