from django.contrib import admin

# models 
from administrator.models import Customer,Country

# Register your models here.

admin.site.register(Customer)
admin.site.register(Country)