from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        # Or your PostgreSQL host IP
        'HOST': 'postgres',
        'PORT': '5432',       # Default PostgreSQL port
    }
}

DEBUG = True
