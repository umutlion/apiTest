from Mysite.settings.base import *

# base.py settings here

try:
    from Mysite.settings.local_settings import *
except:
    pass
