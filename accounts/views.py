from urllib import request
from django.shortcuts import render
import json
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password, ValidationError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def register():
  """
  Register a new user.
  Except a username, email and a password.
  """
  
  if request.method != 'POST':
    return JsonResponse({'error': 'POST request required.'}, status=400)
  try:
    data = json.loads(request.body)
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username and password:
      return JsonResponse({'error': 'Username and password required.'}, status=400)
    if User.objects.filter(username=username).exists():
      return JsonResponse({'error': 'Username already exists.'}, status=400)
    try:
      validate_password(password)
    except ValidationError as e:
      return JsonResponse({'error': e.messages}, status=400)
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
    return JsonResponse({'message': 'User created successfully.'}, status=201)
  except json.JSONDecodeError:
    return JsonResponse({'error': 'Invalid JSON.'}, status=400)
  
@csrf_exempt
def login():
  """
  Logs in a user.
  Expect an email and a password.
  """
  if request.method != 'POST':
    return JsonResponse({'error': 'POST request required.'}, status=400)
  try:
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')
    user = authenticate(request, email = email, password = password)
    if user is None:
      return JsonResponse({'error': 'Invalid credentials.'}, status=400)
    login(request, user)
    return JsonResponse({'message': 'User logged in successfully.'}, status=200)
  except json.JSONDecodeError:
    return JsonResponse({'error': 'Invalid JSON.'}, status=400)
  
