from flask.ext.security import Security, SQLAlchemyUserDatastore
from . import app
from . models.users import db, User, Role


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
