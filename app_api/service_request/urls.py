from django.urls import path
from .views import getRequest, getRequests, createRequest, updateRequest, discardRequest, show_location, count_customer, count_mechanic
from .views import count_requests, successful_requests, un_successful_requests, pending_requests, accept_request, cost_estimation

urlpatterns = [
    path('', getRequests),
    path('<str:pk>/', getRequest),
    path('api/add/', createRequest),
    path('api/estimate/', cost_estimation),
    path('api/<str:pk>/accept/', accept_request),
    path('api/<str:pk>/update', updateRequest),
    path('api/<str:pk>/delete', discardRequest),
    path('api/showloc/', show_location),
    path('api/count_mechanic/', count_mechanic),
    path('api/count_customer/', count_customer),
    path('api/count_requests/', count_requests),
    path('api/count_succ_request/', successful_requests),
    path('api/count_un_succ_request/', un_successful_requests),
    path('api/count_pending_request/', pending_requests),

]

