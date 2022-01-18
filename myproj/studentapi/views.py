from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import  status
from .models import *
# from .serializers import studentSerializer
# # Create your views here.
# class StudentList(APIView):
#     def get(self, request):
#         students=student.objects.all()
#         serializer=studentSerializer(students, many=True)
#         return Response(serializer.data)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
@api_view(['GET','POST','PUT','DELETE'])
def StudentList(request,key=None):
    id=key
    if request.method=='GET':
        if id is None:
            students=Student.objects.all()
            serializer=StudentSerializer(students, many=True)
            return Response(serializer.data)
        else:
            students=Student.objects.get(id=id)
            serializer=StudentSerializer(students)
            return Response(serializer.data)
    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Data Inserted Successfully.....!'})
    if request.method=='PUT':
        students=Student.objects.get(id=id)
        serializer=StudentSerializer(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Updated Successfully")
    if request.method == 'DELETE':
        students = Student.objects.get(id=id)
        students.delete()
        return Response({'Deleted Successfully...!'})

def index(request):
    return render(request,'signup.html')
#getting data from form
def newPage(request):
    f_name=request.POST.get('fname')
    l_name = request.POST.get('lastname')
    mail = request.POST.get('email')
    mobile = request.POST.get('mobileno')
    Dob = request.POST.get('dob')
    gen=request.POST.get('gen')
    pas1=request.POST.get('pass')
    # pas2=request.POST.get('pass2')
    ref=StudentDetails(first_name=f_name, last_name=l_name, mail=mail, mobile=mobile, Dob=Dob, gender=gen, pas1=pas1)
    ref.save()
    return render(request, 'signup.html',{"message":'registered'})




