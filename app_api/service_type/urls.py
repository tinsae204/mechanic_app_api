from django.urls import path
from .views import getServices, getService, addService, updateService, deleteService

urlpatterns = [
    path('', getServices),
    path('<str:pk>/', getService),
    path('api/add/', addService),
    path('api/<str:pk>/update', updateService),
    path('api/<str:pk>/delete', deleteService)

]
