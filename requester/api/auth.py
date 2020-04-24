from functools import wraps
from http import HTTPStatus
from flask import request
from flask_restx import abort

from ..database.models import Token


def token_required(function):
    @wraps(function)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')

        if token not in [t.token for t in Token.query]:
            return abort(code=HTTPStatus.UNAUTHORIZED,
                         message='Authentication is required')

        return function(*args, **kwargs)

    return decorator
