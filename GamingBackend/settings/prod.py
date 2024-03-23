import os
from .common import *
import dj_database_url

DATABASES = {}

DATABASES['default'] = dj_database_url.parse(os.environ['DATABASE_URL'])

DEBUG = True

# AWS S3
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = "gamingbackend-bucket"
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = False


STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
}

EMAIL_HOST = 'smtp.ionos.de'
EMAIL_HOST_USER = "gamingbackend@bedynek.org"
EMAIL_HOST_PASSWORD = "DUZ-qcg3mna7npv.ncm"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER