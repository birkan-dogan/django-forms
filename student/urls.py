from django.urls import path
from student.views import student_page

urlpatterns=[
    path("",student_page,name="student")
]