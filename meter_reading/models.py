from django.db import models
from meter.models import Meter

class MeterReading(models.Model):
    # meter = models.ForeignKey(Meter, on_delete=models.CASCADE, related_name='readings', null=True)
    current_reading = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null=True)
    
    def __str__(self):
        return f"Meter Reading - Date: {self.date}, Current Reading: {self.current_reading}"
