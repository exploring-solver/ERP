from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Student(AbstractUser):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'student'  # This sets the table name to 'student'

    # Add related_name to resolve naming conflicts
    groups = models.ManyToManyField(Group, related_name='student_set')
    user_permissions = models.ManyToManyField(Permission, related_name='student_set')