from django.db import models

class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    min_price = models.FloatField()
    max_price = models.FloatField()

