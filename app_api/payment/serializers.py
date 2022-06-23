from rest_framework import serializers
from .models import Payment, Invoice


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model= Payment
        fields= '__all__'

    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    mechanic = serializers.PrimaryKeyRelatedField(read_only=True)
    service_request = serializers.PrimaryKeyRelatedField(read_only=True)
    scheduled_service_request = serializers.PrimaryKeyRelatedField(read_only=True)
    payment_number = serializers.IntegerField(required=True)
    amount = serializers.FloatField(required=True)


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model= Invoice
        fields= '__all__'

    reference_no = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)
    picture = serializers.FileField(required=True)
