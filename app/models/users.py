from flask.ext.security import UserMixin
from . import db
from . games import games_users
from . roles import roles_users


class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    friend_id = db.Column(db.Integer(), db.ForeignKey('user.id'),
        primary_key=True)
    friend = db.relationship('User', foreign_keys='Friend.friend_id')
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'),
        primary_key=True)
    user = db.relationship('User', foreign_keys='Friend.user_id')
    request_status = db.Boolean()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(255))
    current_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary = roles_users,
        backref = db.backref('users', lazy = 'dynamic'))
    games = db.relationship('Game', secondary = games_users,
        backref = db.backref('users', lazy = 'dynamic'))
    friends = db.relationship('Friend', backref='Friend.friend_id',
        primaryjoin='User.id==Friend.user_id', lazy='joined')
