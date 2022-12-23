from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from administrator.models import Domain
from administrator.models import Tickets,Replayes
from datetime import date

# Create your views here.

# homepage view
@login_required
def user_home(request,username):
    user = request.user
    context = {
        'user':user
    }
    return render(request,'user/user-home.html',context)

######################################################################################################

@login_required
def list_domains(request):
    user = request.user
    domains = Domain.objects.all()
    context = {
        'domains' : domains
    }
    return render(request,'user/domains-list.html',context)

######################################################################################################

@login_required
def user_tickets(request,id):
    usr = request.user
    replayes = Replayes.objects.filter(Ticket__id=id).order_by('-id')
    ticket = Tickets.objects.get(id=id)
    if request.method == 'POST':
        replay = request.POST.get('message')
        dt = date.today() 
        attachment = request.FILES['attachment']
        data = Replayes(Ticket=ticket,Sender=usr,Replay=replay,Date=dt,Attachment=attachment)
        data.save()
        return redirect('/user-tickets/%s'%ticket.id)
    context = {
        'ticket' : ticket,
        'replays' : replayes,
    }
    return render(request,'user/user-tickets.html',context)

######################################################################################################

@login_required
def user_tickets_list(request):
    usr = request.user
    tickets = Tickets.objects.filter(Creator=usr).order_by('-id')
    context = {
        'tickets' : tickets
    }
    return render(request,'user/user-tickets-list.html',context)

######################################################################################################


@login_required
def create_ticket(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        attachment = request.FILES['attachment']
        creator = request.user
        dat = date.today()
        ticket = Tickets(Creator=creator,Message=message,Attachment=attachment,Date=dat)
        ticket.save()
        return redirect('.')
    return render(request,'user/create-ticket.html')