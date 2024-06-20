from django.urls import path
from .views import login_view, signup_view, transaction_view, custom_error_handler

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('transaction/', transaction_view, name='transaction'),
]

# Custom error handler (Optional)
handler500 = custom_error_handler
