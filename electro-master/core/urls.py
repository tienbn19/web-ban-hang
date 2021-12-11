from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='index' ),
    path('item/<int:id>', product, name='item' ),
    path('checkout', checkout, name='checkout' ),
]
