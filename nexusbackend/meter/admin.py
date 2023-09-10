from django.contrib import admin
from .models import Meter

# Register your models here.

class MeterAdmin(admin.ModelAdmin):
    list_display = ('meter_serial_number','current_reading','status')
admin.site.register(Meter,MeterAdmin)