from django.urls import path
from login import views

urlpatterns = [
    path('', views.login_panel, name='login_panel' ),
    path('log/', views.login),
]