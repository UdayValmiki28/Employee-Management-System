"""Company Employee URLs Configuration"""
from django.urls import path
from .views import home, add_employee, employee_list, delete_employee, edit_employee,employee_detail

urlpatterns = [
    path('', home, name='home'),
    path('employee/add/',add_employee, name='employee_add'),
    path('employee/view/',employee_list, name='employee_list'),
    path('employee/delete/<int:emp_id>/',delete_employee, name='employee_delete'),
    path('employee/edit/<int:emp_id>/',edit_employee, name='employee_edit'),
    path('employee/view/<int:emp_id>/',employee_detail, name='employee_details'),
]
