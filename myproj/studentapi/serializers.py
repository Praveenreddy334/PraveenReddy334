from rest_framework import serializers
from .models import Student, StudentDetails,Assignment


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ('id','first_name', 'last_name', 'mail', 'mobile', 'Dob', 'gender')

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Assignment
        fields ='__all__'
