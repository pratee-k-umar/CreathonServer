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
def user_register(request):
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
def user_login(request):
  """
  Logs in a user.
  Expect an email and a password.
  """
  if request.method != 'POST':
    return JsonResponse({'error': 'POST request required.'}, status=400)
  try:
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(request, username = username, password = password)
    if user is None:
      return JsonResponse({'error': 'Invalid credentials.'}, status=400)
    login(request, user)
    return JsonResponse({'message': 'User logged in successfully.'}, status=200)
  except json.JSONDecodeError:
    return JsonResponse({'error': 'Invalid JSON.'}, status=400)
  
@csrf_exempt
def user_logout(request):
  """
  Logs out current authenticated user.
  """
  if request.method != 'POST':
    return JsonResponse({'error': 'POST request required.'}, status=400)
  try:
    logout(request)
    return JsonResponse({'message': 'User logged out successfully.'}, status=200)
  except:
    return JsonResponse({'error': 'Something went wrong.'}, status=500)

@csrf_exempt
def user_data(request):
  """
  Fetch authenticated user data
  """
  if not request.user.is_authenticated:
    return JsonResponse({'error': 'User not authenticated.'}, status=401)
  if request.method != 'GET':
    return JsonResponse({'error': 'GET request required.'}, status=400)
  return JsonResponse({
    'username': request.user.username,
    'email': request.user.email,
  })
  
@csrf_exempt
def change_pass(request):
  """
  Change authenticated user password.
  Expect old and new password.
  """
  if not request.user.is_authenticated:
    return JsonResponse({'error': 'User not authenticated.'}, status=401)
  if request.method != 'POST':
    return JsonResponse({'error': 'POST request required.'}, status=400)
  try:
    data = json.loads(request.body)
    old_password = data.get('old_password')
    new_password = data.get('new_password')
    user = request.user
    if not old_password and new_password:
      return JsonResponse({'error': 'Old and new password required.'}, status=400)
    if not request.user.check_password(old_password):
      return JsonResponse({'error': 'Invalid old password.'}, status=400)
    try:
      validate_password(new_password, user = user)
    except ValidationError as e:
      return JsonResponse({'error': e.messages}, status=400)
    user.set_password(new_password)
    user.save()
    update_session_auth_hash(request, user)
    return JsonResponse({'message': 'Password changed successfully.'}, status=200)
  except json.JSONDecodeError:
    return JsonResponse({'error': 'Invalid JSON.'}, status=400)
  