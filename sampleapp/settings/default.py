#! /usr/bin/env python2.7
import os, sys

# Django settings for sampleapp project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Absolute paths for where the project and templates are stored.
ABSOLUTE_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
ABSOLUTE_TEMPLATES_PATH = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, 'templates/'))

# add root directory to PYTHONPATH
if not ABSOLUTE_PROJECT_ROOT in sys.path:
    sys.path.insert(0, ABSOLUTE_PROJECT_ROOT)


# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, 'media/'))


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, 'static/'))

# URL that handles the media, static, etc.
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, 'static_extra/')),
)

ADMINS = (
    ('Your Name', 'admin@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'prod_database_name',                      # Or path to database file if using sqlite3.
        'USER': 'prod_user',                      # Not used with sqlite3.
        'PASSWORD': 'prod_p@ssword',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Istanbul'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = '!!! paste your own secret key here !!!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sampleapp.urls'

# Python dotted path to the WSGI application used by Django's runserver.
# disabled - outsite the app
WSGI_APPLICATION = 'wsgihandler.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ABSOLUTE_TEMPLATES_PATH,
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    # required by django-admin-tools
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

# APPS
# django debugging stuff
ADMIN_TOOL_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
)

# django
CORE_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # django admin
    'django.contrib.admin',
    'django.contrib.admindocs',
)

EXTERNAL_APPS = (
    'django_extensions',
    'south',
)

LOCAL_APPS = (
    'sampleapp.home',
)

# the order is important!
INSTALLED_APPS = ADMIN_TOOL_APPS + CORE_APPS + LOCAL_APPS + EXTERNAL_APPS


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
#        New in Django 1.5
#        'require_debug_true': {
#            '()': 'django.utils.log.RequireDebugTrue',
#        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

