
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

secret_file_path=os.path.join(os.path.join(BASE_DIR, 'secret'),'secret.sec')

with open(secret_file_path) as f:
    SECRET_KEY = f.read().strip()

DEBUG = False

ALLOWED_HOSTS = ['khafonline.com','www.khafonline.com']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


TIME_ZONE = 'Asia/Tehran'

SITE_URL='/'
ADMIN_URL=SITE_URL+'admin/'
STATIC_URL = '/static/'
STATIC_ROOT = '/home/khafonli/public_html/instamarket/static'
MEDIA_URL =  '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
STATICFILES_DIRS=['/home/khafonli/instamarket/static']