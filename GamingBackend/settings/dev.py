from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECRET_KEY = 'django-insecure-a&to=#q3j65vij+56$uvqi_-0jfj@t95ch57!a=k7)^qo0x%dj'

DEBUG = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "gamingbackend.onrender.com",
    "https://gaming-frontend-one.vercel.app",
]

ALLOWED_HOSTS = [
    "gamingbackend.onrender.com",
    "127.0.0.1",
    "localhost",
]
