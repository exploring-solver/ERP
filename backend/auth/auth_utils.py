from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status

def perform_login(request, user_type):
    id = request.data.get('id')
    password = request.data.get('password')
    
    user = authenticate(id=id, password=password)
    
    if user and getattr(user, f'is_{user_type}'):
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': f'Invalid {user_type} credentials'}, status=status.HTTP_400_BAD_REQUEST)

def perform_registration(request, user_type):
    id = request.data.get('id')
    name = request.data.get('name')
    email = request.data.get('email')
    contact = request.data.get('contact')
    password = request.data.get('password')
    
    # Perform user registration logic here
    
    # After successful registration, authenticate the user
    user = authenticate(id=id, password=password)
    
    if user and getattr(user, f'is_{user_type}'):
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': f'Invalid {user_type} credentials'}, status=status.HTTP_400_BAD_REQUEST)
