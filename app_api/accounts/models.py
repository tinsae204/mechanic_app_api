from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_trmanager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_mechanic = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    date_joined = models.DateField(auto_now_add=True)


class CustomAdmin(models.Model):
    custom_admin = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class TRmanager(models.Model):
    tr_manager = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phoneno = models.CharField(max_length=15, unique=True)


class Mechanic(models.Model):
    mechanic = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phoneno = models.CharField(max_length=15, unique=True)
    specialization = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    docs = models.FileField(upload_to='uploads', blank=True)
    pic = models.FileField(upload_to='uploads', blank=True)
    is_online = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)
