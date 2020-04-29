import atexit as at_exit
import sentry_sdk
from os import getenv as get_env, path
from sentry_sdk.integrations.flask import FlaskIntegration

from .constants import TESTING_DB, FALLBACK_DB


PRODUCTION = get_env('PRODUCTION', False)
TESTING = get_env('TESTING', False)
DEVELOPMENT = get_env('DEVELOPMENT', False)
basedir = path.abspath(path.dirname(__file__))
configuration = {'SQLALCHEMY_TRACK_MODIFICATIONS': False,
                 'SECRET_KEY': get_env('SECRET_KEY'),
                 'RESTX_VALIDATE': True}


if PRODUCTION:
    sentry_dsn = get_env('SENTRY_DSN')
    sentry_dsn and sentry_sdk.init(dsn=sentry_dsn,
                                   integrations=[FlaskIntegration()])
    configuration.update({'SQLALCHEMY_DATABASE_URI': get_env('DATABASE_URI'),
                          'DEBUG': False})
elif TESTING:
    configuration.update({'SQLALCHEMY_DATABASE_URI': f'sqlite:///{TESTING_DB}',
                          'TESTING': True})
    at_exit.register(lambda: path.isfile(TESTING_DB) and get_env(TESTING_DB))
elif DEVELOPMENT:
    configuration.update({'SQLALCHEMY_DATABASE_URI': get_env('DATABASE_URI',
                                                             'sqlite:///' + path.join(basedir, FALLBACK_DB))})
