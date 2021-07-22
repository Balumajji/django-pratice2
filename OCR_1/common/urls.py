from django.contrib import admin
from django.urls import path
from django.urls import include
from common import views

urlpatterns = [
    path('', views.showHome, name='home_page'),
    path('student/', views.showstudent, name='student_page'),
    path('student_registration/', views.showStudentRegistration,name='student_Registration'),
    path('student_otp/', views.showstudentotp, name="student_otp"),
    path('faculty/', views.showfaculty, name='faculty_page'),
    path('admin/', views.showadmin, name='admin_page'),
    path('contact/', views.showcontact, name='contact_page'),

]