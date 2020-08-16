
from pathlib import Path
import os
import dj_database_url
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

secret_file_path=os.path.join(os.path.join(BASE_DIR, 'secret'),'secret.sec')

secret_file_path=os.path.join(os.path.join(BASE_DIR, 'secret'),'secret.sec')

with open(secret_file_path) as f:
    SECRET_KEY = f.read().strip()
DEBUG = True

ALLOWED_HOSTS = ['khafonline.com','www.khafonline.com']
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': os.path.join(os.path.join(BASE_DIR, 'secret'),'server.cnf'),

            },
        }
    }
MYSQL=True


DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': os.path.join(os.path.join(BASE_DIR, 'secret'),'server.cnf'),

            },
        }
    }


TIME_ZONE = 'Asia/Tehran'

SITE_URL='/instamarket/'


ADMIN_URL=SITE_URL+'admin/'
STATIC_URL = SITE_URL+'static/'

STATIC_ROOT = '/home/khafonli/public_html/instamarket/staticfiles/'

MEDIA_URL =  SITE_URL+'media/'
MEDIA_ROOT = '/home/khafonli/public_html/instamarket/media/'
STATICFILES_DIRS=['/home/khafonli/instamarket/static/']
PUSHER_IS_ENABLE=False
REMOTE_MEDIA=False
COMING_SOON=False
DOWNLOAD_ROOT=os.path.join(BASE_DIR,'download')