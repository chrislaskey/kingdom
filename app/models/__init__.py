from flask.ext.sqlalchemy import SQLAlchemy
from .. import app
from .. database import config


app.config.update(config)
db = SQLAlchemy(app)
