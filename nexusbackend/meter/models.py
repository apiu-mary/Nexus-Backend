from django.db import models

# Create your models here.
class Meter (models.Model):
    meter_serial_number = models.CharField(max_length=50)
    current_reading = models.PositiveIntegerField()
    status =  models.CharField(max_length=32)
    
def __str__(self):
    return self.reading





