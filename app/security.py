from flask.ext.security import Security, SQLAlchemyUserDatastore
from . import app
from . models.roles import db, Role
from . models.users import User


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
