from django.contrib import admin
from .models import  MeterReading
# Register your models here.

class MeterReadingAdmin(admin.ModelAdmin):
    list_display = ('date','current_reading')
admin.site.register(MeterReading,MeterReadingAdmin)
