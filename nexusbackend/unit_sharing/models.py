from django.db import models
from meter.models import Meter  

class UnitSharing(models.Model):
    sender_meter = models.ForeignKey(
        Meter, related_name='units_sent',
        on_delete=models.CASCADE,null=True
    )
    recipient_meter = models.ForeignKey(
        Meter, related_name='units_received',
        on_delete=models.CASCADE,  null=True
    )
    shared_units = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Shared Units: {self.shared_units}, Created At: {self.created_at}, Updated At: {self.updated_at}"
