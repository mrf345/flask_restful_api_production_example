from . import db
from .models import Role, Token
from ..constants import DEFAULT_ROLES, TOKENS


def add_default_roles():
    for def_role_name in DEFAULT_ROLES:
        role = Role.get_by_name(def_role_name)

        if not role:
            db.session.add(Role(def_role_name))

    db.session.commit()


def add_default_tokens():
    for value in TOKENS:
        token = Token.query.filter_by(token=value).first()

        if not token:
            db.session.add(Token(value))

    db.session.commit()
