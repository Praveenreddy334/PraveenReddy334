from django.db import models


# Create your models here.
#for crud api
class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    department=models.CharField(max_length=10)
    # def __str__(self):
    #     return self.first_name

    # signup form model
class StudentDetails(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    mail=models.EmailField()
    mobile=models.BigIntegerField()
    Dob = models.DateField()
    gender=models.CharField(max_length=6,blank=True,null=True)
    pas1=models.CharField(max_length=20,null=True)
    # many_assignments=models.ManyToManyField(Assignment)
    # pas2 = models.CharField(max_length=20)


    def __str__(self):
         return self.first_name+" "+self.last_name

class Assignment(models.Model):
    subject=models.CharField(max_length=20,null=True,blank=True)
    assignment_num=models.BigIntegerField(null=True,blank=True)
    file=models.FileField(upload_to='media',default='')
    many_students=models.ManyToManyField(StudentDetails)
    def __str__(self):
        return self.subject


class Task(models.Model):
    task_name=models.CharField(max_length=40)
    task_start_date=models.DateField()
    complete_by=models.DateField()
    task_priority=models.CharField(max_length=10)
    many_students=models.ManyToManyField(StudentDetails)

    def __str__(self):
         return self.task_name








