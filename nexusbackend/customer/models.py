from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    company_name = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=64, default=None)

    def __str__(self):
        return self.company_name