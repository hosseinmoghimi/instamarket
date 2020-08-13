
from pathlib import Path
import os
import dj_database_url
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

secret_file_path=os.path.join(os.path.join(BASE_DIR, 'secret'),'secret.sec')

SECRET_KEY = "5a@8$h^m0-jtc+w7%xnd7q8r2pct8v77+p^+jt-%&-x8&iw92r"

DEBUG = True

ALLOWED_HOSTS = ['khafonline.com','www.khafonline.com']

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

MYSQL=False


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


TIME_ZONE = 'Asia/Tehran'

SITE_URL='/instamarket/'
SITE_URL='/'

ADMIN_URL=SITE_URL+'admin/'
STATIC_URL = SITE_URL+'static/'

STATIC_ROOT = '/home/khafonli/public_html/instamarket/static/'
STATIC_ROOT = '/app/static/'

MEDIA_URL =  SITE_URL+'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
STATICFILES_DIRS=['/home/khafonli/instamarket/static']
STATICFILES_DIRS=['/app/static']