from django.urls import path
from .import views
urlpatterns=[
    path('student-list/', views.StudentList, name='student-list'),
    path('student-list/<int:key>',views.StudentList,name='student-list'),
    path('index/',views.index),
    path('new/',views.newPage),
]