from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', ''),

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

DEBUG = True

INTERNAL_IPS = ['127.0.0.1']    

MIDDLEWARE +=(
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
