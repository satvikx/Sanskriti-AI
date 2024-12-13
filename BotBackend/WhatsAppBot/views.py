import logging
import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from django.views.decorators.http import require_http_methods
from .decorators.security import signature_required
from .utils.whatsapp_utils import (
    process_whatsapp_message,
    is_valid_whatsapp_message,
)

@signature_required
def handle_message(request):
    """
    Handle incoming webhook events from the WhatsApp API.

    This function processes incoming WhatsApp messages and other events,
    such as delivery statuses. If the event is a valid message, it gets
    processed. If the incoming payload is not a recognized WhatsApp event,
    an error is returned.

    Every message send will trigger 4 HTTP requests to your webhook: message, sent, delivered, read.
    """
    payload = json.loads(request.body)
    if (
        payload.get("entry", [{}])[0]
        .get("changes", [{}])[0]
        .get("value", {})
        .get("statuses")
    ):
        logging.info("Received a WhatsApp status update.")
        return JsonResponse({"status": "success"}, status=200)
    
    try:
        if is_valid_whatsapp_message(payload):
            process_whatsapp_message(payload)
            logging.info("WhatsApp Message Processed.")
            return JsonResponse({"status": "success"}, status=200)
        else:
            print("Invalid message, not WhatsApp API")
            return JsonResponse({"error": "Invalid message, not WhatsApp API"}, status=400)
    except json.JSONDecodeError:
        logging.error("Failed to decode JSON")
        print("Invalid JSON")
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        logging.error(f"Error processing message: {e}", exc_info=True)
        return JsonResponse({"error": "Internal server error"}, status=500)


# Required webhook verifictaion for WhatsApp
def verify(request):
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    # Check if a token and mode were sent
    if mode and token:
        # Check the mode and token sent are correct
        if mode == "subscribe" and token == settings.VERIFY_TOKEN:
            # Respond with 200 OK and challenge token from the request
            logging.info("WEBHOOK_VERIFIED")
            return HttpResponse(challenge, status=200)
        else:
            # Responds with '403 Forbidden' if verify tokens do not match
            logging.info("VERIFICATION_FAILED")
            return JsonResponse({"status": "error", "message": "Verification failed"}, status=403)
    else:
        # Responds with '400 Bad Request' if verify tokens do not match
        logging.info("MISSING_PARAMETER")
        print("Missing parameters")
        return JsonResponse({"status": "error", "message": "Missing parameters"}, status=400)



# @csrf_exempt
# @require_http_methods(["GET"])
# def webhook_get(request):
#     return verify(request)

# @csrf_exempt
# @signature_required
# @require_http_methods(["POST"])
# def webhook_post(request):
#     return handle_message(request)

@require_http_methods(["GET", "POST"])
@csrf_exempt
def webhook(request):
    if request.method == "GET":
        return verify(request)

    elif request.method == "POST":
        return handle_message(request)