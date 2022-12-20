from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect('admin-home')
            else:
                usr = request.user
                return redirect('/%s'%user.username)
        else:
            messages.error(request,'incorrect email or password')
            return redirect('.')
    return render(request,'auth/admin_login.html')