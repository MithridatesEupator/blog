from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.make_post, name='make_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('post/<slug:slug>/', views.see_post, name='see_post'),
    path('comments/<int:pk>/', views.make_comment, name='make_comment')
]
