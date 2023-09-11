from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    # meter = models.OneToOneField(Meter, on_delete=models.CASCADE)  
    # units = models.ForeignKey(Units, on_delete=models.CASCADE)  
    # meter_reading = models.OneToOneField(MeterReading, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=64, default=None)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.company_name
