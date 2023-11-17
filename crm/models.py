from django.db import models

class Employees(models.Model):
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    salary=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=20,null=True)
    age=models.PositiveIntegerField(null=True)  
    profilepic=models.ImageField(upload_to="image",null=True,blank=True) 
    dob=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name 