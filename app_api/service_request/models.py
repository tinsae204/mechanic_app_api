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
    location = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    requested_at = models.DateTimeField(auto_now_add=True)

