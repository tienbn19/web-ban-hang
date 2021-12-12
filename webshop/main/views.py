from django.shortcuts import render,redirect
from item_panel.models import items
from django.views import View
import json
# Create your views here.
def main(request):
    if 'order_item' in request.session:
        order_item = request.session.get('order_item')
    else:
        order_item = ''
    if 'quantity' in request.session:
        quantity = int(request.session.get('quantity'))
    else:
        quantity = 0
    if 'total' in request.session:
        total = int(request.session.get('total'))
    else:
        total = 0
    order_item = json.dumps(order_item)
    request.session['order_item'] = order_item
    request.session['quantity'] = quantity
    request.session['total'] = total
    query = "SELECT * FROM item_panel_items"
    item_list = items.objects.raw(query)
    return render(request, 'main.html', {'item_list': item_list, 'quantity': quantity, 'total':total})

def addtocart(request, product_id):
    query = "SELECT * FROM item_panel_items WHERE id = %s"
    product = items.objects.raw(query,[product_id])
    quantity = int(request.session.get('quantity'))+1
    total = int(request.session.get('total'))
    order_item = request.session.get('order_item')
    list = order_item+str(product_id)
    request.session['order_item'] = list
    request.session['quantity'] = quantity
    request.session['total'] = total + product[0].price
    return redirect('main')
def product(request, id):
    query = "SELECT * FROM item_panel_items WHERE id = %s" % id
    item = items.objects.raw(query)[0]
    context = {
        "item" : item
    }
    return render(request,'product.html', context)
def checkout(request):
    quantity = int(request.session.get('quantity'))
    total = int(request.session.get('total'))
    return render(request,'checkout.html',{ 'quantity': quantity, 'total':total})