from os import path


basedir = path.abspath(path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'app.db')
