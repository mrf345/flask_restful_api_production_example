from http import HTTPStatus
from flask import request
from flask_restx import Resource, abort

from .. import api
from . import UserSerializer, FeatureSerializer
from ..auth import token_required
from ...database import db
from ...database.models import Feature as FeatureDB
from ...constants import LIMIT_PER_PAGE
from ...utils import convert_safely


def setup_features_endpoint():
    description = 'Endpoint to handle features CRUD'
    endpoint = api.namespace('features', description=description)

    @endpoint.route('/')
    class ListFeatures(Resource):
        ''' List and Add features. '''

        @endpoint.marshal_list_with(FeatureSerializer)
        @endpoint.param('page', 'page number to retrieve features for')
        def get(self):
            '''List of paginated features'''
            page = convert_safely(int, request.args.get('page'), 1)
            features = FeatureDB.query.paginate(page, per_page=LIMIT_PER_PAGE, error_out=False).items

            return features, HTTPStatus.OK

        @endpoint.expect(FeatureSerializer)
        @endpoint.marshal_with(FeatureSerializer)
        def post(self):
            ''' Add new feature, update it with users if name is identical'''
            feature = FeatureDB.get_by_name(api.payload.get('name'))

            try:
                if feature:
                    feature.add_users(api.payload.get('users', []))
                else:
                    feature = FeatureDB(**api.payload)

                db.session.commit()
            except Exception as exc:
                return abort(message=exc)

            return feature, HTTPStatus.CREATED

    @endpoint.route('/<int:id>')
    @endpoint.param('id', description='The feature identifier')
    class Feature(Resource):
        ''' Get, Update and Delete feature. '''

        @endpoint.marshal_with(FeatureSerializer)
        def get(self, id):
            ''' Get feature '''
            feature = FeatureDB.get(id)

            if not feature:
                return abort(message='Feature not found', code=HTTPStatus.NOT_FOUND)

            return feature, HTTPStatus.OK

        @endpoint.expect(FeatureSerializer)
        @endpoint.marshal_with(FeatureSerializer)
        @endpoint.doc(security='apiKey')
        @token_required
        def put(self, id):
            ''' Update feature '''
            feature = FeatureDB.get(id)

            if not feature:
                return abort(message='Feature not found', code=HTTPStatus.NOT_FOUND)

            feature.update(api.payload)
            feature.add_users(api.payload.get('users'))
            db.session.commit()

            return feature, HTTPStatus.OK

        @endpoint.marshal_with(FeatureSerializer)
        @endpoint.doc(security='apiKey')
        @token_required
        def delete(self, id):
            ''' Delete feature '''
            feature = FeatureDB.get(id)

            if not feature:
                return abort(message='Feature not found', code=HTTPStatus.NOT_FOUND)

            db.session.delete(feature)
            db.session.commit()
            return '', HTTPStatus.NO_CONTENT

    @endpoint.route('/<int:id>/users')
    @endpoint.param('id', description='The feature identifier')
    class UserFeatures(Resource):
        ''' List feature's users '''

        @endpoint.marshal_list_with(UserSerializer)
        @endpoint.param('page', 'page number to retrieve users for')
        def get(self, id):
            ''' List feature's users '''
            page = convert_safely(int, request.args.get('page'), 1)
            feature = FeatureDB.get(id)

            if not feature:
                return abort(message='Feature not found', code=HTTPStatus.NOT_FOUND)

            return feature.users\
                          .paginate(page, per_page=LIMIT_PER_PAGE, error_out=False)\
                          .items
