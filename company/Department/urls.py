"""Company department URLs Configuration"""
from django.urls import path 
from .views import home, add_department, department_list, edit_department, delete_department, department_detail

urlpatterns = [
    path('', home, name='Department Home'),
    path('departments/add/', add_department, name='Add Department'),
    path('departments/view/', department_list, name='Department list'),
    path('departments/edit/<int:dept_id>', edit_department, name='Edit Department'),
    path('departments/delete/<int:dept_id>', delete_department, name='Delete Department'),
    path('departments/view/<int:dept_id>', department_detail, name='Department Detail'),
]
