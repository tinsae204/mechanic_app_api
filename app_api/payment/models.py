from django.db import models
from accounts.models import Customer, Mechanic
from service_request.models import ServiceRequest
from scheduled_service_request.models import ScheduledServiceRequest

class Payment(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    mechanic = models.ForeignKey(Mechanic, null=True, on_delete=models.SET_NULL)
    service_request = models.ForeignKey(ServiceRequest, null=True, on_delete=models.SET_NULL)
    scheduled_service_request = models.ForeignKey(ScheduledServiceRequest, null=True, on_delete=models.SET_NULL)
    payment_number = models.IntegerField()
    amount = models.FloatField()
    completed = models.BooleanField(default=False)
