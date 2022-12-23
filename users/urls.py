from django.urls import path
from users import views

urlpatterns = [
    path('user/<str:username>/',views.user_home,name='user-home'),
    path('list-domains/',views.list_domains,name='list-domains'),
    path('user-tickets-list/',views.user_tickets_list,name='user-tickets-list'),
    path('user-tickets/<int:id>',views.user_tickets,name='user-tickets'),
    path('create-ticket/',views.create_ticket,name='create-ticket'),
]