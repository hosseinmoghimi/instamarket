from pathlib import Path
import os
import dj_database_url
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


DEBUG = True

ALLOWED_HOSTS = ['192.168.100.198']

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': os.path.join(os.path.join(BASE_DIR, 'instamarket'),'secret_my_sql_local.cnf'),

            },
        }
    }


# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


MYSQL=True



TIME_ZONE = 'Asia/Tehran'

SITE_URL='/'
ADMIN_URL=SITE_URL+'admin/'
STATIC_URL = SITE_URL+'static/'
STATIC_ROOT = 'c:\\users\\hossein\\repo\\instamarket\\staticfiles\\'
MEDIA_URL =  SITE_URL+'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
STATICFILES_DIRS=['c:\\users\\hossein\\repo\\instamarket\\static\\']
PUSHER_IS_ENABLE=False
REMOTE_MEDIA=False
COMING_SOON=False
DOWNLOAD_ROOT=os.path.join(BASE_DIR,'download')