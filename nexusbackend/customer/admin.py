from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'country', 'city')

admin.site.register(Customer, CustomerAdmin)
