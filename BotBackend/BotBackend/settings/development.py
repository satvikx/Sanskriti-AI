from .base import *
import environ

env = environ.Env()
environ.Env.read_env()
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = ['darling-suited-jay.ngrok-free.app', 'localhost','127.0.0.1']
# Disable APPEND_SLASH
# APPEND_SLASH = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Additional development-specific settings
