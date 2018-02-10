from __future__ import absolute_import, unicode_literals
import os
from .base import *

DEBUG = False


PUBLIC_HOST = os.environ.get('PUBLIC_HOST')
PRIVATE_HOST = os.environ.get('PRIVATE_HOST')
ALLOWED_HOSTS = [PUBLIC_HOST, PRIVATE_HOST]

SECRET_KEY = os.environ.get('SECRET_KEY', 'asdko_UYIUnm_1231_ADSd=-8!sss'),

try:
    from .local import *
except ImportError:
    pass
