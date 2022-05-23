# from multiprocessing.reduction import AbstractReducer
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_trmanager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_mechanic = models.BooleanField(default=False)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

class CustomAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class TAmanager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fullname = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=15)

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