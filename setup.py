#!/usr/lib/virtualenvs/dominion/bin/python

from app.models import db
from app.models import user
db.create_all()
