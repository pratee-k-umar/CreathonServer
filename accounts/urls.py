from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.user_register, name='register'),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
  path('change-pass/', views.change_pass, name='change-pass'),
  path('user/<str:username>/', views.profile, name='fetch-user')
]