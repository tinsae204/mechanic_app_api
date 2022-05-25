from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_trmanager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_mechanic = models.BooleanField(default=False)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class CustomAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.username

class TAmanager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fullname = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=15)

    def __str__(self):
        return self.fullname

class Mechanic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    docs = models.FileField(upload_to='uploads', blank=True)
    is_online = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created: 
        Token.objects.create(user=instance)