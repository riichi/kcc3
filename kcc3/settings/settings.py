from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY', '3on#7^-^=nxx0_npqt3r_gr6c#5))vdt!v5n876_vv78em9b!v')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', default=0))

ALLOWED_HOSTS = os.environ.get(
    'DJANGO_ALLOWED_HOSTS',
    'fanpai.localhost,yakuman.localhost,localhost'
).split(',')
PARENT_HOST = os.environ.get('DJANGO_PARENT_HOST', 'localhost:8000')


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('SQL_USER', None),
        'PASSWORD': os.environ.get('SQL_PASSWORD', None),
        'HOST': os.environ.get('SQL_HOST', None),
        'PORT': os.environ.get('SQL_PORT', None),
    }
}


MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

CELERY_BROKER_URL = os.environ.get(
    'CELERY_BROKER', 'amqp://guest:guest@localhost:5672//')
