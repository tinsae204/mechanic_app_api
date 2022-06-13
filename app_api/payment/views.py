from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Payment, Invoice
from .serializers import PaymentSerializer, InvoiceSerializer


# payment api views

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
def makePayment(request):
    data = request.data
    payment = Payment.objects.create(
        payment_number = data['payment_number'],
        amount = data['amount'],
    )

    serializer = PaymentSerializer(payment, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updatePayment(request, pk):
    data = request.data
    payment = Payment.objects.get(id = pk)

    serializer = Payment(payment, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Invoice api views

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
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




