from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.make_post, name='make_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
]
