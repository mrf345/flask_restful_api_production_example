from flask_restx import Api


title = 'PRF API'
description = 'Production Ready Flask API'
api = Api(title=title, description=description)
auth_config = {'apiKey': {'type': 'apiKey',
                          'in': 'headers',
                          'name': 'Authorization'}}

api = Api(title=title, description=description, authorizations=auth_config)
