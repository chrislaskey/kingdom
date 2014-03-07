from . import db


games_users = db.Table(
    'games_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('game_id', db.Integer(), db.ForeignKey('game.id'))
)


class Game(db.Model):
    '''
    status - text field
        game status, values created|declined|started|withdrew|ended
    '''
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(255))
    name = db.Column(db.Text())
    type = db.Column(db.String(255))
    description = db.Column(db.Text())
    date_created = db.Column(db.DateTime())
    players = db.relationship('User', secondary = games_users,
        backref = db.backref('game', lazy = 'dynamic'))
