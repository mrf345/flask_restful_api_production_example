import os
# from flask_migrate import upgrade as db_upgrade

from . import db, migrate
from .defaults import add_default_roles, add_default_tokens
# from ..constants import MIGRATION_FOLDER


def setup_database(app):
    db.init_app(app)
    migrate.init_app(app)

    with app.app_context():
        db.create_all()
        add_default_roles()
        add_default_tokens()

        if not os.getenv('TESTING'):
            pass
            # FIXME: Migrating on the go with RDS, is a bad idea!
            # Turn into a separate task to be lunched prior to deployment
            # db_upgrade(directory=MIGRATION_FOLDER)
