from django.urls import path
from .views import register_user, user_exists

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('user_exists/<str:username>/', user_exists, name='user_exists'),
]
