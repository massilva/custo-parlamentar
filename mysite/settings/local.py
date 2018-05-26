from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6inbnsa4z7zfl^1e7af1+w4pnri+rufkf!mr7tug)vtyl!oi43'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'deputados.local']

INTERNAL_IPS = ['127.0.0.1','192.168.1.109', '192.168.1.102', '192.168.1.104']


MIDDLEWARE +=(
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    'debug_toolbar',
)

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if os.environ.get('DOCKER'):

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DATABASE_NAME', ''),
            'USER': os.environ.get('DATABASE_USER', ''),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
            'HOST': os.environ.get('DATABASE_HOST', ''),
            'PORT': os.environ.get('DATABASE_PORT', '')
        }
    }

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'assembleia',
            'USER': 'alba',
            'PASSWORD': '123456',
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }
