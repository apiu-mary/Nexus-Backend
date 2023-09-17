import uuid
from django.db import models

class Meter(models.Model):
    meter_serial_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    current_reading = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.current_reading} A"

class MeterReading(models.Model):
    current_reading = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null=True)
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, related_name='readings',null=True)
    


    def __str__(self):
        return f"Meter Reading - Date: {self.date}, Current Reading: {self.current_reading}"
