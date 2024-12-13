"""
ASGI config for BotBackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

environment = os.getenv('DJANGO_ENV') or 'production'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'BotBackend.settings.{environment}')

application = get_asgi_application()
