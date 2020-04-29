import pytest
from faker import Faker
from random import choice

from requester import app
from requester.database import db
from requester.database.models import (User, Feature)
from requester.constants import DEFAULT_ROLES


MODULES = [User, Feature]
RANGE = 10
fakes = Faker()


@pytest.fixture
def c():
    with app.test_client() as test_client:
        with app.app_context():
            db.create_all()
            teardown_modules()
            fill_users()
            fill_features()
            yield test_client


def teardown_modules():
    for module in MODULES:
        for record in module.query:
            db.session.delete(record)

    db.session.commit()


def fill_users():
    for _ in range(0, RANGE):
        db.session.add(User(name=fakes.name(),
                            role=choice(DEFAULT_ROLES),
                            address=fakes.address()))

    db.session.commit()


def fill_features():
    for _ in range(0, RANGE):
        db.session.add(Feature(name=fakes.name(),
                               users=[choice([u.id for u in User.query])],
                               content=fakes.text()))

    db.session.commit()


def get_random_user(client):
    with client.application.app_context():
        return User.get(choice([u.id for u in User.query]))


def get_random_feature(client):
    with client.application.app_context():
        return Feature.get(choice([f.id for f in Feature.query]))
