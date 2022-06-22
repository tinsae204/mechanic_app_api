
from django.contrib import admin
from django.urls import path, include
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter
from .views import notify

router = DefaultRouter()
router.register('devices', FCMDeviceAuthorizedViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('auth/', include('accounts.urls')),
    path('car_info/', include('car_info.urls')),
    path('service_type/', include('service_type.urls')),
    path('service_request/',include('service_request.urls')),
    path('scheduled_service_request/',include('scheduled_service_request.urls')),
    path('payment/',include('payment.urls')),
    path('', include(router.urls)),
    path('rating/', include('ratings.urls')),
    path('notify/', notify)
]
