# auth/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('student/login/', views.StudentLoginView.as_view(), name='student-login'),
    path('student/register/', views.StudentRegistrationView.as_view(), name='student-register'),
    path('student/admission/', views.StudentAdmissionView.as_view(), name='student-admission'),

    path('employee/login/', views.EmployeeLoginView.as_view(), name='employee-login'),
    path('employee/register/', views.EmployeeRegistrationView.as_view(), name='employee-register'),
    path('employee/apply/', views.EmployeeApplyView.as_view(), name='employee-apply'),
]
