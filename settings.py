import os
import django
import logging.config


# Django settings for GiraffeGraftersMap project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# Base paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

# Import the logging configuration from file
logging.config.fileConfig(os.path.join(SITE_ROOT, 'logging.fileconfig'))

# Predefined domain
MY_SITE_DOMAIN = 'ec2-50-16-132-231.compute-1.amazonaws.com'

# Static file hosting paths
STATIC_URL = 'http://rebounds-dev.s3-website-us-east-1.amazonaws.com/guerillagrafters/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin_media/media/"

# Database (uncomment for staging)
DATABASE_ENGINE = 'django.contrib.gis.db.backends.postgis'
DATABASE_NAME = 'guerillagrafters'
DATABASE_USER = 'guerillagrafters'
DATABASE_HOST = 'localhost'
DATABASE_PASSWORD = '5IQZe7WEix'
DATABASE_PORT = '5432'

# temporary local development options (comment for staging)
# DATABASE_ENGINE = 'django.contrib.gis.db.backends.postgis'
# DATABASE_NAME = 'ggdb'
# DATABASE_USER = 'postgres'
# GEOS_LIBRARY_PATH='/usr/local/lib/libgeos_c.dylib'
# GDAL_LIBRARY_PATH='/usr/local/lib/libgdal.dylib'
# STATIC_ROOT = ''

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6f@dyoq0&1ehftrrhl2p%vi!d)t@l3rp9yiso7u8m6g3(z1dqt'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	os.path.join(os.path.dirname(__file__), 'templates'),
)

ROOT_URLCONF = 'urls'

STATICFILES_FINDERS = ("django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder")

# Django Compressor
COMPRESS_ROOT = os.path.join(os.path.dirname(__file__), 'public')
COMPRESS_ENABLED = True
COMPRESS_URL = "/public/"
COMPRESS_PARSER = "compressor.parser.BeautifulSoupParser"

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
	'django.contrib.gis',
	'sanfran',
    'compressor',
	# Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

