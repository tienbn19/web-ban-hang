from django.shortcuts import render
from django.views import View
# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
class ItemView(View):
    def get(self, request):
        return render(request, 'product.html')
class CartView(View):
    def get(self, request):
        return render(request, 'checkout.html')
