from os import path


path = '{0}/data.db'.format(path.dirname(__file__))
config = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///{0}'.format(path),
}
