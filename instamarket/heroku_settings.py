
from pathlib import Path
import os
import sys
import dj_database_url

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

secret_file_path=os.path.join(os.path.join(BASE_DIR, 'secret'),'secret.sec')

with open(secret_file_path) as f:
    SECRET_KEY = f.read().strip()


ALLOWED_HOSTS=['instamarket-django.herokuapp.com','www.herokuapp.com','dashboard.heroku.com','www.heroku.com','heroku.com']

DATABASES = {

}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

SITE_URL='/'
ADMIN_URL=SITE_URL+'admin/'
COMING_SOON=False
DEBUG = True
DOWNLOAD_ROOT=os.path.join(BASE_DIR,'download')
MEDIA_URL =  SITE_URL+'media/'
MEDIA_ROOT = '/app/media/'
MYSQL=False
PUSHER_IS_ENABLE=False
REMOTE_MEDIA=False
STATICFILES_DIRS=['/app/static/']
STATIC_ROOT = '/app/staticfiles/'
STATIC_URL = SITE_URL+'static/'
TIME_ZONE = 'Asia/Tehran'
