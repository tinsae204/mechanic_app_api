from rest_framework import serializers
from .models import ServiceType

class ServiceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model= ServiceType
        fields= '__all__'

    name = serializers.CharField(required=True)
    min_price = serializers.FloatField(required=True)
    max_price = serializers.FloatField(required=True)

    # def get_cleaned_data(self):
    #     data = super(ServiceTypeSerializer, self).get_cleaned_data()
    #     return data

    # def save(self, request):
    #     service_type = super(ServiceTypeSerializer, self).save(request)
    #     service_type.save()
    #     return service_type
