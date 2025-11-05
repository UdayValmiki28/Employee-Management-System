"""Company Employee View"""
from django.shortcuts import render
from .models import Employee

# Create your views here.


def home(request):
    """renders the employee page for the employee app"""
    return render(request,'home.html')

def add_employee(request):
    """view to add the new employee"""
    if request.method == 'POST':
        employee_name = request.POST['emp_name']
        employee_age = request.POST['emp_age']
        employee_address = request.POST['emp_address']
        employee_department = request.POST['emp_department']
        employee_reporting_manager = request.POST['emp_reporting_manager']
        employee_email = request.POST['emp_email']
        employee_data = Employee(employee_name = employee_name, employee_age = employee_age,
                        employee_address = employee_address, employee_department = employee_department,
                        employee_reporting_manager = employee_reporting_manager,
                        employee_Email = employee_email)
        employee_data.save()
        return render(request, 'message.html', context={
        'msg':'employee data added successfully'
        })
    return render(request,'employee/add_employee.html')

def employee_list(request):
    """view to see the employee list"""
    employees = Employee.objects.all()
    return render(request,'employee/employee_list.html', context={
        'employees':employees
    })

def employee_detail(request, emp_id):
    """view to the specific employee details"""
    employee = Employee.objects.get(id = emp_id)
    return render(request,'employee/employee_detail.html', context={
        'employee' : employee
    })

def delete_employee(request, emp_id):
    """view to delete an employee"""
    employee = Employee.objects.get(id = emp_id)
    employee.delete()
    return render(request, 'message.html', context={
        'msg':'employee data added successfully'
        })

def edit_employee(request, emp_id):
    """view to edit the employee detais"""
    employee = Employee.objects.get(id = emp_id)
    if request.method == "POST":
        employee.employee_name = request.POST['emp_name']
        employee.employee_age = request.POST['emp_age']
        employee.employee_address = request.POST['emp_address']
        employee.employee_department = request.POST['emp_department']
        employee.employee_reporting_manager = request.POST['emp_reporting_manager']
        employee.employee_Email = request.POST['emp_email']
        employee.save()
        return render(request,'message.html', context={
            'msg':"employee data updated successfully......"
        })
    return render(request,'employee/edit_employee.html', context={
        'employee':employee
    })
