
import uuid
from django.db import models

class Meter(models.Model):
    meter_serial_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    current_reading = models.PositiveIntegerField()
    status = models.CharField(max_length=32)
    
    def __str__(self):
        return self.current_reading





