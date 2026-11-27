from django.db import models
from rest_framework.fields import ImageField


#Schema Definition
class Employee(models.Model):
    Name=models.CharField(max_length=20)
    Empid=models.IntegerField(unique=True)
    Age=models.IntegerField()
    Place=models.CharField(max_length=30)
    gender_choices=(('male','Male'),('female','Female'))
    Gender=models.CharField(max_length=20,choices=gender_choices)
    Joining_date=models.DateField(auto_now_add=True)        #automatically adds current date to employee record
    Salary=models.IntegerField()
    Designation=models.CharField(max_length=20)
    image=models.ImageField(upload_to="employees",null=True)
