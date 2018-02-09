import subprocess
from configparser import ConfigParser


# instantiate
config = ConfigParser()

# parse existing file
config.read('config.ini')


def set_env():
    try:
        # [DB]
        subprocess.call(["export {}={}".format('DB_HOST', config.get('DB', 'DB_HOST'))])
        subprocess.call(["export {}={}".format('DB_PORT', config.get('DB', 'DB_PORT'))])
        subprocess.call(["export {}={}".format('DB_NAME', config.get('DB', 'DB_NAME'))])
        subprocess.call(["export {}={}".format('DB_USER', config.get('DB', 'DB_USER'))])
        subprocess.call(["export {}={}".format('DB_PASS', config.get('DB', 'DB_PASS'))])

        # [SECRET]
        subprocess.call(["export {}={}".format('SECRET_KEY', config.get('SECRET', 'SECRET_KEY'))])

        return False
    except Exception as e:
        return e
