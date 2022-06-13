from django.urls import path
from .views import getRequest, getRequests, createRequest, updateRequest, discardRequest

urlpatterns = [
    path('', getRequests),
    path('<str:pk>/', getRequest),
    path('api/add/', createRequest),
    path('api/<str:pk>/update', updateRequest),
    path('api/<str:pk>/delete', discardRequest),
]

