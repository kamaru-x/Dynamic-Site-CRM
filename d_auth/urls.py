from django.urls import path
from d_auth import views

urlpatterns = [
    path('login/',views.admin_login,name='login'),
]