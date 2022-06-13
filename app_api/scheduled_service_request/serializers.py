from rest_framework import serializers
from .models import ScheduledServiceRequest


class ScheduledServiceRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model= ScheduledServiceRequest
        fields= '__all__'

    service_type = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    char_info = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    location = serializers.CharField(required=True)
    scheduled_date = serializers.DateTimeField(required=True)
