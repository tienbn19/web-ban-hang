from django.urls import path
from item_panel import views

urlpatterns = [
    path('', views.item_panel, name='item_panel'),
    path('add/', views.add_item),
    path('edit/<int:item_id>', views.edit_item),
    path('delete/<int:item_id>', views.delete_item),
    path('employee', views.employee_panel, name='employee_panel'),
    path('employee/add/', views.add_employee),
    path('employee/edit/<int:employee_id>', views.edit_employee),
    path('employee/delete/<int:employee_id>', views.delete_employee),
]