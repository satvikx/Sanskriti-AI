from .base import *

DEBUG = False

ALLOWED_HOSTS = ['your-production-domain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prod_db_name',
        'USER': 'prod_db_user',
        'PASSWORD': 'prod_db_password',
        'HOST': 'prod_db_host',
        'PORT': 'prod_db_port',
    }
}

# Additional production-specific settings

# Static files and media settings
STATIC_ROOT = BASE_DIR / 'static/'
MEDIA_ROOT = BASE_DIR / 'media/'
