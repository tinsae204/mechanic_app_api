from django.urls import path
from .views import getPayment, getPayments, makePayment, updatePayment, getInvoice, getInvoices, updateInvoice, makeInvoice

urlpatterns = [
    # payment views
    path('', getPayments),
    path('<str:pk>/', getPayment),
    path('api/add/', makePayment),
    path('api/<str:pk>/update', updatePayment),
    # invoice views
    path('invoice/', getInvoices),
    path('invoice/<str:pk>/', getInvoice),
    path('api/invoice/add/', makeInvoice),
    path('api/invoice/<str:pk>/update', updateInvoice),
]

