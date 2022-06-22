from django.urls import path
from .views import getRequest, getRequests, createRequest, updateRequest, discardRequest, show_location, count_customer, count_mechanic
from .views import count_requests, successful_requests

urlpatterns = [
    path('', getRequests),
    path('<str:pk>/', getRequest),
    path('api/add/', createRequest),
    path('api/<str:pk>/update', updateRequest),
    path('api/<str:pk>/delete', discardRequest),
    path('api/showloc/', show_location),
    path('api/count_mechanic/', count_mechanic),
    path('api/count_customer/', count_customer),
    path('api/count_requests/', count_requests),
    path('api/count_succ_request/', successful_requests),
]

