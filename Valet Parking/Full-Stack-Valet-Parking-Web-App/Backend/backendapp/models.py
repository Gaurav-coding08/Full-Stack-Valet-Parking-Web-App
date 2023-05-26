from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.

class Admin_info(models.Model):
    Email =models.EmailField() 
    Password=models.CharField(max_length=20,blank=True)
    
    def __str__(self):
        return self.Email
    
class Car_info(models.Model):
    Car_Number=models.CharField(max_length=6)
    Date=models.DateField()
    Time=models.TimeField()
    
    
    def __str__(self):
        return self.Car_Number
