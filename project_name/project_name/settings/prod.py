from .base import *

ENV = 'prod'

# debug
DEBUG = False
TEMPLATE_DEBUG = DEBUG


# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_name }}_prod',
        'USER': 'dbuser',
        'PASSWORD': 'dbpass', 
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Base url
BASE_URL = 'http://{{ project_name }}.com'

# Facebook App specific settings
FB_APP_ID = 'fbappid'
FB_APP_SECRET = 'fbappsecret'

# AWS S3
AWS_ACCESS_KEY_ID = "awskeyid"
AWS_SECRET_ACCESS_KEY = "awskey"
AWS_STORAGE_BUCKET_NAME = "awss3bucket"
AWS_STORAGE_BUCKET_PREFIX = ""

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Email settings
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'emailhost'
EMAIL_HOST_USER = 'emailuser'
EMAIL_HOST_PASSWORD = 'emailpass'

DEFAULT_FROM_EMAIL = 'user@{{ project_name }}.com'
