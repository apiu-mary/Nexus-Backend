
import uuid
from django.db import models

class Meter(models.Model):
    meter_serial_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    current_reading = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  
    status = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.meter_serial_number} A"

   
   



