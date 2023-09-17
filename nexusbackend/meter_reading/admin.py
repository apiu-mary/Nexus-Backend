from django.contrib import admin
from .models import Meter, MeterReading 

@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    list_display = ('meter_serial_number', 'current_reading', 'status')
   

@admin.register(MeterReading)
class MeterReadingAdmin(admin.ModelAdmin):
    list_display = ('date', 'current_reading', 'meter') 
    list_filter = ('date', 'meter') 
    search_fields = ('date', 'meter__meter_serial_number')  

 
