from django.urls import path
from administrator import views

urlpatterns = [
    path('home/',views.admin_home,name='admin-home'),
    path('add-customer/',views.add_customer,name='add-customer'),
]