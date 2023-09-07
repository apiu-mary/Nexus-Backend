from django.db import models
# Create your models here.

class UnitSharing(models.Model):
    shared_units = models.DecimalField(max_digits=4,decimal_places=2)
    created_at = models.DateField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return str(self.shared_units)
