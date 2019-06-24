# -*- coding: utf-8 -*-
"""
Django settings for my_site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'xiuxd#7kn0t=1srr@^x0q*0rs-689ul5#g5y%p+eh+-1^e861j')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

if os.getenv('DJANGO_ALLOWED_HOSTS', None) is not None:
    for allowed_host in os.getenv('DJANGO_ALLOWED_HOSTS').split(','):
        ALLOWED_HOSTS.append(allowed_host)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'precise_bbcode',
    'my_site',
    'my_resume',
)

MIDDLEWARE = [
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'loaders': (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ),
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'my_site.context_processors.google_analytics',
                'my_site.context_processors.google_analytics_account',
            ]
        }
    }
]


ROOT_URLCONF = 'my_site.urls'

WSGI_APPLICATION = 'my_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : os.environ.get('DJANGO_DB_NAME'),
        'USER' : os.environ.get('DJANGO_DB_USER'),
        'PASSWORD' : os.environ.get('DJANGO_DB_PASS'),
        'HOST' : os.environ.get('DJANGO_DB_HOST'),
        'PORT' : os.environ.get('DJANGO_DB_PORT'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s %(module)s %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'handlers': {
       'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Paramètres de contact
CONTACT_EMAIL = os.environ.get('MY_SITE_EMAIL', 'jean.dupont@domain.net')
CONTACT_PHONE = os.environ.get('MY_SITE_PHONE', '0102030405')
CONTACT_FNAME = os.environ.get('MY_SITE_FNAME', 'Jean')
CONTACT_LNAME = os.environ.get('MY_SITE_LNAME', 'Dupont')
CONTACT_LINKED_IN = os.environ.get('MY_SITE_LINKEDIN', '')

# Paramètres Google Analytics
GOOGLE_ANALYTICS = 'true' == os.environ.get('MY_SITE_GOOGLE_ANALYTICS', 'false')
GOOGLE_ANALYTICS_ACCOUNT = os.environ.get('MY_SITE_GOOGLE_ANALYTICS_ACCOUNT')

try:
    from local_settings import *
except ImportError:
    pass
