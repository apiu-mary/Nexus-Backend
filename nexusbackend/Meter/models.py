from django.db import models

# Create your models here.
class Meter(models.Model):
    meter_serial_number = models.IntegerField()
    current_reading = models.DecimalField(max_digits=6,decimal_places=6)
    status =  models.CharField(max_length=32)
def __str__(self):
    return self.status





