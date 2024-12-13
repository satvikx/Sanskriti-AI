from functools import wraps
from django.conf import settings
from django.http import JsonResponse
import logging
import hashlib
import hmac

def validate_signature(payload, signature):
    """
    Validate the incoming payload's signature against our expected signature
    """
    # Use the App Secret to hash the payload
    expected_signature = hmac.new(
        bytes(settings.APP_SECRET, "latin-1"),
        msg=payload.encode("utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()

    # Check if the signature matches
    return hmac.compare_digest(expected_signature, signature)

def signature_required(func):
    """
    Decorator to ensure that the incoming requests to our webhook are valid and signed with the correct signature
    """
    # @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        signature = request.headers.get("X-Hub-Signature-256", "")[
            7:
        ]
        if not signature:
            print("Signature missing")
            return JsonResponse({'error': 'Signature missing'}, status=400)
        payload = request.body.decode('utf-8')
        if not validate_signature(payload, signature):
            return JsonResponse({'error': 'Invalid signature'}, status=403)
        return func(request, *args, **kwargs)
    return wrapped_view



# def signature_decorator(func):
#     """
#     Decorator to verify the signature of the incoming request
#     """
#     def wrapper(request, *args, **kwargs):
#         if not verify_signature(request):
#             return HttpResponseForbidden()
#         return func(request, *args, **kwargs)
#     return wrapper