from django.shortcuts import render, redirect
from django.db import connection
from .models import employees, items
from .forms import ItemCreate, EmployeeCreate
from django.contrib import messages
# Create your views here.

def item_panel(request):
    user = request.session.get('user')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM item_panel_items")
        item_list = cursor.fetchall()
    return render(request, 'item_panel.html', {'item_list': item_list, 'user': user})

def add_item(request):
    user = request.session.get('user')
    add = ItemCreate()
    if request.method == 'POST':
        add = ItemCreate(request.POST, request.FILES)
        if add.is_valid():
            add.save()
            return redirect('item_panel')
    else:
        return render(request, 'upload_form.html', {'upload_form':add, 'user': user})

def edit_item(request, item_id):
    user = request.session.get('user')
    item_id = int(item_id)
    try:
        item_sel = items.objects.get(id = item_id)
    except items.DoesNotExist:
        return redirect('item_panel')
    item_form = ItemCreate(request.POST or None, instance = item_sel)
    if item_form.is_valid():
       item_form.save()
       return redirect('item_panel')
    return render(request, 'upload_form.html', {'upload_form':item_form, 'user': user})

def delete_item(request, item_id):
    item_id = int(item_id)
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM item_panel_items WHERE id = %s", [item_id])
    return redirect('item_panel')

def employee_panel(request):
    user = request.session.get('user')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM item_panel_employees")
        employees_list = cursor.fetchall()
    return render(request, 'employee_panel.html', {'employees_list': employees_list, 'user': user})

def add_employee(request):
    user = request.session.get('user')
    add = EmployeeCreate()
    if request.method == 'POST':
        add = EmployeeCreate(request.POST, request.FILES)
        if add.is_valid():
            add.save()
            return redirect('employee_panel')
    else:
        return render(request, 'e_upload_form.html', {'e_upload_form':add, 'user': user})

def edit_employee(request, employee_id):
    user = request.session.get('user')
    employee_id = int(employee_id)
    try:
        employee_sel = employees.objects.get(id = employee_id)
    except employees.DoesNotExist:
        return redirect('employee_panel')
    employee_form = EmployeeCreate(request.POST or None, instance = employee_sel)
    if employee_form.is_valid():
       employee_form.save()
       return redirect('employee_panel')
    return render(request, 'e_upload_form.html', {'e_upload_form':employee_form, 'user': user})

def delete_employee(request, employee_id):
    employee_id = int(employee_id)
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM item_panel_employees WHERE id = %s", [employee_id])
    return redirect('employee_panel')