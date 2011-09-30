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

DATABASES = {
  'default': {
     'ENGINE': 'django.contrib.gis.db.backends.postgis',
     'NAME': 'guerrilla_grafters_staging',
     'USER': 'guerrilla_grafters_staging',
     'PASSWORD': 'password',
     'HOST': 'localhost',
     'PORT': '5432',
  }
}

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

STATIC_ROOT = (
  os.path.join(SITE_ROOT, 'public')
)

STATICFILES_FINDERS = ("django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder")

# Django Compressor
COMPRESS_ENABLED = True
COMPRESS_MTIME_DELAY = 3
COMPRESS_ROOT = os.path.join(os.path.dirname(__file__), 'public')
COMPRESS_URL = "/public/"
COMPRESS_PARSER = "compressor.parser.BeautifulSoupParser"
COMPRESS_PRECOMPILERS = (
  ('text/less', os.path.join(SITE_ROOT, 'less/bin/lessc {infile} {outfile}')),
)

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
)

