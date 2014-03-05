#!/usr/lib/virtualenvs/dominion/bin/python

# Create database
# Load all app.models.* first, hooking them into db. Then call db.create_all().

from app.models import db
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
    db.session.commit()
