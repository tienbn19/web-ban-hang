from django.db.models import query
from django.shortcuts import render
from django.views import View
from item.models import Item
from django.contrib.auth.models import User
# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
def home(request):
    query = "SELECT * FROM item_item "
    all_item = Item.objects.raw(query)
    context = {
        "all_item" : all_item
    }
    return render(request,'index.html', context)
def product(request, id):
    query = "SELECT * FROM item_item WHERE id = %s" % id
    item = Item.objects.raw(query)[0]
    context = {
        "item" : item
    }
    return render(request,'product.html', context)
def checkout(request):
    return render(request,'checkout.html')
