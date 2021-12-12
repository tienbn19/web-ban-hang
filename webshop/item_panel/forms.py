from django import forms
from django.forms import fields
from .models import items, employees

class ItemCreate(forms.ModelForm):
    class Meta:
        model = items
        fields = '__all__'

class EmployeeCreate(forms.ModelForm):
    class Meta:
        model = employees
        fields = '__all__'