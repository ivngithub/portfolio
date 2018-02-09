import os
from configparser import ConfigParser


# instantiate
config = ConfigParser()

# parse existing file
config.read('config.ini')


def set_env():
    try:
        # [DB]
        os.environ.setdefault('DB_HOST', config.get('DB', 'DB_HOST'))
        os.environ.setdefault('DB_PORT', config.get('DB', 'DB_PORT'))
        os.environ.setdefault('DB_NAME', config.get('DB', 'DB_NAME'))
        os.environ.setdefault('DB_USER', config.get('DB', 'DB_USER'))
        os.environ.setdefault('DB_PASS', config.get('DB', 'DB_PASS'))

        # [SECRET]
        os.environ.setdefault('SECRET_KEY', config.get('SECRET', 'SECRET_KEY'))
        return False
    except Exception as e:
        return e
