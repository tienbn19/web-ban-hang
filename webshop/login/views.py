from django.shortcuts import render,redirect
from item_panel.models import employees
# Create your views here.

def login_panel(request):
    return render(request, 'login_panel.html',{})

def login(request):
    m = employees.objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['member_id'] = m.id
        request.session['role'] = m.roles
        request.session['user'] = m.username
        return redirect("item_panel")
    else:
        return redirect("login_panel")