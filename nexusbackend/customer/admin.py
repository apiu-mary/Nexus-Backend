from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'country', 'city','phone')

admin.site.register(Customer, CustomerAdmin)
