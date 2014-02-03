#!/usr/lib/virtualenvs/dominion/bin/python

# Create database
# Load all app.models.* first, hooking them into db. Then call db.create_all().

from app.models import db
from app.models import security
from app.security import user_datastore

db.create_all()
user_datastore.create_user(email='contact@chrislaskey.com', password='test')
db.session.commit()
