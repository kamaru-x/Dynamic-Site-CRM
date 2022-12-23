from django.contrib import admin

# models 
from administrator.models import Customer,Country,Domain,Tickets,Replayes

# Register your models here.

admin.site.register(Customer)
admin.site.register(Country)
admin.site.register(Domain)
admin.site.register(Tickets)
admin.site.register(Replayes)