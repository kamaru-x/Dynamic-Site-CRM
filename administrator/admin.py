from django.contrib import admin

# models 
from administrator.models import Customer,Country,Domain

# Register your models here.

admin.site.register(Customer)
admin.site.register(Country)
admin.site.register(Domain)