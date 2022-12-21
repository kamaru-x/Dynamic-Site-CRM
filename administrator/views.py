from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth.models import User
from administrator.models import Country,Customer

# Create your views here.

# admin dashboard & login redirects here
@user_passes_test(lambda u: u.is_superuser)
def admin_home(request):
    return render(request,'adm/admin-home.html')

######################################################################################################

# Add customer view
@user_passes_test(lambda u: u.is_superuser)
def add_customer(request):
	countries = Country.objects.all()
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		country = request.POST.get('country_selector_code')
		data = Customer(Name=name,Email=email,Mobile=mobile,Country=country)
		data.save()
		return redirect('.')
	context = {
		'countries' : countries,
	}
	return render(request,'adm/add-customer.html',context)

######################################################################################################
