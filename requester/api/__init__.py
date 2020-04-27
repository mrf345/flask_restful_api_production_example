from flask_restx import Api

from ..constants import AUTH_HEADER_KEY


title = 'PRF API'
description = 'Production Ready Flask API'
api = Api(title=title, description=description)
auth_config = {'apiKey': {'type': 'apiKey',
                          'in': 'headers',
                          'name': AUTH_HEADER_KEY}}

api = Api(title=title,
          description=description,
          authorizations=auth_config,
          validate=True)
