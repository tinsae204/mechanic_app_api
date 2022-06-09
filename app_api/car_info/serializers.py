from rest_framework import serializers
from .models import CarInfo

class CarInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model: CarInfo
        fields=['maker','model','year']

    maker = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    year = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(CarInfoSerializer, self).get_cleaned_data()
        return data

    def save(self, request):
        car_info = super(CarInfoSerializer, self).save(request)
        car_info.save()
        return car_info
