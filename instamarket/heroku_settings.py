
from pathlib import Path
import os
import dj_database_url
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

secret_file_path=os.path.join(os.path.join(BASE_DIR, 'secret'),'secret.sec')

with open(secret_file_path) as f:
    SECRET_KEY = f.read().strip()

    
DEBUG = True

ALLOWED_HOSTS = ['khafonline.com','www.khafonline.com','instamarket-django.herokuapp.com','www.herokuapp.com','dashboard.heroku.com','www.heroku.com','heroku.com']

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

SITE_URL='/'

ADMIN_URL=SITE_URL+'admin/'
STATIC_URL = SITE_URL+'static/'

STATIC_ROOT = '/app/staticfiles/'

MEDIA_URL =  SITE_URL+'media/'
MEDIA_ROOT = '/app/media/'
STATICFILES_DIRS=['/app/static/']