from django.db import models

# Create your models here.

class Department(models.Model):
    """creating the model for the department"""
    department_name = models.CharField(max_length=25, default=None)
    department_no_of_projects = models.IntegerField(default=None)
    department_head = models.CharField(max_length=20, default=None)
    department_region = models.CharField(max_length=25, default=None)
