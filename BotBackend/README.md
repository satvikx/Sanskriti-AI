# Sanskriti AI WhatsApp Chatbot

## Setup the Django Project

1. **Install Django**:
    ```bash
    pip install django
    ```

2. **Create a new Django project**:
    ```bash
    django-admin startproject BotBackend
    cd BotBackend
    ```

3. **Create a new Django app**:
    ```bash
    python manage.py startapp chatbot
    ```

4. **Add the app to your project settings**:
    ```python
    # BotBackend/settings.py
    INSTALLED_APPS = [
        ...
        'chatbot',
    ]
    ```

## Setup the Webhook using ngrok

1. **Download and install ngrok**:
    - Visit [ngrok](https://ngrok.com/download) and download the appropriate version for your OS.
    - Unzip the downloaded file and place it in a directory of your choice.

2. **Expose your local server to the internet**:
    ```bash
    ./ngrok http 8000
    ```

3. **Copy the forwarding URL provided by ngrok** (e.g., `http://<ngrok-id>.ngrok.io`).

4. **Set up the webhook in your Django app**:
    - Create a view to handle the webhook:
        ```python
        # chatbot/views.py
        from django.http import HttpResponse
        from django.views.decorators.csrf import csrf_exempt

        @csrf_exempt
        def webhook(request):
            if request.method == 'POST':
                # Handle the webhook payload here
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=405)
        ```

    - Add the URL pattern for the webhook:
        ```python
        # chatbot/urls.py
        from django.urls import path
        from .views import webhook

        urlpatterns = [
            path('webhook/', webhook, name='webhook'),
        ]
        ```

    - Include the app URLs in the project:
        ```python
        # BotBackend/urls.py
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('webhook/', include('WhatsAppBot.urls')),
        ]
        ```

5. **Update your webhook URL in the WhatsApp API settings** with the ngrok forwarding URL followed by `/chatbot/webhook/` (e.g., `http://<ngrok-id>.ngrok.io/chatbot/webhook/`).

That's it! Our Django project is set up, and the webhook is exposed using ngrok.