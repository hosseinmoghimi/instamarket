
from pathlib import Path
import os
import sys
import dj_database_url

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


DEBUG = True

DATABASES = {

}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

MYSQL=False


TIME_ZONE = 'Asia/Tehran'

SITE_URL='/'

ADMIN_URL=SITE_URL+'admin/'
STATIC_URL = SITE_URL+'static/'

STATIC_ROOT = '/app/staticfiles/'

MEDIA_URL =  SITE_URL+'media/'
MEDIA_ROOT = '/app/media/'
STATICFILES_DIRS=['/app/static/']
PUSHER_IS_ENABLE=False
REMOTE_MEDIA=False
COMING_SOON=False
DOWNLOAD_ROOT=os.path.join(BASE_DIR,'download')
