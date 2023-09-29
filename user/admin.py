from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'location', 'phonenumber', 'company_name')
admin.site.register(CustomUser, CustomUserAdmin)