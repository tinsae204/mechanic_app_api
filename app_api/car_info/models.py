from django.db import models

class CarInfo(models.Model):
    maker = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
