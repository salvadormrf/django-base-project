"""Common settings and globals."""

import os
import sys

########## PATH CONFIGURATION
# Absolute filesystem path to this Django project directory.
BASE_DIR = os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

# Add all necessary filesystem paths to our system path so that we can use
# python import statements.
#sys.path.append(SITE_ROOT)
sys.path.append(os.path.join(BASE_DIR, 'libs'))
sys.path.append(os.path.join(BASE_DIR, 'apps'))
########## END PATH CONFIGURATION


# keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'


########## DEBUG CONFIGURATION
# Disable debugging by default.
DEBUG = False
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## ALLOWED DOMAINS
# Allow all by default
ALLOWED_HOSTS = ['*']


########## MANAGER CONFIGURATION
# Admin and managers for this project. 
# These people receive private site alerts.
ADMINS = (
    ('Salvador Faria', 'salvador.mrf@gmail.com'),
)

MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## APP CONFIGURATION
DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'south',
    'widget_tweaks',
    'sorl.thumbnail',
)

LOCAL_APPS = (
    'testapp',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## WEB PROTECTION
X_FRAME_OPTIONS = 'ALLOWALL'
########## END WEB PROTECTION


########## URL CONFIGURATION
ROOT_URLCONF = '{{ project_name }}.urls'


WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


########## GENERAL CONFIGURATION
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# Absolute path to the directory static files should be collected to.
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    
    # other finders
    #'compressor.finders.CompressorFinder',
)
########## END STATIC FILE CONFIGURATION


########## LOGIN CONFIGURATION
LOGIN_REDIRECT_URL = '/admin/'
LOGIN_URL = '/admin/login'
########## END LOGIN CONFIGURATION


########## TEMPLATE CONFIGURATION
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)

# Directories to search when loading templates.
TEMPLATE_DIRS = (
    # Don't forget to use absolute paths, not relative paths.
)
########## END TEMPLATE CONFIGURATION


########## MESSAGES CONFIGURATION
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert',
    messages.ERROR: 'alert-error'
}
########## END MESSAGES CONFIGURATION


########## EMAIL CONFIGURATION
DEFAULT_FROM_EMAIL = 'salvador.mrf@gmail.com'
########## END EMAIL CONFIGURATION

