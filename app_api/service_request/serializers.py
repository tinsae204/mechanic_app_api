from rest_framework import serializers
from .models import ServiceRequest
from django.contrib.postgres.fields import ArrayField


class ServiceRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model= ServiceRequest
        fields= '__all__'

    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    service_type = serializers.PrimaryKeyRelatedField(read_only=True)
    char_info = serializers.PrimaryKeyRelatedField(read_only=True)
    customer_lat= serializers.IntegerField(required=True)
    customer_lon= serializers.IntegerField(required=True)
