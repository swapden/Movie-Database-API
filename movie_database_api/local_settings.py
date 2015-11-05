from settings import BASE_DIR, PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
