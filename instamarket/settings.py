
from pathlib import Path
import os
import sys

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


ON_MAGGIE=False
ON_HEROKU=False
ON_SERVER=True





if '--no-color' in sys.argv:
    ON_MAGGIE=True  
    ON_HEROKU=False
    ON_SERVER=False
    from . import local_settings

elif ON_SERVER:
    ON_SERVER=True
    ON_MAGGIE=False  
    ON_HEROKU=False
    from . import server_settings
    
elif ON_HEROKU:
    ON_MAGGIE=False  
    ON_SERVER=False
    ON_HEROKU=True
    from . import heroku_settings
    import django_heroku



# Application definition

INSTALLED_APPS = [
    'manager',
    'django_cleanup',
    'rest_framework',
    'dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if ON_HEROKU: 
    MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware'
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

ROOT_URLCONF = 'instamarket.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'instamarket.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'



USE_I18N = True

USE_L10N = True

USE_TZ = True






if ON_HEROKU:
    ADMIN_URL=heroku_settings.ADMIN_URL
    ALLOWED_HOSTS = heroku_settings.ALLOWED_HOSTS
    COMING_SOON=heroku_settings.COMING_SOON
    DATABASES=heroku_settings.DATABASES
    DOWNLOAD_ROOT=heroku_settings.DOWNLOAD_ROOT
    DEBUG = heroku_settings.DEBUG
    MEDIA_ROOT = heroku_settings.MEDIA_ROOT
    MEDIA_URL = heroku_settings.MEDIA_URL
    MYSQL=heroku_settings.MYSQL
    PUSHER_IS_ENABLE=heroku_settings.PUSHER_IS_ENABLE
    REMOTE_MEDIA=heroku_settings.REMOTE_MEDIA
    SECRET_KEY = heroku_settings.SECRET_KEY
    SITE_URL=heroku_settings.SITE_URL
    STATIC_ROOT = heroku_settings.STATIC_ROOT
    STATICFILES_DIRS=heroku_settings.STATICFILES_DIRS
    STATIC_URL = heroku_settings.STATIC_URL
    TIME_ZONE = heroku_settings.TIME_ZONE
    django_heroku.settings(locals())
    

elif ON_SERVER:
    ADMIN_URL=server_settings.ADMIN_URL
    ALLOWED_HOSTS = server_settings.ALLOWED_HOSTS
    COMING_SOON=server_settings.COMING_SOON
    DATABASES=server_settings.DATABASES
    DEBUG = server_settings.DEBUG
    DOWNLOAD_ROOT=server_settings.DOWNLOAD_ROOT
    MEDIA_ROOT = server_settings.MEDIA_ROOT
    MEDIA_URL = server_settings.MEDIA_URL
    MYSQL=server_settings.MYSQL
    PUSHER_IS_ENABLE=server_settings.PUSHER_IS_ENABLE
    REMOTE_MEDIA=server_settings.REMOTE_MEDIA
    SECRET_KEY = server_settings.SECRET_KEY
    SITE_URL=server_settings.SITE_URL
    STATIC_ROOT = server_settings.STATIC_ROOT
    STATIC_URL = server_settings.STATIC_URL
    STATICFILES_DIRS=server_settings.STATICFILES_DIRS
    TIME_ZONE = server_settings.TIME_ZONE



elif ON_MAGGIE:    
    ADMIN_URL=local_settings.ADMIN_URL    
    ALLOWED_HOSTS = local_settings.ALLOWED_HOSTS
    COMING_SOON=local_settings.COMING_SOON
    DATABASES=local_settings.DATABASES
    DEBUG = local_settings.DEBUG
    DOWNLOAD_ROOT=local_settings.DOWNLOAD_ROOT
    MEDIA_ROOT = local_settings.MEDIA_ROOT
    MEDIA_URL = local_settings.MEDIA_URL
    MYSQL=local_settings.MYSQL
    PUSHER_IS_ENABLE=local_settings.PUSHER_IS_ENABLE
    REMOTE_MEDIA=local_settings.REMOTE_MEDIA
    SECRET_KEY = local_settings.SECRET_KEY
    SITE_URL=local_settings.SITE_URL
    STATIC_ROOT = local_settings.STATIC_ROOT
    STATIC_URL = local_settings.STATIC_URL
    STATICFILES_DIRS=local_settings.STATICFILES_DIRS
    TIME_ZONE = local_settings.TIME_ZONE









