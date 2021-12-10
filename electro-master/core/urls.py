from django.urls import path
from .views import HomeView,ItemView,CartView
urlpatterns = [
    path('1', HomeView.as_view(), name='index' ),
    path('2', ItemView.as_view(), name='item' ),
    path('3', CartView.as_view(), name='cart' ),
]
