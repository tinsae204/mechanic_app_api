from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from .models import Payment, Invoice
from .serializers import PaymentSerializer, InvoiceSerializer
from .helpers import send_otp_to_phone
from accounts.models import Mechanic, Customer
from service_request.models import ServiceRequest
import jwt
import random


#payment api views
@api_view(['GET'])
def getPayments(request):
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPayment(request, pk):
    payment = Payment.objects.get(id = pk)
    serializer = PaymentSerializer(payment, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def makePayment(request, pk):
    data = request.data
    token = request.headers.get('jwt')
    payload = jwt.decode(jwt=token, key='secret', algorithms=['HS256'])
    customer = Customer.objects.filter(customer_id = payload['id']).first()
    service_request = ServiceRequest.objects.get(id = pk)

    payment = Payment.objects.create(
        customer = customer,
        service_request = service_request,
        payment_number = random.randint(10000, 99999),
        amount = data['amount'],
    )

    serializer = PaymentSerializer(payment, many=False)
    return Response(serializer.data) 

@api_view(['POST'])
def confirmPayment(request, pk):
    data = request.data
    token = request.headers.get('jwt')
    payload = jwt.decode(jwt=token, key='secret', algorithms=['HS256'])
    mechanic = Mechanic.objects.filter(mechanic_id = payload['id']).first()

    payment = Payment.objects.get(id = pk)
    payment.mechanic = mechanic
    payment.completed = True
    payment.save()

    # serializer = PaymentSerializer(payment, data = request.data)
    # if serializer.is_valid():
    #     serializer.save()

    response = Response()

    response.data = {
       "id":payment.id,  
       "amount":payment.amount, 
       "completed":payment.completed, 
    }

    return response

@api_view(['PUT'])
def updatePayment(request, pk):
    data = request.data
    payment = Payment.objects.get(id = pk)
    serializer = Payment(payment, data = request.data)
    # if serializer.is_valid():
    #     serializer.save()
    return Response(serializer.data)


#Invoice api views
@api_view(['GET'])
def getInvoices(request):
    invoices = Invoice.objects.all()
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getInvoice(request, pk):
    invoice = Invoice.objects.get(id = pk)
    serializer = InvoiceSerializer(invoice, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def makeInvoice(request):
    data = request.data
    invoice = Invoice.objects.create(
        reference_no = data['reference_no'],
        amount = data['amount'],
        picture = data['picture'],
    )
    serializer = InvoiceSerializer(invoice, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateInvoice(request, pk):
    data = request.data
    invoice = Invoice.objects.get(id = pk)

    serializer = Invoice(invoice, data = request.data)
    # if serializer.is_valid():
    #     serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def confirm_invoice(request, pk):
    invoice = Invoice.objects.get(id = pk)
    invoice.status = True
    serializer = InvoiceSerializer(invoice, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def confirmed_invoices(request):
    invoices = Invoice.objects.filter(status = True)
    return Response(invoices)

@api_view(['GET'])
def send_otp(request):
    data = request.data
    otp = send_otp_to_phone(data.get('phoneno1'), data.get('phoneno2'))
    return Response({
        "OTP sent": otp
    })



