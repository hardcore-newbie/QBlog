from xblog.settings_pro import PRODUCTION_SECRET_FILE
import os

if 0 != os.system("which pip"):
	os.system("wget https://bootstrap.pypa.io/ez_setup.py -O- | python")
	os.system("easy_install pip")

if True == os.path.exists(PRODUCTION_SECRET_FILE):
	os.system("pip install -r ./requirements/pro.txt")
else:
	os.system("pip install -r ./requirements/dev.txt")