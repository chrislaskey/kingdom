from flask.ext.security import Security, SQLAlchemyUserDatastore
from . import app
from . models.security import db, User, Role


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
