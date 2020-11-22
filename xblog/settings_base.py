# -*- coding: utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'abcdefghijklmnopqrstuvwxyz1234567890'

# SECURITY WARNING: don't run with debug turned on in production!
# ---------------------------------------------------------------------
DEBUG = TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition
# ---------------------------------------------------------------------
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',
	'django_markdown',
	'adminfiles',
	'sorl.thumbnail',
	'haystack',
	'apps.blog',
	'apps.personalinfo',
    'django_cleanup',
	'templateaddons',
	#'django.contrib.flatpages',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	#'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.request',
)

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
#MEDIAFILES_DIRS = (os.path.join(BASE_DIR, 'media'), )
ROOT_URLCONF = 'xblog.urls'
WSGI_APPLICATION = 'xblog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# ---------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'admin',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
# ---------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/data/static/'

MEDIA_URL = '/media/' 
MEDIA_ROOT = '/data/media/' 

JQUERY_URL = 'js/jquery.min.js'

MARKDOWN_EXTENSIONS = ['extra', 'codehilite']

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 6
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
