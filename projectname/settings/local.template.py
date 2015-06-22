#! /usr/bin/env python2.7
from default import *

"""
This is the local settings template file. So, do not modify this file.
Instead, make a copy as "local.py" and set the development variables in it.
"""

# local settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = True


DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dev_database_name',
        # The rest is not used with sqlite3:
        'USER': 'dev_user',
        'PASSWORD': 'dev_p@ssword',
        'HOST': 'localhost',
        'PORT': '',
    }
}


if DEBUG:
    # set INTERNAL_IPS to entire local network
    from fnmatch import fnmatch

    class WildcardNetwork(list):
        def __contains__(self, key):
            for address in self:
                if fnmatch(key, address):
                    return True
            return False

    INTERNAL_IPS = WildcardNetwork(['127.0.0.1', '192.168.*.*'])

    # URL that handles the media, static, etc.
    STATIC_URL = '/static/'
    MEDIA_URL = STATIC_URL + 'media/'

    INSTALLED_APPS += (
        # 'debug_toolbar',
    )
