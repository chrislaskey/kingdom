from os import path


basedir = path.abspath(path.dirname(__file__))


DEBUG = True
TESTING = False
SECRET_KEY = 'Academicam omnem quaestionem duabus formis a Cicerone esse expositam olim cognitum est'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'app.db')
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
