from django.db import models
from datetime import datetime


# Create your models here.

#Choices for Gender
EMPLOYEE_GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

#Employee data class with the exception of phone numbers
class employeebiodata(models.Model):
    firstname = models.CharField(max_length=220)
    lastname = models.CharField(max_length=220)
    gender = models.CharField(max_length=1, choices= EMPLOYEE_GENDER)
    email = models.CharField(max_length=60, unique=True)
    dateCreated = models.DateTimeField(default=datetime.now, blank=True)
    dateUpdated = models.DateTimeField(default=datetime.now, blank=True)
