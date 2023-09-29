from django.db import models

from meter_reading.models import MeterReading
# Create your models here.

class UnitSharing(models.Model):
    shared_units = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Shared Units: {self.shared_units}, Created At: {self.created_at}, Updated At: {self.updated_at}"
