from flask.ext.sqlalchemy import SQLAlchemy
from .. import app


db = SQLAlchemy(app)
