from settings_pro import PRODUCTION_SECRET_FILE
import os.path

if True == os.path.exists(PRODUCTION_SECRET_FILE):
	from settings_pro import *
else:
	from settings_dev import *
	








