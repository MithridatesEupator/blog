from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<slug:slug>', views.see_account, name='see_account'),
    path('profile/edit/<slug:slug>', views.edit_profile, name='edit_profile'),
    path('profile/submit/<slug:slug>', views.submit_changes, name='submit_changes'),
    
]
