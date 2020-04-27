from . import api
from .endpoints.features import setup_features_endpoint
from .endpoints.users import setup_users_endpoint
from .limiter import requests_limiter


def setup_api(app):
    api.init_app(app)
    setup_features_endpoint()
    setup_users_endpoint()
    app.before_request(requests_limiter)
