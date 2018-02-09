from __future__ import absolute_import, unicode_literals
from .env import set_env

from .base import *

DEBUG = False

set_env()

try:
    from .local import *
except ImportError:
    pass
