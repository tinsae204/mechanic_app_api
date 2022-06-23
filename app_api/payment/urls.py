from django.urls import path
from .views import getPayment, getPayments, makePayment, updatePayment, getInvoice, getInvoices, updateInvoice, makeInvoice, send_otp
from .views import confirm_invoice, confirmed_invoices, confirmPayment

urlpatterns = [
    # payment views
    path('', getPayments),
    path('<str:pk>/', getPayment),
    path('api/<str:pk>/add/', makePayment),
    path('api/<str:pk>/confirm/', confirmPayment),
    path('api/<str:pk>/update/', updatePayment),
    path('api/send_otp/', send_otp),
    # invoice views
    path('invoice/', getInvoices),
    path('invoice/<str:pk>/', getInvoice),
    path('api/invoice/add/', makeInvoice),
    path('api/invoice/<str:pk>/update/', updateInvoice),
    path('api/invoice/<str:pk>/confirm/', confirm_invoice),
    path('api/invoice/confirmed/', confirmed_invoices),
]

