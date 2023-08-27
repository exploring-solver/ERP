from rest_framework import serializers
from .models import CustomUser

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'contact', 'password', 'is_student')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'contact', 'password', 'is_employee')

# Add more serializers as needed
