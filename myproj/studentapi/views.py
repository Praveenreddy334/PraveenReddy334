import pydoc
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer,StudentDetailsSerializer,AssignmentSerializer
from .models import Student,StudentDetails,Assignment
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
    f_name = request.POST.get('fname')
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

@api_view(['GET'])
def get_student_details(request):
    if request.method=="GET":
        student_id=request.GET.get('student_id',None)
        gender=request.GET.get('gender',None)
        if student_id is None:
            if gender is not None:
                if gender=="Male":
                    all_students=StudentDetails.objects.filter(gender='Male')
                    serializer=StudentDetailsSerializer(all_students,many=True)
                    return Response(serializer.data)
                elif gender=="Female":
                    all_students=StudentDetails.objects.filter(gender='Female')
                    serializer=StudentDetailsSerializer(all_students,many=True)
                    return Response(serializer.data)
            else:
                all_students=StudentDetails.objects.all()
                serializer=StudentDetailsSerializer(all_students,many=True)
                return Response(serializer.data)
        else:
            if gender is None:
                all_students = StudentDetails.objects.get(id=student_id)
                serializer = StudentDetailsSerializer(all_students)
                return Response(serializer.data)
            else:
                return Response({"Invalid"})





def assign(request):

    return render(request,'p.html'  )
def assignment(request):
    # if request.method=="POST":
        subject=request.POST.get('subject')
        assignment_num=request.POST.get('assignment_num')
        # file=( request.FILES['file'])
        re=Assignment(subject=subject,  assignment_num= assignment_num)
        re.save()
        return render(request,'p.html',{"message":'done'})



