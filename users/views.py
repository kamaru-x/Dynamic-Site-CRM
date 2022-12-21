from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def user_home(request,username):
    user = request.user
    context = {
        'user':user
    }
    return render(request,'user/user-home.html',context)