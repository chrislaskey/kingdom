from os import path


basedir = path.abspath(path.dirname(__file__))


# Flask
# See: http://flask.pocoo.org/docs/config/
DEBUG = True
TESTING = False
SECRET_KEY = 'Academicam omnem quaestionem duabus formis a Cicerone esse expositam olim cognitum est'

# Flask-SQLAlchemy
# See: http://pythonhosted.org/Flask-SQLAlchemy/config.html
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, '../app.db')

# Flask-Mail
# See: http://pythonhosted.org/flask-mail/
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_DEBUG = DEBUG
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_DEFAULT_SENDER = None
MAIL_MAX_EMAILS = None
MAIL_SUPPRESS_SEND = TESTING

# Flask-Security
# See: http://pythonhosted.org/Flask-Security/configuration.html
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'SnK2na02nlnmsWsna01nvmac1SNAncKS9acn3m11aZmQEiAk9314jXma'
SECURITY_EMAIL_SENDER = 'no-reply@localhost'
