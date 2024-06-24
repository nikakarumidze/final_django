from django.urls import path
from .views import home, login, signup, transaction, custom_error_handler

urlpatterns = [
    path('', home, name='home'),  # Root path for the app
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('transaction', transaction, name='transaction'),
]

# Custom error handler (Optional)
handler500 = custom_error_handler
