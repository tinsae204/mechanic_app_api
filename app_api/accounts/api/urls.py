from django.urls import path

from .views import CustomerSignUpView

urlpatterns = [
    path('customer_signup/', CustomerSignUpView.as_view())
]
