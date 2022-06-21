from django.urls import path, include
from .views import add_mechanic, add_trmanager, customer_login, admin_login, mechanic_login
from .views import get_auth_admin, get_auth_mechanic, get_auth_customer, logout, customer_signup, add_mechanic

urlpatterns = [
    path('customer_signup/', customer_signup),
    path('add_mechanic/', add_mechanic),
    path('add_trmanager/', add_trmanager,),
    path('customer_login/', customer_login),
    path('mechanic_login/', mechanic_login),
    path('admin_login/', admin_login),
    path('admin_home/', get_auth_admin),
    path('mechanic_home/', get_auth_mechanic),
    path('customer_home/', get_auth_customer),
    path('logout/', logout),
]