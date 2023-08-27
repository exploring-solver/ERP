from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate
from .auth_utils import perform_login, perform_registration

User = get_user_model()

class StudentLoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        return perform_login(request, 'student')

class StudentRegistrationView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        return perform_registration(request, 'student')

class StudentAdmissionView(generics.CreateAPIView):
    # Placeholder for student admission view
    pass

class EmployeeLoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        return perform_login(request, 'employee')

class EmployeeRegistrationView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        return perform_registration(request, 'employee')

class EmployeeApplyView(generics.CreateAPIView):
    # Placeholder for employee apply view
    pass
