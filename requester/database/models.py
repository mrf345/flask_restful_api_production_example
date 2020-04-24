from datetime import datetime

from . import db
from .relations import UserFeatures
from .mixins import GenericMixin, NameMixin


class Role(db.Model, GenericMixin, NameMixin):
    '''User roles table'''
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __init__(self, name):
        ''' Add a new role.

        Parameters
        ----------
        name : str
            new role's name.
        '''
        self.name = name

        db.session.add(self)


class User(db.Model, GenericMixin, NameMixin):
    '''Users table'''
    __tablename__ = 'users'
    props = ['role']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200), nullable=True)
    created = db.Column(db.DateTime(), default=datetime.utcnow)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    features = db.relationship('Feature',
                               secondary=UserFeatures,
                               lazy='subquery',
                               backref=db.backref('users', lazy=True))

    @property
    def role(self):
        role = Role.get(self.role_id)

        if role:
            return role.name

    def __init__(self, name, role, address=None):
        ''' Add a new user.

        Parameters
        ----------
        name : str
            new user's name.
        role : str
            new user's role.
        address : str
            new user's address.
        '''
        roleRecord = Role.get_by_name(role)

        if not roleRecord:
            raise AttributeError('Users role not found')

        self.name = name
        self.role_id = roleRecord.id
        self.address = address

        db.session.add(self)


class Feature(db.Model, GenericMixin, NameMixin):
    '''Features table'''
    __tablename__ = 'features'
    props = ['users']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    content = db.Column(db.String(3000), nullable=True)
    created = db.Column(db.DateTime(), index=True, default=datetime.utcnow)

    def add_users(self, ids):
        ''' Add users to feature by ids.

        Parameters
        ----------
        ids : list
            list of users ids.
        '''
        users = []

        for uid in ids:
            user = User.get(uid)

            if not user:
                raise AttributeError("Wrong user's id entered.")

            users += [user]
        self.users = users

    def __init__(self, name, users=[], content=None):
        ''' Add a new feature.

        Parameters
        ----------
        name : str
            new feature's name.
        users : list
            new feature's user ids list.
        content : str
            new feature's content.
        '''
        self.name = name
        self.content = content

        self.add_users(users)
        db.session.add(self)


class Token(db.Model, GenericMixin):
    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(200), unique=True)

    def __init__(self, token):
        self.token = token
