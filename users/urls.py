from django.urls import path
from users import views

urlpatterns = [
    path('<str:username>/',views.user_home,name='user-home')
]