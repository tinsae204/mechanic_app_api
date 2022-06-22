from django.db import models
from accounts.models import Customer, Mechanic
from car_info.models import CarInfo
from service_type.models import ServiceType
from django.contrib.postgres.fields import ArrayField

class ServiceRequest(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    mechanic = models.ForeignKey(Mechanic, null=True, on_delete=models.SET_NULL)
    car_info = models.ForeignKey(CarInfo, null=True, on_delete=models.SET_NULL)
    service_type = models.ForeignKey(ServiceType, null=True, on_delete=models.SET_NULL)
    customer_lat = models.IntegerField(default=0)
    customer_lon = models.IntegerField(default=0)
    mechanic_lat = models.IntegerField(default=0)
    mechanic_lon = models.IntegerField(default=0)
    # location = models.CharField(max_length=255)
    is_accepted = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)
    requested_at = models.DateTimeField(auto_now_add=True)

