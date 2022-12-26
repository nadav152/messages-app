from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hw6vd#kkw#@-5qq2@qut!=5cixud-0oj35%(4zoz!_pr(%vbe5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", True)

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('SQL_DATABASE_NAME', 'messages'),
        'USER': os.getenv('SQL_USER', 'postgres'),
        'PASSWORD': os.getenv('SQL_PASSWORD', 'test4Life!'),
        'HOST': os.getenv('SQL_HOST', 'localhost'),
        'PORT': os.getenv('SQL_PORT', '5432'),
    }
}