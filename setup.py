#!/usr/lib/virtualenvs/dominion/bin/python

# Create database
# Load all app.models.* first, hooking them into db. Then call db.create_all().

from datetime import datetime
from app.models import db
from app.models.friends import Friend
from app.models.games import Game, games_users
from app.models.users import User
from app.security import user_datastore
from sys import argv


try:
    command = argv[1]
except IndexError:
    command = None


db.create_all()


if command == 'test':

    # password: player-one
    user_datastore.create_user(email='player-one@chrislaskey.com',
        password='$2a$12$96vs6hmhJzBgi1fw4b6vIu87VuzMP2lFIcoIxTJ1U6h9m.AjuNDdO')

    # password: player-two
    user_datastore.create_user(email='player-two@chrislaskey.com',
        password='$2a$12$obgmmSNEhciOEbg.Ob1tAuFyopqA4/JsTt/V3OoD.QGkckp0Qc0FW')

    # password: player-three
    user_datastore.create_user(email='player-three@chrislaskey.com',
        password='$2a$12$bSeMt/jhBiltPTxHHPzcHO/q.vaeN57l25RyFp4eDnow9jegOfEo6')

    db.session.commit()

    db.session.add_all([
        Friend(user_id=1, friend_id=2),
        Friend(user_id=2, friend_id=1),
        Friend(user_id=1, friend_id=3)
    ])

    db.session.add_all([
        Game(
            name = 'Game 1',
            type = 'classic',
            description = 'First description',
            date_created = datetime.utcnow(),
            players = db.session.query(User).filter(User.id.in_([1,2])).all()
        ),
        Game(
            name = 'Game 2',
            type = 'classic',
            description = 'Second description',
            date_created = datetime.utcnow(),
            players = db.session.query(User).filter(User.id.in_([2,3])).all()
        ),
        Game(
            name = 'Game 3',
            type = 'classic',
            description = 'Third description',
            date_created = datetime.utcnow(),
            players = db.session.query(User).filter(User.id.in_([1,2,3])).all()
        )
    ])

    db.session.commit()
