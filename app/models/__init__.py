from flask.ext.sqlalchemy import SQLAlchemy
from .. import app


app.config.from_object('app.config')


db = SQLAlchemy(app)
