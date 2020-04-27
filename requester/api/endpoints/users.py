from http import HTTPStatus
from flask import request
from flask_restx import Resource, fields, abort

from .. import api
from ..auth import token_required
from ...database import db
from ...database.models import User as UserDB, Role as RoleDB
from ...constants import LIMIT_PER_PAGE, DEFAULT_ROLES
from ...utils import convert_safely


def setup_users_endpoint():
    endpoint = api.namespace(name='users', description='Endpoint to handle users CRUD')
    model = api.model('User', {'id': fields.Integer(required=False, description='user identification number'),
                               'name': fields.String(required=True, description='user full name', max_length=100, min_length=3),
                               'role': fields.String(required=True, description='user role name', enum=DEFAULT_ROLES),
                               'address': fields.String(required=False, description='user full address', max_length=200)})

    @endpoint.route('/')
    class ListUsers(Resource):
        ''' List and Add users. '''

        @endpoint.marshal_list_with(model)
        @endpoint.param('page', description='page number to retrieve users for')
        def get(self):
            ''' List of paginated users'''
            page = convert_safely(int, request.args.get('page'), 1)
            pagination = UserDB.query.paginate(page, per_page=LIMIT_PER_PAGE, error_out=False)

            return pagination.items, HTTPStatus.OK

        @endpoint.expect(model)
        @endpoint.marshal_with(model)
        def post(self):
            ''' Add new user '''
            try:
                user = UserDB(**api.payload)
                db.session.commit()
            except Exception as exc:
                return abort(message=exc)

            return user, HTTPStatus.CREATED

    @endpoint.route('/<int:id>')
    @endpoint.param('id', 'The user identifier')
    class User(Resource):
        ''' Get, Update and Delete users. '''

        @endpoint.marshal_with(model)
        def get(self, id):
            ''' Get user '''
            user = UserDB.get(id)

            if not user:
                abort(message='User not found', code=HTTPStatus.NOT_FOUND)

            return user, HTTPStatus.OK

        @endpoint.expect(model)
        @endpoint.marshal_with(model)
        @endpoint.doc(security='apiKey')
        @token_required
        def put(self, id):
            ''' Update user '''
            user = UserDB.get(id)
            role = RoleDB.get_by_name(api.payload and api.payload.get('role'))

            if not user:
                abort(message='User not found', code=HTTPStatus.NOT_FOUND)

            if not role:
                abort(message='Role name is wrong', code=HTTPStatus.NOT_FOUND)

            user.update(api.payload)
            user.role_id = role.id
            db.session.commit()
            return user, HTTPStatus.OK

        @endpoint.marshal_with(model)
        @endpoint.doc(security='apiKey')
        @token_required
        def delete(self, id):
            ''' Delete user '''
            user = UserDB.get(id)

            if not user:
                abort(message='User not found', code=HTTPStatus.NOT_FOUND)

            db.session.delete(user)
            db.session.commit()
            return '', HTTPStatus.NO_CONTENT
