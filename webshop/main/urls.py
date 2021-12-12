from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('addtocart/<int:product_id>', addtocart),
    path('item/<int:id>', product),
    path('checkout', checkout, name='checkout' ),
]