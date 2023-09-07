from django.db import models
# Create your models here.


class MeterReading(models.Model):
    date = models.DateField()
    current_reading = models.DecimalField(max_digits=6,decimal_places=6)

    def __str__(self):
        return self.date