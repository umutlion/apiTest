from Mysite.settings import *
from .production import *

try:
    from .local import *
except:
    pass
