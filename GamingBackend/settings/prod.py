import os
from .common import *
import dj_database_url

DATABASES['default'] = dj_database_url.parse(os.environ['DATABASE_URL'])

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']

CORS_ALLOWED_ORIGINS = os.environ['CORS_ALLOWED_ORIGINS']

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS']
