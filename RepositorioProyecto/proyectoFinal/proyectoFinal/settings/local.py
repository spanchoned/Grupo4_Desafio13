from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#ESTA ES LA CONFIGURACION PARA BD SQLITE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
# 'default': {
# 'ENGINE': 'django.db.backends.mysql',
# 'NAME': 'proyecto2023',
# 'USER': 'root',
# 'PASSWORD': 'root',
# 'HOST': 'localhost',
# 'PORT': '3308',
# }
# }