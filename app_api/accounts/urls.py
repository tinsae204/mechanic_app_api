from django.urls import path
from .views import AddMechanicView, AddTRManagerView, CustomerSignupView, CustomerLoginView, AdminLoginView, MechanicLoginView

urlpatterns = [
    path('customer_signup/', CustomerSignupView.as_view(), name='signup-customer'),
    path('add_mechanic/', AddMechanicView.as_view(), name='add-mechanic'),
    path('add_trmanager/', AddTRManagerView.as_view(), name="add-trmanager"),
    path('customer_login/', CustomerLoginView.as_view(), name="customer-login"),
    path('mechanic_login/', MechanicLoginView.as_view(), name="mechanic-login"),
    path('admin_login/', AdminLoginView.as_view(), name="admin-login"),
]