#!/usr/lib/virtualenvs/dominion/bin/python

# Create database
# Load all app.models.* first, hooking them into db. Then call db.create_all().

from app.models import db


db.create_all()
