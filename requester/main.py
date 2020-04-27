import os
import atexit
import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

from .api.setup import setup_api
from .database.setup import setup_database
from .constants import TESTING_DB, FALLBACK_DB

basedir = os.path.abspath(os.path.dirname(__file__))
production = os.getenv('PRODUCTION', False)
testing = os.getenv('TESTING', False)
development = os.getenv('DEVELOPMENT', False)
sentry_dsn = os.getenv('SENTRY_DSN')


if production and sentry_dsn:
    sentry_sdk.init(dsn=sentry_dsn,
                    integrations=[FlaskIntegration()])


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['RESTX_VALIDATE'] = True
app.config['DEBUG'] = True

if production:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['DEBUG'] = False
elif testing:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{TESTING_DB}'
    app.config['TESTING'] = True
    atexit.register(lambda: os.path.isfile(TESTING_DB) and os.remove(TESTING_DB))
elif development:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI',
                                                      'sqlite:///' + os.path.join(basedir, FALLBACK_DB))


setup_api(app)
setup_database(app)
