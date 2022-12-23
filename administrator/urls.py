from django.urls import path
from administrator import views

urlpatterns = [
    path('home/',views.admin_home,name='admin-home'),
    path('add-customer/',views.add_customer,name='add-customer'),
    path('list-customers/',views.list_customer,name='list-customers'),
    path('customer/<str:name>/',views.customer_details,name='customer-details'),
    path('add-domain/',views.add_domain,name='add-domain'),
    path('edit/<str:name>/',views.edit_customer,name='edit-customer'),
    path('tickets/',views.all_tickets,name='tickets'),
    path('replay-ticket/<int:id>',views.replay_ticket,name='replay-ticket'),
]