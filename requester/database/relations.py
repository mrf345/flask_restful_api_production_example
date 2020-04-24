from . import db

UserFeatures = db.Table('user_features',
                        db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
                        db.Column('feature_id', db.Integer, db.ForeignKey('features.id'), primary_key=True))
