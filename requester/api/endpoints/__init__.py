from flask_restx import fields

from .. import api
from ...constants import DEFAULT_ROLES


UserSerializer = api.model('User', {
    'id': fields.Integer(required=False, description='user identification number'),
    'name': fields.String(required=True, description='user full name', max_length=100, min_length=3),
    'role': fields.String(required=True, description='user role name', enum=DEFAULT_ROLES),
    'address': fields.String(required=False, description='user full address', max_length=200)})

FeatureSerializer = api.model('Feature', {
    'id': fields.Integer(required=False, description='feature identifier'),
    'name': fields.String(required=True, description='feature full name'),
    'content': fields.String(required=False, description='feature content details')})
