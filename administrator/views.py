from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth.models import User
from administrator.models import Country,Customer,Domain
from datetime import date

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

@user_passes_test(lambda u: u.is_superuser)
def list_customer(request):
	customers = Customer.objects.all()
	context = {
		'customers' : customers
	}
	return render(request,'adm/list-customer.html',context)

######################################################################################################

@user_passes_test(lambda u: u.is_superuser)
def customer_details(request,name):
	customer = Customer.objects.get(Name=name)
	domains = Domain.objects.filter(Customer_Name=customer)
	count = domains.count()
	
	context = {
		'customer' : customer,
		'domains' : domains,
		'count' : count,
	}
	return render(request,'adm/customer-details.html',context)

######################################################################################################

@user_passes_test(lambda u: u.is_superuser)
def add_domain(request):
	customers = Customer.objects.all()
	if request.method == 'POST':
		customer = request.POST.get('customer')
		domain = request.POST.get('domain')
		s_date = request.POST.get('date')
		r_date = s_date
		cus = Customer.objects.get(id=customer)
		data = Domain(Customer_Name=cus,Domain_Name=domain,Purchase_Date=s_date,Renewal_Date=r_date)
		data.save()
	context = {
		'customers' : customers
	}
	return render(request,'adm/add-domain.html',context)

######################################################################################################

@user_passes_test(lambda u: u.is_superuser)
def edit_customer(request,name):
	customer = Customer.objects.get(Name=name)
	if request.method == "POST" :
		customer.Name = request.POST.get('name')
		customer.Email = request.POST.get('email')
		customer.Mobile = request.POST.get('mobile')
		customer.Country = request.POST.get('country_selector_code')
		customer.save()
		return redirect('.')
	context = {
		'customer' : customer
	}
	return render(request,'adm/edit-customer.html',context)
