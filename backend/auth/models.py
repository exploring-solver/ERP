from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Common fields for both Student and Employee
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    # Fields specific to Student
    is_student = models.BooleanField(default=False)

    # Fields specific to Employee
    is_employee = models.BooleanField(default=False)

    # Add other fields as needed

    def __str__(self):
        return self.username
