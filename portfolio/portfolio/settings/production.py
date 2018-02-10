from __future__ import absolute_import, unicode_literals
import os
from .base import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', 'asdko_UYIUnm_1231_ADSd=-8!sss'),

try:
    from .local import *
except ImportError:
    pass
