from . import api
from .endpoints.features import setup_features_endpoint
from .endpoints.users import setup_users_endpoint


def setup_api(app):
    api.init_app(app)
    setup_features_endpoint()
    setup_users_endpoint()
