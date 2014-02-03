from os import path


basedir = path.abspath(path.dirname(__file__))


SECRET_KEY = 'Academicam omnem quaestionem duabus formis a Cicerone esse expositam olim cognitum est'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'app.db')
