from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.modelfields import  PhoneNumberField


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    company_name = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=64, default=None)
    phone = PhoneNumberField(null=False, blank=False, unique=True)


    def __str__(self):
        return self.company_name
    