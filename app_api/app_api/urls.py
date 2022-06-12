
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('auth/', include('accounts.urls')),
    path('car_info/', include('car_info.urls')),
    path('service_type/', include('service_type.urls')),
    path('service_request/',include('service_request.urls')),
]
