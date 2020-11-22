# -*- coding: utf-8 -*-
from settings_base import *

DEBUG = TEMPLATE_DEBUG = True
INSTALLED_APPS += ()
MIDDLEWARE_CLASSES += ()

DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
DATABASES['default']['NAME'] = 'xblog'
DATABASES['default']['USER'] = 'root'
DATABASES['default']['PASSWORD'] = '123456'
DATABASES['default']['HOST'] = '127.0.0.1'
DATABASES['default']['PORT'] = '3306'

