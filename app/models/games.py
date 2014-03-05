from . import db


class Game(db.Model):
    '''
    status - text field
        game status, values created|declined|started|withdrew|ended
    '''
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Text())
    name = db.Column(db.Text())
    type = db.Column(db.Text())
    description = db.Column(db.Text())
    date_created = db.Column(db.DateTime())
