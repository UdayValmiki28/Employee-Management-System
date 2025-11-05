"""Views for the Company Departments"""
from django.shortcuts import render
from .models import Department

# Create your views here.

def home(request):
    """view for the home page"""
    return render(request, 'home.html')

def add_department(request):
    """view for the add department"""
    if request.method == 'POST':
        department_name = request.POST['dept_name']
        department_no_of_projects = request.POST['dept_projects']
        department_head = request.POST['dept_head']
        department_region = request.POST['dept_region']
        department_data = Department(department_name = department_name, department_no_of_projects = department_no_of_projects,
                                     department_head = department_head, department_region = department_region)
        department_data.save()
        return render(request, 'message.html', context={
        'msg':'department data added successfully'
        })
    return render(request,'department/add_department.html')

def department_list(request):
    """view for the department list"""
    department = Department.objects.all()
    return render(request,'department/department_list.html', context={
        'department': department
    })

def edit_department(request, dept_id):
    """ view for the department edit"""
    department = Department.objects.get(id = dept_id)
    if request.method == 'POST':
        department.department_name = request.POST['dept_name']
        department.department_no_of_projects = request.POST['dept_projects']
        department.department_head = request.POST['dept_head']
        department.department_region = request.POST['dept_region']
        return render(request,'message.html', context={
            'msg':'department data updated successfully'
        })
    return render(request,'department/edit_department.html', context={
        'dept_id':dept_id
    })

def delete_department(request, dept_id):
    """view for the department delete"""
    department = Department.objects.get(id = dept_id)
    department.delete()
    return render(request, 'message.html', context={
        'msg': 'employee data deleted successfully'
    })

def department_detail(request, dept_id):
    """view for the department details"""
    department = Department.objects.get(id = dept_id)
    return render(request, 'department/department_detail.html', context={
        'department': department
    })
