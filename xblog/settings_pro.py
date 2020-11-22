# -*- coding: utf-8 -*-
from settings_base import *
import json

PRODUCTION_SECRET_FILE = '/data/production_secret.json'

DEBUG = TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

if True == os.path.exists(PRODUCTION_SECRET_FILE):
	with open(PRODUCTION_SECRET_FILE) as json_file:
		data = json.load(json_file)
		SECRET_KEY = data['SECRET_KEY']
		DATABASES['default']['USER'] = data['DB']['USER']
		DATABASES['default']['PASSWORD'] = data['DB']['PASSWORD']

DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
DATABASES['default']['NAME'] = 'xblog'
DATABASES['default']['HOST'] = '127.0.0.1'
DATABASES['default']['PORT'] = '3306'

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

INSTALLED_APPS += ()
MIDDLEWARE_CLASSES += ()

STATIC_ROOT = '/data/static/'
MEDIA_ROOT = '/data/media/' 

