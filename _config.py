# _config.py


import os


# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'ansibletasker.db'
WTF_CSRF_ENABLED = True
SECRET_KEY = 's3cr3t'
DEBUG = True

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH