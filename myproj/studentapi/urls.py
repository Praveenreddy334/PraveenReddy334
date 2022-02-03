from django.urls import path
from .import views
urlpatterns=[
    path('student-list/',views.StudentList,name='student-list'),
    path('student-list/<int:key>',views.StudentList,name='student-list'),
    path('index/',views.index),#signup
    path('new/',views.newPage),
    path('all-students/', views.get_student_details, name='all-students'),#get api
    # path('all-students/<int:key>/',views.get_student_details,name='all-students'),
    path('assign/',views.assign),#assignment
    path('assignment/',views.assignment),
]