import pytest
from random import choice
from http import HTTPStatus
from sqlalchemy.sql.expression import func

from . import get_random_feature
from requester.database.models import Feature as FeatureDB, User as UserDB
from requester.constants import LIMIT_PER_PAGE, TOKENS


@pytest.mark.usefixtures('c')
def test_get_feature(c):
    feature = get_random_feature(c)

    response = c.get(f'/features/{feature.id}')
    fetched_feature = response.json

    assert fetched_feature is not None and fetched_feature != {}
    for key, value in fetched_feature.items():
        if key != 'users':
            assert getattr(feature, key, None) == value


@pytest.mark.usefixtures('c')
def test_get_features(c):
    response = c.get('/features/', follow_redirects=True)
    features = response.json

    assert [
        {'id': f.id, 'name': f.name, 'content': f.content}
        for f in FeatureDB.query.limit(LIMIT_PER_PAGE)
    ] == features


@pytest.mark.usefixtures('c')
def test_update_feature_fails_with_wrong_token(c):
    feature = get_random_feature(c)
    new_data = {'id': feature.id, 'name': 'testing', 'content': 'testing', 'users': [1, 2]}
    headers = {'Authorization': f'Schema wrong-token-should-fails'}
    response = c.put(f'/features/{feature.id}',
                     json=new_data,
                     headers=headers,
                     follow_redirects=True)

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json.get('message') == 'Authentication is required'


@pytest.mark.usefixtures('c')
def test_update_feature(c):
    feature = get_random_feature(c)
    new_data = {'id': feature.id, 'name': 'testing', 'content': 'testing', 'users': [1, 2]}
    token = choice(TOKENS)
    headers = {'Authorization': f'Schema {token}'}
    response = c.put(f'/features/{feature.id}',
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


@pytest.mark.usefixtures('c')
def test_list_feature_users(c):
    feature = None

    with c.application.app_context():
        feature = FeatureDB.query.filter(func.length(FeatureDB.users) > 0).first()

    assert feature is not None

    response = c.get(f'/features/{feature.id}/users',
                     json=True,
                     follow_redirects=True)
    users = response.json

    for user in users:
        user_rec = UserDB.get(user.get('id'))

        for key, value in user.items():
            assert getattr(user_rec, key, None) == value
