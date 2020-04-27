from random import choice
from http import HTTPStatus

from . import client, get_random_user, get_random_feature
from requester.database.models import Feature, User
from requester.constants import LIMIT_PER_PAGE, TOKENS


def test_get_feature(client):
    feature = get_random_feature(client)

    response = client.get(f'/features/{feature.id}')
    fetched_feature = response.json

    assert fetched_feature is not None and fetched_feature != {}
    for key, value in fetched_feature.items():
        if key != 'users':
            assert getattr(feature, key, None) == value


def test_get_features(client):
    response = client.get('/features/', follow_redirects=True)
    features = response.json

    assert [
        {'id': f.id, 'name': f.name, 'content': f.content, 'users': [u.id for u in f.users]}
        for f in Feature.query.limit(LIMIT_PER_PAGE)
    ] == features


def test_update_feature_fails_with_wrong_token(client):
    feature = get_random_feature(client)
    new_data = {'id': feature.id, 'name': 'testing', 'content': 'testing', 'users': [1, 2]}
    headers = {'Authorization': f'Schema wrong-token-should-fails'}
    response = client.put(f'/features/{feature.id}',
                          json=new_data,
                          headers=headers,
                          follow_redirects=True)

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json.get('message') == 'Authentication is required'


def test_update_feature(client):
    feature = get_random_feature(client)
    new_data = {'id': feature.id, 'name': 'testing', 'content': 'testing', 'users': [1, 2]}
    token = choice(TOKENS)
    headers = {'Authorization': f'Schema {token}'}
    response = client.put(f'/features/{feature.id}',
                          json=new_data,
                          headers=headers,
                          follow_redirects=True)
    fetched_feature = response.json

    assert fetched_feature is not None and fetched_feature != {}
    for key, value in fetched_feature.items():
        if key == 'users':
            assert sorted(new_data.get(key)) == sorted(value)
        else:
            assert new_data.get(key) == value
