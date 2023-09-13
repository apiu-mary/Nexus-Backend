from django.contrib import admin
from.models import UnitSharing
# Register your models here.

class UnitSharingAdmin(admin.ModelAdmin):
    list_display = ('shared_units','created_at','updated_at')
admin.site.register(UnitSharing,UnitSharingAdmin)    
