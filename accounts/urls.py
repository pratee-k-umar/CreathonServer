from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.user_register, name='register'),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
  path('profile/', views.user_data, name='profile'),
  path('change-pass/', views.change_pass, name='change-pass'),
]