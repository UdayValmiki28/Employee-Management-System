"""model field for the employee"""
from django.db import models

# Create your models here.

class Employee(models.Model):
    """creating the models for the employee data"""
    employee_name = models.CharField(max_length=50, default = None)
    employee_age = models.IntegerField(default= None)
    employee_address = models.CharField(max_length=100, default=None)
    employee_department = models.CharField(max_length=25, default=None)
    employee_reporting_manager = models.CharField(max_length=15, default=None)
    employee_Email = models.CharField(max_length=30, default=True)
