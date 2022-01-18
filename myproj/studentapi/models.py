from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    department=models.CharField(max_length=10)
    # def __str__(self):
    #     return self.first_name
class StudentDetails(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mail=models.EmailField()
    mobile=models.BigIntegerField()
    Dob = models.DateField()
    gender=models.CharField(max_length=6,blank=True,null=True)
    pas1=models.CharField(max_length=20,null=True)
    # pas2 = models.CharField(max_length=20)





