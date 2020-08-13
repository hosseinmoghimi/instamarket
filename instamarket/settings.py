
from pathlib import Path
import os
import sys
from . import server_settings
from . import local_settings

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent



ON_SERVER=True
if '--no-color' in sys.argv:
    ON_SERVER=False

if ON_SERVER:
    SECRET_KEY = server_settings.SECRET_KEY
    DEBUG = server_settings.DEBUG
    ALLOWED_HOSTS = server_settings.ALLOWED_HOSTS
    TIME_ZONE = server_settings.TIME_ZONE
    STATIC_URL = server_settings.STATIC_URL
    STATIC_ROOT = server_settings.STATIC_ROOT
    MEDIA_URL = server_settings.MEDIA_URL
    MEDIA_ROOT = server_settings.MEDIA_ROOT
    SITE_URL=server_settings.SITE_URL
    ADMIN_URL=server_settings.ADMIN_URL
    STATICFILES_DIRS=server_settings.STATICFILES_DIRS

if not ON_SERVER:    
    SECRET_KEY = local_settings.SECRET_KEY
    DEBUG = local_settings.DEBUG
    ALLOWED_HOSTS = local_settings.ALLOWED_HOSTS
    TIME_ZONE = local_settings.TIME_ZONE
    STATIC_URL = local_settings.STATIC_URL
    STATIC_ROOT = local_settings.STATIC_ROOT
    MEDIA_URL = local_settings.MEDIA_URL
    MEDIA_ROOT = local_settings.MEDIA_ROOT
    SITE_URL=local_settings.SITE_URL
    ADMIN_URL=local_settings.ADMIN_URL    
    STATICFILES_DIRS=local_settings.STATICFILES_DIRS





# Application definition

INSTALLED_APPS = [
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

