from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    location =  models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32)

    def __str__(self):
        return self.first_name