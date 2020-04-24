import os
import atexit
from flask import Flask

from .api.setup import setup_api
from .database.setup import setup_database


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


def configure_app(app, production=os.getenv('PRODUCTION', False), testing=os.getenv('TESTING', False)):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'development_testing_local_key')

    if production:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
        app.config['DEBUG'] = False
    elif testing:
        db_file_path = os.path.join(basedir, 'testing.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///${db_file_path}'
        app.config['TESTING'] = testing

        atexit.register(lambda: os.remove(db_file_path))
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI',
                                                          'sqlite:///' + os.path.join(basedir, 'database.db'))


configure_app(app)
setup_api(app)
setup_database(app)
