from rest_framework import serializers
from .models import Payment, Invoice


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model= Payment
        fields= '__all__'

    payment_number = serializers.IntegerField(required=True)
    amount = serializers.FloatField(required=True)


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model= Invoice
        fields= '__all__'

    reference_no = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)
    picture = serializers.FileField(required=True)
