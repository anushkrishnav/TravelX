import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # its a key used as a signature key used to make sure the content
    # sent isn't intercepted
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    ENV = os.getenv('FLASK_ENV', default='production')
    DEBUG = ENV == 'development'
    SQLALCHEMY_DATABASE_URI = '''postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ.get('DBUSER'),
    dbpass=os.environ.get('DBPASS'),
    dbhost=os.environ.get('DBHOST'),
    dbname=os.environ.get('DBNAME'),
    dbsslmode =os.environ.get('db_ssl')) or''' 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.getenv('SECRET_KEY', default='octocat')
    G_KEY = os.getenv('G_KEY')
    RSECRET_KEY = os.environ.get('RSECRET_KEY')
