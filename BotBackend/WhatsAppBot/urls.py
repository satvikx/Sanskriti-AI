from django.urls import path
from .views import webhook

urlpatterns = [
    # path('webhook', webhook_get, name='webhook_get'),
    # path('webhook', webhook_post, name='webhook_post'),
    path('', webhook, name='webhook'),
]