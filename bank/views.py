from django.urls import path, include
from django.contrib import admin
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .services import UserService
import json

# Initialize UserService
user_service = UserService()


def home(request):
    return JsonResponse({'message': 'Hello Home'}, status=200)


@require_POST
def login(request):
    data = json.loads(request.body)
    result, status_code = user_service.authenticate_user(
        data.get("username"), data.get("password")
    )
    return JsonResponse(result, status=status_code)


@require_POST
def signup(request):
    data = json.loads(request.body)
    result, status_code = user_service.register_user(
        data.get("username"), data.get("password"), data.get("email")
    )
    return JsonResponse(result, status=status_code)


@require_POST
def transaction(request):
    data = json.loads(request.body)
    result, status_code = user_service.add_transaction(
        data.get("sender"),
        data.get("receiver"),
        data.get("amount"),
    )
    return JsonResponse(result, status=status_code)


def custom_error_handler(request, exception=None):
    response = JsonResponse({
        "code": exception.status_code if hasattr(exception, 'status_code') else 500,
        "name": str(exception),
        "description": str(exception),
    })
    response.status_code = exception.status_code if hasattr(
        exception, 'status_code') else 500
    return response
