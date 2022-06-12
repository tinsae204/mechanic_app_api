from rest_framework import serializers
from .models import ServiceRequest
from django.contrib.postgres.fields import ArrayField


class ServiceRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model= ServiceRequest
        fields= '__all__'

    service_type = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    char_info = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    location = serializers.CharField(required=True)
