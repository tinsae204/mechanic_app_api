from django.db import models
from accounts.models import Mechanic
from accounts.models import Customer

class Rating(models.Model):
    mechanic = models.ForeignKey(Mechanic, null=True, on_delete=models.SET_NULL)
    rating = models.IntegerField()
    is_submitted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
