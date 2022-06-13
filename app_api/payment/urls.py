from django.urls import path
from .views import getPayment, getPayments, makePayment, updatePayment

urlpatterns = [
    path('', getPayments),
    path('<str:pk>/', getPayment),
    path('api/add/', makePayment),
    path('api/<str:pk>/update', updatePayment),
]

