from django.urls import path
from .views import AddMechanicView, AddTRManagerView, CustomerSignupView, CustomerLoginView, AdminLoginView, MechanicLoginView
from .views import AdminView, MechanicView, CustomerView, LogoutView

urlpatterns = [
    path('customer_signup/', CustomerSignupView.as_view(), name='signup-customer'),
    path('add_mechanic/', AddMechanicView.as_view(), name='add-mechanic'),
    path('add_trmanager/', AddTRManagerView.as_view(), name="add-trmanager"),
    path('customer_login/', CustomerLoginView.as_view(), name="customer-login"),
    path('mechanic_login/', MechanicLoginView.as_view(), name="mechanic-login"),
    path('admin_login/', AdminLoginView.as_view(), name="admin-login"),
    path('admin_home/', AdminView.as_view(), name="admin-home"),
    path('mechanic_home/', MechanicView.as_view(), name="mechanic-home"),
    path('customer_home/', CustomerView.as_view(), name="customer-home"),
    path('logout/', LogoutView.as_view(), name="logout"),


]