import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = 'random_string_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'zaman.bd')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


