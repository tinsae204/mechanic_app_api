from django.urls import path
from .views import CarInfoViews

urlpatterns = [
    path('', CarInfoViews.as_view())
]
