from . import db, migrate
from .defaults import add_default_roles, add_default_tokens


def setup_database(app):
    db.init_app(app)
    migrate.init_app(app)

    with app.app_context():
        db.create_all()
        add_default_roles()
        add_default_tokens()
