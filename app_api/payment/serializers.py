from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model= Payment
        fields= '__all__'

    payment_number = serializers.IntegerField(required=True)
    amount = serializers.FloatField(required=True)
