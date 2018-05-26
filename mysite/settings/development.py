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

DEBUG = False

#INTERNAL_IPS = ['127.0.0.1']
if DEBUG == True:
    MIDDLEWARE +=(
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

MIDDLEWARE +=(
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

ALLOWED_HOSTS = [os.environ.get('PRIMARY_HOST', '')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)
