from django.urls import path
from .views import HomeView,product,CartView
urlpatterns = [
    path('index', HomeView.as_view(), name='index' ),
    path('item/<int:id>', product, name='item' ),
    path('cart', CartView.as_view(), name='cart' ),
]
