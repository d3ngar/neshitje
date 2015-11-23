"""
Django settings for neshitje project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from nonrepofiles.secrets import Secrets
#Basedir
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = Secrets.secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # installed apps
    #'crispy_forms',
    #'bootstrap3',
    ## does tweak forms and stuff dynamically in Django
    'widget_tweaks',
    ## Resizing of images uses that
    'sorl.thumbnail',
    ## Search on the site with Whoosh and Haystack
    'whoosh',
    'haystack',
    #Modified Pre-order Tree Traversal
    'mptt',
    # written apps
    'main_app',
    'user_track',
    'search',
    'order',
    'listing',
    'user_details',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

     # Now we add here our custom middleware
     'user_track.middleware.track.UserSessionTracking',
)

ROOT_URLCONF = 'neshitje.urls'

WSGI_APPLICATION = 'neshitje.wsgi.application'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'neshitje',
        'USER': Secrets.database_user,
        'PASSWORD': Secrets.database_pass
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Setting up all sorts of email things:
# For email
if not DEBUG:
    EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
    EMAIL_HOST = Secrets.email_host
    EMAIL_PORT = 465
    EMAIL_USERNAME = Secrets.email_username
    EMAIL_PASSWORD = Secrets.email_password


## For debugging, but you will also need to run python -m smtpd -n -c DebuggingServer localhost:1025
if DEBUG:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = 'testing@example.com'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = '/home/dengar/Documents/development/neshitje/neshitje/media/uploads/'
#MEDIA_URL = ''

# recaptcha
RECAPTCHA_PUBLIC_KEY = Secrets.captcha_site_key
RECAPTCHA_PRIVATE_KEY = Secrets.captcha_secret_key

# close sessions at browser exit
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# settings for Whoosh
WHOOSH_INDEX = os.path.join(BASE_DIR, 'whoosh/')
# settings for Haystack
HAYSTACK_CONNECTIONS = {
    'default' : {
        'ENGINE' : 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH' : WHOOSH_INDEX,
    },
}
